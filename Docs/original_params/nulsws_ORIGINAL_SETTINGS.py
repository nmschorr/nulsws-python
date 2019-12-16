#!/usr/bin/python3.7
# for use in api calls
# the originally requested java types are in comments on each line
# fill in your default params here


# be carefull with these - don't delete them

my_amount: int = 0     # java-type-BigInteger
my_initnumber: int = 0     # java-type-BigInteger
my_value: int = 0     # java-type-BigInteger
my_maxsignaturecount: int = 0     # java-type-Integer
my_signaturebftratio: int = 0     # java-type-Integer
my_assets: list = []             # java-type-List
my_cmdregisterlist: list = []             # java-type-List
my_contractlist: list = []             # java-type-List
my_dellist: list = []             # java-type-List
my_hashlist: list = []             # java-type-List
my_inputs: list = []             # java-type-List
my_list: list = []             # java-type-List
my_listfrom: list = []             # java-type-List
my_listto: list = []             # java-type-List
my_outputs: list = []             # java-type-List
my_prefixlist: list = []             # java-type-List
my_protocolcmds: list = []             # java-type-List
my_pubkeys: list = []             # java-type-List
my_txhashlist: list = []             # java-type-List
my_txlist: list = []             # java-type-List
my_verifierlist: list = []             #  java-type-List
my_assetinfolist: list = []             #  l java-type-List<assetinfo>
my_headerlist: list = []           #  java-type-List<string>
my_args: str = ''                # java-Object
my_lmodulename: str = ''           # java-type-String # Qstring
my_lmoduleversion: str= ''           # Qstring
my_address: str = ''           # java-type-String
my_addressprefix: str = 'NULS'           # java-type-String
my_agentaddress: str = ''           # java-type-String
my_agenthash: str = ''           # java-type-String
my_algorithm: str = 'zlib'           # java-type-String
my_alias: str = ''           # java-type-String
my_assetids: str = ''           # java-type-String
my_assetname: str = ''           # java-type-String
my_block: str = ''           # java-type-String
my_blockhash: str = ''           # java-type-String
my_blockheader: str = ''           # java-type-String
my_chainname: str = 'nuls'           # java-type-String
my_cmd: str = ''           # java-type-String
my_command: str = ''           # java-type-String
my_contractaddress: str = ''           # java-type-String
my_contractbalance: str = ''           # java-type-String
my_contractcode: str = ''           # java-type-String
my_contractNonce: str = ''           # java-type-String
my_contractsender: str = ''           # java-type-String
my_data: str = ''           # java-type-String
my_deposit: str = ''           # java-type-String
my_evidenceheader: str = ''           # java-type-String
my_excludenodes: str = ''           # java-type-String
my_extend: str = ''           # java-type-String
my_extendsdata: str = ''           # java-type-String
my_filepath: str = ''           # java-type-String
my_hash: str = ''           # java-type-String
my_jarfiledata: str = ''           # java-type-String
my_joinagenthash: str = ''           # java-type-String
my_keystore: str = ''           # java-type-String
my_keyword: str = ''           # java-type-String
my_maxout: str = ''           # java-type-String
my_messagebody: str = ''           # java-type-String
my_methoddesc: str = ''           # java-type-String
my_methodname: str = ''           # java-type-String
my_modulecode: str = ''           # java-type-String
my_newpassword: str = ''           # java-type-String
my_nodeid: str = ''           # java-type-String
my_nodes: str = ''           # java-type-String
my_packingaddress: str = ''           # java-type-String
my_password: str = ''           # java-type-String
my_prestateroot: str = ''           # java-type-String
my_prikey: str = ''           # java-type-String
my_pubkey: str = ''           # java-type-String
my_remark: str = ''           # java-type-String
my_rewardaddress: str = ''           # java-type-String
my_role: str = ''           # java-type-String
my_seedips: str = ''           # java-type-String
my_sender: str = ''           # java-type-String
my_sig: str = ''           # java-type-String
my_signaddress: str = ''           # java-type-String
my_signpassword: str = ''           # java-type-String
my_stateroot: str = ''           # java-type-String
my_symbol: str = ''           # java-type-String
my_toaddress: str = ''           # java-type-String
my_tx: str = ''           # java-type-String
my_txhash: str = ''           # java-type-String
my_frestartifrunning: bool = False
my_allhits: bool = False           #  java-type-Boolean
my_isconfirmed: bool = False           #   java-type-Boolean
my_iscrossgroup: bool = False           #   java-type-Boolean
my_overwrite: bool = False           #   java-type-Boolean
my_packaging: bool = False           #   java-type-Boolean
my_usable: bool = False           #   java-type-Boolean
my_bytecount: int = 0             #  java-type-Byte
my_addresstype: int = 0               # int
my_assetchainid: int = 1               # int
my_assetid: int = 1               # int
my_blocktype: int = 0               # int
my_chainid: int = 1               # int
my_circulatechainid: int = 0               # int
my_commissionrate: int = 0               # int
my_count: int = 0               # int
my_download: int = 0               # int
my_height: int = 0               # int
my_intcount: int = 0               # int
my_interval: int = 0               # int
my_iscross: int = 0               # int
my_lmaxcpus: int = 0               # int
my_maxin: int = 0               # int
my_maxtxdatasize: int = 0               # int
my_minavailablecount: int = 0               # int
my_minavailablenodenum: int = 0               # int
my_minsigns: int = 0               # int
my_pagenumber: int = 0               # int
my_pagesize: int = 0               # int
my_percent: int = 0               # int
my_round: int = 0               # int
my_size: int = 0               # int
my_startpage: int = 0               # int
my_state: int = 0               # int
my_status: int = 0               # int
my_type: int = 0               # int
my_begin: int = 0               # java-type-Long
my_blockheight: int = 0               # java-type-Long
my_blocktime: int = 0               # java-type-Long
my_end: int = 0               # java-type-Long
my_endheight: int = 0               # java-type-Long
my_endtimestamp: int = 0               # java-type-Long
my_gaslimit: int = 0               # java-type-Long
my_longcount: int = 0               # java-type-Long
my_magicnumber: int = 0               # java-type-Long
my_price: int = 0               # java-type-Long
my_registertime: int = 0               # java-type-Long
my_startheight: int = 0               # java-type-Long
my_decimalplaces: int = 0                    # java-type-Short
my_protocolversion: int = 0                   # java-type-Short
my_shortcount: int = 0                     # java-type-Short


#
# __ALL__  = ['my_address', 'my_addressprefix', 'my_addresstype', 'my_agentaddress', 'my_agenthash',
#            'my_algorithm', 'my_alias', 'my_allhits', 'my_amount', 'my_args', 'my_assetchainid', 'my_assetid',
#            'my_assetids', 'my_assetinfolist', 'my_assetname', 'my_assets', 'my_begin', 'my_block',
#            'my_blockhash', 'my_blockheader', 'my_blockheight', 'my_blocktime', 'my_blocktype', 'my_bytecount',
#            'my_chainid', 'my_chainname', 'my_circulatechainid', 'my_cmd', 'my_cmdregisterlist', 'my_command',
#            'my_commissionrate', 'my_contractaddress', 'my_contractbalance', 'my_contractcode',
#            'my_contractlist', 'my_contractNonce', 'my_contractsender', 'my_count', 'my_data',
#            'my_decimalplaces', 'my_dellist', 'my_deposit', 'my_download', 'my_end', 'my_endheight',
#            'my_endtimestamp', 'my_evidenceheader', 'my_excludenodes', 'my_extend', 'my_extendsdata',
#            'my_frestartifrunning', 'my_filepath', 'my_gaslimit', 'my_hash', 'my_hashlist', 'my_headerlist',
#            'my_height', 'my_initnumber', 'my_inputs', 'my_intcount', 'my_interval', 'my_isconfirmed',
#            'my_iscross', 'my_iscrossgroup', 'my_jarfiledata', 'my_joinagenthash', 'my_keystore', 'my_keyword',
#            'my_lmaxcpus', 'my_lmodulename', 'my_lmoduleversion', 'my_list', 'my_listfrom', 'my_listto',
#            'my_longcount', 'my_magicnumber', 'my_maxin', 'my_maxout', 'my_maxsignaturecount',
#            'my_maxtxdatasize', 'my_messagebody', 'my_methoddesc', 'my_methodname', 'my_minavailablecount',
#            'my_minavailablenodenum', 'my_minsigns', 'my_modulecode', 'my_newpassword', 'my_nodeid',
#            'my_nodes', 'my_outputs', 'my_overwrite', 'my_packaging', 'my_packingaddress', 'my_pagenumber',
#            'my_pagesize', 'my_password', 'my_percent', 'my_prestateroot', 'my_prefixlist', 'my_prikey',
#            'my_price', 'my_protocolcmds', 'my_protocolversion', 'my_pubkey', 'my_pubkeys', 'my_registertime',
#            'my_remark', 'my_rewardaddress', 'my_role', 'my_round', 'my_seedips', 'my_sender', 'my_shortcount',
#            'my_sig', 'my_signaddress', 'my_signpassword', 'my_signaturebftratio', 'my_size', 'my_startheight',
#            'my_startpage', 'my_state', 'my_stateroot', 'my_status', 'my_symbol', 'my_toaddress', 'my_tx',
#            'my_txhash', 'my_txhashlist', 'my_txlist', 'my_type', 'my_usable', 'my_value',
#             'my_verifierlist'].append(__ALL1__)
