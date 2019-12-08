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


from asyncio import run
from tornado.websocket import websocket_connect  #, WebSocketClosedError
from nulsws_library import prep_data_type1, prep_data_type3, myprint, check_json_answer
from nulsws_msgtype1 import websock_url1
from nulsws_msgtype_register import make_nulsws_reg
from tornado.websocket import WebSocketClientConnection
import asyncio

class NulsWebsocket(object):
    def __init__(self):
        myprint("the url:  ", websock_url1)
        self.mindex = 0

    async def first_connect(self, json_cnnect, the_tup):
        print("inside first_connect")
        conntn = await websocket_connect(websock_url1)   # 1) CONNECT
        await asyncio.sleep(2)
        response_awaiteda = await conntn.write_message(json_cnnect) # 2) WRITE
        print("got response_awaiteda for write response...", response_awaiteda)
        await asyncio.sleep(1.5)

        await conntn.read_message()    # 3 READ
        await asyncio.sleep(1)
        await self.connect_actual_msg(conntn, the_tup)

    def nms_callback(self, x):
        print("inside nms callback: ", x)


    async def connect_actual_msg(self, websock_connct: WebSocketClientConnection, a_tup):
        print("inside connect_actual_msg")
        print("sending: ", a_tup[0])
        print(await websock_connct.write_message(a_tup[0])) # 2) WRITE
        await asyncio.sleep(1)
        # websock_connct.final_callback(self.nms_callback("final callback msg read in two"))
        print(await websock_connct.read_message(self.nms_callback("msg read in two")) ) # 3
        await asyncio.sleep(1)

        print("inside part two connect_actual_msg, sending: ")
        print(a_tup[1])
        a = a_tup[1]
        print(await websock_connct.write_message(a_tup[1])) # 2) WRITE
        await asyncio.sleep(1)
        read_msg_b = await websock_connct.read_message(self.nms_callback("msg read b"))  # 3 READ
        await asyncio.sleep(1)
        myprint("Got response in ws_runner_main part two: \n", read_msg_b)
        myprint("Finished and exiting.")

    def commander(self, jconnect, mytup):
        run(self.first_connect(jconnect, mytup))   # starts event loop

    def main(self, mtpe):
        self.mindex += 1
        mind = self.mindex
        json_main_type = None
        json_connect_type = prep_data_type1()
        json_reg_type = make_nulsws_reg(mind)

        if mtpe == 3:
            json_main_type = prep_data_type3()
        if mtpe == 5:
            pass
            # json_main_type = prep_data_type5()
        if mtpe == 7:
            pass
            # json_main_type = prep_data_type7()
        json_tup = (json_reg_type, json_main_type)
        self.commander(json_connect_type, json_tup)


if __name__ == '__main__':
    mtype = 3                       # either 3, 5, or 7, or 99 for r
    n = NulsWebsocket()
    n.main(mtype)


## -- enter user data via the library file nulsws_msgtype<1,2,3>.py


