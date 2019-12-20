#!usr/bin/python3.7
# This file right now is the client only.
# author:  Nancy M Schorr, for Nuls
# December 2, 2019

# for applications using Connector module there are the  other 2 public and admin
# private only for private means that only registered modules inside the system can use that method
# public means that every  application can run that method and admin means
# that methods will be available in the admin port opened by connector
# see, connector opens 2 ports to external apps
# one for normal use and another for admin
# check module.ncf of Connector
# port 0 means it is not opened by default

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
# Note: Maybe don't use typing.Dict - it can cause json problems when converted

import json
from asyncio import run as asyncio_run
from asyncio import sleep as a_sleep
from tornado.websocket import websocket_connect, WebSocketClientConnection  # WebSocketClosedError

from Libraries.Constants.CLASSES import nulsws_c_labels as nlab
from Libraries import nulsws_REQUEST as mw
from UserSettings.nulsws_SET import *
import Libraries.nulsws_library as nulib
from Libraries.nulsws_library import Nulsws_Library as nuLIB

class NulsWebsocket(nuLIB):

    def __init__(self):
        nw = nuLIB()
        self.nw = nw
        nw.myprint("the url:  ", websock_url)
        mindex = 0
        self.mindex = mindex
        self.s_time = .7
        self.ORIG_RUNLIST = []
        self.rundict = {}
        self.MSG_TYPE = 0
        self.json_prt = nuLIB.json_prt()
        self.json_dumps = nuLIB.json_dumps()
        self.myprint = nuLIB.myprint()

    async def REGULAR_req(self, websock_connct: WebSocketClientConnection, j_reg_dict):
        json_REG = json.dumps(j_reg_dict)
        await websock_connct.write_message(json_REG)  # 2 WRITE
        self.json_prt(json_REG, "\n* * * REGULAR message going out: \n")
        #await a_sleep(self.s_time)
        read_REG = await websock_connct.read_message()  # 3 READ
        await a_sleep(self.s_time)
        if len(read_REG) > 0:
            self.json_prt(read_REG, "   -----------> ! ! ! REGULAR response received: ")
        self.myprint("--------------end previous / begin next request--------------------------------")

    async def negotiate_list(self, top_plus_mid_dict, m_indx, runlist, mtpe=3):
        connection = await websocket_connect(websock_url)  # 1) CONNECT
        #await a_sleep(self.s_time)
        while not connection:
            await a_sleep(self.s_time)
        jd = self.json_dumps(top_plus_mid_dict)
        self.nw.json_prt(top_plus_mid_dict, "* * * First message going out- NEGOTIATE: \n")
        await connection.write_message(jd)  # 2) WRITE
        #await a_sleep(self.s_time)

        negotiate_result = await connection.read_message()  # 3 READ
        await a_sleep(self.s_time)
        self.nw.json_prt(negotiate_result, "--------- ! ! ! NEGOTIATE response received: ")
        self.myprint("------end Negotiate----------------------------------------")

        for run_item in runlist:
            m_indx += 1
            print("starting this item: ", run_item)
                                # TEST ONLY SECTION -------------------------->
                                # if self.msg_type == 77: await self.REGULAR_req(connection, run_item)   # this runs register api
                                # END TEST ONLY SECTION ----------------------
            if mtpe == 3:
                main_request = mw.prep_REQUEST(m_indx, run_item)  ##TEST ONLY PUT BACK WHEN DONE
                await self.REGULAR_req(connection, main_request)

    def main(self, runlist, msg_type=3):
        mtpe = msg_type
        self.mindex += 1
        myindx = self.mindex
        if mtpe == 3:  # if a regular request Nulstar type 3
            top_pls_middle_dict = mw.prep_NEGOTIATE_request(myindx)  # must be done first
            asyncio_run(
                self.negotiate_list(
                    top_pls_middle_dict, myindx, runlist, mtpe))  # starts event


if __name__ == '__main__':
    n = nlab.nulsws_C_Labels

    RUNLIST1 = [n.AC_GET_ACCOUNT_BYADDRESS, n.AC_GET_ALL_ADDRESS_PREFIX, n.AC_GET_ACCOUNT_LIST,
                n.AC_GET_ADDRESS_LIST, n.AC_GET_ADDRESS_PREFIX_BY_CHAINID, n.AC_GET_ALL_ADDRESS_PREFIX,
                n.AC_GET_ALL_PRIKEY, n.AC_GET_ALIASBY_ADDRESS]

    RUNLIST2 = [
        n.AC_EXPORT_ACCOUNT_KEYSTORE, n.AC_EXPORT_KEYSTORE_JSON, n.AC_GET_ACCOUNT_BYADDRESS,
        n.AC_GET_ACCOUNT_LIST, n.AC_GET_ADDRESS_LIST, n.AC_GET_ADDRESS_PREFIX_BY_CHAINID,
        n.AC_GET_ALIASBY_ADDRESS, n.AC_GET_ALL_ADDRESS_PREFIX, n.AC_GET_ALL_PRIKEY,
        n.AC_GET_ENCRYPTED_ADDRESS_LIST, n.AC_GET_MULTI_SIGN_ACCOUNT, n.AC_GET_PRIKEY, n.AC_GET_PUBKEY]

    RUNLIST3 = [n.GET_LATEST_BLOCKHEADERS,
                n.GET_LATEST_ROUND_BLOCKHEADERS, n.GET_NETWORK_GROUP, n.GET_NONCE, n.GET_OTHERCTX,
                n.GET_REGISTERED_CHAIN_INFO_LIST, n.GET_REGISTERED_CHAIN_MESSAGE, n.GET_ROUND_BLOCKHEADERS,
                n.GET_STATUS, n.GET_VERSION, n.INFO, n.LATEST_BLOCK, n.LATEST_BLOCKHEADER,
                n.LATEST_BLOCKHEADER_PO,
                n.LATEST_HEIGHT]

    #RUN_LIST = RUNLIST2
    RUN_LIST = RUNLIST1
    message_type = 3  # 3 is request, 99 is test, 77 is negotiate only

    nws = NulsWebsocket()
    nws.main(RUN_LIST, message_type)



# old code for testing:
# json_main_type = mw.prep_data_REQUEST_type5()
# json_main_type = mw.prep_data_REQUEST_type7()
# if mtpe == 99:   # test dev only
#     for run_item in runlist:
#         print("starting this item: ", run_item)
# if mtpe == 77:  # test only
#     self.msg_type = 77
#     j = make_nulsws_REGISTER_method(m_indx)
#     self.commander_by_list(top_plus_mid_dict, m_indx, [j])  #big list
