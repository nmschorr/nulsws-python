#!/usr/bin/python3.7
"""
by Nancy Schorr for Nuls, None),
(December, None),
(2019

"""
from Libraries.Constants.nulsws_CONSTANTS_API_LABELS import *
from Libraries.Constants.nulsws_CONSTANTS_PARAM_LABELS import *


# change settings to suit
# return a list of vals for each constant
# LATEST_BLOCK CHAINID needs CHAINID only
mychainid = 1
myone = 1
mypassword = 'nuls123456'
myaddress = '124'
mycount = 0 


# a list of  lists of tuples

user_parameters = [

[
REGISTER_API, None
]], 

[
AC_CREATE_ACCOUNT, [
(CHAINID, mychainid),
(COUNT, myone),
(PASSWORD, mypassword)
]], 

[
AC_CREATE_CONTRACT_ACCOUNT, [
(CHAINID, mychainid)
]], 

[
AC_CREATE_MULTI_SIGN_ACCOUNT, [
(CHAINID, mychainid),
(PUBKEYS, None),
(MINSIGNS, None)
]], 

[
AC_CREATE_MULTI_SIGN_TRANSFER, [
(CHAINID, mychainid),
(INPUTS, None),
(OUTPUTS, None),
(REMARK, None),
(SIGNADDRESS, None),
(SIGNPASSWORD, mypassword)
]], 

[
AC_CREATE_OFFLINE_ACCOUNT, [
(CHAINID, mychainid),
(COUNT, mycount),
(PASSWORD, mypassword)
]], 

[
AC_EXPORT_ACCOUNT_KEYSTORE, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword),
(FILEPATH, None)
]], 

[
AC_EXPORT_KEYSTORE_JSON, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword)
]], 

[
AC_GET_ACCOUNT_BYADDRESS, [
(CHAINID, mychainid),
(ADDRESS, mychainid)
]], 

[
AC_GET_ACCOUNT_LIST, [
(CHAINID, mychainid)
]], 

[

AC_GET_ADDRESS_LIST, [
(CHAINID, mychainid),
(PAGENUMBER, None),
(PAGESIZE, None)
]], 

[
AC_GET_ADDRESS_PREFIX_BY_CHAINID, [
(CHAINID, mychainid)
]], 

[
AC_GET_ALIASBY_ADDRESS, [
(CHAINID, mychainid),
(ADDRESS, mychainid)
]], 

[
AC_GET_ALL_ADDRESS_PREFIX, [
]], 

[
AC_GET_ALL_PRIKEY, [
(CHAINID, mychainid),
(PASSWORD, mypassword)
],


AC_GET_ENCRYPTED_ADDRESS_LIST, [
(CHAINID, mychainid),
], [
AC_GET_MULTI_SIGN_ACCOUNT, [
(CHAINID, mychainid),
(ADDRESS, mychainid)
]], 

[
AC_GET_PUBKEY, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword)
]], 

[
AC_IMPORT_ACCOUNT_BY_KEYSTORE, [
(CHAINID, mychainid),
(PASSWORD, mypassword),
(KEYSTORE, None),
(OVERWRITE, None)
]], 

[
AC_IMPORT_ACCOUNT_BY_PRIKEY, [
(CHAINID, mychainid),
(PASSWORD, mypassword),
(PRIKEY, None),
(OVERWRITE, None)
]], 

[
AC_IS_ALIAS_USABLE, [
(CHAINID, mychainid),
(ALIAS, None)
]], 

[
AC_IS_MULTISIGN_ACCOUNT_BUILDER, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PUBKEY, None)
]], 

[
AC_REMOVE_ACCOUNT, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword)
]], 

[
AC_REMOVE_MULTISIGN_ACCOUNT, [
(CHAINID, mychainid),
(ADDRESS, mychainid)
]], 

[
AC_SET_ALIAS, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword),
(ALIAS, None)
]], 

[
AC_SET_MULTISIGN_ALIAS, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(ALIAS, None),
(SIGNADDRESS, None),
(SIGNPASSWORD, mypassword)
]], 

[
AC_SET_REMARK, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(REMARK, None)
]], 

[
AC_SIGN_BLOCKDIGEST, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword),
(DATA, None)
]], 

[
AC_SIGN_DIGEST, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword),
(DATA, None)
]], 

[
AC_SIGN_MULTISIGN_TRANSACTION, [
(CHAINID, mychainid),
(TX, None),
(SIGNADDRESS, None),
(SIGNPASSWORD, mypassword)
]], 

[
AC_TRANSFER, [
(CHAINID, mychainid),
(INPUTS, None),
(OUTPUTS, None),
(REMARK, None)
]], 

[
AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword),
(NEWPASSWORD, mypassword),
(PRIKEY, None)
]], 

[
AC_UPDATE_PASSWORD, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword),
(NEWPASSWORD, mypassword)
]], 

[
AC_VALIDATION_PASSWORD, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword)
]], 

[
AC_VERIFY_SIGN_DATA, [
(PUBKEY, None),
(SIG, None),
(DATA, None)
]], 

[
BATCH_VALIDATE_BEGIN, [
(CHAINID, mychainid)
]], 

[
BLOCK_VALIDATE, [
(CHAINID, mychainid),
(TXLIST, None)
]], 

[
BLOCKHEIGHT, [
]], 

[
CANCEL_CROSSCHAIN, [
(CHAINID, mychainid),
(ASSETID, None)
]], 

[
CHECK_BLOCK_VERSION, [
(CHAINID, mychainid),
(EXTENDSDATA, None)
]], 

[
CM_ASSET, [
(CHAINID, mychainid),
(ASSETID, None)
]], 

[
CM_ASSET_CIRCULATE_COMMIT, [
(CHAINID, mychainid),
(TXLIST, None),
(BLOCKHEADER, None)
]], 

[
CM_ASSET_CIRCULATE_ROLLBACK, [
(CHAINID, mychainid),
(TXLIST, None),
(BLOCKHEADER, None)
]], 

[
CM_ASSET_CIRCULATE_VALIDATOR, [
(CHAINID, mychainid),
(TX, None)
]], 

[
CM_ASSET_DISABLE, [
(CHAINID, mychainid),
(ASSETID, None),
(ADDRESS, myaddress),
(PASSWORD, mypassword)
]], 

[
CM_ASSET_REG, [
(CHAINID, mychainid),
(ASSETID, None),
(SYMBOL, None),
(ASSETNAME, None),
(INITNUMBER, None),
(DECIMALPLACES, None),
(ADDRESS, myaddress),
(PASSWORD, mypassword)
]], 

[
CM_CHAIN, [
(CHAINID, mychainid)],
],

[
CM_CHAIN_ACTIVE, [
(CHAINID, mychainid),
(CHAINNAME, None),
(ADDRESSTYPE, None),
(ADDRESSPREFIX, None),
(MAGICNUMBER, None),
(MINAVAILABLENODENUM, None),
(ASSETID, None),
(SYMBOL, None),
(ASSETNAME, None),
(INITNUMBER, None),
(DECIMALPLACES, None),
(ADDRESS, myaddress),
(PASSWORD, mypassword),
(VERIFIERLIST, None),
(SIGNATUREBFTRATIO, None),
(MAXSIGNATURECOUNT, mycount)
]], 

[
CM_CHAIN_REG, [
(CHAINID, mychainid),
(CHAINNAME, None),
(ADDRESSTYPE, None),
(ADDRESSPREFIX, None),
(MAGICNUMBER, None),
(MINAVAILABLENODENUM, None),
(ASSETID, None),
(SYMBOL, None),
(ASSETNAME, None),
(INITNUMBER, None),
(DECIMALPLACES, None),
(ADDRESS, myaddress),
(PASSWORD, mypassword),
(VERIFIERLIST, None),
(SIGNATUREBFTRATIO, None),
(MAXSIGNATURECOUNT, mycount)
]], 

[
CM_GET_CHAIN_ASSET, [
(CHAINID, mychainid),
(ASSETCHAINID, None),
(ASSETID, None)
]], 

[
CM_GET_CIRCULATE_CHAIN_ASSET, [
(CIRCULATECHAINID, None),
(ASSETCHAINID, None),
(ASSETID, None)
]], 

[
COMMIT_BATCH_UNCONFIRMED_TXS, [
(CHAINID, mychainid),
(TXLIST, None)
]], 

[
COMMIT_BLOCKTXS, [
(CHAINID, mychainid),
(TXLIST, None),
(BLOCKHEIGHT, None)
]], 

[
COMMIT_UNCONFIRMEDTX, [
(CHAINID, mychainid),
(TX, None)
]], 

[
CONNECT_READY, [
]], 

[
CREATE_AGENT_VALID, [
(CHAINID, mychainid),
(TX, None)
]], 

[
CREATE_CROSSTX, [
(CHAINID, mychainid),
(LISTFROM, None),
(LISTTO, None),
(REMARK, None)
]], 

[
CROSSCHAIN_REGISTER_CHANGE, [
(CHAINID, mychainid)
]],
CS_ADD_BLOCK, [
(CHAINID, mychainid),
(BLOCKHEADER, None)
]], 

[
CS_ADD_EVIDENCE_RECORD, [
(CHAINID, mychainid),
(BLOCKHEADER, None),
(EVIDENCEHEADER, None)
]], 

[
CS_CHAIN_ROLLBACK, [
(CHAINID, mychainid),
(HEIGHT, None)
]], 

[
CS_CONTRACT_DEPOSIT, [
(CHAINID, mychainid),
(AGENTHASH, None),
(DEPOSIT, None),
(CONTRACTADDRESS, None),
(CONTRACTSENDER, None),
(CONTRACTBALANCE, None),
(CONTRACTNONCE, None),
(BLOCKTIME, None)
]], 

[
CS_CONTRACT_WITHDRAW, [
(CHAINID, mychainid),
(JOINAGENTHASH, None),
(CONTRACTADDRESS, None),
(CONTRACTSENDER, None),
(CONTRACTBALANCE, None),
(CONTRACTNONCE, None),
(BLOCKTIME, None)
]], 

[
CS_CREATE_AGENT, [
(CHAINID, mychainid),
(AGENTADDRESS, None),
(PACKINGADDRESS, None),
(REWARDADDRESS, None),
(COMMISSIONRATE, None),
(DEPOSIT, None),
(PASSWORD, mypassword)
]], 

[
CS_CREATE_CONTRACT_AGENT, [
(CHAINID, mychainid),
(PACKINGADDRESS, None),
(DEPOSIT, None),
(COMMISSIONRATE, None),
(CONTRACTADDRESS, None),
(CONTRACTSENDER, None),
(CONTRACTBALANCE, None),
(CONTRACTNONCE, None),
(BLOCKTIME, None)
]], 

[
CS_CREATE_MULTI_AGENT, [
(CHAINID, mychainid),
(AGENTADDRESS, None),
(PACKINGADDRESS, None),
(REWARDADDRESS, None),
(COMMISSIONRATE, None),
(DEPOSIT, None),
(PASSWORD, mypassword),
(SIGNADDRESS, mychainid)
]],

[
CS_DEPOSIT_TOAGENT, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(AGENTHASH, None),
(DEPOSIT, None),
(PASSWORD, mypassword)
]], 

[
CS_DOUBLE_SPEND_RECORD, [
(CHAINID, mychainid),
(BLOCK, None),
(TX, None)
]], 

[
CS_GET_AGENT_ADDRESS_LIST, [
(CHAINID, mychainid)
]], 

[
CS_GET_AGENT_CHANGE_INFO, [
(CHAINID, mychainid)
]], 

[
CS_GET_AGENT_INFO, [
(CHAINID, mychainid),
(AGENTHASH, None)
]], 

[
CS_GET_AGENT_LIST, [
(CHAINID, mychainid),
(PAGENUMBER, None),
(PAGESIZE, None),
(KEYWORD, None)
]], 

[
CS_GET_AGENT_STATUS, [
(CHAINID, mychainid),
(AGENTHASH, None)
]], 

[
CS_GET_CONSENSUS_CONFIG, [
(CHAINID, mychainid)
]], 

[
CS_GET_CONTRACT_AGENT_INFO, [
(CHAINID, mychainid),
(AGENTHASH, None),
(CONTRACTADDRESS, None),
(CONTRACTSENDER, None)
]], 

[
CS_GET_CONTRACT_DEPOSIT_INFO, [
(CHAINID, mychainid),
(JOINAGENTHASH, None),
(CONTRACTADDRESS, None),
(CONTRACTSENDER, None)
]], 

[
CS_GET_DEPOSIT_LIST, [
(CHAINID, mychainid),
(PAGENUMBER, None),
(PAGESIZE, None),
(ADDRESS, myaddress),
(AGENTHASH, None)
]], 

[
CS_GET_INFO, [
(CHAINID, mychainid),
(ADDRESS, mychainid)
]], 

[
CS_GET_PACKER_INFO, [
(CHAINID, mychainid)
]], 

[
CS_GET_PUBLISH_LIST, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(TYPE, None)
]], 

[
CS_GET_ROUND_INFO, [
(CHAINID, mychainid)
]], 

[
CS_GET_ROUND_MEMBER_LIST, [
(CHAINID, mychainid),
(EXTEND, None)
]], 

[
CS_GET_SEED_NODE_INFO, [
(CHAINID, mychainid)
]], 

[
CS_GET_WHOLEINFO, [
(CHAINID, mychainid)
]], 

[
CS_MULTI_DEPOSIT, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(AGENTHASH, None),
(DEPOSIT, None),
(PASSWORD, mypassword),
(SIGNADDRESS, mychainid)
]], 

[
CS_MULTI_WITHDRAW, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(TXHASH, None),
(PASSWORD, mypassword),
(SIGNADDRESS, mychainid)
]], 

[
CS_RANDOM_RAW_SEEDS_COUNT, [
(CHAINID, mychainid),
(HEIGHT, None),
(COUNT, mycount)
]], 

[
CS_RANDOM_RAW_SEEDS_HEIGHT, [
(CHAINID, mychainid),
(STARTHEIGHT, None),
(ENDHEIGHT, None)
]], 

[
CS_RANDOM_SEED_COUNT, [
(CHAINID, mychainid),
(HEIGHT, None),
(COUNT, 0)
(ALGORITHM, None)
]], 

[
CS_RANDOM_SEED_HEIGHT, [
(CHAINID, mychainid),
(STARTHEIGHT, None),
(ENDHEIGHT, None),
(ALGORITHM, None)
]], 

[
CS_RECEIVE_HEADERLIST, [
(CHAINID, mychainid),
(HEADERLIST, None)
]], 

[
CS_RUN_CHAIN, [
(CHAINID, mychainid)
]], 

[
CS_RUN_MAINCHAIN, [
(CHAINID, mychainid)
]], 

[
CS_STOPAGENT, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword)
]], 

[
CS_STOP_AGENT, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword)
]], 

[
CS_STOPCHAIN, [
(CHAINID, mychainid)
]], 

[
CS_STOP_CHAIN, [
(CHAINID, mychainid)
]], 

[
CS_STOP_CONTRACT_AGENT, [
(CHAINID, mychainid),
(CONTRACTADDRESS, None),
(CONTRACTSENDER, None),
(CONTRACTBALANCE, None),
(CONTRACTNONCE, None),
(BLOCKTIME, None)
]], 

[
CS_STOP_MULTI_AGENT, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(PASSWORD, mypassword),
(SIGNADDRESS, mychainid)
]], 

[
CS_TRIGGER_COINBASE_CONTRACT, [
(CHAINID, mychainid),
(TX, None),
(BLOCKHEADER, None),
(STATEROOT, None)
]], 

[
CS_UPDATE_AGENT_CONSENSUS_STATUS, [
(CHAINID, mychainid)
]], 

[
CS_UPDATE_AGENT_STATUS, [
(CHAINID, mychainid),
(STATUS, None)
]], 

[
CS_VALIDBLOCK, [
(CHAINID, mychainid),
(DOWNLOAD, None),
(BLOCK, None)
]], 

[
CS_WITHDRAW, [
(CHAINID, mychainid),
(ADDRESS, myaddress),
(TXHASH, None),
(PASSWORD, mypassword)
]], 

[
DEPOSIT_VALID, [
(CHAINID, mychainid),
(TX, None)
]], 

[
GET_ASSETS_BY_ID, [
(CHAINID, mychainid),
(ASSETIDS, None)
]], 

[
GET_BALANCE, [
(CHAINID, mychainid),
(ASSETCHAINID, None),
(ASSETID, None),
(ADDRESS, mychainid)
]], 

[
GET_BALANCE_NONCE, [
(CHAINID, mychainid),
(ASSETCHAINID, None),
(ASSETID, None),
(ADDRESS, myaddress),
(ISCONFIRMED, None)
]], 

[
GET_BLOCK_BY_HASH, [
(CHAINID, mychainid),
(HASH, None)
]], 

[
GET_BLOCK_BY_HEIGHT, [
(CHAINID, mychainid),
(HEIGHT, None)
]], 

[
GET_BLOCKHEADER_BY_HASH, [
(CHAINID, mychainid),
(HASH, None)
]], 

[
GET_BLOCKHEADER_BY_HEIGHT, [
(CHAINID, mychainid),
(HEIGHT, None)
]], 

[
GET_BLOCKHEADER_PO_BY_HASH, [
(CHAINID, mychainid),
(HASH, None)
]], 

[
GET_BLOCKHEADER_POBY_HEIGHT, [
(CHAINID, mychainid),
(HEIGHT, None)
]], 

[
GET_BLOCKHEADERS_BY_HEIGHT_RANGE, [
(CHAINID, mychainid),
(BEGIN, None),
(END, None)
]], 

[
GET_BLOCKHEADERS_FOR_PROTOCOL, [
(CHAINID, mychainid),
(INTERVAL, None)
]], 

[
GET_BYZANTINE_COUNT, [
(CHAINID, mychainid)
]], 

[
GET_CIRCULAT, [
(CHAINID, mychainid),
(NODEID, None),
(MESSAGEBODY, None)
]], 

[
GET_CROSSCHAIN_INFOS, [
]], 

[
GET_CROSSTX_STATE, [
(CHAINID, mychainid),
(TXHASH, None)
]], 

[
GET_CTX, [
(CHAINID, mychainid),
(NODEID, None),
(MESSAGEBODY, None)
]], 

[
GET_CTX_STATE, [
(CHAINID, mychainid),
(NODEID, None),
(MESSAGEBODY, None)
]], 

[
GET_FRIEND_CHAIN_CIRCULATE, [
(CHAINID, mychainid),
(ASSETIDS, None)
]], 

[
GET_LATEST_BLOCKHEADERS, [
(CHAINID, mychainid),
(SIZE, None)
]], 

[
GET_LATEST__ROUND_BLOCKHEADERS,[
(CHAINID, mychainid),
(ROUND, None)
]], 

[
GET_NONCE, [
(CHAINID, mychainid),
(ASSETCHAINID, None),
(ASSETID, None),
(ADDRESS, myaddress),
(ISCONFIRMED, None)
]], 

[
GET_OTHERCTX, [
(CHAINID, mychainid),
(NODEID, None),
(MESSAGEBODY, None)
]], 

[
GET_REGISTERED_CHAIN_INFO_LIST, [
]], 

[
GET_ROUND_BLOCKHEADERS, [
(CHAINID, mychainid),
(HEIGHT, None),
(ROUND, None)
]], 

[
GET_STATUS, [
(CHAINID, mychainid)
]], 

[
GET_VERSION, [
(CHAINID, mychainid)
]], 

[
INFO, [
(CHAINID, mychainid)
]], 

[
LATEST_BLOCK, [
(CHAINID, mychainid)
]], 

[
LATEST_BLOCKHEADER, [
(CHAINID, mychainid)
]], 

[
LATEST_BLOCKHEADER_PO, [
(CHAINID, mychainid)
]], 

[
LATEST__HEIGHT, [
(CHAINID, mychainid)
]], 

[
LISTENER_DEPENDENCIES_READY, []
], [

MSG_PROCESS,[
(CHAINID, mychainid),
( NODEID, None),
( CMD, None),
(MESSAGEBODY, None)
]], 

[
NEW_BLOCK_HEIGHT, [
(CHAINID, mychainid),
(HEIGHT,None)
]], 

[
NW_ACTIVE_CROSS, [
(CHAINID, mychainid),
( MAXOUT, None),
( MAXIN, None),
( SEEDIPS, None)
]], 

[
NW_ADD_NODES, [
(CHAINID, mychainid),
( ISCROSS, None),
( NODES, None)
]], 

[
NW_BROADCAST, [
( CHAINID, mychainid),
( EXCLUDENODES, None),
( MESSAGEBODY, None),
( COMMAND, None),
( ISCROSS, None),
( PERCENT, None)
]], 

[
NW_CREATE_NODEGROUP, [
( CHAINID, mychainid),
( MAGICNUMBER, None),
( MAXOUT, None),
( MAXIN, None),
( MINAVAILABLECOUNT, None),
    (ISCROSSGROUP, None)
]], 

[
NW_DEL_NODES, [
( CHAINID, mychainid),
( NODES, None)
]], 

[
NW_GET_CHAIN_CONNECT_AMOUNT, [
( CHAINID, mychainid),
( ISCROSS, None)
]], 

[
NW_GET_GROUP_BY_CHAINID,[
( CHAINID, mychainid)
]],
    
[
NW_GET_GROUPS, [
( STARTPAGE, None),
( PAGESIZE, None)
]],

[
NW_GET_NODES, [
( CHAINID, mychainid),
( STATE, None),
( ISCROSS, None),
( STARTPAGE, None),
( PAGESIZE, None)
]], 

[
NW_GET_SEEDS, [
]], 

[
NW_INFO, [
( CHAINID, mychainid)
]],

[
 NW_NODES, [
( CHAINID, mychainid)
]],

[
 NW_PROTOCOL_REGISTER, [
( ROLE, None),
( PROTOCOLCMDS, None)
]],

[
NW_RECONNECT, [
( CHAINID, mychainid)
]],

[
 NW_SEND_PEERS_MSG, [
( CHAINID, mychainid),
   ( NODES, None),
   ( MESSAGEBODY, None),
   ( COMMAND, None)
]],

[
NW_UPDATE_NODE_INFO, [
( CHAINID, mychainid),
( NODEID, None),
( BLOCKHEIGHT, None),
( BLOCKHASH, None)
]],

[
PARAM_TEST_CMD, [
( INTCOUNT, None),
( BYTECOUNT, mycount),
( SHORTCOUNT, None),
( LONGCOUNT, None)
]], 

[
PROTOCOL_VERSION_CHANGE, [
( CHAINID, mychainid),
( PROTOCOLVERSION, None)
]], 

[
RECEIVE_PACKING_BLOCK, [
( CHAINID, mychainid),
( BLOCK, None)
]], 

[
RECV_CIRCULAT, [
( CHAINID, mychainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_CTX, [
( CHAINID, mychainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_CTX_HASH, [
( CHAINID, mychainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_CTX_SIGN, [
( CHAINID, mychainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_CTX_STATE, [
( CHAINID, mychainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_OTHER_CTX, [
( CHAINID, mychainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_REGCHAIN, [
( CHAINID, mychainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
REGISTER_MODULE_DEPENDENCIES, [
]], 

[
REGISTER_PROTOCOL, [
( CHAINID, mychainid),
( MODULECODE, None),
( LIST, None)
]], 

[
ROLLBACK_BLOCK_TXS, [
( CHAINID, mychainid),
( TXLIST, None),
( BLOCKHEIGHT, None)
]], 

[
ROLLBACK_UNCONFIRM_TX, [
( CHAINID, mychainid),
( TX, None)
]], 

[
ROLLBACK_BLOCK, [
( CHAINID, mychainid),
( BLOCKHEADER, None)
]], 

[
ROLLBACK_TX_VALIDATE_STATUS, [
( CHAINID, mychainid),
( TX, None)
]], 

[
SAVE_BLOCK, [
( CHAINID, mychainid),
( BLOCKHEADER, None)
]], 

[
SC_BATCH_BEFORE_END, [
( CHAINID, mychainid),
( BLOCKTYPE, None),
( BLOCKHEIGHT, None)
]], 

[
SC_BATCH_BEGIN, [
( CHAINID, mychainid),
( BLOCKTYPE, None),
( BLOCKHEIGHT, None),
( BLOCKTIME, None),
( PACKINGADDRESS, None),
( PRESTATEROOT, None)
]], 

[
SC_BATCH_END, [
( CHAINID, mychainid),
( BLOCKHEIGHT, None)
]],

[
SC_CALL, [
( CHAINID, mychainid),
( SENDER, None),
( PASSWORD, None),
( VALUE, None),
( GASLIMIT, None),
( PRICE, None),
( CONTRACTADDRESS, None),
( METHODNAME, None),
( METHODDESC, None),
( ARGS, None),
( REMARK, None)
]], 

[
SC_CALL_VALIDATOR, [
( CHAINID, mychainid),
( TX, None)
]],

[
SC_CONSTRUCTOR, [
( CHAINID, mychainid),
( CONTRACTCODE, None)
]], 

[
SC_CONTRACT_INFO, [
( CHAINID, mychainid),
( CONTRACTADDRESS, None)
]],

[
 SC_CONTRACT_OFFLINE_TX_HASH_LIST, [
( CHAINID, mychainid),
( BLOCKHASH, None)
]],

[
SC_CONTRACT_RESULT, [
( CHAINID, mychainid),
( HASH, None)
]],

[
SC_CONTRACT_RESULT_LIST, [
( CHAINID, mychainid),
( HASHLIST, None)
]],

[
SC_CONTRACT_TX, [
( CHAINID, mychainid),
( HASH, None)
]],

[
SC_CREATE, [
( CHAINID, mychainid),
( SENDER, None),
( PASSWORD, None),
( ALIAS, None),
( GASLIMIT, None),
( PRICE, None),
( CONTRACTCODE, None),
( ARGS, None),
( REMARK, None)
]],

[
SC_CREATE_VALIDATOR, [
( CHAINID, mychainid),
( TX, None)
]],

[
SC_DELETE, [
( CHAINID, mychainid),
( SENDER, None),
( PASSWORD, None),
( CONTRACTADDRESS, None),
( REMARK, None)
]],

[
SC_DELETE_VALIDATOR, [
( CHAINID, mychainid),
( TX, None)
]],

[
SC_IMPUTED_CALL_GAS, [
( CHAINID, mychainid),
( SENDER, None),
( VALUE, None),
( CONTRACTADDRESS, None),
( METHODNAME, None),
( METHODDESC, None),
( ARGS, None)
]],

[
SC_IMPUTED_CREATE_GAS, [
( CHAINID, mychainid),
( SENDER, None),
( CONTRACTCODE, None),
( ARGS, None)
]],

[
SC_INITIAL_ACCOUNT_TOKEN, [
( CHAINID, mychainid),
( ADDRESS, myaddress),
]],

[
SC_INVOKE_CONTRACT, [
( CHAINID, mychainid),
( BLOCKTYPE, None),
( TX, None)
]],

[
SC_INVOKE_VIEW, [
( CHAINID, mychainid),
( CONTRACTADDRESS, None),
( METHODNAME, None),
( METHODDESC, None),
( ARGS, None)
]],

[
SC_PACKAGE_BATCH_END, [
( CHAINID, mychainid),
( BLOCKHEIGHT, None)
]],

[
SC_TOKEN_ASSETS_LIST, [
( CHAINID, mychainid),
( ADDRESS, myaddress),
( PAGENUMBER, None),
( PAGESIZE, None)
]],

[
SC_TOKEN_BALANCE, [
( CHAINID, mychainid),
( CONTRACTADDRESS, None),
( ADDRESS, mychainid)
],

[
SC_TOKEN_TRANSFER, [
( CHAINID, mychainid),
( ADDRESS, myaddress),
( TOADDRESS, None),
( CONTRACTADDRESS, None),
( PASSWORD, None),
( AMOUNT, None),
( REMARK, None)
]],

[
SC_TOKEN_TRANSFER_LIST, [
( CHAINID, mychainid),
( ADDRESS,
myaddress),
( PAGENUMBER, None),
( PAGESIZE, None)
]],

[
SC_TRANSFER, [
( CHAINID, mychainid),
( ADDRESS,
myaddress),
( TOADDRESS, None),
( PASSWORD, None),
( AMOUNT, None),
( REMARK, None)
]],

[
SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT, [
( CHAINID, mychainid),
( STATEROOT, None),
( BLOCKHEIGHT, None),
( CONTRACTADDRESS, None),
( TX, None)
]],

[
SC_UPLOAD, [
( CHAINID, mychainid),
( JARFILEDATA, None)
]],

[
SC_VALIDATE_CALL, [
( CHAINID, mychainid),
( SENDER, None),
( VALUE, None),
( GASLIMIT, None),
( PRICE, None),
( CONTRACTADDRESS, None),
( METHODNAME, None),
( METHODDESC, None),
( ARGS, None)
]],

[
SC_VALIDATE_CREATE, [
( CHAINID, mychainid),
( SENDER, None),
( GASLIMIT, None),
( PRICE, None),
( CONTRACTCODE, None),
( ARGS, None)
]],

[
SC_VALIDATE_DELETE, [
( CHAINID, mychainid),
( CONTRACTADDRESS, None),
]],

[
STOP_AGENTVALID, [
( CHAINID, mychainid),
( TX, None)
]],

[
TX_COMMIT, [
( CHAINID, mychainid),
( TXLIST, None),
( BLOCKHEADER, None)
]],

[
TX_VALIDATOR, [
( CHAINID, mychainid),
( TXLIST, None),
( BLOCKHEADER, None)
]],

[
TX_BACK_PACKABLE_TXS, [
( CHAINID, mychainid),
( TXLIST, None)
]],

[
TX_BATCH_VERIFY, [
( CHAINID, mychainid),
( TXLIST, None),
( BLOCKHEADER, None),
( PRESTATEROOT, None)
]],

[
TX_BL_STATE, [
( CHAINID, mychainid),
( STATUS, None)
]],

[
TX_BLOCK_HEIGHT, [
( CHAINID, mychainid),
( HEIGHT, None)
]],

[
TX_CS_STATE, [
( CHAINID, mychainid),
( PACKAGING, None)
]],

[
TX_GET_BLOCKTXS, [
( CHAINID, mychainid),
( TXHASHLIST, None)
]],

[
TX_GET_BLOCKTXS_EXTEND, [
( CHAINID, mychainid),
( TXHASHLIST, None),
( ALLHITS, None)
]],

[
TX_GET_CONFIRMED_TX, [
( CHAINID, mychainid),
( TXHASH, None)
]],

[
TX_GET_CONFIRMED_TX_CLIENT, [
( CHAINID, mychainid),
( TXHASH, None)
]],

[
TX_GET_NONEXISTENT_UNCONFIRMED_HASHS, [
( CHAINID, mychainid),
( TXHASHLIST, None)
]],

[
TX_GET_SYSTEMTYPES, [
( CHAINID, mychainid),
]],

[
TX_GET_TX, [
( CHAINID, mychainid),
( TXHASH, None)
]],

[
TX_GET_TX_CLIENT, [
( CHAINID, mychainid),
( TXHASH, None)
]],

[
TX_NEWTX, [
( CHAINID, mychainid),
( TX, None)
]],

[
TX_PACKABLE_TXS, [
( CHAINID, mychainid),
( ENDTIMESTAMP, None),
( MAXTXDATASIZE, None),
( BLOCKTIME, None),
( PACKINGADDRESS, None),
( PRESTATEROOT, None)
]],

[
TX_REGISTER, [
( CHAINID, mychainid),
( MODULECODE, None),
( LIST, None),
( DELLIST, None)
]],

[
TX_ROLLBACK, [
( CHAINID, mychainid),
( TXHASHLIST, None),
( BLOCKHEADER, None)
]],

[
TX_SAVE, [
( CHAINID, mychainid),
( TXLIST, None),
( CONTRACTLIST, None),
( BLOCKHEADER, None)
]],

[
TX_VERIFY_TX, [
( CHAINID, mychainid),
( TX, None)
]],

[
UPDATE_CHAIN_ASSET, [
( CHAINID, mychainid),
( ASSETS, None)
]],

[
VERIFY_COINDATA, [
( CHAINID, mychainid),
( TX, None)
]],

[
VERIFY_COINDATA_BATCH_PACKAGED, [
( CHAINID, mychainid),
( TXLIST, None)
]],

[
WITHDRAW_VALID, [
( CHAINID, mychainid),
( TX, None)
]],

[
FORWARD_MESSAGE, [
]], 

[
GET_CONSOLIDATEDAPI, [
]], 

[
CHECK_UPDATES, [
]], 

[
SCAN_MANAGED_MODULES, [
]], 

[
SHUTDOWN_SYSTEM, [
]], 

[
STOP_ALL_MODULES, []
]
] #end big list



# ---------------- Example -------------------------------------------------------------------
