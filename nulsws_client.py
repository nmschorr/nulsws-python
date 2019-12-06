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
from nulsws_library import *
from nulsws_msgtype1 import websock_url1, compress_tp1, comp_int1

import nulsws_msgtype1 as m1

class NulsWebsocket(object):
    def __init__(self):
        myprint("the url:  ", websock_url1)

    async def client_connect(self, json_str, deb=False):
        try:
            connection = await websocket_connect(websock_url1)
                ### only continue if connection is ok

            response_awaited = await connection.write_message(json_str)

            if (response_awaited is not None) and (len(response_awaited) > 0):
                myprint("Got response: ", response_awaited)
            myprint("Waiting for data...")

            answer = await connection.read_message()
            result = check_answer(answer)
            if result == 1:
                print("all is good, was 1, ok to continue")
        except WebSocketClosedError as e:
            print(e)

    async def ws_runner(self, args_list, jsonstr):
        await self.client_connect(jsonstr)                       # in same
        # dir as

    def prep_run(self, args_list):
        ztype, zcomp, good_msg = prep_async(args_list)
        json_str = prep_data1(ztype, zcomp)
        myprint('sending: \n\n', json_str)
        run(self.ws_runner(args_list, json_str))   # starts event loop

    def main(self, mtype):
        if mtype == 1:
            compr_type = compress_tp1
        args = [mtype, [compr_type, str(comp_int1)]]
        self.prep_run(args)  # starts event loop


if __name__ == '__main__':
    mtype = 1
    n = NulsWebsocket()
    n.main(mtype)
## -- enter user data via the library file nulsuserone.py

