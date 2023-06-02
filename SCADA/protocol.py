import struct


class Protocol:

    def __init__(self, protocol_id_):
        self.protocol_id = protocol_id_
        self.modbus = "MODBUS"
        self.http = "HTTP"
        self.opcua = "OPCUA"


class Modbus(Protocol):

    def __init__(self, data_):
        super().__init__()
        self.mbap_header = data_[:4]
        self.mbap_request = data_[4:6]
        pass


request = ''
Modbus(request)
response = ''
Modbus(response)


class Request(Modbus):

    def __init__(self, mbap_request_):
        super().__init__()
        self.function_code, *self.data = mbap_request_


class Response(Modbus):

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