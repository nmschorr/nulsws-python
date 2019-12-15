#!usr/bin/python3.7
# This file right now is the client only.
# author:  Nancy M Schorr, for Nuls
# December 2, 2019

# for applications using Connector module there are the  other 2 public and admin
# private only for private means that only registered modules inside the system can use that method
# public means that every  application can run that methid and admin means
# that methids will be available in the admin port opened by connector
# see, connector opens 2 ports to exrternal apps
# one for normal use and another for admin
# check module.ncf of Connector
# port 0 means it is not openend by default

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


from asyncio import run as asyncio_run
from asyncio import sleep as a_sleep
from tornado.websocket import websocket_connect, WebSocketClientConnection  # WebSocketClosedError
from Libraries.nulsws_library import *
from UnusedSoFar.nulsws_USER_static_settings import *
from UnusedSoFar.nulsws_USER_settings import MSG_TYPE, RUN_LIST
from Libraries import nulsws_REQUEST as mw


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
            #await asyncio_sleep(self.s_time)
        read_REG= await websock_connct.read_message(self.nms_callback(""))  # 3 READ
            #await asyncio_sleep(self.s_time)
        if len(read_REG) > 10:
            json_prt(read_REG, "   -----------> ! ! ! REGULAR response received: ")
        myprint("--------------end previous / begin next request--------------------------------")

    async def negotiate_list(self, json_negotiate, m_indx, runlist):
        connection = await websocket_connect(websock_url)  # 1) CONNECT
        await a_sleep(self.s_time)
        while not connection:
            await a_sleep(self.s_time)
        jd = json_dumps(json_negotiate)
        json_prt(json_negotiate, "* * * First message going out- NEGOTIATE: ")
        await connection.write_message(jd)  # 2) WRITE
        await a_sleep(self.s_time)

        negotiate_result = await connection.read_message()  # 3 READ
        await a_sleep(self.s_time)
        json_prt(negotiate_result, "--------- ! ! ! NEGOTIATE response received: ")
        myprint("------end Negotiate----------------------------------------")

        for run_item in runlist:
            print("starting this item: ", run_item)
            main_request = mw.prep_REQUEST(m_indx, run_item)
            await self.REGULAR_req(connection, main_request)

    def commander_by_list(self, j_negotiate, m_indx, runlist):  #multiples
        asyncio_run(self.negotiate_list(j_negotiate, m_indx, runlist)) # starts event

    def main(self, mtpe):
        # we always do type 1 just before anything
        self.mindex += 1
        m_indx = self.mindex
        json_negotiate = mw.prep_NEGOTIATE_request(m_indx)  #dict

        if mtpe == 3:
            self.commander_by_list(json_negotiate, m_indx, RUN_LIST)  #big list

        # json_main_type = mw.prep_data_REQUEST_type5()
        # json_main_type = mw.prep_data_REQUEST_type7()


if __name__ == '__main__':
    n = NulsWebsocket()
    n.main(MSG_TYPE)

