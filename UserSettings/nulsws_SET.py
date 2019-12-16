#!/usr/bin/python3.7
"""
by Nancy Schorr for Nuls, None),
(December, None),
(2019

"""

# change settings to suit
# for use in api calls
# fill in your default params here

connect_method = "ws://"   # could be wss
host_req = "127.0.0.1"
port_req = "7772"    
websock_url: str = ''.join([connect_method, host_req, ":", port_req])
proto_ver = "0.1"
compatible_proto_versions = [proto_ver]

compress_type_VALUE = "zlib"
compress_rate_VALUE = 0                      # 0-9
subscriptionRange = 0
request_int = 1
sub_event_ct = 0
sub_period_int = 1
sub_range = 0
res_max_size = 0
MSG_TYPE = 3
# msg_type_req = "3"
RequestType = 2                   # two is ack and a response, 1 is just response


SHORT_MSG = "Empty"
REMARK = "No remarks"
ZERO = 0
FALSE = False
TRUE = True
ZLIB = "zlib"


my_chainid: int = 1               # int
my_password = 'nuls123456'   # str
my_addresstype: int = 0               # int
my_assetchainid: int = 1               # int
my_assetid: int = 1               # int
my_blocktype: int = 0               # int
my_circulatechainid: int = 0               # int
my_commissionrate: int = 0               # int
my_count: int = 0               # int
my_download: int = 0               # int
my_height: int = 0               # int
my_intcount: int = 0               # int
my_interval: int = 0               # int
my_address: str = "NULSd6Hggvrij3MPW9QTHJGBv7uiyMKw41i7t"             # java-type-String
my_addressprefix: str = 'NULS'           # java-type-String
address_val = my_address

