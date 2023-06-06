import struct


class MBAPClient:
    transaction_id = 0
    protocol_id = struct.pack(">H", 0)
    slave_addr = struct.pack(">B", 1)

    def __init__(self,):
        self.quantity_registers = 0
        self.register_values = b""
        self.byte_count = None
        self.response_mask_message = ""

    def __del__(self):
        self.register_values = b""

    @classmethod
    def __next_transaction_id(cls):
        cls.transaction_id += 1
        cls.transaction_id %= 65535

    @classmethod
    def __create_header(cls, length_msg):
        return struct.pack(">H", MBAPClient.transaction_id) + MBAPClient.protocol_id \
            + struct.pack(">H", length_msg) + MBAPClient.slave_addr

    @classmethod
    def __calc_length(cls, byte_count, quantity_registers):
        return struct.calcsize(">BBHH" + "B" * bool(byte_count) + "H" * quantity_registers)

    def get_register_values(self, start_register, quantity_registers):
        MBAPClient.__next_transaction_id()
        self.response_mask_message = ">HHHBB" + "HHB" + "H" * quantity_registers
        return MBAPClient.__create_header(MBAPClient.__calc_length(self.byte_count, self.quantity_registers)) \
            + struct.pack(">B", 3) + struct.pack(">H", start_register) + struct.pack(">H", quantity_registers)

    def set_register_values(self, start_register, data_type, register_values):
        MBAPClient.__next_transaction_id()
        self.quantity_registers = len(register_values)
        self.byte_count = 2 * self.quantity_registers
        self.response_mask_message = ">HHHBB" + "HH"
        self.register_values = b""
        for i in range(len(register_values)):
            self.register_values += struct.pack(">" + data_type, register_values[i])
        return MBAPClient.__create_header(MBAPClient.__calc_length(self.byte_count, self.quantity_registers)) \
            + struct.pack(">B", 16) + struct.pack(">H", start_register) + struct.pack(">H", self.quantity_registers) \
            + struct.pack(">B", self.byte_count) + self.register_values

    def response_handler(self, response):
        length = len(response)
        return struct.unpack(self.response_mask_message, response)

    """
    Example UDP MODBUS Header:
            |-ADU-------------| (ADU = Application Data Unit)
            |-MBAP-Header-----| (MBAP - ModBus Application Protocol)
            00 01 02 03 04 05 06 (Byte number   DEC)
    Client: 00 01 00 00 xx xx 01 (Transmit byte HEX)
            |  |  |  |  |  |  |  ('>HHHB') Pack/unpack struct (Big-endian Byte order)
            |  |  |  |  |  |  +- (Bx6) Slave address (usually constant)
            |  |  |  |  |  +---- (Hx5) Message length low byte (variable) - after this
            |  |  |  |  +------- (Hx4) Message length high byte (variable)
            |  |  |  +---------- (Hx3) Protocol Identifier low byte (constant)
            |  |  +------------- (Hx2) Protocol Identifier high byte (constant)
            |  +---------------- (Hx1) Transaction Identifier low byte (counter)
            +------------------- (Hx0) Transaction Identifier high byte (counter) 
    """
    """
    Example UDP MODBUS Request:
            |-ADU----------------| (ADU = Application Data Unit)
            |-FCD----------|-Data| (FCD = Function Codes Descriptions)
            07 08 09 10 11 12 13 (Byte number   DEC)
    Client: xx 00 00 yy yy zz aa aa (Transmit byte HEX)
            |  |  |  |  |  |  |  |  ('>BHHBHH') Pack/unpack struct (Big-endian Byte order)
            |  |  |  |  |  |  |  +- (Hx8) Register value low byte (variable)
            |  |  |  |  |  |  +---- (Hx8) Register value high byte (variable)
            |  |  |  |  |  +------- (Bx6) Byte count (variable)
            |  |  |  |  +---------- (Hx6) Quantity of Register low byte (variable)
            |  |  |  +------------- (Hx6) Quantity of Register high byte (variable)
            |  |  +---------------- (Hx5) Starting Address low byte (variable)
            |  +------------------- (Hx5) Starting Address high byte (variable)
            +---------------------- (Bx4) Function code (constant)
                                          | | 
                                          | +- (0x03) only read register
                                          +--- (0x10) only write register
    """


if __name__ == "__main__":
    """Test"""
    client1 = MBAPClient()
    request = client1.get_register_values(0, 16)
    print(client1.response_mask_message)
    request = client1.get_register_values(0, 16)
    print(client1.response_mask_message)

    client2 = MBAPClient()
    for i in range(10):
        request = client2.set_register_values(0, 'H', [65535, 0, 255])
        x = b'\x00\x03\x00\x00\x00\r\x01\x10\x00\x00\x00\x03'
        print(client2.response_handler(x))
        print(request)
    print(client1.__dict__)
    print(client2.__dict__)
    print(MBAPClient.__dict__)
