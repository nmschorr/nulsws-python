#!/usr/bin/python3.7
"""
    by Nancy Schorr for Nuls, December 2, 2019

    Instructions for Message type Three - Request

    - Edit this file for message type Request.

    Message type one must have a return value from the server of "1"
    (type: NegotiateConnectionResponse=OK) before the message type 3 can proceed.

    Nulstar should respond to this call with a Message of  and a number representing success or failure.

    Receiving a "1" means success, "0" is failure
"""


#  Message Type - string
MSG_TYPE = 3
from Constants.nulsws_CONSTANTS_API_names import *
from Constants.nulsws_CONSTANTS_otherlabels import CHAINID_LABEL as CL
from Constants.nulsws_CONSTANTS_API_names import GET_REGISTERED_CHAIN_INFO_LIST

onesies = [(AC_GET_ALL_ADDRESS_PREFIX,[]),
    (CM_GET_CROSS_CHAIN_SIMPLE_INFOS, []),
    (REGISTER_MODULEDEPENDENCIES, []),
    (NW_CUR_TIME_MILLIS, []),
    (LISTENER_DEPENDENCIES_READY, []),
    (GET_REGISTERED_CHAIN_INFO_LIST, []),
    (NW_GET_MAIN_NET_MAGIC_NUMBER, []),
    (CS_GET_CONSENSUS_CONFIG, []),
    (NW_GET_SEEDS, []),
    (CHECKUPDATES, []),
    ]


#don't use: private
# (REGISTER_API, []),
# (CONNECTREADY, []),
# (GET_CONSOLIDATEDAPI, [])

onesies_b = [
    (CM_CHAIN, [CL]),
    (AC_GET_ENCRYPTED_ADDRESS_LIST, [CL]),
    (BATCH_VALIDATE_BEGIN, [CL]),
    (CLEAR_UNCONFIRMED_TX, [CL]),
    (CROSS_CHAIN_REGISTER_CHANGE, [CL]),
    (CS_GET_AGENT_CHANGE_INFO, [CL]),
    (CS_GET_CONSENSUS_CONFIG, [CL]),
    (CS_GET_NODE_PACKING_ADDR, [CL]),
    (AC_ADDRESS_PREFIX, [CL]),
    (AC_CREATE_CONTRACT_ACCT, [CL]) ]


#
# 1 ac_getAccountList
# 1 ac_getAddressPrefixByChainId
# 1 ac_getEncryptedAddressList
# 1 batchValidateBegin
# 1 clearUnconfirmTxs
# 1 cm_chain
# 1 crossChainRegisterChange
# 1 cs_getAgentAddressList
# 1 cs_getAgentChangeInfo
# 1 cs_getConsensusConfig
# 1 cs_getNodePackingAddress
# 1 cs_getPackerInfo
# 1 cs_getRoundInfo
# 1 cs_getSeedNodeInfo
# 1 cs_getWholeInfo
# 1 cs_runChain
# 1 cs_runMainChain
# 1 cs_stopChain
# 1 cs_updateAgentConsensusStatus
# 1 getByzantineCount
# 1 GetCPUInfo
# 1 getStatus
# 1 getVersion
# 1 info
# 1 latestBlock
# 1 latestBlockHeader
# 1 latestBlockHeaderPo
# 1 latestHeight
# 1 nw_delNodeGroup
# 1 nw_getGroupByChainId
# 1 nw_info
# 1 nw_nodes
# 1 nw_reconnect
# 1 startallmodules
# 1 tx_getSystemTypes

# "ListAPI": #works!
# "cm_getChainsSimpleInfo":   #works!
# "getRegisteredChainInfoList" :  {}   #works
# "nw_getSeeds": {}  # works!
# "nw_getMainMagicNumber": {}  #  works!
# "nw_currentTimeMillis": {}  # works!
# "cs_getConsensusConfig" : { "chainId": 1} #works
# NULSd6HghM9Z9XytwZEHGDGRJLnNR5ybiy5gt
#NULSd6Hge7xHDnvsSpnzbR2gWHd31zJ1How11
# -----------------------------------------------------------------------------------

#
# Example of type 3 message:
# {
#     "ProtocolVersion": "0.1.0"
#     "MessageID": m_id,
#     "TimeZone": tzone,
#     "Timestamp": t_stamp
#     "MessageType": "Request",
#     "MessageData": {
#         "RequestType": "1",
#         "SubscriptionEventCounter": "0",
#         "SubscriptionPeriod": "1",
#         "SubscriptionRange": "[100]",
#         "ResponseMaxSize": "0",
#         "RequestMethods": [
#           {
#             "GetBalance": {
#               "Address": "tNULSeBaMnrs6JKrCy6TQdzYJZkMZJDng7QAsD"
#             }
#           },
#           {
#             "GetHeight": {}
#           }
#         ]
#        }
#     }
