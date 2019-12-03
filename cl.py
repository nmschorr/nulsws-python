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
import NulsWSLib as nw
import nulsuserone as nu

class NulsWebsocket(object):
    def __init__(self):
        nw.myprint("the url:  ", nu.my_url)

    async def connect_serve1(self, t_vars):
        try:
            ztype, zcomp, good_msg = nw.prep_async(t_vars)
            connection = await websocket_connect(nu.my_url)
                ### only continue if connection is ok
            json_str = nw.prep_data1(ztype, zcomp)

            nw.myprint('sending: ', json_str)
            resp = await connection.write_message(json_str)
            if (resp is not None) and (len(resp) > 0):
                nw.myprint("Got response: ", resp)
            nw.myprint("Waiting for data...")
            answer = await connection.read_message()
            result = nw.check_answer(answer)
            if result == 1:
                print("all is good, was 1, ok to continue")
        except WebSocketClosedError as e:
            print(e)

    async def ws_runner(self, mtype, vars):
        #if mtype == 1:
        await self.connect_serve1(vars)                       # in same dir as

    def main(self):
        args_list = [nu.comp_type, str(nu.comp_int)]
        run(self.ws_runner(nu.mtype, args_list), debug=True)   # starts event loop


n = NulsWebsocket()
n.main()
## -- enter user data via the library file nulsuserone.py

