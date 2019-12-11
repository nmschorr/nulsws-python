#!/usr/bin/python3.7
'''
    by Nancy Schorr for Nuls, December 2, 2019

    Instructions for Message type Three - Request

    - Edit this file for message type Request.

    Message type one must have a return value from the server of "1"
    (type: NegotiateConnectionResponse=OK) before the message type 3 can proceed.

    Nulstar should respond to this call with a Message of  and a number representing success or failure.

    Receiving a "1" means success, "0" is failure
'''


#  Message Type - string
onesy_label = "nw_getSeeds"
MSG_TYPE = 3
ACCT_ADDRESS = ''
# note to coders - the __ALL__ list must be kept up to date and include all values in this file
__ALL__ =[onesy_label, MSG_TYPE, ACCT_ADDRESS]




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
