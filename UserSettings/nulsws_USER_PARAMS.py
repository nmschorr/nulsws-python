#!/usr/bin/python3.7
"""
by Nancy Schorr for Nuls, None),
(December, None),
(2019

"""
from Libraries.Constants.nulsws_CONSTANTS_API_LABELS import *
from Libraries.Constants.nulsws_CONSTANTS_PARAM_LABELS import *
from UserSettings.nulsws_CONSTANTS_PARAM_userwords import *

# change settings to suit
# return a list of vals for each constant
# LATEST_BLOCK CHAINID needs CHAINID only



# a list of  lists of tuples

user_parameters = [

[
REGISTER_API, None
]], 

[
AC_CREATE_ACCOUNT, [
(CHAINID, my_chainid),
(COUNT, my_count),
(PASSWORD, my_password)
]], 

[
AC_CREATE_CONTRACT_ACCOUNT, [
(CHAINID, my_chainid)
]], 

[
AC_CREATE_MULTI_SIGN_ACCOUNT, [
(CHAINID, my_chainid),
(PUBKEYS, None),
(MINSIGNS, None)
]], 

[
AC_CREATE_MULTI_SIGN_TRANSFER, [
(CHAINID, my_chainid),
(INPUTS, None),
(OUTPUTS, None),
(REMARK, None),
(SIGNADDRESS, None),
(SIGNPASSWORD, my_password)
]], 

[
AC_CREATE_OFFLINE_ACCOUNT, [
(CHAINID, my_chainid),
(COUNT, my_count),
(PASSWORD, my_password)
]], 

[
AC_EXPORT_ACCOUNT_KEYSTORE, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password),
(FILEPATH, None)
]], 

[
AC_EXPORT_KEYSTORE_JSON, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password)
]], 

[
AC_GET_ACCOUNT_BYADDRESS, [
(CHAINID, my_chainid),
(ADDRESS, my_chainid)
]], 

[
AC_GET_ACCOUNT_LIST, [
(CHAINID, my_chainid)
]], 

[

AC_GET_ADDRESS_LIST, [
(CHAINID, my_chainid),
(PAGENUMBER, None),
(PAGESIZE, None)
]], 

[
AC_GET_ADDRESS_PREFIX_BY_CHAINID, [
(CHAINID, my_chainid)
]], 

[
AC_GET_ALIASBY_ADDRESS, [
(CHAINID, my_chainid),
(ADDRESS, my_chainid)
]], 

[
AC_GET_ALL_ADDRESS_PREFIX, [
]], 

[
AC_GET_ALL_PRIKEY, [
(CHAINID, my_chainid),
(PASSWORD, my_password)
]],

[
AC_GET_ENCRYPTED_ADDRESS_LIST, [
(CHAINID, my_chainid),
]],

[
AC_GET_MULTI_SIGN_ACCOUNT, [
(CHAINID, my_chainid),
(ADDRESS, my_chainid)
]], 

[
AC_GET_PUBKEY, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password)
]], 

[
AC_IMPORT_ACCOUNT_BY_KEYSTORE, [
(CHAINID, my_chainid),
(PASSWORD, my_password),
(KEYSTORE, None),
(OVERWRITE, None)
]], 

[
AC_IMPORT_ACCOUNT_BY_PRIKEY, [
(CHAINID, my_chainid),
(PASSWORD, my_password),
(PRIKEY, None),
(OVERWRITE, None)
]], 

[
AC_IS_ALIAS_USABLE, [
(CHAINID, my_chainid),
(ALIAS, None)
]], 

[
AC_IS_MULTISIGN_ACCOUNT_BUILDER, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PUBKEY, None)
]], 

[
AC_REMOVE_ACCOUNT, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password)
]], 

[
AC_REMOVE_MULTISIGN_ACCOUNT, [
(CHAINID, my_chainid),
(ADDRESS, my_chainid)
]], 

[
AC_SET_ALIAS, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password),
(ALIAS, None)
]], 

[
AC_SET_MULTISIGN_ALIAS, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(ALIAS, None),
(SIGNADDRESS, None),
(SIGNPASSWORD, my_password)
]], 

[
AC_SET_REMARK, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(REMARK, None)
]], 

[
AC_SIGN_BLOCKDIGEST, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password),
(DATA, None)
]], 

[
AC_SIGN_DIGEST, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password),
(DATA, None)
]], 

[
AC_SIGN_MULTISIGN_TRANSACTION, [
(CHAINID, my_chainid),
(TX, None),
(SIGNADDRESS, None),
(SIGNPASSWORD, my_password)
]], 

[
AC_TRANSFER, [
(CHAINID, my_chainid),
(INPUTS, None),
(OUTPUTS, None),
(REMARK, None)
]], 

[
AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password),
(NEWPASSWORD, my_password),
(PRIKEY, None)
]], 

[
AC_UPDATE_PASSWORD, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password),
(NEWPASSWORD, my_password)
]], 

[
AC_VALIDATION_PASSWORD, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password)
]], 

[
AC_VERIFY_SIGN_DATA, [
(PUBKEY, None),
(SIG, None),
(DATA, None)
]], 

[
BATCH_VALIDATE_BEGIN, [
(CHAINID, my_chainid)
]], 

[
BLOCK_VALIDATE, [
(CHAINID, my_chainid),
(TXLIST, None)
]], 

[
BLOCKHEIGHT, [
]], 

[
CANCEL_CROSSCHAIN, [
(CHAINID, my_chainid),
(ASSETID, None)
]], 

[
CHECK_BLOCK_VERSION, [
(CHAINID, my_chainid),
(EXTENDSDATA, None)
]], 

[
CM_ASSET, [
(CHAINID, my_chainid),
(ASSETID, None)
]], 

[
CM_ASSET_CIRCULATE_COMMIT, [
(CHAINID, my_chainid),
(TXLIST, None),
(BLOCKHEADER, None)
]], 

[
CM_ASSET_CIRCULATE_ROLLBACK, [
(CHAINID, my_chainid),
(TXLIST, None),
(BLOCKHEADER, None)
]], 

[
CM_ASSET_CIRCULATE_VALIDATOR, [
(CHAINID, my_chainid),
(TX, None)
]], 

[
CM_ASSET_DISABLE, [
(CHAINID, my_chainid),
(ASSETID, None),
(ADDRESS, my_address),
(PASSWORD, my_password)
]], 

[
CM_ASSET_REG, [
(CHAINID, my_chainid),
(ASSETID, None),
(SYMBOL, None),
(ASSETNAME, None),
(INITNUMBER, None),
(DECIMALPLACES, None),
(ADDRESS, my_address),
(PASSWORD, my_password)
]], 

[
CM_CHAIN, [
(CHAINID, my_chainid)],
],

[
CM_CHAIN_ACTIVE, [
(CHAINID, my_chainid),
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
(ADDRESS, my_address),
(PASSWORD, my_password),
(VERIFIERLIST, None),
(SIGNATUREBFTRATIO, None),
(MAXSIGNATURECOUNT, my_count)
]], 

[
CM_CHAIN_REG, [
(CHAINID, my_chainid),
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
(ADDRESS, my_address),
(PASSWORD, my_password),
(VERIFIERLIST, None),
(SIGNATUREBFTRATIO, None),
(MAXSIGNATURECOUNT, my_count)
]], 

[
CM_GET_CHAIN_ASSET, [
(CHAINID, my_chainid),
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
(CHAINID, my_chainid),
(TXLIST, None)
]], 

[
COMMIT_BLOCKTXS, [
(CHAINID, my_chainid),
(TXLIST, None),
(BLOCKHEIGHT, None)
]], 

[
COMMIT_UNCONFIRMEDTX, [
(CHAINID, my_chainid),
(TX, None)
]], 

[
CONNECT_READY, [
]], 

[
CREATE_AGENT_VALID, [
(CHAINID, my_chainid),
(TX, None)
]], 

[
CREATE_CROSSTX, [
(CHAINID, my_chainid),
(LISTFROM, None),
(LISTTO, None),
(REMARK, None)
]], 

[
CROSSCHAIN_REGISTER_CHANGE, [
(CHAINID, my_chainid)
]],

[
CS_ADD_BLOCK, [
(CHAINID, my_chainid),
(BLOCKHEADER, None)
]], 

[
CS_ADD_EVIDENCE_RECORD, [
(CHAINID, my_chainid),
(BLOCKHEADER, None),
(EVIDENCEHEADER, None)
]], 

[
CS_CHAIN_ROLLBACK, [
(CHAINID, my_chainid),
(HEIGHT, None)
]], 

[
CS_CONTRACT_DEPOSIT, [
(CHAINID, my_chainid),
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
(CHAINID, my_chainid),
(JOINAGENTHASH, None),
(CONTRACTADDRESS, None),
(CONTRACTSENDER, None),
(CONTRACTBALANCE, None),
(CONTRACTNONCE, None),
(BLOCKTIME, None)
]], 

[
CS_CREATE_AGENT, [
(CHAINID, my_chainid),
(AGENTADDRESS, None),
(PACKINGADDRESS, None),
(REWARDADDRESS, None),
(COMMISSIONRATE, None),
(DEPOSIT, None),
(PASSWORD, my_password)
]], 

[
CS_CREATE_CONTRACT_AGENT, [
(CHAINID, my_chainid),
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
(CHAINID, my_chainid),
(AGENTADDRESS, None),
(PACKINGADDRESS, None),
(REWARDADDRESS, None),
(COMMISSIONRATE, None),
(DEPOSIT, None),
(PASSWORD, my_password),
(SIGNADDRESS, my_chainid)
]],

[
CS_DEPOSIT_TOAGENT, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(AGENTHASH, None),
(DEPOSIT, None),
(PASSWORD, my_password)
]], 

[
CS_DOUBLE_SPEND_RECORD, [
(CHAINID, my_chainid),
(BLOCK, None),
(TX, None)
]], 

[
CS_GET_AGENT_ADDRESS_LIST, [
(CHAINID, my_chainid)
]], 

[
CS_GET_AGENT_CHANGE_INFO, [
(CHAINID, my_chainid)
]], 

[
CS_GET_AGENT_INFO, [
(CHAINID, my_chainid),
(AGENTHASH, None)
]], 

[
CS_GET_AGENT_LIST, [
(CHAINID, my_chainid),
(PAGENUMBER, None),
(PAGESIZE, None),
(KEYWORD, None)
]], 

[
CS_GET_AGENT_STATUS, [
(CHAINID, my_chainid),
(AGENTHASH, None)
]], 

[
CS_GET_CONSENSUS_CONFIG, [
(CHAINID, my_chainid)
]], 

[
CS_GET_CONTRACT_AGENT_INFO, [
(CHAINID, my_chainid),
(AGENTHASH, None),
(CONTRACTADDRESS, None),
(CONTRACTSENDER, None)
]], 

[
CS_GET_CONTRACT_DEPOSIT_INFO, [
(CHAINID, my_chainid),
(JOINAGENTHASH, None),
(CONTRACTADDRESS, None),
(CONTRACTSENDER, None)
]], 

[
CS_GET_DEPOSIT_LIST, [
(CHAINID, my_chainid),
(PAGENUMBER, None),
(PAGESIZE, None),
(ADDRESS, my_address),
(AGENTHASH, None)
]], 

[
CS_GET_INFO, [
(CHAINID, my_chainid),
(ADDRESS, my_chainid)
]], 

[
CS_GET_PACKER_INFO, [
(CHAINID, my_chainid)
]], 

[
CS_GET_PUBLISH_LIST, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(TYPE, None)
]], 

[
CS_GET_ROUND_INFO, [
(CHAINID, my_chainid)
]], 

[
CS_GET_ROUND_MEMBER_LIST, [
(CHAINID, my_chainid),
(EXTEND, None)
]], 

[
CS_GET_SEED_NODE_INFO, [
(CHAINID, my_chainid)
]], 

[
CS_GET_WHOLEINFO, [
(CHAINID, my_chainid)
]], 

[
CS_MULTI_DEPOSIT, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(AGENTHASH, None),
(DEPOSIT, None),
(PASSWORD, my_password),
(SIGNADDRESS, my_chainid)
]], 

[
CS_MULTI_WITHDRAW, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(TXHASH, None),
(PASSWORD, my_password),
(SIGNADDRESS, my_chainid)
]], 

[
CS_RANDOM_RAW_SEEDS_COUNT, [
(CHAINID, my_chainid),
(HEIGHT, None),
(COUNT, my_count)
]], 

[
CS_RANDOM_RAW_SEEDS_HEIGHT, [
(CHAINID, my_chainid),
(STARTHEIGHT, None),
(ENDHEIGHT, None)
]], 

[
CS_RANDOM_SEED_COUNT, [
(CHAINID, my_chainid),
(HEIGHT, None),
(COUNT, 0)
(ALGORITHM, None)
]], 

[
CS_RANDOM_SEED_HEIGHT, [
(CHAINID, my_chainid),
(STARTHEIGHT, None),
(ENDHEIGHT, None),
(ALGORITHM, None)
]], 

[
CS_RECEIVE_HEADERLIST, [
(CHAINID, my_chainid),
(HEADERLIST, None)
]], 

[
CS_RUN_CHAIN, [
(CHAINID, my_chainid)
]], 

[
CS_RUN_MAINCHAIN, [
(CHAINID, my_chainid)
]], 

[
CS_STOPAGENT, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password)
]], 

[
CS_STOP_AGENT, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password)
]], 

[
CS_STOPCHAIN, [
(CHAINID, my_chainid)
]], 

[
CS_STOP_CHAIN, [
(CHAINID, my_chainid)
]], 

[
CS_STOP_CONTRACT_AGENT, [
(CHAINID, my_chainid),
(CONTRACTADDRESS, None),
(CONTRACTSENDER, None),
(CONTRACTBALANCE, None),
(CONTRACTNONCE, None),
(BLOCKTIME, None)
]], 

[
CS_STOP_MULTI_AGENT, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(PASSWORD, my_password),
(SIGNADDRESS, my_chainid)
]], 

[
CS_TRIGGER_COINBASE_CONTRACT, [
(CHAINID, my_chainid),
(TX, None),
(BLOCKHEADER, None),
(STATEROOT, None)
]], 

[
CS_UPDATE_AGENT_CONSENSUS_STATUS, [
(CHAINID, my_chainid)
]], 

[
CS_UPDATE_AGENT_STATUS, [
(CHAINID, my_chainid),
(STATUS, None)
]], 

[
CS_VALIDBLOCK, [
(CHAINID, my_chainid),
(DOWNLOAD, None),
(BLOCK, None)
]], 

[
CS_WITHDRAW, [
(CHAINID, my_chainid),
(ADDRESS, my_address),
(TXHASH, None),
(PASSWORD, my_password)
]], 

[
DEPOSIT_VALID, [
(CHAINID, my_chainid),
(TX, None)
]], 

[
GET_ASSETS_BY_ID, [
(CHAINID, my_chainid),
(ASSETIDS, None)
]], 

[
GET_BALANCE, [
(CHAINID, my_chainid),
(ASSETCHAINID, None),
(ASSETID, None),
(ADDRESS, my_chainid)
]], 

[
GET_BALANCE_NONCE, [
(CHAINID, my_chainid),
(ASSETCHAINID, None),
(ASSETID, None),
(ADDRESS, my_address),
(ISCONFIRMED, None)
]], 

[
GET_BLOCK_BY_HASH, [
(CHAINID, my_chainid),
(HASH, None)
]], 

[
GET_BLOCK_BY_HEIGHT, [
(CHAINID, my_chainid),
(HEIGHT, None)
]], 

[
GET_BLOCKHEADER_BY_HASH, [
(CHAINID, my_chainid),
(HASH, None)
]], 

[
GET_BLOCKHEADER_BY_HEIGHT, [
(CHAINID, my_chainid),
(HEIGHT, None)
]], 

[
GET_BLOCKHEADER_PO_BY_HASH, [
(CHAINID, my_chainid),
(HASH, None)
]], 

[
GET_BLOCKHEADER_POBY_HEIGHT, [
(CHAINID, my_chainid),
(HEIGHT, None)
]], 

[
GET_BLOCKHEADERS_BY_HEIGHT_RANGE, [
(CHAINID, my_chainid),
(BEGIN, None),
(END, None)
]], 

[
GET_BLOCKHEADERS_FOR_PROTOCOL, [
(CHAINID, my_chainid),
(INTERVAL, None)
]], 

[
GET_BYZANTINE_COUNT, [
(CHAINID, my_chainid)
]], 

[
GET_CIRCULAT, [
(CHAINID, my_chainid),
(NODEID, None),
(MESSAGEBODY, None)
]], 

[
GET_CROSSCHAIN_INFOS, [
]], 

[
GET_CROSSTX_STATE, [
(CHAINID, my_chainid),
(TXHASH, None)
]], 

[
GET_CTX, [
(CHAINID, my_chainid),
(NODEID, None),
(MESSAGEBODY, None)
]], 

[
GET_CTX_STATE, [
(CHAINID, my_chainid),
(NODEID, None),
(MESSAGEBODY, None)
]], 

[
GET_FRIEND_CHAIN_CIRCULATE, [
(CHAINID, my_chainid),
(ASSETIDS, None)
]], 

[
GET_LATEST_BLOCKHEADERS, [
(CHAINID, my_chainid),
(SIZE, None)
]], 

[
GET_LATEST__ROUND_BLOCKHEADERS,[
(CHAINID, my_chainid),
(ROUND, None)
]], 

[
GET_NONCE, [
(CHAINID, my_chainid),
(ASSETCHAINID, None),
(ASSETID, None),
(ADDRESS, my_address),
(ISCONFIRMED, None)
]], 

[
GET_OTHERCTX, [
(CHAINID, my_chainid),
(NODEID, None),
(MESSAGEBODY, None)
]], 

[
GET_REGISTERED_CHAIN_INFO_LIST, [
]], 

[
GET_ROUND_BLOCKHEADERS, [
(CHAINID, my_chainid),
(HEIGHT, None),
(ROUND, None)
]], 

[
GET_STATUS, [
(CHAINID, my_chainid)
]], 

[
GET_VERSION, [
(CHAINID, my_chainid)
]], 

[
INFO, [
(CHAINID, my_chainid)
]], 

[
LATEST_BLOCK, [
(CHAINID, my_chainid)
]], 

[
LATEST_BLOCKHEADER, [
(CHAINID, my_chainid)
]], 

[
LATEST_BLOCKHEADER_PO, [
(CHAINID, my_chainid)
]], 

[
LATEST__HEIGHT, [
(CHAINID, my_chainid)
]], 

[
LISTENER_DEPENDENCIES_READY, []
], [

MSG_PROCESS,[
(CHAINID, my_chainid),
( NODEID, None),
( CMD, None),
(MESSAGEBODY, None)
]], 

[
NEW_BLOCK_HEIGHT, [
(CHAINID, my_chainid),
(HEIGHT,None)
]], 

[
NW_ACTIVE_CROSS, [
(CHAINID, my_chainid),
( MAXOUT, None),
( MAXIN, None),
( SEEDIPS, None)
]], 

[
NW_ADD_NODES, [
(CHAINID, my_chainid),
( ISCROSS, None),
( NODES, None)
]], 

[
NW_BROADCAST, [
( CHAINID, my_chainid),
( EXCLUDENODES, None),
( MESSAGEBODY, None),
( COMMAND, None),
( ISCROSS, None),
( PERCENT, None)
]], 

[
NW_CREATE_NODEGROUP, [
( CHAINID, my_chainid),
( MAGICNUMBER, None),
( MAXOUT, None),
( MAXIN, None),
( MINAVAILABLECOUNT, None),
    (ISCROSSGROUP, None)
]], 

[
NW_DEL_NODES, [
( CHAINID, my_chainid),
( NODES, None)
]], 

[
NW_GET_CHAIN_CONNECT_AMOUNT, [
( CHAINID, my_chainid),
( ISCROSS, None)
]], 

[
NW_GET_GROUP_BY_CHAINID,[
( CHAINID, my_chainid)
]],
    
[
NW_GET_GROUPS, [
( STARTPAGE, None),
( PAGESIZE, None)
]],

[
NW_GET_NODES, [
( CHAINID, my_chainid),
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
( CHAINID, my_chainid)
]],

[
 NW_NODES, [
( CHAINID, my_chainid)
]],

[
 NW_PROTOCOL_REGISTER, [
( ROLE, None),
( PROTOCOLCMDS, None)
]],

[
NW_RECONNECT, [
( CHAINID, my_chainid)
]],

[
 NW_SEND_PEERS_MSG, [
( CHAINID, my_chainid),
   ( NODES, None),
   ( MESSAGEBODY, None),
   ( COMMAND, None)
]],

[
NW_UPDATE_NODE_INFO, [
( CHAINID, my_chainid),
( NODEID, None),
( BLOCKHEIGHT, None),
( BLOCKHASH, None)
]],

[
PARAM_TEST_CMD, [
( INTCOUNT, None),
( BYTECOUNT, my_count),
( SHORTCOUNT, None),
( LONGCOUNT, None)
]], 

[
PROTOCOL_VERSION_CHANGE, [
( CHAINID, my_chainid),
( PROTOCOLVERSION, None)
]], 

[
RECEIVE_PACKING_BLOCK, [
( CHAINID, my_chainid),
( BLOCK, None)
]], 

[
RECV_CIRCULAT, [
( CHAINID, my_chainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_CTX, [
( CHAINID, my_chainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_CTX_HASH, [
( CHAINID, my_chainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_CTX_SIGN, [
( CHAINID, my_chainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_CTX_STATE, [
( CHAINID, my_chainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_OTHER_CTX, [
( CHAINID, my_chainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
RECV_REGCHAIN, [
( CHAINID, my_chainid),
( NODEID, None),
( MESSAGEBODY, None)
]], 

[
REGISTER_MODULE_DEPENDENCIES, [
]], 

[
REGISTER_PROTOCOL, [
( CHAINID, my_chainid),
( MODULECODE, None),
( LIST, None)
]], 

[
ROLLBACK_BLOCK_TXS, [
( CHAINID, my_chainid),
( TXLIST, None),
( BLOCKHEIGHT, None)
]], 

[
ROLLBACK_UNCONFIRM_TX, [
( CHAINID, my_chainid),
( TX, None)
]], 

[
ROLLBACK_BLOCK, [
( CHAINID, my_chainid),
( BLOCKHEADER, None)
]], 

[
ROLLBACK_TX_VALIDATE_STATUS, [
( CHAINID, my_chainid),
( TX, None)
]], 

[
SAVE_BLOCK, [
( CHAINID, my_chainid),
( BLOCKHEADER, None)
]], 

[
SC_BATCH_BEFORE_END, [
( CHAINID, my_chainid),
( BLOCKTYPE, None),
( BLOCKHEIGHT, None)
]], 

[
SC_BATCH_BEGIN, [
( CHAINID, my_chainid),
( BLOCKTYPE, None),
( BLOCKHEIGHT, None),
( BLOCKTIME, None),
( PACKINGADDRESS, None),
( PRESTATEROOT, None)
]], 

[
SC_BATCH_END, [
( CHAINID, my_chainid),
( BLOCKHEIGHT, None)
]],

[
SC_CALL, [
( CHAINID, my_chainid),
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
( CHAINID, my_chainid),
( TX, None)
]],

[
SC_CONSTRUCTOR, [
( CHAINID, my_chainid),
( CONTRACTCODE, None)
]], 

[
SC_CONTRACT_INFO, [
( CHAINID, my_chainid),
( CONTRACTADDRESS, None)
]],

[
 SC_CONTRACT_OFFLINE_TX_HASH_LIST, [
( CHAINID, my_chainid),
( BLOCKHASH, None)
]],

[
SC_CONTRACT_RESULT, [
( CHAINID, my_chainid),
( HASH, None)
]],

[
SC_CONTRACT_RESULT_LIST, [
( CHAINID, my_chainid),
( HASHLIST, None)
]],

[
SC_CONTRACT_TX, [
( CHAINID, my_chainid),
( HASH, None)
]],

[
SC_CREATE, [
( CHAINID, my_chainid),
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
( CHAINID, my_chainid),
( TX, None)
]],

[
SC_DELETE, [
( CHAINID, my_chainid),
( SENDER, None),
( PASSWORD, None),
( CONTRACTADDRESS, None),
( REMARK, None)
]],

[
SC_DELETE_VALIDATOR, [
( CHAINID, my_chainid),
( TX, None)
]],

[
SC_IMPUTED_CALL_GAS, [
( CHAINID, my_chainid),
( SENDER, None),
( VALUE, None),
( CONTRACTADDRESS, None),
( METHODNAME, None),
( METHODDESC, None),
( ARGS, None)
]],

[
SC_IMPUTED_CREATE_GAS, [
( CHAINID, my_chainid),
( SENDER, None),
( CONTRACTCODE, None),
( ARGS, None)
]],

[
SC_INITIAL_ACCOUNT_TOKEN, [
( CHAINID, my_chainid),
( ADDRESS, my_address),
]],

[
SC_INVOKE_CONTRACT, [
( CHAINID, my_chainid),
( BLOCKTYPE, None),
( TX, None)
]],

[
SC_INVOKE_VIEW, [
( CHAINID, my_chainid),
( CONTRACTADDRESS, None),
( METHODNAME, None),
( METHODDESC, None),
( ARGS, None)
]],

[
SC_PACKAGE_BATCH_END, [
( CHAINID, my_chainid),
( BLOCKHEIGHT, None)
]],

[
SC_TOKEN_ASSETS_LIST, [
( CHAINID, my_chainid),
( ADDRESS, my_address),
( PAGENUMBER, None),
( PAGESIZE, None)
]],

[
SC_TOKEN_BALANCE, [
( CHAINID, my_chainid),
( CONTRACTADDRESS, None),
( ADDRESS, my_chainid)
],

[
SC_TOKEN_TRANSFER, [
( CHAINID, my_chainid),
( ADDRESS, my_address),
( TOADDRESS, None),
( CONTRACTADDRESS, None),
( PASSWORD, None),
( AMOUNT, None),
( REMARK, None)
]],

[
SC_TOKEN_TRANSFER_LIST, [
( CHAINID, my_chainid),
( ADDRESS,
my_address),
( PAGENUMBER, None),
( PAGESIZE, None)
]],

[
SC_TRANSFER, [
( CHAINID, my_chainid),
( ADDRESS,
my_address),
( TOADDRESS, None),
( PASSWORD, None),
( AMOUNT, None),
( REMARK, None)
]],

[
SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT, [
( CHAINID, my_chainid),
( STATEROOT, None),
( BLOCKHEIGHT, None),
( CONTRACTADDRESS, None),
( TX, None)
]],

[
SC_UPLOAD, [
( CHAINID, my_chainid),
( JARFILEDATA, None)
]],

[
SC_VALIDATE_CALL, [
( CHAINID, my_chainid),
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
( CHAINID, my_chainid),
( SENDER, None),
( GASLIMIT, None),
( PRICE, None),
( CONTRACTCODE, None),
( ARGS, None)
]],

[
SC_VALIDATE_DELETE, [
( CHAINID, my_chainid),
( CONTRACTADDRESS, None),
]],

[
STOP_AGENTVALID, [
( CHAINID, my_chainid),
( TX, None)
]],

[
TX_COMMIT, [
( CHAINID, my_chainid),
( TXLIST, None),
( BLOCKHEADER, None)
]],

[
TX_VALIDATOR, [
( CHAINID, my_chainid),
( TXLIST, None),
( BLOCKHEADER, None)
]],

[
TX_BACK_PACKABLE_TXS, [
( CHAINID, my_chainid),
( TXLIST, None)
]],

[
TX_BATCH_VERIFY, [
( CHAINID, my_chainid),
( TXLIST, None),
( BLOCKHEADER, None),
( PRESTATEROOT, None)
]],

[
TX_BL_STATE, [
( CHAINID, my_chainid),
( STATUS, None)
]],

[
TX_BLOCK_HEIGHT, [
( CHAINID, my_chainid),
( HEIGHT, None)
]],

[
TX_CS_STATE, [
( CHAINID, my_chainid),
( PACKAGING, None)
]],

[
TX_GET_BLOCKTXS, [
( CHAINID, my_chainid),
( TXHASHLIST, None)
]],

[
TX_GET_BLOCKTXS_EXTEND, [
( CHAINID, my_chainid),
( TXHASHLIST, None),
( ALLHITS, None)
]],

[
TX_GET_CONFIRMED_TX, [
( CHAINID, my_chainid),
( TXHASH, None)
]],

[
TX_GET_CONFIRMED_TX_CLIENT, [
( CHAINID, my_chainid),
( TXHASH, None)
]],

[
TX_GET_NONEXISTENT_UNCONFIRMED_HASHS, [
( CHAINID, my_chainid),
( TXHASHLIST, None)
]],

[
TX_GET_SYSTEMTYPES, [
( CHAINID, my_chainid),
]],

[
TX_GET_TX, [
( CHAINID, my_chainid),
( TXHASH, None)
]],

[
TX_GET_TX_CLIENT, [
( CHAINID, my_chainid),
( TXHASH, None)
]],

[
TX_NEWTX, [
( CHAINID, my_chainid),
( TX, None)
]],

[
TX_PACKABLE_TXS, [
( CHAINID, my_chainid),
( ENDTIMESTAMP, None),
( MAXTXDATASIZE, None),
( BLOCKTIME, None),
( PACKINGADDRESS, None),
( PRESTATEROOT, None)
]],

[
TX_REGISTER, [
( CHAINID, my_chainid),
( MODULECODE, None),
( LIST, None),
( DELLIST, None)
]],

[
TX_ROLLBACK, [
( CHAINID, my_chainid),
( TXHASHLIST, None),
( BLOCKHEADER, None)
]],

[
TX_SAVE, [
( CHAINID, my_chainid),
( TXLIST, None),
( CONTRACTLIST, None),
( BLOCKHEADER, None)
]],

[
TX_VERIFY_TX, [
( CHAINID, my_chainid),
( TX, None)
]],

[
UPDATE_CHAIN_ASSET, [
( CHAINID, my_chainid),
( ASSETS, None)
]],

[
VERIFY_COINDATA, [
( CHAINID, my_chainid),
( TX, None)
]],

[
VERIFY_COINDATA_BATCH_PACKAGED, [
( CHAINID, my_chainid),
( TXLIST, None)
]],

[
WITHDRAW_VALID, [
( CHAINID, my_chainid),
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
