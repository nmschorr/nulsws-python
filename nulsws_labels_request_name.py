
# method name constants representing possible api calls to Nulstar.
# Nancy Schorr, December, 2019

AC_GET_ACCOUNT_LIST = "ac_getAccountList"








CALL = "sc_call"
CALL_VALIDATOR = "sc_call_validator"
CMD_AC_ADDRESS_PREFIX = "ac_addAddressPrefix"
CMD_AC_GET_PRI_KEY = "ac_getPriKeyByAddress"
CMD_AC_SIGN_DIGEST = "ac_signDigest"
CMD_ASSET_CIRCULATE_COMMIT = "cm_assetCirculateCommit"
CMD_ASSET_CIRCULATE_ROLLBACK = "cm_assetCirculateRollBack"
CMD_ASSET_CIRCULATE_VALIDATOR = "cm_assetCirculateValidator"
CMD_ASSET_DISABLE = "cm_assetDisable"
CMD_ASSET_REG = "cm_assetReg"
CMD_BL_BEST_BLOCK_HEADER = "latestBlockHeader"
CMD_CANCEL_CROSS_CHAIN = "cancelCrossChain"
CMD_CHAIN_ACTIVE = "cm_chainActive"
CMD_CHAIN = "cm_chain"
CMD_CHAIN_REG = "cm_chainReg"
CMD_CROSS_CHAIN_REGISTER_CHANGE = "crossChainRegisterChange"
CMD_CS_GET_SEED_NODE_INFO = "cs_getSeedNodeInfo"
CMD_GET_CHAIN_ASSET = "cm_getChainAsset"
CMD_GET_CIRCULATE_CHAIN_ASSET = "cm_getCirculateChainAsset"
CMD_GET_CROSS_CHAIN_INFOS = "getCrossChainInfos"
CMD_GET_CROSS_CHAIN_SIMPLE_INFOS = "cm_getChainsSimpleInfo"
CMD_GET_FRIEND_CHAIN_CIRCULATE = "getFriendChainCirculate"
CMD_LG_GET_ASSETS_BY_ID = "getAssetsById"
CMD_LG_GET_COINDATA = "getBalanceNonce"
CMD_NW_ACTIVE_CROSS = "nw_activeCross"
CMD_NW_ADD_NODES = "nw_addNodes"
CMD_NW_BROADCAST = "nw_broadcast"
CMD_NW_CREATE_NODEGROUP = "nw_createNodeGroup"
CMD_NW_CROSS_RANDOM_BROADCAST = "nw_crossRandomBroadcast"
CMD_NW_CROSS_SEEDS = "nw_getSeeds"
CMD_NW_DELETE_NODEGROUP = "nw_delNodeGroup"
CMD_NW_DEL_NODES = "nw_delNodes"
CMD_NW_GET_CHAIN_CONNECT_AMOUNT = "nw_getChainConnectAmount"
CMD_NW_GET_DELETE_NODEGROUP = "nw_delNodeGroup"
CMD_NW_GET_GROUP_BY_CHAINID = "nw_getGroupByChainId"
CMD_NW_GET_GROUPS = "nw_getGroups"
CMD_NW_GET_MAIN_NET_MAGIC_NUMBER = "nw_getMainMagicNumber"
CMD_NW_GET_NODES = "nw_getNodes"
CMD_NW_GET_SEEDS = "nw_getSeeds"
CMD_NW_GET_TIME_CALL = "nw_currentTimeMillis"
CMD_NW_PROTOCOL_PRIORITY_REGISTER = "protocolRegisterWithPriority"
CMD_NW_PROTOCOL_REGISTER = "nw_protocolRegister"
CMD_NW_RECONNECT = "nw_reconnect"
CMD_NW_SEND_PEERS_MSG = "nw_sendPeersMsg"
CMD_NW_UPDATE_NODE_INFO = "nw_updateNodeInfo"
CMD_REG_CROSS_ASSET = "registerAsset"
CMD_REG_CROSS_CHAIN = "registerCrossChain"
CMD_TX_NEW = "tx_newTx"
CMD_UPDATE_CHAIN_ASSET = "updateChainAsset"
CONTRACT_OFFLINE_TX_HASH_LIST = "sc_contract_offline_tx_hash_list"
CONTRACT_RESULT_LIST = "sc_contract_result_list"
CONTRACT_RESULT = "sc_contract_result"
CONTRACT_TX = "sc_contract_tx"
CREATE = "sc_create"
GET_ALL_ADDRESS_PREFIX = "ac_getAllAddressPrefix"
GET_BALANCE = "getBalanceNonce"
GET_BLOCK_BY_HASH = "getBlockByHash"
GET_BLOCK_BY_HEIGHT = "getBlockByHeight"
GET_BYZANTINE_COUNT = "getByzantineCount"
GET_CONSENSUS_CONFIG = "cs_getConsensusConfig"
GET_NETWORK_GROUP = "nw_getGroupByChainId"
GET_REGISTERED_CHAIN = "getRegisteredChainInfoList"
GET_REGISTERED_CHAIN_MESSAGE = "getChains"
GET_TX = "tx_getTxClient"
IMPUTED_CALL_GAS = "sc_imputed_call_gas"
IMPUTED_CREATE_GAS = "sc_imputed_create_gas"
INITIAL_ACCOUNT_TOKEN = "sc_initial_account_token"
INVOKE_CONTRACT = "sc_invoke_contract"
INVOKE_VIEW = "sc_invoke_view"
IS_ALAIS_USABLE= "ac_isAliasUsable"
REGISTER_CMD_FOR_CONTRACT = "sc_register_cmd_for_contract"
SEND_CROSS_TX = "newApiModuleCrossTx"
ACCOUNT_CONTRACTS = "sc_account_contracts"
TOKEN_ASSETS_LIST = "sc_token_assets_list"
TOKEN_BALANCE = "sc_token_balance"
TOKEN_TRANSFER_LIST = "sc_token_transfer_list"
TOKEN_TRANSFER = "sc_token_transfer"
TRANSFER_FEE = "sc_transfer_fee"
TRANSFER = "sc_transfer"
TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT = "sc_trigger_payable_for_consensus_contract"
TX_BASE_VALIDATE = "tx_baseValidateTx"
TX_CHAIN_ID = "chainId"
TX_CLEAN_THREAD = "cleanTxThread"
TX_COUNT = "txCount"
TX_HASH_LIST = "txHashList"
TX_HASH = "txHash"
TX_LIST = "txList"
TX_NEW_CMD = "tx_newTx"
TX_NEWTX = "tx_newTx"
TX_THREAD = "newNetTxThread"
TX_VALIEDATE = "tx_verifyTx"
VALIDATE_CALL = "sc_validate_call"
VALIDATE_CREATE = "sc_validate_create"
VALIDATE_DELETE = "sc_validate_delete"
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
# cs_getAgentChangeInfo
# cs_getAgentInfo
# cs_getAgentList
# cs_getAgentStatus
# cs_getContractAgentInfo
# cs_getContractDepositInfo
# cs_getDepositList
# cs_getInfo
# cs_getNodePackingAddress
# cs_getPackerInfo
# cs_getPublishList
# cs_getRoundInfo
# cs_getRoundMemberList
# ac_createAccount
# ac_createContractAccount
# ac_createMultiSignAccount
# ac_createMultiSignTransfer
# ac_createOfflineAccount
# ac_exportAccountKeyStore
# ac_exportKeyStoreJson
# ac_getAccountByAddress
# ac_getAddressList
# ac_getAddressPrefixByChainId
# ac_getAliasByAddress
# ac_getAllPriKey
# ac_getEncryptedAddressList
# ac_getMultiSignAccount
# ac_getPubKey
# ac_importAccountByKeystore
# ac_isMultiSignAccountBuilder
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