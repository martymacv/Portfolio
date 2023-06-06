import struct


class MBAPServer:
    header = ">HHHB"

    transaction_id = 0
    protocol_id = struct.pack(">H", 0)
    slave_addr = struct.pack(">B", 1)

    def __init__(self):
        self.request = "BHHBHHH"
        self.response = None
        # self.length = struct.unpack(">H", mbap_package[4:6])
        # self.function_code = struct.unpack(">B", mbap_package[7])
        # self.quantity_registers = 0
        # self.register_values = b""
        # self.byte_count = None
        # self.response_mask_message = ""

    # @classmethod
    # def __update_header(cls, length_msg, mbap_package=None):
    #     return mbap_package[:4] + struct.pack(">H", length_msg) + mbap_package[6:]
    #
    # @classmethod
    # def __calc_length(cls, byte_count, quantity_registers):
    #     return struct.calcsize(">BBHH" + "B" * bool(byte_count) + "H" * quantity_registers)
    #
    # def get_register_values(self, start_register, quantity_registers):
    #     MBAPClient.__next_transaction_id()
    #     self.response_mask_message = ">HHHBB" + "HHB" + "H" * quantity_registers
    #     return MBAPClient.__create_header(MBAPClient.__calc_length(self.byte_count, self.quantity_registers)) \
    #         + struct.pack(">B", 3) + struct.pack(">H", start_register) + struct.pack(">H", quantity_registers)
    #
    # def set_register_values(self, start_register, data_type, register_values):
    #     MBAPClient.__next_transaction_id()
    #     self.quantity_registers = len(register_values)
    #     self.byte_count = 2 * self.quantity_registers
    #     self.response_mask_message = ">HHHBB" + "HH"
    #     for i in range(len(register_values)):
    #         self.register_values += struct.pack(">" + data_type, register_values[i])
    #     return MBAPClient.__create_header(MBAPClient.__calc_length(self.byte_count, self.quantity_registers)) \
    #         + struct.pack(">B", 16) + struct.pack(">H", start_register) + struct.pack(">H", self.quantity_registers) \
    #         + struct.pack(">B", self.byte_count) + self.register_values

    def pars_message(self, rqst):
        length = len(bytearray(rqst[:4]) + bytearray(struct.pack(">H", 6)) + bytearray(rqst[7:12]))
        # return bytearray(b"").join([bytearray(rqst[:4]), bytearray(rqst[5]), bytearray(rqst[7:12])])
        return bytearray(rqst[:4]) + bytearray(struct.pack(">H", 6)) + bytearray(rqst[7:12])

    # struct.unpack(MBAPServer.header + self.request, rqst)

#
# if __name__ == "__main__":
#     server1 = MBAPServer()
#     request = b'\x00\x03\x00\x00\x00\r\x01\x10\x00\x00\x00\x03\x06\xff\xff\x00\x00\x00\xff'
#     print(server1.pars_message(request))
