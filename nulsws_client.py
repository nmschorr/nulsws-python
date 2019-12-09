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
from nulsws_library import *
from nulsws_usersets_negt_type1 import websock_url_negt
from tornado.websocket import WebSocketClientConnection
from json import dumps as json_dumps

from nulsws_staticvals import type_name_dict

class NulsWebsocket(object):
    def __init__(self):
        myprint("the url:  ", websock_url_negt)
        self.mindex = 0



    def nms_callback(self, x):
        print("inside nms callback: ", x)


    async def connect_actual_msg(self, websock_connct: WebSocketClientConnection, a_tup):
        json_a = a_tup[0]
        json_b = a_tup[1]
        print("\ninside part two connect_actual_msg, sending: ")
        print(json_a)
        amsg = await websock_connct.write_message(json_a)      # 2 WRITE
        await asyncio_sleep(2)
        print("msg rec: ", amsg)
        read_msg_a = await websock_connct.read_message(self.nms_callback(""))  # 3 READ
        await asyncio_sleep(3)
        myprint("Got response in ws_runner_main part two: \n", read_msg_a)

        myprint("sending part two.")
        bmsg = await websock_connct.write_message(json_b)      # 2 WRITE
        await asyncio_sleep(2)
        print("msg rec: ", bmsg)
        read_msg_b= await websock_connct.read_message(self.nms_callback(""))  # 3 READ
        await asyncio_sleep(2)
        myprint("Got response in ws_runner_main part two: \n", read_msg_b)
        myprint("Finished and exiting.")

    async def negotiate(self, json_negotiate, the_tup):
        print("inside negotiate")
        connection = await websocket_connect(websock_url_negt)   # 1) CONNECT
        await asyncio_sleep(2)
        print("\nnegotiate writing this: ")
        print(json_dumps(json_negotiate, indent=4), "\n")

        response_awaiteda = await connection.write_message(json_negotiate) # 2) WRITE
        print("negotiate got response_awaiteda for write response...", response_awaiteda)
        await asyncio_sleep(1.5)

        await connection.read_message()    # 3 READ
        await asyncio_sleep(1)
        await self.connect_actual_msg(connection, the_tup)

    def commander(self, jconnect, mytup):
        asyncio_run(self.negotiate(jconnect, mytup))   # starts event loop

    def main(self, mtpe):
        # we always do type 1 just before anything
        import nulsws_msgs_others as mw
        from nulsws_msgtype_register import make_nulsws_REGISTER_method
        self.mindex += 1
        mind = self.mindex

        json_main_type = type_name_dict.get(mtpe)
        json_negotiate = mw.prep_NEGOTIATE_data_type1(mind)
        json_register =  make_nulsws_REGISTER_method(mind)

        if mtpe == 3:
            json_main_type = mw.prep_data_REQUEST_type3(mind)
        if mtpe == 5:
            pass
            # json_main_type = mw.prep_data_REQUEST_type5()
        if mtpe == 7:
            pass
            # json_main_type = mw.prep_data_REQUEST_type7()
        a_tup = (json_register, json_main_type)
        print("\nsending: json_negotiate", json_dumps(json_negotiate, indent=3))
        print("\nsending: json_register", json_dumps(json_register, indent=3))
        print("\nsending: json_main_type ", json_dumps(json_main_type, indent=3))
        self.commander(json_negotiate, a_tup)


if __name__ == '__main__':
    mtype = 3                       # either 3, 5, or 7, or 99 for r
    n = NulsWebsocket()
    n.main(mtype)


## -- enter user data via the library file nulsws_msgtype<1,2,3>.py


