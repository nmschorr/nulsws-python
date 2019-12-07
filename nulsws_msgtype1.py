#!/usr/bin/python3.7

'''
 Instructions for Message type One - Negotiate Connection

  - Edit this file for message type Negotiate Connection

 The Nulstar should respond to this call with a Message of type: NegotiateConnectionResponse
 and a number representing success or failure.

 Receiving a "1" means success, "0" is failure

 by Nancy Schorr for Nuls, December 2, 2019
'''
# "MessageData": {
#     "CompressionAlgorithm": "zlib",
#     "CompressionRate": "0",
#     "ProtocolVersion": "0.1.0"
# },
#
#
#  protocool version

proto_ver = "0.1"

# this can be a list once other versions are supported
compatible_proto_versions = [proto_ver]

# ------ msg_type1 --------------------
#  Message Type - string

msg_type1 = "1"

# ----- host1 ----------------------------------------------

host1= "127.0.0.1"    ## change to suit

# Websocket method -either secure (wss) or not (ws) edit ws or wss to suit
# at this time only unsecure (ws) is implemented, although secure with ssl
# is in the works
# ----------------c
# connect_method1 -----------------------------------

connect_method1= "ws://"
# connect_method1: str = "wss://"

# ------- port1 --------------------------------------------
# this is the port to communicate with on the Nulstar blockchain.  7771 is standard.

#port1 = "7770"
port1 = "7771"
#port1 = "9006"

websock_url1: str = ''.join([connect_method1, host1, ":", port1])

# ------- compression type and level --------------------------------------------

# change compression type if necessary although these settings are standard. zlib
# is the standard as it is
compress_type1 = "zlib"

# An integer between 0 and 9, 3 being the default setting
comp_rate1 = 0

# -----------------------------------------------------------------------------------

