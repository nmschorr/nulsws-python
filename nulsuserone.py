#!usr/bin/python3.7

'''
 Instructions for Message type One - Negotiate Connection

  - Edit this file for message type Negotiate Connection

 The Nulstar should respond to this call with a Message of type: NegotiateConnectionResponse
 and a number representing success or failure.

 Receiving a "1" means success, "0" is failure

 by Nancy Schorr for Nuls, December 2, 2019
'''

# ------ mtype --------------------
#  Message Type - string

mtype = "1"

# ----- host ----------------------------------------------

host = "127.0.0.1"    ## change to suit

# Websocket method -either secure (wss) or not (ws) edit ws or wss to suit
# at this time only unsecure (ws) is implemented, although secure with ssl
# is in the works
# ---------------------------------------------------

method = "ws://"
# method: str = "wss://"

# ------- port --------------------------------------------
# this is the port to communicate with on the Nulstar blockchain.  7771 is standard.

# port = "9006"
# port = "18003"
port = "7771"

# ------- compression type --------------------------------------------

# change compression type if necessary although these settings are standard. zlib
# is the standard as it is
comp_type= "zlib"

# An integer between 0 and 9, 3 being the default setting
comp_int = 3

my_url: str = ''.join([method, host, ":", port])

# print("the url:  ", my_url)


