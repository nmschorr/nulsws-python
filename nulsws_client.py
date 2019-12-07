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
import time
# import nulsws_msgtype1 as m1
from nulsws_staticvals import reg

class NulsWebsocket(object):
    def __init__(self):
        myprint("the url:  ", websock_url1)

    async def ws_runner_main(self, jsona, jsonb):
        print("inside ws_runner_main")
        connection = await websocket_connect(websock_url1)
        time.sleep(1)

        response_awaiteda = await connection.write_message(jsona)
        print("waiting for second read response...")

        if (response_awaiteda is not None) and (len(str(response_awaiteda)) > 0):
            myprint("Got response in client_connect2: ", response_awaiteda)
        answera = await connection.read_message()
        result = check_answer(answera)

        response_awaited_b = await connection.write_message(jsonb)
        if (response_awaited_b is not None) and (len(response_awaited_b) > 0):
            myprint("Got response in client_connect_b: ", response_awaited_b)

        answer_b = await connection.read_message()
        print("waiting for second read response...")

        if answer_b is not None:
            print("Got answer in b: ", answer_b)


    def first_runner(self, json_st_a, json_st_b):
        cc = run(self.ws_runner_main(json_st_a, json_st_b))   # starts event loop

    def main(self, mtpe):
        json_str_b = ''
        json_str_a = prep_data_type1()
        if mtpe == 3:
            json_str_b = prep_data_type3()
        if mtpe == 5:
            pass
            # json_str_b = prep_data_type5()
        if mtpe == 7:
            pass
            # json_str_b = prep_data_type7()
        self.first_runner(json_str_a, json_str_b)


# if __name__ == '__main__':
mtype = 3  # either 3, 5, or 7
n = NulsWebsocket()
n.main(mtype)


## -- enter user data via the library file nulsws_msgtype<1,2,3>.py


