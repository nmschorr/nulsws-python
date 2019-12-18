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

my_pubkeys: 1
my_chainid: int = 1               # int
my_account: str = "NULSd6Hggvrij3MPW9QTHJGBv7uiyMKw41i7t"             # java-type-String
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
my_addressval = my_address
my_agentaddress= 1 
my_agenthash= 1
my_algorithm = 1 
my_alias = 1 
my_allhits = 1 
my_amount = 1
my_args = 1
my_assetids = 1 
my_assetinfolist = 1 
my_assetname = 1 
my_assets = 1 
my_begin = 1 
my_block = 1 
my_blockhash = 1 
my_blockheader = 1 
my_blockheight = 1 
my_blocktime = 1
my_bytecount = 1
my_chainname = 1
my_cmd = 1
my_cmdregisterlistmy_command = 1 
my_contractaddress = 1
my_contractbalance = 1 
my_contractcode = 1 
my_contractlist = 1 
my_contractnonce = 1 
my_contractsender = 1 
my_data = 1
my_decimalplaces = 1 
my_dellist = 1 
my_deposit = 1 
my_end = 1
my_endheight = 1 
my_endtimestamp = 1 
my_evidenceheader = 1 
my_excludenodes = 1 
my_extend = 1 
my_extendsdata = 1 
my_frestartifrunning = 1 
my_filepath = 1 
my_gaslimit = 1 
my_hash = 1 
my_hashlist = 1 
my_headerlist = 1 
my_initnumber = 1
my_inputs = 1 
my_isconfirmed = 1
my_iscross = 1 
my_iscrossgroup = 1 
my_jarfiledata = 1 
my_joinagenthash = 1 
my_keystore = 1 
my_keyword = 1 
my_lmaxcpus = 1 
my_lmodulename = 1 
my_lmoduleversion = 1 
my_list = 1 
my_listfrom = 1 
my_listto = 1 
my_longcount = 1 
my_magicnumber = 1 
my_maxin = 1 
my_maxout = 1 
my_maxsignaturecount = 1 
my_maxtxdatasize = 1 
my_messagebody = 1 
my_methoddesc = 1 
my_methodname = 1 
my_minavailablecount = 1 
my_minavailablenodenum = 1 
my_minsigns = 1 
my_modulecode = 1 
my_newpassword = 1 
my_nodeid = 1 
my_nodes = 1 
my_outputs = 1 
my_overwrite = 1 
my_packaging = 1 
my_packingaddress = 1 
my_pagenumber = 1 
my_pagesize = 1 
my_percent = 1
my_prestateroot = 1 
my_prefixlist = 1 
my_prikey = 1 
my_price = 1 
my_protocolcmds = 1 
my_protocolversion = 1 
my_pubkey = 1 
my_pubkeys = 1 
my_registertime = 1 
my_remark = 1 
my_rewardaddress = 1 
my_role = 1 
my_round = 1 
my_seedips = 1 
my_sender = 1 
my_shortcount = 1 
my_sig = 1 
my_signaddress = 1 
my_signpassword = 1 
my_signaturebftratio = 1 
my_size = 1 
my_startheight = 1 
my_startpage = 1 
my_state = 1 
my_stateroot = 1 
my_status = 1 
my_symbol = 1 
my_toaddress = 1 
my_tx = 1 
my_txhash = 1 
my_txhashlist = 1 
my_txlist = 1 
my_type = 1 
my_usable = 1 
my_value = 1 
my_verifierlist = 1


__ALL__ = ['FALSE', 'MSG_TYPE', 'REMARK', 'RequestType', 'SHORT_MSG', 'TRUE', 'ZERO', 'ZLIB',
'compatible_proto_versions', 'compress_rate_VALUE', 'compress_type_VALUE',
 'connect_method', 'host_req', 'my_account', 'my_address', 'my_addressprefix', 'my_addresstype',
 'my_addressval', 'my_agentaddress', 'my_agenthash', 'my_algorithm', 'my_alias', 'my_allhits', 'my_amount',
 'my_args', 'my_assetchainid', 'my_assetid', 'my_assetids', 'my_assetinfolist', 'my_assetname', 'my_assets',
 'my_begin', 'my_block', 'my_blockhash', 'my_blockheader', 'my_blockheight', 'my_blocktime', 'my_blocktype',
 'my_bytecount', 'my_chainid', 'my_chainname', 'my_circulatechainid', 'my_cmd',
 'my_cmdregisterlistmy_command', 'my_commissionrate', 'my_contractaddress', 'my_contractbalance',
 'my_contractcode', 'my_contractlist', 'my_contractnonce', 'my_contractsender', 'my_count', 'my_data',
 'my_decimalplaces', 'my_dellist', 'my_deposit', 'my_download', 'my_end', 'my_endheight', 'my_endtimestamp',
 'my_evidenceheader', 'my_excludenodes', 'my_extend', 'my_extendsdata', 'my_filepath', 'my_frestartifrunning',
 'my_gaslimit', 'my_hash', 'my_hashlist', 'my_headerlist', 'my_height', 'my_initnumber', 'my_inputs',
 'my_intcount', 'my_interval', 'my_isconfirmed', 'my_iscross', 'my_iscrossgroup', 'my_jarfiledata',
 'my_joinagenthash', 'my_keystore', 'my_keyword', 'my_list', 'my_listfrom', 'my_listto', 'my_lmaxcpus',
 'my_lmodulename', 'my_lmoduleversion', 'my_longcount', 'my_magicnumber', 'my_maxin', 'my_maxout',
 'my_maxsignaturecount', 'my_maxtxdatasize', 'my_messagebody', 'my_methoddesc', 'my_methodname',
 'my_minavailablecount', 'my_minavailablenodenum', 'my_minsigns', 'my_modulecode', 'my_newpassword',
 'my_nodeid', 'my_nodes', 'my_outputs', 'my_overwrite', 'my_packaging', 'my_packingaddress', 'my_pagenumber',
 'my_pagesize', 'my_password', 'my_percent', 'my_prefixlist', 'my_prestateroot', 'my_price', 'my_prikey',
 'my_protocolcmds', 'my_protocolversion', 'my_pubkey', 'my_pubkeys', 'my_registertime', 'my_remark',
 'my_rewardaddress', 'my_role', 'my_round', 'my_seedips', 'my_sender', 'my_shortcount', 'my_sig',
 'my_signaddress', 'my_signaturebftratio', 'my_signpassword', 'my_size', 'my_startheight', 'my_startpage',
 'my_state', 'my_stateroot', 'my_status', 'my_symbol', 'my_toaddress', 'my_tx', 'my_txhash', 'my_txhashlist',
 'my_txlist', 'my_type', 'my_usable', 'my_value', 'my_verifierlist', 'port_req', 'proto_ver', 'request_int',
 'res_max_size', 'sub_event_ct', 'sub_period_int', 'sub_range', 'subscriptionRange', 'websock_url']

# to generate __all__:
# import UserSettings.nulsws_SET as u
# dir(u)
# then remove globals from generated list
