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
from nulsws_python.src.nulsws_python.user_settings.nulsws_user_set import NulsWsUserSet
from nulsws_python.src.nulsws_python.nulsws_request import NulsWsRequest


class NulsWsClient(object):

    def __init__(self):
        self.s_time = .7
        self.nreq_obj = NulsWsRequest()
        self.myprint = nlib.NulsWsLib.myprint
        self.json_prt = nlib.NulsWsLib.json_prt
        self.nreq_obj = NulsWsRequest()
        self.that_dict: dict = {}

    def get_that_dict(self):
        return self.that_dict

    async def regular_request(self, websock_cont: WebSocketClientConnection, j_reg_dict):
        json_reg = json.dumps(j_reg_dict)
        await websock_cont.write_message(json_reg)  # 2 WRITE
        self.json_prt(json_reg, "\n* * * REGULAR message going out: \n")
        await a_sleep(self.s_time)
        read_reg = await websock_cont.read_message()  # 3 READ
        await a_sleep(self.s_time)
        if len(read_reg) > 0:
            self.json_prt(read_reg, "   -----------> ! ! ! REGULAR response received: ")
        nlib.NulsWsLib.myprint("--------------end previous / begin next "
                                   "request--------------------------")
        nlib.NulsWsLib.myprint(0, "x")

    async def negotiate_list(self, top_plus_mid_dict, m_indx, run_list, dd, mtpe=3):
        conn_m = eval(dd.get("connect_method"))
        host_r = eval(dd.get("host_req"))
        port_r = eval(dd.get("port_req"))
        websock_url = ''.join([conn_m, host_r, ":", port_r])
        debug = 1

        if not debug:
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

            if mtpe == 3:
                main_request = self.nreq_obj.prep_request(m_indx, run_item, dd)  # TEST ONLY PUT BACK WHEN DONE

                if debug:
                    json_reg = json.dumps(main_request)
                    self.json_prt(json_reg, " ")

                else:
                    await self.regular_request(connection, main_request)

    def main(self, rr_list, mtpe=3):
        nus = NulsWsUserSet()
        cfd = nus.get_conf_dict()
        import copy
        that_dict: dict = copy.deepcopy(cfd)
        self.that_dict = that_dict
        nreq_obj = NulsWsRequest()
        mindx = 0
        if mtpe == 3:  # if a regular request Nulstar type 3
            top_pls_middle_dict = nreq_obj.prep_negotiate_request(mindx, cfd)  # must be done
            # first (self, msg_indx, dd):
            asyncio_run(
                self.negotiate_list(
                    top_pls_middle_dict, mindx, rr_list, cfd, mtpe))  # starts event

if __name__ == "__main__":
    nws = NulsWsClient()

    r_1 = ['AC_GET_ACCOUNT_BYADDRESS', 'AC_GET_ALL_ADDRESS_PREFIX', 'AC_GET_ACCOUNT_LIST',
           'AC_GET_ADDRESS_LIST', 'AC_GET_ADDRESS_PREFIX_BY_CHAINID',
           'AC_GET_ALL_ADDRESS_PREFIX',
           'AC_GET_ALL_PRIKEY', 'AC_GET_ALIASBY_ADDRESS']

    r_2 = [
        'AC_EXPORT_ACCOUNT_KEYSTORE', 'AC_EXPORT_KEYSTORE_JSON', 'AC_GET_ACCOUNT_BYADDRESS',
        'AC_GET_ACCOUNT_LIST', 'AC_GET_ADDRESS_LIST', 'AC_GET_ADDRESS_PREFIX_BY_CHAINID',
        'AC_GET_ALIASBY_ADDRESS', 'AC_GET_ALL_ADDRESS_PREFIX', 'AC_GET_ALL_PRIKEY',
        'AC_GET_ENCRYPTED_ADDRESS_LIST', 'AC_GET_MULTI_SIGN_ACCOUNT',
        'AC_GET_PUBKEY']

    r_3 = ['GET_LATEST_BLOCKHEADERS',   'GET_LATEST_ROUND_BLOCKHEADERS',
           'GET_OTHERCTX', 'GET_ROUND_BLOCKHEADERS',
           'GET_STATUS', 'GET_VERSION', 'INFO', 'LATEST_BLOCK', 'LATEST_BLOCKHEADER',
           'LATEST_BLOCKHEADER_PO', 'LATEST_HEIGHT']

    # RUN_LIST = runlist_2
    # runlist = runlist_1 + runlist_2 + runlist_3

    r_4 = ['GET_STATUS', 'GET_VERSION', 'INFO','LATEST_BLOCK', 'LATEST_BLOCKHEADER',
          'LATEST_BLOCKHEADER_PO', 'LATEST_HEIGHT']

    r_4 = ['GET_STATUS', 'GET_VERSION', 'INFO','LATEST_BLOCK', 'LATEST_BLOCKHEADER',
          'LATEST_BLOCKHEADER_PO', 'LATEST_HEIGHT']

    r_5 = ['AC_ADD_ADDRESS_PREFIX', 'AC_CREATE_ACCOUNT', 'AC_CREATE_CONTRACT_ACCOUNT',
           'AC_CREATE_MULTI_SIGN_ACCOUNT', 'AC_CREATE_MULTI_SIGN_TRANSFER', 'AC_CREATE_OFFLINE_ACCOUNT',
           'AC_EXPORT_ACCOUNT_KEYSTORE', 'AC_EXPORT_KEYSTORE_JSON', 'AC_GET_ACCOUNT_BYADDRESS',
           'AC_GET_ACCOUNT_LIST', 'AC_GET_ADDRESS_LIST', 'AC_GET_ADDRESS_PREFIX_BY_CHAINID',
           'AC_GET_ALIASBY_ADDRESS', 'AC_GET_ALL_ADDRESS_PREFIX', 'AC_GET_ALL_PRIKEY',
           'AC_GET_ENCRYPTED_ADDRESS_LIST', 'AC_GET_MULTI_SIGN_ACCOUNT', 'AC_GET_PRIKEY_BY_ADDRESS',
           'AC_GET_PUBKEY', 'AC_IMPORT_ACCOUNT_BY_KEYSTORE', 'AC_IMPORT_ACCOUNT_BY_PRIKEY',
           'AC_IS_ALIAS_USABLE', 'AC_IS_MULTISIGN_ACCOUNT_BUILDER', 'AC_REMOVE_ACCOUNT',
           'AC_REMOVE_MULTISIGN_ACCOUNT', 'AC_SET_ALIAS', 'AC_SET_MULTISIGN_ALIAS', 'AC_SET_REMARK',
           'AC_SIGN_BLOCKDIGEST', 'AC_SIGN_DIGEST', 'AC_SIGN_MULTISIGN_TRANSACTION', 'AC_TRANSFER',
           'AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD', 'AC_UPDATE_PASSWORD', 'AC_VALIDATION_PASSWORD',
           'AC_VERIFY_SIGN_DATA', 'BATCH_VALIDATE_BEGIN', 'BLOCK_VALIDATE', 'CANCEL_CROSSCHAIN',
           'CHECK_BLOCK_VERSION', 'CM_ASSET', 'CM_ASSET_CIRCULATE_COMMIT', 'CM_ASSET_CIRCULATE_ROLLBACK',
           'CM_ASSET_CIRCULATE_VALIDATOR', 'CM_ASSET_DISABLE', 'CM_ASSET_REG', 'CM_CHAIN', 'CM_CHAIN_ACTIVE',
           'CM_CHAIN_REG', 'CM_GET_CHAIN_ASSET', 'CM_GET_CIRCULATE_CHAIN_ASSET',
           'COMMIT_BATCH_UNCONFIRMED_TXS', 'COMMIT_BLOCKTXS', 'COMMIT_UNCONFIRMEDTX', 'CREATE_AGENT_VALID',
           'CREATE_CROSSTX', 'CROSSCHAIN_REGISTER_CHANGE', 'CS_ADD_BLOCK', 'CS_ADD_EVIDENCE_RECORD',
           'CS_CHAIN_ROLLBACK', 'CS_CONTRACT_DEPOSIT', 'CS_CONTRACT_WITHDRAW', 'CS_CREATE_AGENT',
           'CS_CREATE_CONTRACT_AGENT', 'CS_CREATE_MULTI_AGENT', 'CS_DEPOSIT_TOAGENT',
           'CS_DOUBLE_SPEND_RECORD', 'CS_GET_AGENT_ADDRESS_LIST', 'CS_GET_AGENT_CHANGE_INFO',
           'CS_GET_AGENT_INFO', 'CS_GET_AGENT_LIST', 'CS_GET_AGENT_STATUS', 'CS_GET_CONSENSUS_CONFIG',
           'CS_GET_CONTRACT_AGENT_INFO', 'CS_GET_CONTRACT_DEPOSIT_INFO', 'CS_GET_DEPOSIT_LIST', 'CS_GET_INFO',
           'CS_GET_PACKER_INFO', 'CS_GET_PUBLISH_LIST', 'CS_GET_ROUND_INFO', 'CS_GET_ROUND_MEMBER_LIST',
           'CS_GET_SEED_NODE_INFO', 'CS_GET_WHOLEINFO', 'CS_MULTI_DEPOSIT', 'CS_MULTI_WITHDRAW',
           'CS_RANDOM_RAW_SEEDS_COUNT', 'CS_RANDOM_RAW_SEEDS_HEIGHT', 'CS_RANDOM_SEED_COUNT',
           'CS_RANDOM_SEED_HEIGHT', 'CS_RECEIVE_HEADERLIST', 'CS_RUN_CHAIN', 'CS_RUN_MAINCHAIN',
           'CS_STOP_AGENT', 'CS_STOP_CHAIN', 'CS_STOP_CONTRACT_AGENT', 'CS_STOP_MULTI_AGENT', 'CS_STOPAGENT',
           'CS_STOPCHAIN', 'CS_TRIGGER_COINBASE_CONTRACT', 'CS_UPDATE_AGENT_CONSENSUS_STATUS',
           'CS_UPDATE_AGENT_STATUS', 'CS_VALIDBLOCK', 'CS_WITHDRAW', 'DEPOSIT_VALID', 'GET_ASSETS_BY_ID',
           'GET_BALANCE', 'GET_BALANCE_NONCE', 'GET_BLOCK_BY_HASH', 'GET_BLOCK_BY_HEIGHT',
           'GET_BLOCKHEADER_BY_HASH', 'GET_BLOCKHEADER_BY_HEIGHT', 'GET_BLOCKHEADER_PO_BY_HASH',
           'GET_BLOCKHEADER_POBY_HEIGHT', 'GET_BLOCKHEADERS_BY_HEIGHT_RANGE', 'GET_BLOCKHEADERS_FOR_PROTOCOL',
           'GET_BYZANTINE_COUNT', 'GET_CIRCULAT', 'GET_CROSSTX_STATE', 'GET_CTX', 'GET_CTX_STATE',
           'GET_FRIEND_CHAIN_CIRCULATE', 'GET_LATEST_BLOCKHEADERS', 'GET_LATEST_ROUND_BLOCKHEADERS',
           'GET_NONCE', 'GET_OTHERCTX', 'GET_ROUND_BLOCKHEADERS', 'GET_STATUS', 'GET_VERSION', 'INFO',
           'LATEST_BLOCK', 'LATEST_BLOCKHEADER', 'LATEST_BLOCKHEADER_PO', 'LATEST_HEIGHT', 'MSG_PROCESS',
           'NEW_BLOCK_HEIGHT', 'NW_ACTIVE_CROSS', 'NW_ADD_NODES', 'NW_BROADCAST', 'NW_CREATE_NODEGROUP',
           'NW_DEL_NODES', 'NW_GET_CHAIN_CONNECT_AMOUNT', 'NW_GET_GROUP_BY_CHAINID', 'NW_GET_GROUPS',
           'NW_GET_NODES', 'NW_INFO', 'NW_NODES', 'NW_PROTOCOL_REGISTER', 'NW_RECONNECT', 'NW_SEND_PEERS_MSG',
           'NW_UPDATE_NODE_INFO', 'PARAM_TEST_CMD', 'PROTOCOL_VERSION_CHANGE', 'RECEIVE_PACKING_BLOCK',
           'RECV_CIRCULAT', 'RECV_CTX', 'RECV_CTX_HASH', 'RECV_CTX_SIGN', 'RECV_CTX_STATE', 'RECV_OTHER_CTX',
           'RECV_REGCHAIN', 'REGISTER_PROTOCOL', 'ROLLBACK_BLOCK', 'ROLLBACK_BLOCK_TXS',
           'ROLLBACK_TX_VALIDATE_STATUS', 'ROLLBACK_UNCONFIRM_TX', 'SAVE_BLOCK', 'SC_BATCH_BEFORE_END',
           'SC_BATCH_BEGIN', 'SC_BATCH_END', 'SC_CALL', 'SC_CALL_VALIDATOR', 'SC_CONSTRUCTOR',
           'SC_CONTRACT_INFO', 'SC_CONTRACT_OFFLINE_TX_HASH_LIST', 'SC_CONTRACT_RESULT',
           'SC_CONTRACT_RESULT_LIST', 'SC_CONTRACT_TX', 'SC_CREATE', 'SC_CREATE_VALIDATOR', 'SC_DELETE',
           'SC_DELETE_VALIDATOR', 'SC_IMPUTED_CALL_GAS', 'SC_IMPUTED_CREATE_GAS', 'SC_INITIAL_ACCOUNT_TOKEN',
           'SC_INVOKE_CONTRACT', 'SC_INVOKE_VIEW', 'SC_PACKAGE_BATCH_END', 'SC_TOKEN_ASSETS_LIST',
           'SC_TOKEN_BALANCE', 'SC_TOKEN_TRANSFER', 'SC_TOKEN_TRANSFER_LIST', 'SC_TRANSFER',
           'SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT', 'SC_UPLOAD', 'SC_VALIDATE_CALL', 'SC_VALIDATE_CREATE',
           'SC_VALIDATE_DELETE', 'STOP_AGENTVALID', 'TX_BACK_PACKABLE_TXS', 'TX_BATCH_VERIFY', 'TX_BL_STATE',
           'TX_BLOCK_HEIGHT', 'TX_COMMIT', 'TX_CS_STATE', 'TX_GET_BLOCKTXS', 'TX_GET_BLOCKTXS_EXTEND',
           'TX_GET_CONFIRMED_TX', 'TX_GET_CONFIRMED_TX_CLIENT', 'TX_GET_NONEXISTENT_UNCONFIRMED_HASHS',
           'TX_GET_SYSTEMTYPES', 'TX_GET_TX', 'TX_GET_TX_CLIENT', 'TX_NEWTX', 'TX_PACKABLE_TXS',
           'TX_REGISTER', 'TX_ROLLBACK', 'TX_SAVE', 'TX_VALIDATOR', 'TX_VERIFY_TX', 'UPDATE_CHAIN_ASSET',
           'VERIFY_COINDATA', 'VERIFY_COINDATA_BATCH_PACKAGED', 'WITHDRAW_VALID']

    runlist = r_1 + r_2 + r_3 + r_4
    runlist = r_4
    message_type = 3  # 3 is request, 99 is test, 77 is negotiate only
    nws.main(r_5, message_type)


