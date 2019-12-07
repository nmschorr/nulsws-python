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

class NulsWebsocket(object):
    def __init__(self):
        myprint("the url:  ", websock_url1)

    async def initial_connect(self, json_str):  #only for initial connection type 1
        try:
            connection = await websocket_connect(websock_url1)
                ### only continue if connection is ok

            response_awaited = await connection.write_message(json_str)

            if (response_awaited is not None) and (len(response_awaited) > 0):
                myprint("Got response in 1: ", response_awaited)
            myprint("Waiting for data in 1...")

            answer1 = await connection.read_message()
            result = check_answer(answer1)
            if result == 1:
                print("all is good, was 1, ok to continue")
                time.sleep(2)
                return connection
            else:
                print("broken")
                exit(1)
        except BaseException as e:
            print(e)


    async def ws_runner_a(self, jsonstr):
        connection_main = await self.initial_connect(jsonstr)     # in same
        print("here now a")
        print("c: ", str(connection_main.start_time))
        connection_main.start_time
        return connection_main

    async def client_connect2(self, connection, json_str):
        answer_b = None
        response_awaited = await connection.write_message(json_str)
        if (response_awaited is not None) and (len(response_awaited) > 0):
            myprint("Got response in client_connect2: ", response_awaited)
        myprint("Waiting for data in client_connect2...")
        print("c: ", str(connection.start_time))
        answer_b = await connection.read_message()
        if answer_b is not None:
            print("Got answer in b: ", answer_b)


    async def ws_runner_b(self, connection, jsonstr):
        await self.client_connect2(connection, jsonstr)     # in same
        print("here now b")

    def prep_run(self, json_st_a, json_st_b):
        myprint('sending: \n\n', json_st_a)
        connection_a = run(self.ws_runner_a(json_st_a))   # starts event loop
        time.sleep(3)
        myprint('sending: \n\n', json_st_b)
        if connection_a:
            print("we have a live connection")
        run(self.ws_runner_b(connection_a, json_st_b))   # starts event loop

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
        self.prep_run(json_str_a, json_str_b)

# if __name__ == '__main__':

mtype = 3  # either 3, 5, or 7
n = NulsWebsocket()
n.main(mtype)

## -- enter user data via the library file nulsws_msgtype<1,2,3>.py

