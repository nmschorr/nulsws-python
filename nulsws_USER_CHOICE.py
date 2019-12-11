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
onesy_label = "nw_getSeeds"
MSG_TYPE = 3
ACCT_ADDRESS = ''
from nulsws_CONSTANTS_API_names import *
# note to coders - the __ALL__ list must be kept up to date and include all values in this file


from nulsws_CONSTANTS_otherlabels import CHAINID_LABEL as CL
from nulsws_CONSTANTS_API_names import *

onesies = [(AC_GET_ADDRESS_PREFIXBY_CHAINID,[CL]),
          (AC_GET_ALL_ADDRESS_PREFIX,[]),
          (AC_GET_ENCRYPTED_ADDRESS_LIST, [CL]),
          (BATCH_VALIDATE_BEGIN, [CL]),
          (CLEAR_UNCONFIRMED_TX, [CL]),
          (CM_CHAIN, [CL]),
          (CM_GET_CROSS_CHAIN_SIMPLE_INFOS, []),
          ("connectReady", []),
          ("getRegisteredChainInfoList", []),
          (NW_GET_MAIN_NET_MAGIC_NUMBER, []),
          ("nw_currentTimeMillis", []),
          (CS_GET_CONSENSUS_CONFIG, []),

          (CROSS_CHAIN_REGISTER_CHANGE, [CL]),
          (CS_GET_AGENT_CHANGE_INFO, [CL]),
          ("c", [CL]), (CS_GET_CONSENSUS_CONFIG, [CL]),
          (CS_GET_NODE_PACKING_ADDR, [CL]),
          ("nw_getSeeds", []), ("nw_getSeeds", []),("nw_getSeeds", []),
          ("nw_getSeeds", []), ("nw_getSeeds", []), ("nw_getSeeds", [])]


__ALL__ =[onesy_label, MSG_TYPE, ACCT_ADDRESS, onesies]





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
