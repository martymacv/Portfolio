import struct


class Modbus:
    """MODBUS Aplication Protocol"""
    transaction_id = 0
    msg_length = 0

    def get_msg(self, x, y):
        self.x = x
        self.y = y
        print("Вызов метода get_msg ", x, y, str(self))


if __name__ == "__main__":
    # Modbus.get_msg
    get_msg = Modbus()
    get_msg.get_msg(1, 2)
    Modbus.get_msg(get_msg, 1, 2)
    get_msg.msg_length = 6
    set_msg = Modbus()
    set_msg.msg_length = 9
    Modbus.transaction_id += 1
    print(get_msg.transaction_id, get_msg.msg_length, Modbus.transaction_id, Modbus.msg_length)
    print(set_msg.transaction_id, set_msg.msg_length, Modbus.transaction_id, Modbus.msg_length)
    Modbus.transaction_id += 1
    print(get_msg.transaction_id, Modbus.transaction_id)
    print(set_msg.transaction_id, Modbus.transaction_id)
    get_msg.transaction_id += 1
    set_msg.transaction_id += 1
    print(get_msg.transaction_id, Modbus.transaction_id)
    print(set_msg.transaction_id, Modbus.transaction_id)


class ReadRegister(Modbus):

    def __init__(self, start_register, quantity_registers):
        self.start_register = start_register
        self.quantity_registers = quantity_registers

    def get(self):
        struct_format = ">HHHBBHH"
        return struct.pack(struct_format, 1, 0, struct.calcsize(struct_format), 1,
                           3, self.start_register, self.quantity_registers)


class Header(Modbus):
    """MODBUS Header"""
    """
    Example UDP MODBUS Header:
            |-ADU-------------| (ADU = Application Data Unit)
            |-MBAP-Header-----| (MBAP - ModBus Application Protocol)
            00 01 02 03 04 05 06 (Byte number   DEC)
    Client: 00 01 00 00 xx xx 01 (Transmit byte HEX)
            |  |  |  |  |  |  |  ('>HHHB') Pack/unpack struct (Big-endian Byte order)
            |  |  |  |  |  |  +- (Bx3) Slave address (usually constant)
            |  |  |  |  |  +---- (Hx2) Message length low byte (variable) - after this
            |  |  |  |  +------- (Hx2) Message length high byte (variable)
            |  |  |  +---------- (Hx1) Protocol Identifier low byte (constant)
            |  |  +------------- (Hx1) Protocol Identifier high byte (constant)
            |  +---------------- (Hx0) Transaction Identifier low byte (counter)
            +------------------- (Hx0) Transaction Identifier high byte (counter) 
    """
    def length(self):
        return len(self.pars())


class Request(Modbus):
    """MODBUS Request"""
    """
    Example UDP MODBUS Request:
            |-ADU-------| (ADU = Application Data Unit)
            |-FCD-RHR---| (FCD = Function Codes Descriptions) (RHR = Read Holding Registers)
            07 08 09 10 11 (Byte number   DEC)
    Client: xx 00 00 yy yy (Transmit byte HEX)
            |  |  |  |  |  ('>BHH') Pack/unpack struct (Big-endian Byte order)
            |  |  |  |  +- (Hx6) Quantity of Register low byte (variable)
            |  |  |  +---- (Hx6) Quantity of Register high byte (variable)
            |  |  +------- (Hx5) Starting Address low byte (variable)
            |  +---------- (Hx5) Starting Address high byte (variable)
            +------------- (Bx4) Function code (constant)
                            | | 
                            | +- (0x03) only read register
                            +--- (0x10) only write register
    """


class Response(Modbus):
    """MODBUS Response"""
    """
    Example UDP MODBUS Response:
            |-ADU-------| (ADU = Application Data Unit)
            |-FCD-RHR---| (FCD = Function Codes Descriptions) (RHR = Read Holding Registers)
            07 08 09 10 11 (Byte number   DEC)
    Client: xx 00 00 yy yy (Transmit byte HEX)
            |  |  |  |  |  ('>BHH') Pack/unpack struct (Big-endian Byte order)
            |  |  |  |  +- (Hx6) Quantity of Register low byte (variable)
            |  |  |  +---- (Hx6) Quantity of Register high byte (variable)
            |  |  +------- (Hx5) Starting Address low byte (variable)
            |  +---------- (Hx5) Starting Address high byte (variable)
            +------------- (Bx4) Function code (constant)
                            | | 
                            | +- (0x03) only read register
                            +--- (0x10) read/write register
    """
    def __init__(self, mbap_response_):
        super().__init__()
        self.data = mbap_response_

"""
first
|- first
|  |- first
|- second
   |- first
   
"""