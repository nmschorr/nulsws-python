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
from Libraries import nulsws_REQUEST as mw
from UserSettings.nulsws_USER_PARAMS import *


class NulsWebsocket(object):
    def __init__(self):
        myprint("the url:  ", websock_url)
        self.mindex = 0
        self.s_time = 1
        self.ORIG_RUNLIST = []
        self.rundict = {}
        self.MSG_TYPE = 0

    async def REGULAR_req(self, websock_connct: WebSocketClientConnection, j_reg_dict):
        json_REG = json_dumps(j_reg_dict)
        await websock_connct.write_message(json_REG)      # 2 WRITE
        json_prt(json_REG, "\n* * * REGULAR message going out: \n")
        #await a_sleep(self.s_time)
        read_REG= await websock_connct.read_message()  # 3 READ
        await a_sleep(self.s_time)
        if len(read_REG) > 0:
            json_prt(read_REG, "   -----------> ! ! ! REGULAR response received: ")
        myprint("--------------end previous / begin next request--------------------------------")

    async def negotiate_list(self, json_negotiate, m_indx, runlist, mtpe=3):
        connection = await websocket_connect(websock_url)  # 1) CONNECT
        #await a_sleep(self.s_time)
        while not connection:
            await a_sleep(self.s_time)
        jd = json_dumps(json_negotiate)
        json_prt(json_negotiate, "* * * First message going out- NEGOTIATE: \n")
        await connection.write_message(jd)  # 2) WRITE
        #await a_sleep(self.s_time)

        negotiate_result = await connection.read_message()  # 3 READ
        #await a_sleep(self.s_time)
        json_prt(negotiate_result, "--------- ! ! ! NEGOTIATE response received: ")
        myprint("------end Negotiate----------------------------------------")

        for run_item in runlist:
            m_indx += 1
            print("starting this item: ", run_item)
                # TEST ONLY SECTION -------------------------->
                # if self.msg_type == 77:    # this runs register api
                #     await self.REGULAR_req(connection, run_item)
                # END TEST ONLY SECTION ----------------------
            if mtpe == 3:
                main_request = mw.prep_REQUEST(m_indx, run_item)   ##TEST ONLY PUT BACK WHEN DONE
                await self.REGULAR_req(connection, main_request)

    def main(self, mtpe, runlist):
        self.mindex += 1
        if mtpe == 3:
            j_negotiate = mw.prep_NEGOTIATE_request(self.mindex)  # must be done first
            asyncio_run(self.negotiate_list(j_negotiate, self.mindex, runlist, mtpe)) # starts event


if __name__ == '__main__':
    RUN_LIST = [AC_GET_ACCOUNT_BYADDRESS, AC_GET_ALL_ADDRESS_PREFIX]
    MSG_TYPE = 3            # 3 is request, 99 is test, 77 is negotiate only
    n = NulsWebsocket()
    n.main(MSG_TYPE, RUN_LIST)



# json_main_type = mw.prep_data_REQUEST_type5()
# json_main_type = mw.prep_data_REQUEST_type7()
# if mtpe == 99:   # test dev only
#     for run_item in runlist:
#         print("starting this item: ", run_item)
# if mtpe == 77:  # test only
#     self.msg_type = 77
#     j = make_nulsws_REGISTER_method(m_indx)
#     self.commander_by_list(json_negotiate, m_indx, [j])  #big list