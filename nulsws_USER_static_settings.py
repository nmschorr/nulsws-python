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
# Author: Nancy Schorr

# compatible_proto_versions can be a list once other versions are supported
# connect_method - either secure (wss) or not (ws) edit ws or wss to suit
# at this time only unsecure (ws) is implemented, although secure with ssl
# is in the works
# port_req is the port to communicate with on the Nulstar blockchain.  7771 is standard.
# Change compression type if necessary although these settings are standard. zlib
# is the standard
# these rarely change from request to request
# if you need to change them, do it here:

proto_ver = "0.1"
compatible_proto_versions = [proto_ver]
host_req = "127.0.0.1"
connect_method = "ws://"
# connect_method =  "wss://"
port_req = "7772"   # or 7771, 7773, etc.

websock_url: str = ''.join([connect_method, host_req, ":", port_req])

__ALL__ = [proto_ver, compatible_proto_versions, host_req, connect_method, port_req,
           websock_url]

# ------- Example ----------------------------------------------------------------------------

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
