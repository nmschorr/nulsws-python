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

from Constants.nulsws_CONSTANTS_params import CHAINID

AC_GET_ACCOUNT_LIST_user_settings_list = [{ CHAINID: 1} ]
AC_ADDRESS_PREFIX_user_settings_list = [{ CHAINID: 1} ]
AC_CREATE_ACCOUNT_user_settings_list = [{ CHAINID: 1} ]
AC_CREATE_CONTRACT_ACCT_user_settings_list = [{ CHAINID: 1}]
AC_CREATE_MULTISIGN_ACCT_user_settings_list = []
AC_CREATE_MULTISIGN_TRANSFER_user_settings_list = []
AC_CREATE_OFFLINE_ACCT_user_settings_list = []
AC_EXPORTACCOUNTKEYSTORE_user_settings_list = []
AC_EXPORT_KEYSTORE_JSON_user_settings_list = []
AC_EXPORT_ACCT_KEYSTORE_user_settings_list = []
AC_GET_ACCOUNT_LIST_user_settings_list = []
AC_GET_ADDRESS_LIST_user_settings_list = []





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

# NULSd6HghM9Z9XytwZEHGDGRJLnNR5ybiy5gt
# NULSd6Hge7xHDnvsSpnzbR2gWHd31zJ1How11
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
