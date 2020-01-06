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

<<<<<<< HEAD:client/nulsws_client.py
import libraries.constants.nulsws_api_labels as apilab
import libraries.nulsws_library as lib
from libraries import nulsws_request as reqs
from user_settings.nulsws_settings import *

class NulsWebsocket(object):
    def __init__(self):
=======
import Libraries.nulsws_library as lib2
from Libraries.nulsws_library import Nulsws_Library as nw
from Libraries.nulsws_library import Nulsws_Library as lib

from Libraries import nulsws_REQUEST as reqs
from UserSettings.nulsws_SET import *

class NulsWebsocket():


    def __init__(self):
        super().__init__()
>>>>>>> master:ClientApp/nulsws_RUNNER_client.py
        mindex = 0
        self.mindex = mindex
        self.s_time = .7
        self.ORIG_RUNLIST = []
        self.rundict = {}
        self.MSG_TYPE = 0
<<<<<<< HEAD:client/nulsws_client.py
        self.json_dumps = lib.json_dumps
        self.myprint = lib.NulswsLibrary.myprint
        self.myprint("the url:  ", websock_url)
        self.json_prt = lib.NulswsLibrary.json_prt

    async def REGULAR_req(self, websock_cont: WebSocketClientConnection, j_reg_dict):
=======
        print("the url:  ", websock_url)
        self.json_prt = lib.json_prt
        
    async def REGULAR_req(self, websock_connct: WebSocketClientConnection, j_reg_dict):
>>>>>>> master:ClientApp/nulsws_RUNNER_client.py
        json_REG = json.dumps(j_reg_dict)
        await websock_cont.write_message(json_REG)  # 2 WRITE
        self.json_prt(json_REG, "\n* * * REGULAR message going out: \n")
        #await a_sleep(self.s_time)
        read_REG = await websock_cont.read_message()  # 3 READ
        await a_sleep(self.s_time)
        if len(read_REG) > 0:
            self.json_prt(read_REG, "   -----------> ! ! ! REGULAR response received: ")
        lib.myprint("--------------end previous / begin next request--------------------------------")

    async def negotiate_list(self, top_plus_mid_dict, m_indx, runlist, mtpe=3):
        connection = await websocket_connect(websock_url)  # 1) CONNECT
        #await a_sleep(self.s_time)
        while not connection:
            await a_sleep(self.s_time)
<<<<<<< HEAD:client/nulsws_client.py
        jd = self.json_dumps(top_plus_mid_dict)
        self.json_prt(top_plus_mid_dict, "* * * First message going out- NEGOTIATE: \n")
=======
        jd = json.dumps(top_plus_mid_dict)
        lib.json_prt(top_plus_mid_dict, "* * * First message going out- NEGOTIATE: \n")
>>>>>>> master:ClientApp/nulsws_RUNNER_client.py
        await connection.write_message(jd)  # 2) WRITE
        #await a_sleep(self.s_time)

        negotiate_result = await connection.read_message()  # 3 READ
        await a_sleep(self.s_time)
<<<<<<< HEAD:client/nulsws_client.py
        self.json_prt(negotiate_result, "--------- ! ! ! NEGOTIATE response received: ")
        self.myprint("------end Negotiate----------------------------------------")
=======
        lib.json_prt(negotiate_result, "--------- ! ! ! NEGOTIATE response received: ")
        lib.myprint("------end Negotiate----------------------------------------")
>>>>>>> master:ClientApp/nulsws_RUNNER_client.py

        for run_item in runlist:
            m_indx += 1
            print("starting this item: ", run_item)
                                # TEST ONLY SECTION -------------------------->
                                # if self.msg_type == 77: await self.REGULAR_req(connection, run_item)   # this runs register api
                                # END TEST ONLY SECTION ----------------------
            if mtpe == 3:
                main_request = reqs.prep_REQUEST(m_indx, run_item)  ##TEST ONLY PUT BACK WHEN DONE
                await self.REGULAR_req(connection, main_request)

    def main(self, runlist, msg_type=3):
        mtpe = msg_type
        self.mindex += 1
        myindx = self.mindex
        if mtpe == 3:  # if a regular request Nulstar type 3
            top_pls_middle_dict = reqs.prep_NEGOTIATE_request(myindx)  # must be done first
            asyncio_run(
                self.negotiate_list(
                    top_pls_middle_dict, myindx, runlist, mtpe))  # starts event


if __name__ == '__main__':
<<<<<<< HEAD:client/nulsws_client.py
    b = apilab.NulswsApiLabel()
=======
    from Libraries.Constants.CLASSES import nulsws_api_labels
    b = nulsws_api_labels.nulsws_Labels()
>>>>>>> master:ClientApp/nulsws_RUNNER_client.py

    RUNLIST1 = [b.AC_GET_ACCOUNT_BYADDRESS, b.AC_GET_ALL_ADDRESS_PREFIX, b.AC_GET_ACCOUNT_LIST,
                b.AC_GET_ADDRESS_LIST, b.AC_GET_ADDRESS_PREFIX_BY_CHAINID, b.AC_GET_ALL_ADDRESS_PREFIX,
                b.AC_GET_ALL_PRIKEY, b.AC_GET_ALIASBY_ADDRESS]

    RUNLIST2 = [
        b.AC_EXPORT_ACCOUNT_KEYSTORE, b.AC_EXPORT_KEYSTORE_JSON, b.AC_GET_ACCOUNT_BYADDRESS,
        b.AC_GET_ACCOUNT_LIST, b.AC_GET_ADDRESS_LIST, b.AC_GET_ADDRESS_PREFIX_BY_CHAINID,
        b.AC_GET_ALIASBY_ADDRESS, b.AC_GET_ALL_ADDRESS_PREFIX, b.AC_GET_ALL_PRIKEY,
        b.AC_GET_ENCRYPTED_ADDRESS_LIST, b.AC_GET_MULTI_SIGN_ACCOUNT, b.AC_GET_PRIKEY, b.AC_GET_PUBKEY]

    RUNLIST3 = [b.GET_LATEST_BLOCKHEADERS,
                b.GET_LATEST_ROUND_BLOCKHEADERS, b.GET_NETWORK_GROUP, b.GET_NONCE, b.GET_OTHERCTX,
                b.GET_REGISTERED_CHAIN_INFO_LIST, b.GET_REGISTERED_CHAIN_MESSAGE, b.GET_ROUND_BLOCKHEADERS,
                b.GET_STATUS, b.GET_VERSION, b.INFO, b.LATEST_BLOCK, b.LATEST_BLOCKHEADER,
                b.LATEST_BLOCKHEADER_PO,
                b.LATEST_HEIGHT]

    #RUN_LIST = RUNLIST2
    RUN_LIST = RUNLIST1
    message_type = 3  # 3 is request, 99 is test, 77 is negotiate only

    nws = NulsWebsocket()
    nws.main(RUN_LIST, message_type)





# old code for testing:
# json_main_type = reqs.prep_data_REQUEST_type5()
# json_main_type = reqs.prep_data_REQUEST_type7()
# if mtpe == 99:   # test dev only
#     for run_item in runlist:
#         print("starting this item: ", run_item)
# if mtpe == 77:  # test only
#     self.msg_type = 77
#     j = make_nulsws_REGISTER_method(m_indx)
#     self.commander_by_list(top_plus_mid_dict, m_indx, [j])  #big list

    # FORWARD_MESSAGE = "ForwardMessage"
    # GET_BALANCE = "getBalance"
    # GET_BALANCE_NONCE = "getBalanceNonce"
    # GET_BLOCK_BY_HASH = "getBlockByHash"
    # GET_BLOCK_BY_HEIGHT = "getBlockByHeight"
    # GET_BLOCKHEADER_BY_HASH = "getBlockHeaderByHash"
    # GET_BLOCKHEADER_BY_HEIGHT = "getBlockHeaderByHeight"
    # GET_BLOCKHEADER_PO_BY_HASH = "getBlockHeaderPoByHash"
    # GET_BLOCKHEADER_POBY_HEIGHT = "getBlockHeaderPoByHeight"
    # GET_BLOCKHEADERS_BY_HEIGHT_RANGE = "getBlockHeadersByHeightRange"
    # GET_BLOCKHEADERS_FOR_PROTOCOL = "getBlockHeadersForProtocol"
    # GET_BYZANTINE_COUNT = "getByzantineCount"
    # GET_CIRCULAT = "getCirculat"
    # GET_CONSOLIDATEDAPI = "GetConsolidatedAPI"
    # GET_CROSSCHAIN_INFOS = "getCrossChainInfos"
    # GET_CROSSTX_STATE = "getCrossTxState"
    # GET_CTX = "getCtx"
    # GET_CTX_STATE = "getCtxState"
    # GET_FREEZEGET_FREEZELIST_LIST = "getFreezeList"
    # GET_FRIEND_CHAIN_CIRCULATE = "getFriendChainCirculate"
    # GET_LATEST_BLOCKHEADERS = "getLatestBlockHeaders"
    # GET_LATEST_ROUND_BLOCKHEADERS = "getLatestRoundBlockHeaders"
    # GET_NETWORK_GROUP = "getGroupByChainId"
    # GET_NONCE = "getNonce"
    # GET_OTHERCTX = "getOtherCtx"
    # GET_REGISTERED_CHAIN_INFO_LIST = "getRegisteredChainInfoList"
    # GET_REGISTERED_CHAIN_MESSAGE = "getChains"
    # GET_ROUND_BLOCKHEADERS = "getRoundBlockHeaders"
    # GET_STATUS = "getStatus"
    # GET_VERSION = "getVersion"
    # INFO = "info"