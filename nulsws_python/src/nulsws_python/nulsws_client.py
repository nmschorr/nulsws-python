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
import nulsws_python.src.nulsws_python.nulsws_library as nlib
from nulsws_python.src.nulsws_python.user_settings.nulsws_settings_two import *
from nulsws_python.src.nulsws_python.constants.nulsws_api_labels import NulswsApiLabel


class NulsWebsocket(object):

    def __init__(self):
        mindex = 0
        self.mindex = mindex
        self.s_time = .7
        self.ORIG_RUNLIST = []
        self.rundict = {}
        self.MSG_TYPE = 0
        self.myprint = nlib.NulswsLibrary.myprint
        self.myprint("the url:  ", websock_url)
        self.json_prt = nlib.NulswsLibrary.json_prt

    async def regular_request(self, websock_cont: WebSocketClientConnection, j_reg_dict):
        json_reg = json.dumps(j_reg_dict)
        await websock_cont.write_message(json_reg)  # 2 WRITE
        self.json_prt(json_reg, "\n* * * REGULAR message going out: \n")
        # await a_sleep(self.s_time)
        read_reg = await websock_cont.read_message()  # 3 READ
        await a_sleep(self.s_time)
        if len(read_reg) > 0:
            self.json_prt(read_reg, "   -----------> ! ! ! REGULAR response received: ")
        nlib.NulswsLibrary.myprint("--------------end previous / begin next "
                                   "request--------------------------")

    async def negotiate_list(self, top_plus_mid_dict, m_indx, run_list, mtpe=3):
        connection = await websocket_connect(websock_url)  # 1) CONNECT
        # await a_sleep(self.s_time)
        while not connection:
            await a_sleep(self.s_time)
        jd = json.dumps(top_plus_mid_dict)
        self.json_prt(top_plus_mid_dict, "* * * First message going out- NEGOTIATE: \n")

        await connection.write_message(jd)  # 2) WRITE
        # await a_sleep(self.s_time)

        negotiate_result = await connection.read_message()  # 3 READ
        await a_sleep(self.s_time)
        self.json_prt(negotiate_result, "--------- ! ! ! NEGOTIATE response received: ")
        self.myprint("------end Negotiate----------------------------------------")

        for run_item in run_list:
            m_indx += 1
            print("starting this item: ", run_item)
            # TEST ONLY SECTION -------------------------->
            # if self.msg_type == 77: await self.regular_request(connection, run_item)
            # this runs register api
            # END TEST ONLY SECTION ----------------------
            if mtpe == 3:
                main_request = prep_request(m_indx, run_item)  # TEST ONLY PUT BACK WHEN DONE
                await self.regular_request(connection, main_request)

    def main(self, rr_list, msg_type=3):
        mtpe = msg_type
        #self.mindex += 1
        myindx = self.mindex
        if mtpe == 3:  # if a regular request Nulstar type 3
            top_pls_middle_dict = prep_negotiate_request(myindx)  # must be done first
            asyncio_run(
                self.negotiate_list(
                    top_pls_middle_dict, myindx, rr_list, mtpe))  # starts event


if __name__ == "__main__":
    from nulsws_python.src.nulsws_python.nulsws_request import prep_request, prep_negotiate_request
    b = NulswsApiLabel().ApiLabelDict


    runlist_1 = [ b['AC_GET_ACCOUNT_BYADDRESS'], b['AC_GET_ALL_ADDRESS_PREFIX'], b['AC_GET_ACCOUNT_LIST'],
                 b['AC_GET_ADDRESS_LIST'], b['AC_GET_ADDRESS_PREFIX_BY_CHAINID'], b['AC_GET_ALL_ADDRESS_PREFIX'],
                 b['AC_GET_ALL_PRIKEY'], b['AC_GET_ALIASBY_ADDRESS'] ]

    runlist_2 = [
        b['AC_EXPORT_ACCOUNT_KEYSTORE'], b['AC_EXPORT_KEYSTORE_JSON'], b['AC_GET_ACCOUNT_BYADDRESS'],
        b['AC_GET_ACCOUNT_LIST'], b['AC_GET_ADDRESS_LIST'], b['AC_GET_ADDRESS_PREFIX_BY_CHAINID'],
        b['AC_GET_ALIASBY_ADDRESS'], b['AC_GET_ALL_ADDRESS_PREFIX'], b['AC_GET_ALL_PRIKEY'],
        b['AC_GET_ENCRYPTED_ADDRESS_LIST'], b['AC_GET_MULTI_SIGN_ACCOUNT'], b['AC_GET_PRIKEY'], 
        b['AC_GET_PUBKEY'] ]

    runlist_3 = [b['GET_LATEST_BLOCKHEADERS'],
                 b['GET_LATEST_ROUND_BLOCKHEADERS'], b['GET_NETWORK_GROUP'], b['GET_NONCE'], b['GET_OTHERCTX'],
                 b['GET_REGISTERED_CHAIN_INFO_LIST'], b['GET_REGISTERED_CHAIN_MESSAGE'], b['GET_ROUND_BLOCKHEADERS'],
                 b['GET_STATUS'], b['GET_VERSION'], b['INFO'], b['LATEST_BLOCK'], b['LATEST_BLOCKHEADER'],
                 b['LATEST_BLOCKHEADER_PO'], b['LATEST_HEIGHT'] ]

    # RUN_LIST = runlist_2
    runlist = runlist_1 + runlist_2 + runlist_3
    message_type = 3  # 3 is request, 99 is test, 77 is negotiate only

    nws = NulsWebsocket()
    nws.main(runlist, message_type)
