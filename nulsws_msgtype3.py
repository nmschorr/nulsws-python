#!/usr/bin/python3.7


'''
Example of type 3 message:
{
  "MessageType": "Request",
  "MessageData": {
    "RequestType": "3",
    "SubscriptionEventCounter": "0",
    "SubscriptionPeriod": "3",
    "SubscriptionRange": "[300]",
    "ResponseMaxSize": "0",
    "RequestMethods": [
      {
        "GetBalance": {
          "Address": "tNULSeBaMnrs6JKrCy6TQdzYJZkMZJDng7QAsD"
        }
      },
      {
        "GetHeight": {}
      }
    ]
  }
}


'''


'''
 Instructions for Message type Three - Request

  - Edit this file for message type Request.  
  
  Message type one must have a return value from the server of "1" 
  (type: NegotiateConnectionResponse=OK) before the message type 3 can proceed.

Nulstar should respond to this call with a Message of  and a number representing success or failure.

Receiving a "1" means success, "0" is failure

by Nancy Schorr for Nuls, December 2, 2019
'''


proto_ver = "0.1"

# this can be a list once other versions are supported
compatible_proto_versions = [proto_ver]

# ------ msg_type3 --------------------
#  Message Type - string
msg_type3 = "3"

# ----- host3 ----------------------------------------------

host3 = "127.0.0.1"    ## change to suit

# Websocket method -either secure (wss) or not (ws) edit ws or wss to suit
# at this time only unsecure (ws) is implemented, although secure with ssl
# is in the works
# ----------------c
# connect_method3 -----------------------------------

connect_method3= "ws://"
# connect_method3: str = "wss://"

# ------- port3 --------------------------------------------
# this is the port to communicate with on the Nulstar blockchain.  7771 is standard.

#port3 = "7770"
port3 = "7771"

websock_url3: str = ''.join([connect_method3, host3, ":", port3])

# ------- compression type and level --------------------------------------------

# change compression type if necessary although these settings are standard. zlib
# is the standard as it is
compress_type3= "zlib"

# An integer between 0 and 9, 3 being the default setting
compress_rate3 = 0
subscriptionRange = 0
request_int = 1
sub_event_ct = 0
sub_period_int = 1
sub_range = ""
res_max_size = 0

address_val = "NULSd6Hggvrij3MPW9QTHJGBv7uiyMKw41i7t"  ##
# NULSd6HghM9Z9XytwZEHGDGRJLnNR5ybiy5gt
#NULSd6Hge7xHDnvsSpnzbR2gWHd31zJ1How11
# -----------------------------------------------------------------------------------

