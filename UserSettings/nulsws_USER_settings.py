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
from Libraries.Constants.nulsws_CONSTANTS_API_names import *

#change settings to suit
#return a list of vals for each constant
mychain = "1"
mychainid = list(mychain)
MSG_TYPE = 3

# user adjustable
RUN_LIST = [
    AC_GET_ENCRYPTED_ADDRESS_LIST,
    AC_ADDRESS_PREFIX,
    CM_CHAIN,BATCH_VALIDATE_BEGIN, CLEAR_UNCONFIRMED_TX, CS_GET_AGENT_CHANGE_INFO, CS_GET_CONSENSUS_CONFIG,
    CS_GET_NODE_PACKING_ADDR, AC_ADDRESS_PREFIX ]


def get_my_parameter_vals(thevar):
#LATEST_BLOCK CHAINID needs CHAINID only
    if thevar == LATEST_BLOCK:
        answer = mychainid
    elif thevar ==  LATEST_BLOCKHEADER_PO:
        answer = mychainid
    elif thevar ==  CM_CHAIN:
        answer = mychainid
    elif thevar ==  AC_GET_ENCRYPTED_ADDRESS_LIST:
        answer = mychainid
    elif thevar ==  AC_ADDRESS_PREFIX:
        answer = mychainid
    elif thevar == BATCH_VALIDATE_BEGIN:
        answer = mychainid
    elif thevar == CLEAR_UNCONFIRMED_TX:
        answer = mychainid
    elif thevar == CS_GET_AGENT_CHANGE_INFO:
        answer = mychainid
    elif thevar == CS_GET_CONSENSUS_CONFIG:
        answer = mychainid
    elif thevar == CS_GET_NODE_PACKING_ADDR:
        answer = mychainid
    elif thevar == AC_ADDRESS_PREFIX:
        answer = mychainid
    return answer


BATCH_VALIDATE_BEGIN, CLEAR_UNCONFIRMED_TX, CS_GET_AGENT_CHANGE_INFO, CS_GET_CONSENSUS_CONFIG,
CS_GET_NODE_PACKING_ADDR, AC_ADDRESS_PREFIX




#  Message Type - string
msg_type_req = "3"
address_val = "NULSd6Hggvrij3MPW9QTHJGBv7uiyMKw41i7t"  ##
RequestType = 2  # two is ack and a response, 1 is just response

compress_type_VALUE = "zlib"

compress_rate_VALUE = 0  # 0-9
subscriptionRange = 0
request_int = 1
sub_event_ct = 0
sub_period_int = 1
sub_range = ""
res_max_size = 0

# note to coders - the __ALL__ list must be kept up to date and include all values in this file
__ALL__ = [address_val, msg_type_req, compress_rate_VALUE, subscriptionRange, request_int, sub_event_ct,
           sub_period_int, sub_range, res_max_size, RequestType]




# ---------------- Example -------------------------------------------------------------------

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
