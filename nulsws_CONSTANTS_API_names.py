
# method name constants representing possible api calls to Nulstar.
# Nancy Schorr, December, 2019

AC_ADDRESS_PREFIX = "ac_addAddressPrefix"
AC_CREATE_ACCOUNT = "ac_createAccount"
AC_CREATE_CONTRACT_ACCT = "ac_createContractAccount"
AC_CREATE_MULTISIGN_ACCT  = "ac_createMultiSignAccount"
AC_CREATE_MULTISIGN_TRANSFER  = "ac_createMultiSignTransfer"
AC_CREATE_OFFLINE_ACCT  = "ac_createOfflineAccount"
AC_EXPORT__ACCT_KEYSTORE  = "ac_createMultiSignAccount"
AC_EXPORT_KEYSTORE_JSON  = "ac_exportKeyStoreJson"
AC_GET_ACCOUNT_LIST = "ac_getAccountList"
AC_GET__ACCT_BYADDRESS  = "ac_getAccountByAddress"
AC_GET_ADDRESS_LIST  = "ac_getAddressList"
AC_GET_ADDRESS_PREFIXBY_CHAINID  = "ac_getAddressPrefixByChainId"
AC_GET_ALIASBY_ADDRESS  = "ac_getAliasByAddress"
AC_GET_ALL_ADDRESS_PREFIX = "ac_getAllAddressPrefix"
AC_GET_ALL_PRIKEY  = "ac_getAllPriKey"
AC_GET_ENCRYPTED_ADDRESS_LIST  = "ac_getEncryptedAddressList"
AC_GET_MULTISIGN_ACCT  = "ac_getMultiSignAccount"
AC_GET_PRI_KEY = "ac_getPriKeyByAddress"
AC_GET_PUBKEY  = "ac_getPubKey"
AC_IMPORT_ACCT_BY_KEYSTORE  = "ac_importAccountByKeystore"
AC_IS_ALIAS_USABLE= "ac_isAliasUsable"
AC_IS_MULTISIGN_ACCT_BUILDER  = "ac_isMultiSignAccountBuilder"
AC_SIGN_DIGEST = "ac_signDigest"
ASC_CCOUNT_CONTRACTS = "sc_account_contracts"
BATCH_VALIDATE_BEGIN= "batchValidateBegin"
CANCEL_CROSS_CHAIN = "cancelCrossChain"
CLEAR_UNCONFIRMED_TX = "clearUnconfirmTxs"
CM_ASSET_CIRCULATE_COMMIT = "cm_assetCirculateCommit"
CM_ASSET_CIRCULATE_ROLLBACK = "cm_assetCirculateRollBack"
CM_ASSET_CIRCULATE_VALIDATOR = "cm_assetCirculateValidator"
CM_ASSET_DISABLE = "cm_assetDisable"
CM_ASSET_REG = "cm_assetReg"
CM_CHAIN_ACTIVE = "cm_chainActive"
CM_CHAIN = "cm_chain"
CM_CHAIN_REG = "cm_chainReg"
CM_GET_CHAIN_ASSET = "cm_getChainAsset"
CM_GET_CIRCULATE_CHAIN_ASSET = "cm_getCirculateChainAsset"
CM_GET_CROSS_CHAIN_SIMPLE_INFOS = "cm_getChainsSimpleInfo"
CROSS_CHAIN_REGISTER_CHANGE = "crossChainRegisterChange"
CS_ADDBLOCK = "cs_addBlock"
CS_ADD_EVIDENCE_RECORD = "cs_addEvidenceRecord"
CS_CHAIN_ROLLBACK = "cs_chainRollBack"
CS_CONTRACT_DEPOSIT = "cs_contractDeposit"
CS_CONTRACT_WITHDRAW = "cs_contractWithdraw"
CS_CREATE_AGENT = "cs_createAgent"
CS_CREATE_CONTRACT_AGENT = "cs_createContractAgent"
CS_CREATE_MULTIAGENT = "cs_createMultiAgent"
CS_DEPOSIT_TOAGENT = "cs_depositToAgent"
CS_DOUBLE_SPEND_RECORD = "cs_doubleSpendRecord"
CS_GET_AGENT_ADDRESS_LIST = "cs_get_AgentAddressList"
CS_GET_AGENT_CHANGE_INFO = "cs_getAgentChangeInfo"
CS_GET_AGENT_INFO = "cs_getAgentInfo"
CS_GET_AGENT_LIST = "cs_getAgentList"
CS_GET_AGENT_STATUS = "cs_getAgentStatus"
CS_GET_CONSENSUS_CONFIG = "cs_getConsensusConfig"
CS_GET_CONTRACT_AGENT_INFO = "cs_getContractAgentInfo"
CS_GET_CONTRACT_DEPOSIT_INFO = "cs_getContractDepositInfo"
CS_GET_DEPOSIT_LIST = "cs_getDepositList"
CS_GET_INFO = "cs_getInfo"
CS_GET_NODE_PACKING_ADDR = "cs_getNodePackingAddress"
CS_GET_PACKER_INFO = "cs_getPackerInfo"
CS_GET_PUBLISH_LIST = "cs_getPublishList"
CS_GET_ROUND_INFO = "cs_getRoundInfo"
CS_GET_ROUNDMEMBER_LIST = "cs_getRoundMemberList"
CS_GET_SEED_NODE_INFO = "cs_getSeedNodeInfo"
CS_GET_WHOLEINFO = "cs_getwholeinfo"
CS_MULTIDEPOSIT = "cs_multideposit"
CS_MULTIWITHDRAW = "cs_multiwithdraw"
CS_RANDOM_RAW_SEEDS_COUNT = "cs_random_raw_seeds_count"
CS_RANDOM_RAW_SEEDS_HEIGHT = "cs_random_raw_seeds_height"
CS_RANDOM_SEED_COUNT = "cs_random_seed_count"
CS_RANDOM_SEED_HEIGHT = "cs_random_seed_height"
CS_RECEIVE_HEADER_LIST = "cs_receiveheaderlist"
CS_RUNCHAIN = "cs_runchain"
CS_RUNMAINCHAIN = "cs_runmainchain"
CS_STOP_AGENT = "cs_stopagent"
CS_STOP_CHAIN = "cs_stopchain"
CS_STOP_CONTRACTAGENT = "cs_stopcontractagent"
CS_STOPMULTIAGENT = "cs_stopmultiagent"
CS_TRIGGER_COINBASE_CONTRACT = "cs_triggerCoinBaseContract"
CS_UPDATE_AGENT_CONSENSUS_STATUS  = "cs_updateAgentConsensusStatus"
CS_UPDATE_AGENT_STATUS = "cs_updateAgentStatus"
CS_VALIDBLOCK = "cs_validBlock"
CS_WITHDRAW = "cs_withdraw"
DEPOSIT_VALID = "depositValid"
GET_BALANCE = "getBalanceNonce"
GET_BLOCK_BY_HASH = "getBlockByHash"
GET_BLOCK_BY_HEIGHT = "getBlockByHeight"
GET_BYZANTINE_COUNT = "getByzantineCount"
GET_CROSS_CHAIN_INFOS = "getCrossChainInfos"
GET_FRIEND_CHAIN_CIRCULATE = "getFriendChainCirculate"
GET_NETWORK_GROUP = "getGroupByChainId"
GET_REGISTERED_CHAIN = "getRegisteredChainInfoList"
GET_REGISTERED_CHAIN_MESSAGE = "getChains"
LATEST_BLOCK_HEADER = "latestBlockHeader"
LG_GET_ASSETS_BY_ID = "getAssetsById"
LG_GET_COINDATA = "getBalanceNonce"
NEW_API_MOD_CROSS_TX = "newApiModuleCrossTx"
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
NW_PROTOCOL_REGISTER = "nw_protocolRegister"
NW_RECONNECT = "nw_reconnect"
NW_SEND_PEERS_MSG = "nw_sendPeersMsg"
NW_UPDATE_NODE_INFO = "nw_updateNodeInfo"
PROTOCOL_PRIORITY_REGISTER = "protocolRegisterWithPriority"
REG_CROSS_ASSET = "registerAsset"
REG_CROSS_CHAIN = "registerCrossChain"
SC_CALL = "sc_call"
SC_CALL_VALIDATOR = "sc_call_validator"
SC_CONTRACT_OFFLINE_TX_HASH_LIST = "sc_contract_offline_tx_hash_list"
SC_CONTRACT_RESULT_LIST = "sc_contract_result_list"
SC_CONTRACT_RESULT = "sc_contract_result"
SC_CONTRACT_TX = "sc_contract_tx"
SC_CREATE = "sc_create"
SC_IMPUTED_CALL_GAS = "sc_imputed_call_gas"
SC_IMPUTED_CREATE_GAS = "sc_imputed_create_gas"
SC_INITIAL_ACCOUNT_TOKEN = "sc_initial_account_token"
SC_INVOKE_CONTRACT = "sc_invoke_contract"
SC_INVOKE_VIEW = "sc_invoke_view"
SC_REGISTER_CM_FOR_CONTRACT = "sc_register_cmd_for_contract"
SC_TOKEN_ASSETS_LIST = "sc_token_assets_list"
SC_TOKEN_BALANCE = "sc_token_balance"
SC_TOKEN_TRANSFER_LIST = "sc_token_transfer_list"
SC_TOKEN_TRANSFER = "sc_token_transfer"
SC_TRANSFER_FEE = "sc_transfer_fee"
SC_TRANSFER = "sc_transfer"
SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT = "sc_trigger_payable_for_consensus_contract"
SC_VALIDATE_CALL = "sc_validate_call"
SC_VALIDATE_CREATE = "sc_validate_create"
SC_VALIDATE_DELETE = "sc_validate_delete"
TX_BASE_VALIDATE = "tx_baseValidateTx"
TX_CHAIN_ID = "chainId"
TX_CLEAN_THREAD = "cleanTxThread"
TX_COUNT = "txCount"
TX_GET_TX = "tx_getTxClient"
TX_HASH_LIST = "txHashList"
TX_HASH = "txHash"
TX_LIST = "txList"
TX_NEW_CM = "tx_newTx"
TX_NEW = "tx_newTx"
TX_NEWTX = "tx_newTx"
TX_THREAD = "newNetTxThread"
UPDATE_CHAIN_ASSET = "updateChainAsset"

#
# "ac_removeAccount"
# "ac_removeMultiSignAccount"
# "ac_setAlias"
# "ac_setMultiSignAlias"
# "ac_setRemark"
# "ac_signBlockDigest"
# "ac_signDigest"
# "ac_signMultiSignTransaction"
# "ac_transfer"
# "ac_updateOfflineAccountPassword"
# "ac_updatePassword"
# "ac_validationPassword"
# "ac_verifySignData"
# "blockValidate"




__ALL__ = ['AC_ADDRESS_PREFIX', 'AC_GET_ACCOUNT_LIST', 'AC_GET_ALL_ADDRESS_PREFIX', 'AC_GET_PRI_KEY',
           'AC_IS_ALIAS_USABLE', 'AC_SIGN_DIGEST', 'ASC_CCOUNT_CONTRACTS', 'BATCH_VALIDATE_BEGIN',
           'CANCEL_CROSS_CHAIN', 'CM_ASSET_CIRCULATE_COMMIT', 'CM_ASSET_CIRCULATE_ROLLBACK',
           'CM_ASSET_CIRCULATE_VALIDATOR', 'CM_ASSET_DISABLE', 'CM_ASSET_REG', 'CM_CHAIN', 'CM_CHAIN_ACTIVE',
           'CM_CHAIN_REG', 'CM_GET_CHAIN_ASSET', 'CM_GET_CIRCULATE_CHAIN_ASSET',
           'CM_GET_CROSS_CHAIN_SIMPLE_INFOS', 'CROSS_CHAIN_REGISTER_CHANGE', 'CS_GET_CONSENSUS_CONFIG',
           'CS_GET_SEED_NODE_INFO', 'GET_BALANCE', 'GET_BLOCK_BY_HASH', 'GET_BLOCK_BY_HEIGHT',
           'GET_BYZANTINE_COUNT', 'GET_CROSS_CHAIN_INFOS', 'GET_FRIEND_CHAIN_CIRCULATE', 'GET_NETWORK_GROUP',
           'GET_REGISTERED_CHAIN', 'GET_REGISTERED_CHAIN_MESSAGE', 'LATEST_BLOCK_HEADER',
           'LG_GET_ASSETS_BY_ID', 'LG_GET_COINDATA', 'NEW_API_MOD_CROSS_TX', 'NW_ACTIVE_CROSS',
           'NW_ADD_NODES', 'NW_BROADCAST', 'NW_CREATE_NODEGROUP', 'NW_CROSS_RANDOM_BROADCAST',
           'NW_CROSS_SEEDS', 'NW_DELETE_NODEGROUP', 'NW_DEL_NODES', 'NW_GET_CHAIN_CONNECT_AMOUNT',
           'NW_GET_DELETE_NODEGROUP', 'NW_GET_GROUPS', 'NW_GET_GROUP_BY_CHAINID',
           'NW_GET_MAIN_NET_MAGIC_NUMBER', 'NW_GET_NODES', 'NW_GET_SEEDS', 'NW_GET_TIME_CALL',
           'NW_PROTOCOL_REGISTER', 'NW_RECONNECT', 'NW_SEND_PEERS_MSG', 'NW_UPDATE_NODE_INFO',
           'PROTOCOL_PRIORITY_REGISTER', 'REG_CROSS_ASSET', 'REG_CROSS_CHAIN', 'SC_CALL', 'SC_CALL_VALIDATOR',
           'SC_CONTRACT_OFFLINE_TX_HASH_LIST', 'SC_CONTRACT_RESULT', 'SC_CONTRACT_RESULT_LIST',
           'SC_CONTRACT_TX', 'SC_CREATE', 'SC_IMPUTED_CALL_GAS', 'SC_IMPUTED_CREATE_GAS',
           'SC_INITIAL_ACCOUNT_TOKEN', 'SC_INVOKE_CONTRACT', 'SC_INVOKE_VIEW', 'SC_REGISTER_CM_FOR_CONTRACT',
           'SC_TOKEN_ASSETS_LIST', 'SC_TOKEN_BALANCE', 'SC_TOKEN_TRANSFER', 'SC_TOKEN_TRANSFER_LIST',
           'SC_TRANSFER', 'SC_TRANSFER_FEE', 'SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT', 'SC_VALIDATE_CALL',
           'SC_VALIDATE_CREATE', 'SC_VALIDATE_DELETE', 'TX_BASE_VALIDATE', 'TX_CHAIN_ID', 'TX_CLEAN_THREAD',
           'TX_COUNT', 'TX_GET_TX', 'TX_HASH', 'TX_HASH_LIST', 'TX_LIST', 'TX_NEW', 'TX_NEWTX', 'TX_NEW_CM',
           'TX_THREAD', 'TX_VALIEDATE', 'UPDATE_CHAIN_ASSET']




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


# cm_asset
# ac_signMultiSignTransaction
# ac_transfer
# ac_updateOfflineAccountPassword
# ac_updatePassword
# ac_validationPassword
# ac_verifySignData
# batchValidateBegin
# blockValidate