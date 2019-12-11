#!usr/bin/python3.7

# Messages have a common structure composed of six fields:
# •  ProtocolVersion: version the service to understand,2 numbers, major/minor
# •  MessageID: identifies a request.
# •  Timestamp:  Number  of  seconds  since  epoch January 1,1970
# •  TimeZone: The time zone where the request was originated
# •  MessageType: The message type, these are specified on section 3
# •  MessageData: A Json object with the message payload

# the first object that should be sent - only if the negotiation is ok service may process
# further requests -otherwise a NegotiateConnectionResponse object should be received with
# Status set to 0 (Failure) and disconnect immediately.

# "MessageType": "NegotiateConnection",
# "MessageData": {
#     "CompressionAlgorithm": "zlib",
#     "CompressionRate": "3"

## -- Enter your custom settings data via the library file nulsuserone.py
# Note: Don't use typing.Dict - it can cause json problems when converted
# This file right now is the client only.
# author:  Nancy M Schorr, for Nuls
# December 2, 2019


from asyncio import run as asyncio_run
from asyncio import sleep as asyncio_sleep
from tornado.websocket import websocket_connect  # WebSocketClosedError
from tornado.websocket import WebSocketClientConnection
from nulsws_library import *
from nulsws_USER_static_settings import *
import nulsws_REQUEST as mw
from nulsws_USER_CHOICE import MSG_TYPE

class NulsWebsocket(object):
    def __init__(self):
        myprint("the url:  ", websock_url)
        self.mindex = 0
        self.s_time = 1

    def nms_callback(self, x):
        myprint(x)

    async def REGULAR_req(self, websock_connct: WebSocketClientConnection, j_reg_dict):
        json_REG = json_dumps(j_reg_dict)
        json_prt(json_REG, "\n* * * REGULAR message going out: ")
        await websock_connct.write_message(json_REG)      # 2 WRITE
        await asyncio_sleep(self.s_time)
        read_REG= await websock_connct.read_message(self.nms_callback(""))  # 3 READ
        await asyncio_sleep(self.s_time)
        if len(read_REG) > 10:
            json_prt(read_REG, "------- ! ! ! REGULAR response received: ")
        myprint("--------------end Regular request--------------------------------")

    async def negotiate(self, json_negotiate, main_request):
        connection = await websocket_connect(websock_url)   # 1) CONNECT
        await asyncio_sleep(self.s_time)
        while not connection:
            await asyncio_sleep(self.s_time)
        jd = json_dumps(json_negotiate)
        json_prt(json_negotiate, "* * * First message going out- NEGOTIATE: ")
        await connection.write_message(jd)              # 2) WRITE
        await asyncio_sleep(self.s_time)

        negotiate_result = await connection.read_message()    # 3 READ
        await asyncio_sleep(self.s_time)
        json_prt(negotiate_result, "--------- ! ! ! NEGOTIATE response received: ")
        myprint("------end Negotiate----------------------------------------")
        await self.REGULAR_req(connection, main_request)

    def commander(self, j_negotiate, main_request):
        asyncio_run(self.negotiate(j_negotiate, main_request)) # starts event

    def main(self, mtpe):
        # we always do type 1 just before anything
        self.mindex += 1
        m_indx = self.mindex
        main_request_d: dict = dict()
        json_negotiate = mw.prep_NEGOTIATE_data_type1(m_indx)  #dict
        #json_register =  make_nulsws_REGISTER_method(mind)

        if mtpe == 3:
            main_request_d = mw.prep_REQUEST_ONESIE_NO_params(m_indx) #dict

        # if mtpe == 5:   # not implemented yet
            # json_main_type = mw.prep_data_REQUEST_type5()
        # if mtpe == 7:   # not implemented yet
            # json_main_type = mw.prep_data_REQUEST_type7()
        self.commander(json_negotiate, main_request_d)


if __name__ == '__main__':
    n = NulsWebsocket()
    n.main(MSG_TYPE)

