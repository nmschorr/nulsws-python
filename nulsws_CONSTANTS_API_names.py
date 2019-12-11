
# method name constants representing possible api calls to Nulstar.
# Nancy Schorr, December, 2019


__ALL__ = ['AC_ADDRESS_PREFIX', 'AC_GET_ACCOUNT_LIST', 'AC_GET_ALL_ADDRESS_PREFIX', 'AC_GET_PRI_KEY',
 'AC_IS_ALIAS_USABLE', 'AC_SIGN_DIGEST', 'ASC_CCOUNT_CONTRACTS', 'BATCH_VALIDATE_BEGIN', 'CANCEL_CROSS_CHAIN',
 'CM_ASSET_CIRCULATE_COMMIT', 'CM_ASSET_CIRCULATE_ROLLBACK', 'CM_ASSET_CIRCULATE_VALIDATOR',
 'CM_ASSET_DISABLE', 'CM_ASSET_REG', 'CM_CHAIN', 'CM_CHAIN_ACTIVE', 'CM_CHAIN_REG', 'CM_GET_CHAIN_ASSET',
 'CM_GET_CIRCULATE_CHAIN_ASSET', 'CM_GET_CROSS_CHAIN_SIMPLE_INFOS', 'CROSS_CHAIN_REGISTER_CHANGE',
 'CS_GET_CONSENSUS_CONFIG', 'CS_GET_SEED_NODE_INFO', 'GET_BALANCE', 'GET_BLOCK_BY_HASH',
 'GET_BLOCK_BY_HEIGHT', 'GET_BYZANTINE_COUNT', 'GET_CROSS_CHAIN_INFOS', 'GET_FRIEND_CHAIN_CIRCULATE',
 'GET_NETWORK_GROUP', 'GET_REGISTERED_CHAIN', 'GET_REGISTERED_CHAIN_MESSAGE', 'LATEST_BLOCK_HEADER',
 'LG_GET_ASSETS_BY_ID', 'LG_GET_COINDATA', 'NEW_API_MOD_CROSS_TX', 'NW_ACTIVE_CROSS', 'NW_ADD_NODES',
 'NW_BROADCAST', 'NW_CREATE_NODEGROUP', 'NW_CROSS_RANDOM_BROADCAST', 'NW_CROSS_SEEDS', 'NW_DELETE_NODEGROUP',
 'NW_DEL_NODES', 'NW_GET_CHAIN_CONNECT_AMOUNT', 'NW_GET_DELETE_NODEGROUP', 'NW_GET_GROUPS',
 'NW_GET_GROUP_BY_CHAINID', 'NW_GET_MAIN_NET_MAGIC_NUMBER', 'NW_GET_NODES', 'NW_GET_SEEDS',
 'NW_GET_TIME_CALL', 'NW_PROTOCOL_REGISTER', 'NW_RECONNECT', 'NW_SEND_PEERS_MSG', 'NW_UPDATE_NODE_INFO',
 'PROTOCOL_PRIORITY_REGISTER', 'REG_CROSS_ASSET', 'REG_CROSS_CHAIN', 'SC_CALL', 'SC_CALL_VALIDATOR',
 'SC_CONTRACT_OFFLINE_TX_HASH_LIST', 'SC_CONTRACT_RESULT', 'SC_CONTRACT_RESULT_LIST', 'SC_CONTRACT_TX',
 'SC_CREATE', 'SC_IMPUTED_CALL_GAS', 'SC_IMPUTED_CREATE_GAS', 'SC_INITIAL_ACCOUNT_TOKEN',
 'SC_INVOKE_CONTRACT', 'SC_INVOKE_VIEW', 'SC_REGISTER_CM_FOR_CONTRACT', 'SC_TOKEN_ASSETS_LIST',
 'SC_TOKEN_BALANCE', 'SC_TOKEN_TRANSFER', 'SC_TOKEN_TRANSFER_LIST', 'SC_TRANSFER', 'SC_TRANSFER_FEE',
 'SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT', 'SC_VALIDATE_CALL', 'SC_VALIDATE_CREATE', 'SC_VALIDATE_DELETE',
 'TX_BASE_VALIDATE', 'TX_CHAIN_ID', 'TX_CLEAN_THREAD', 'TX_COUNT', 'TX_GET_TX', 'TX_HASH', 'TX_HASH_LIST',
 'TX_LIST', 'TX_NEW', 'TX_NEWTX', 'TX_NEW_CM', 'TX_THREAD', 'TX_VALIEDATE', 'UPDATE_CHAIN_ASSET',
 'CS_GET_NODE_PACKING_ADDR']


AC_GET_ACCOUNT_LIST = "ac_getAccountList"
BATCH_VALIDATE_BEGIN= "batchValidateBegin"


SC_CALL = "sc_call"
SC_CALL_VALIDATOR = "sc_call_validator"
AC_ADDRESS_PREFIX = "ac_addAddressPrefix"
AC_GET_PRI_KEY = "ac_getPriKeyByAddress"
AC_SIGN_DIGEST = "ac_signDigest"
CM_ASSET_CIRCULATE_COMMIT = "cm_assetCirculateCommit"
CM_ASSET_CIRCULATE_ROLLBACK = "cm_assetCirculateRollBack"
CM_ASSET_CIRCULATE_VALIDATOR = "cm_assetCirculateValidator"
CM_ASSET_DISABLE = "cm_assetDisable"
CM_ASSET_REG = "cm_assetReg"
LATEST_BLOCK_HEADER = "latestBlockHeader"
CANCEL_CROSS_CHAIN = "cancelCrossChain"
CM_CHAIN_ACTIVE = "cm_chainActive"
CM_CHAIN = "cm_chain"
CM_CHAIN_REG = "cm_chainReg"
CROSS_CHAIN_REGISTER_CHANGE = "crossChainRegisterChange"
CS_GET_SEED_NODE_INFO = "cs_getSeedNodeInfo"
CM_GET_CHAIN_ASSET = "cm_getChainAsset"
CM_GET_CIRCULATE_CHAIN_ASSET = "cm_getCirculateChainAsset"
GET_CROSS_CHAIN_INFOS = "getCrossChainInfos"
CM_GET_CROSS_CHAIN_SIMPLE_INFOS = "cm_getChainsSimpleInfo"
GET_FRIEND_CHAIN_CIRCULATE = "getFriendChainCirculate"
LG_GET_ASSETS_BY_ID = "getAssetsById"
LG_GET_COINDATA = "getBalanceNonce"
NW_ACTIVE_CROSS = "nw_activeCross"
NW_ADD_NODES = "nw_addNodes"
NW_BROADCAST = "nw_broadcast"
NW_CREATE_NODEGROUP = "nw_createNodeGroup"
NW_CROSS_RANDOM_BROADCAST = "nw_crossRandomBroadcast"
NW_CROSS_SEEDS = "nw_getSeeds"
NW_DELETE_NODEGROUP = "nw_delNodeGroup"
NW_DEL_NODES = "nw_delNodes"
NW_GET_CHAIN_CONNECT_AMOUNT = "nw_getChainConnectAmount"
NW_GET_DELETE_NODEGROUP = "nw_delNodeGroup"
NW_GET_GROUP_BY_CHAINID = "nw_getGroupByChainId"
NW_GET_GROUPS = "nw_getGroups"
NW_GET_MAIN_NET_MAGIC_NUMBER = "nw_getMainMagicNumber"
NW_GET_NODES = "nw_getNodes"
NW_GET_SEEDS = "nw_getSeeds"
NW_GET_TIME_CALL = "nw_currentTimeMillis"
PROTOCOL_PRIORITY_REGISTER = "protocolRegisterWithPriority"
NW_PROTOCOL_REGISTER = "nw_protocolRegister"
NW_RECONNECT = "nw_reconnect"
NW_SEND_PEERS_MSG = "nw_sendPeersMsg"
NW_UPDATE_NODE_INFO = "nw_updateNodeInfo"
REG_CROSS_ASSET = "registerAsset"
REG_CROSS_CHAIN = "registerCrossChain"
TX_NEW = "tx_newTx"
UPDATE_CHAIN_ASSET = "updateChainAsset"
SC_CONTRACT_OFFLINE_TX_HASH_LIST = "sc_contract_offline_tx_hash_list"
SC_CONTRACT_RESULT_LIST = "sc_contract_result_list"
SC_CONTRACT_RESULT = "sc_contract_result"
SC_CONTRACT_TX = "sc_contract_tx"
SC_CREATE = "sc_create"
AC_GET_ALL_ADDRESS_PREFIX = "ac_getAllAddressPrefix"
GET_BALANCE = "getBalanceNonce"
GET_BLOCK_BY_HASH = "getBlockByHash"
GET_BLOCK_BY_HEIGHT = "getBlockByHeight"
GET_BYZANTINE_COUNT = "getByzantineCount"
CS_GET_CONSENSUS_CONFIG = "cs_getConsensusConfig"
GET_NETWORK_GROUP = "getGroupByChainId"
GET_REGISTERED_CHAIN = "getRegisteredChainInfoList"
GET_REGISTERED_CHAIN_MESSAGE = "getChains"
TX_GET_TX = "tx_getTxClient"
SC_IMPUTED_CALL_GAS = "sc_imputed_call_gas"
SC_IMPUTED_CREATE_GAS = "sc_imputed_create_gas"
SC_INITIAL_ACCOUNT_TOKEN = "sc_initial_account_token"
SC_INVOKE_CONTRACT = "sc_invoke_contract"
SC_INVOKE_VIEW = "sc_invoke_view"
AC_IS_ALIAS_USABLE= "ac_isAliasUsable"
SC_REGISTER_CM_FOR_CONTRACT = "sc_register_cmd_for_contract"
NEW_API_MOD_CROSS_TX = "newApiModuleCrossTx"
ASC_CCOUNT_CONTRACTS = "sc_account_contracts"
SC_TOKEN_ASSETS_LIST = "sc_token_assets_list"
SC_TOKEN_BALANCE = "sc_token_balance"
SC_TOKEN_TRANSFER_LIST = "sc_token_transfer_list"
SC_TOKEN_TRANSFER = "sc_token_transfer"
SC_TRANSFER_FEE = "sc_transfer_fee"
SC_TRANSFER = "sc_transfer"
SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT = "sc_trigger_payable_for_consensus_contract"
TX_BASE_VALIDATE = "tx_baseValidateTx"
TX_CHAIN_ID = "chainId"
TX_CLEAN_THREAD = "cleanTxThread"
TX_COUNT = "txCount"
TX_HASH_LIST = "txHashList"
TX_HASH = "txHash"
TX_LIST = "txList"
TX_NEW_CM = "tx_newTx"
TX_NEWTX = "tx_newTx"
TX_THREAD = "newNetTxThread"
TX_VALIEDATE = "tx_verifyTx"
SC_VALIDATE_CALL = "sc_validate_call"
SC_VALIDATE_CREATE = "sc_validate_create"
SC_VALIDATE_DELETE = "sc_validate_delete"
#
# #ones not done yet
# cs_getWholeInfo
# cs_multiDeposit
# cs_multiWithdraw
# cs_random_raw_seeds_count
# cs_random_raw_seeds_height
# cs_random_seed_count
# cs_random_seed_height
# cs_receiveHeaderList
# cs_runChain
# cs_runMainChain
# cs_stopAgent
# cs_stopChain
# cs_stopContractAgent
# cs_stopMultiAgent
# cs_triggerCoinBaseContract
# cs_updateAgentConsensusStatus
# cs_updateAgentStatus
# cs_validBlock
# cs_withdraw
# depositValid
# cs_addBlock
# cs_addEvidenceRecord
# cs_chainRollBack
# cs_contractDeposit
# cs_contractWithdraw
# cs_createAgent
# cs_createContractAgent
# cs_createMultiAgent
# cs_depositToAgent
# cs_doubleSpendRecord
# cs_getAgentAddressList
CS_GET_AGENT_CHANGE_INFO="cs_getAgentChangeInfo"
# cs_getAgentInfo
# cs_getAgentList
# cs_getAgentStatus
# cs_getContractAgentInfo
# cs_getContractDepositInfo
# cs_getDepositList
# cs_getInfo
CS_GET_NODE_PACKING_ADDR = "cs_getNodePackingAddress"
cs_getPackerInfo
cs_getPublishList
cs_getRoundInfo
cs_getRoundMemberList
ac_createAccount
ac_createContractAccount
ac_createMultiSignAccount
ac_createMultiSignTransfer
ac_createOfflineAccount
ac_exportAccountKeyStore
ac_exportKeyStoreJson
ac_getAccountByAddress
ac_getAddressList
ac_getAddressPrefixByChainId
ac_getAliasByAddress
ac_getAllPriKey
ac_getEncryptedAddressList
ac_getMultiSignAccount
ac_getPubKey
ac_importAccountByKeystore
ac_isMultiSignAccountBuilder

CS_GETPACKERINFO = "cs_getPackerInfo"
CS_GETPUBLISHLIST = "cs_getPublishList"
CS_GETROUNDINFO = "cs_getRoundInfo"
CS_GETROUNDMEMBERLIST = "cs_getRoundMemberList"
AC_CREATEACCOUNT = "ac_createAccount"
AC_CREATECONTRACTACCOUNT = "ac_createContractAccount"
AC_CREATEMULTISIGNACCOUNT = "x"
AC_CREATEMULTISIGNTRANSFER = "x"
AC_CREATEOFFLINEACCOUNT = "x"
AC_EXPORTACCOUNTKEYSTORE = "x"
AC_EXPORTKEYSTOREJSON = "x"
AC_GETACCOUNTBYADDRESS=
AC_GETADDRESSLIST = "x"
AC_GETADDRESSPREFIXBYCHAINID = "x"
AC_GETALIASBYADDRESS = "x"
AC_GETALLPRIKEY = "x"
AC_GETENCRYPTEDADDRESSLIST = "x"
AC_GETMULTISIGNACCOUNT = "x"
AC_GETPUBKEY = "x"
AC_IMPORTACCOUNTBYKEYSTORE = "x"
AC_ISMULTISIGNACCOUNTBUILDER = "x"








# ac_removeAccount
# ac_removeMultiSignAccount
# ac_setAlias
# ac_setMultiSignAlias
# ac_setRemark
# ac_signBlockDigest
# commitBatchUnconfirmedTxs
# commitBlockTxs
# commitUnconfirmedTx
# connectReady
# createAgentValid
# createCrossTx
# checkBlockVersion
# checkupdates
# clearUnconfirmTxs
# cm_asset
# ac_signMultiSignTransaction
# ac_transfer
# ac_updateOfflineAccountPassword
# ac_updatePassword
# ac_validationPassword
# ac_verifySignData
# batchValidateBegin
# blockValidate