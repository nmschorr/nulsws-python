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
from tornado.websocket import websocket_connect, WebSocketClosedError
from nulsws_library import prep_data_type1, prep_data_type3, myprint, check_answer
from nulsws_msgtype1 import websock_url1
from nulsws_msgtype_register import nulsws_register
import time
# import nulsws_msgtype1 as m1
from nulsws_staticvals import reg

import tornado
from tornado.websocket import WebSocketClientConnection


class NulsWebsocket(object):
    def __init__(self):
        myprint("the url:  ", websock_url1)


    async def get_connection(self, json_cnnect, json_b_msg):
        print("inside get_connection")
        conntn = await websocket_connect(websock_url1)   # 1) CONNECT
        response_awaiteda = await conntn.write_message(json_cnnect) # 2) WRITE
        print("got response_awaiteda for write response...", response_awaiteda)

        read_msg = conntn.read_message()    # 3 READ
       # read_result = check_answer(read_msg)    # 4 CHECK EVALUATE ANSWER
       # myprint("Got response in get_connection: ", read_result)
        await self.ws_runner_main(conntn, json_b_msg)

    async def ws_runner_main(self, websock_connct: WebSocketClientConnection, jsonb: str):
        print("inside ws_runner_main")
        resp_await_main = await websock_connct.write_message(jsonb) # 2) WRITE
        print("got ws_runner_main for write response...", resp_await_main)
        read_msg = websock_connct.read_message()    # 3 READ
        read_result = check_answer(read_msg)    # 4 CHECK EVALUATE ANSWER
        myprint("Got response in ws_runner_main: ", read_result)
        myprint("Finished and exiting.")

    def commander(self, json_st_a, json_st_b):
        run(self.get_connection(json_st_a, json_st_b))   # starts event loop

    def main(self, mtpe):
        json_connect_type = prep_data_type1()
        if mtpe == 99:
            json_main_type = nulsws_register()

        if mtpe == 3:
            json_main_type = prep_data_type3()
        if mtpe == 5:
            pass
            # json_main_type = prep_data_type5()
        if mtpe == 7:
            pass
            # json_main_type = prep_data_type7()
        self.commander(json_connect_type, json_main_type)


# if __name__ == '__main__':
mtype = 3                       # either 3, 5, or 7, or 99 for r
n = NulsWebsocket()
n.main(mtype)


## -- enter user data via the library file nulsws_msgtype<1,2,3>.py


