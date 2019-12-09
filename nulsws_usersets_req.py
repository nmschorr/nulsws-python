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


proto_ver = "0.1"

# this can be a list once other versions are supported
compatible_proto_versions = [proto_ver]

# ------ msg_type3 --------------------
#  Message Type - string
msg_type_req = "3"

# ----- host3 ----------------------------------------------

host_req = "127.0.0.1"    ## change to suit

# Websocket method -either secure (wss) or not (ws) edit ws or wss to suit
# at this time only unsecure (ws) is implemented, although secure with ssl
# is in the works
# ----------------c
# connect_method3 -----------------------------------

connect_method_req= "ws://"
# or "wss://"

# ------- port3 --------------------------------------------
# this is the port to communicate with on the Nulstar blockchain.  7771 is standard.

port_req = "7772"

websock_url_req: str = ''.join([connect_method_req, host_req, ":", port_req])

# ------- compression type and level --------------------------------------------

# change compression type if necessary although these settings are standard. zlib
# is the standard
compress_type_req= "zlib"

compress_rate_request = 0
subscriptionRange = 0
request_int = 1
sub_event_ct = 0
sub_period_int = 1
sub_range = ""
res_max_size = 0
RequestType: 2 # two is ack and a response, 1 is just response
address_val = "NULSd6Hggvrij3MPW9QTHJGBv7uiyMKw41i7t"  ##







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
