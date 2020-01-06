#!/usr/bin/python3.7

from .nulsws_labels_cls import NulswsLabels

# use these 'CONSTANTS' to make a run list

n = NulswsLabels()


name_pairs_dict = [
    ("AC_CREATE_ACCOUNT", n.AC_CREATE_ACCOUNT),
    ("AC_CREATE_CONTRACT_ACCOUNT", n.AC_CREATE_CONTRACT_ACCOUNT),
    ("AC_CREATE_MULTI_SIGN_ACCOUNT", n.AC_CREATE_MULTI_SIGN_ACCOUNT),
    ("AC_CREATE_MULTI_SIGN_TRANSFER", n.AC_CREATE_MULTI_SIGN_TRANSFER),
    ("AC_CREATE_OFFLINE_ACCOUNT", n.AC_CREATE_OFFLINE_ACCOUNT),
    ("AC_EXPORT_ACCOUNT_KEYSTORE", n.AC_EXPORT_ACCOUNT_KEYSTORE),
    ("AC_EXPORT_KEYSTORE_JSON", n.AC_EXPORT_KEYSTORE_JSON),
    ("AC_GET_ACCOUNT_LIST", n.AC_GET_ACCOUNT_LIST),
    ("AC_GET_ACCOUNT_BYADDRESS", n.AC_GET_ACCOUNT_BYADDRESS),
    ("AC_GET_ADDRESS_LIST", n.AC_GET_ADDRESS_LIST),
    ("AC_GET_ADDRESS_PREFIX_BY_CHAINID", n.AC_GET_ADDRESS_PREFIX_BY_CHAINID),
    ("AC_GET_ALIASBY_ADDRESS", n.AC_GET_ALIASBY_ADDRESS),
    ("AC_GET_ALL_ADDRESS_PREFIX", n.AC_GET_ALL_ADDRESS_PREFIX),
    ("AC_GET_ALL_PRIKEY", n.AC_GET_ALL_PRIKEY),
    ("AC_GET_ENCRYPTED_ADDRESS_LIST", n.AC_GET_ENCRYPTED_ADDRESS_LIST),
    ("AC_GET_MULTI_SIGN_ACCOUNT", n.AC_GET_MULTI_SIGN_ACCOUNT),
    ("AC_GET_PRIKEY", n.AC_GET_PRIKEY),
    ("AC_GET_PUBKEY", n.AC_GET_PUBKEY),
    ("AC_IMPORT_ACCOUNT_BY_PRIKEY", n.AC_IMPORT_ACCOUNT_BY_PRIKEY),
    ("AC_IMPORT_ACCOUNT_BY_KEYSTORE", n.AC_IMPORT_ACCOUNT_BY_KEYSTORE),
    ("AC_IS_ALIAS_USABLE", n.AC_IS_ALIAS_USABLE),
    ("AC_IS_MULTISIGN_ACCOUNT_BUILDER", n.AC_IS_MULTISIGN_ACCOUNT_BUILDER),
    ("AC_REMOVE_ACCOUNT", n.AC_REMOVE_ACCOUNT),
    ("AC_REMOVE_MULTISIGN_ACCOUNT", n.AC_REMOVE_MULTISIGN_ACCOUNT),
    ("AC_SET_ALIAS", n.AC_SET_ALIAS),
    ("AC_SET_MULTISIGN_ALIAS", n.AC_SET_MULTISIGN_ALIAS),
    ("AC_SET_REMARK", n.AC_SET_REMARK),
    ("AC_SIGN_BLOCKDIGEST", n.AC_SIGN_BLOCKDIGEST),
    ("AC_SIGN_DIGEST", n.AC_SIGN_DIGEST),
    ("AC_SIGN_MULTISIGN_TRANSACTION", n.AC_SIGN_MULTISIGN_TRANSACTION),
    ("AC_TRANSFER", n.AC_TRANSFER),
    ("AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD", n.AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD),
    ("AC_UPDATE_PASSWORD", n.AC_UPDATE_PASSWORD),
    ("AC_VALIDATION_PASSWORD", n.AC_VALIDATION_PASSWORD),
    ("AC_VERIFY_SIGN_DATA", n.AC_VERIFY_SIGN_DATA),
    ("SC_CCOUNT_CONTRACTS", n.SC_CCOUNT_CONTRACTS),
    ("BATCH_VALIDATE_BEGIN", n.BATCH_VALIDATE_BEGIN),
    ("BLOCK_VALIDATE", n.BLOCK_VALIDATE),
    ("CANCEL_CROSSCHAIN", n.CANCEL_CROSSCHAIN),
    ("CHECK_BLOCK_VERSION", n.CHECK_BLOCK_VERSION),
    ("CHECK_UPDATES", n.CHECK_UPDATES),
    ("CLEAR_UNCONFIRMED_TX", n.CLEAR_UNCONFIRMED_TX),
    ("CM_ASSET_CIRCULATE_COMMIT", n.CM_ASSET_CIRCULATE_COMMIT),
    ("CM_ASSET_CIRCULATE_ROLLBACK", n.CM_ASSET_CIRCULATE_ROLLBACK),
    ("CM_ASSET_CIRCULATE_VALIDATOR", n.CM_ASSET_CIRCULATE_VALIDATOR),
    ("CM_ASSET", n.CM_ASSET),
    ("CM_ASSET_DISABLE", n.CM_ASSET_DISABLE),
    ("CM_ASSET_REG", n.CM_ASSET_REG),
    ("CM_CHAIN_ACTIVE", n.CM_CHAIN_ACTIVE),
    ("CM_CHAIN", n.CM_CHAIN),
    ("CM_CHAIN_REG", n.CM_CHAIN_REG),
    ("CM_GET_CHAIN_ASSET", n.CM_GET_CHAIN_ASSET),
    ("CM_GET_CIRCULATE_CHAIN_ASSET", n.CM_GET_CIRCULATE_CHAIN_ASSET),
    ("CM_GET_CROSSCHAIN_SIMPLE_INFOS", n.CM_GET_CROSSCHAIN_SIMPLE_INFOS),
    ("COMMIT_BATCH_UNCONFIRMED_TXS", n.COMMIT_BATCH_UNCONFIRMED_TXS),
    ("COMMIT_BLOCKTXS", n.COMMIT_BLOCKTXS),
    ("COMMIT_UNCONFIRMEDTX", n.COMMIT_UNCONFIRMEDTX),
    ("CONNECT_READY", n.CONNECT_READY),
    ("CREATE_AGENT_VALID", n.CREATE_AGENT_VALID),
    ("CREATE_CROSSTX", n.CREATE_CROSSTX),
    ("CROSSCHAIN_REGISTER_CHANGE", n.CROSSCHAIN_REGISTER_CHANGE),
    ("CS_ADD_BLOCK", n.CS_ADD_BLOCK),
    ("CS_ADD_EVIDENCE_RECORD", n.CS_ADD_EVIDENCE_RECORD),
    ("CS_CHAIN_ROLLBACK", n.CS_CHAIN_ROLLBACK),
    ("CS_CONTRACT_DEPOSIT", n.CS_CONTRACT_DEPOSIT),
    ("CS_CONTRACT_WITHDRAW", n.CS_CONTRACT_WITHDRAW),
    ("CS_CREATE_AGENT", n.CS_CREATE_AGENT),
    ("CS_CREATE_CONTRACT_AGENT", n.CS_CREATE_CONTRACT_AGENT),
    ("CS_CREATE_MULTI_AGENT", n.CS_CREATE_MULTI_AGENT),
    ("CS_DEPOSIT_TOAGENT", n.CS_DEPOSIT_TOAGENT),
    ("CS_DOUBLE_SPEND_RECORD", n.CS_DOUBLE_SPEND_RECORD),
    ("CS_GET_AGENT_ADDRESS_LIST", n.CS_GET_AGENT_ADDRESS_LIST),
    ("CS_GET_AGENT_CHANGE_INFO", n.CS_GET_AGENT_CHANGE_INFO),
    ("CS_GET_AGENT_INFO", n.CS_GET_AGENT_INFO),
    ("CS_GET_AGENT_LIST", n.CS_GET_AGENT_LIST),
    ("CS_GET_AGENT_STATUS", n.CS_GET_AGENT_STATUS),
    ("CS_GET_CONSENSUS_CONFIG", n.CS_GET_CONSENSUS_CONFIG),
    ("CS_GET_CONTRACT_AGENT_INFO", n.CS_GET_CONTRACT_AGENT_INFO),
    ("CS_GET_CONTRACT_DEPOSIT_INFO", n.CS_GET_CONTRACT_DEPOSIT_INFO),
    ("CS_GET_DEPOSIT_LIST", n.CS_GET_DEPOSIT_LIST),
    ("CS_GET_INFO", n.CS_GET_INFO),
    ("CS_GET_NODE_PACKING_ADDR", n.CS_GET_NODE_PACKING_ADDR),
    ("CS_GET_PACKER_INFO", n.CS_GET_PACKER_INFO),
    ("CS_GET_PUBLISH_LIST", n.CS_GET_PUBLISH_LIST),
    ("CS_GET_ROUND_INFO", n.CS_GET_ROUND_INFO),
    ("CS_GET_ROUND_MEMBER_LIST", n.CS_GET_ROUND_MEMBER_LIST),
    ("CS_GET_SEED_NODE_INFO", n.CS_GET_SEED_NODE_INFO),
    ("CS_GET_WHOLEINFO", n.CS_GET_WHOLEINFO),
    ("CS_MULTI_DEPOSIT", n.CS_MULTI_DEPOSIT),
    ("CS_MULTI_WITHDRAW", n.CS_MULTI_WITHDRAW),
    ("CS_RANDOM_RAW_SEEDS_COUNT", n.CS_RANDOM_RAW_SEEDS_COUNT),
    ("CS_RANDOM_RAW_SEEDS_HEIGHT", n.CS_RANDOM_RAW_SEEDS_HEIGHT),
    ("CS_RANDOM_SEED_COUNT", n.CS_RANDOM_SEED_COUNT),
    ("CS_RANDOM_SEED_HEIGHT", n.CS_RANDOM_SEED_HEIGHT),
    ("CS_RECEIVE_HEADERLIST", n.CS_RECEIVE_HEADERLIST),
    ("CS_RUN_CHAIN", n.CS_RUN_CHAIN),
    ("CS_RUN_MAINCHAIN", n.CS_RUN_MAINCHAIN),
    ("CS_STOP_AGENT", n.CS_STOP_AGENT),
    ("CS_STOPAGENT", n.CS_STOPAGENT),
    ("CS_STOP_CHAIN", n.CS_STOP_CHAIN),
    ("CS_STOPCHAIN", n.CS_STOPCHAIN),
    ("CS_STOP_CONTRACT_AGENT", n.CS_STOP_CONTRACT_AGENT),
    ("CS_STOP_MULTI_AGENT", n.CS_STOP_MULTI_AGENT),
    ("CS_TRIGGER_COINBASE_CONTRACT", n.CS_TRIGGER_COINBASE_CONTRACT),
    ("CS_UPDATE_AGENT_CONSENSUS_STATUS", n.CS_UPDATE_AGENT_CONSENSUS_STATUS),
    ("CS_UPDATE_AGENT_STATUS", n.CS_UPDATE_AGENT_STATUS),
    ("CS_VALIDBLOCK", n.CS_VALIDBLOCK),
    ("CS_WITHDRAW", n.CS_WITHDRAW),
    ("DEPOSIT_VALID", n.DEPOSIT_VALID),
    ("FORWARD_MESSAGE", n.FORWARD_MESSAGE),
    ("GET_BALANCE", n.GET_BALANCE),
    ("GET_BALANCE_NONCE", n.GET_BALANCE_NONCE),
    ("GET_BLOCK_BY_HASH", n.GET_BLOCK_BY_HASH),
    ("GET_BLOCK_BY_HEIGHT", n.GET_BLOCK_BY_HEIGHT),
    ("GET_BLOCKHEADER_BY_HASH", n.GET_BLOCKHEADER_BY_HASH),
    ("GET_BLOCKHEADER_BY_HEIGHT", n.GET_BLOCKHEADER_BY_HEIGHT),
    ("GET_BLOCKHEADER_PO_BY_HASH", n.GET_BLOCKHEADER_PO_BY_HASH),
    ("GET_BLOCKHEADER_POBY_HEIGHT", n.GET_BLOCKHEADER_POBY_HEIGHT),
    ("GET_BLOCKHEADERS_BY_HEIGHT_RANGE", n.GET_BLOCKHEADERS_BY_HEIGHT_RANGE),
    ("GET_BLOCKHEADERS_FOR_PROTOCOL", n.GET_BLOCKHEADERS_FOR_PROTOCOL),
    ("GET_BYZANTINE_COUNT", n.GET_BYZANTINE_COUNT),
    ("GET_CIRCULAT", n.GET_CIRCULAT),
    ("GET_CONSOLIDATEDAPI", n.GET_CONSOLIDATEDAPI),
    ("GET_CROSSCHAIN_INFOS", n.GET_CROSSCHAIN_INFOS),
    ("GET_CROSSTX_STATE", n.GET_CROSSTX_STATE),
    ("GET_CTX", n.GET_CTX),
    ("GET_CTX_STATE", n.GET_CTX_STATE),
    ("GET_FREEZEGET_FREEZELIST_LIST", n.GET_FREEZEGET_FREEZELIST_LIST),
    ("GET_FRIEND_CHAIN_CIRCULATE", n.GET_FRIEND_CHAIN_CIRCULATE),
    ("GET_LATEST_BLOCKHEADERS", n.GET_LATEST_BLOCKHEADERS),
    ("GET_LATEST_ROUND_BLOCKHEADERS", n.GET_LATEST_ROUND_BLOCKHEADERS),
    ("GET_NETWORK_GROUP", n.GET_NETWORK_GROUP),
    ("GET_NONCE", n.GET_NONCE),
    ("GET_OTHERCTX", n.GET_OTHERCTX),
    ("GET_REGISTERED_CHAIN_INFO_LIST", n.GET_REGISTERED_CHAIN_INFO_LIST),
    ("GET_REGISTERED_CHAIN_MESSAGE", n.GET_REGISTERED_CHAIN_MESSAGE),
    ("GET_ROUND_BLOCKHEADERS", n.GET_ROUND_BLOCKHEADERS),
    ("GET_STATUS", n.GET_STATUS),
    ("GET_VERSION", n.GET_VERSION),
    ("INFO", n.INFO),
    ("LATEST_BLOCKHEADER", n.LATEST_BLOCKHEADER),
    ("LATEST_BLOCKHEADER_PO", n.LATEST_BLOCKHEADER_PO),
    ("LATEST_BLOCK", n.LATEST_BLOCK),
    ("LATEST_HEIGHT", n.LATEST_HEIGHT),
    ("GET_ASSETS_BY_ID", n.GET_ASSETS_BY_ID),
    ("LISTENER_DEPENDENCIES_READY", n.LISTENER_DEPENDENCIES_READY),
    ("MSG_PROCESS", n.MSG_PROCESS),
    ("NEW_API_MOD_CROSS_TX", n.NEW_API_MOD_CROSS_TX),
    ("NEW_BLOCK_HEIGHT", n.NEW_BLOCK_HEIGHT),
    ("NW_ACTIVE_CROSS", n.NW_ACTIVE_CROSS),
    ("NW_ADD_NODES", n.NW_ADD_NODES),
    ("NW_BROADCAST", n.NW_BROADCAST),
    ("NW_CREATE_NODEGROUP", n.NW_CREATE_NODEGROUP),
    ("NW_CROSS_RANDOM_BROADCAST", n.NW_CROSS_RANDOM_BROADCAST),
    ("NW_CUR_TIME_MILLIS", n.NW_CUR_TIME_MILLIS),
    ("NW_DELETE_NODEGROUP", n.NW_DELETE_NODEGROUP),
    ("NW_DEL_NODES", n.NW_DEL_NODES),
    ("NW_GET_CHAIN_CONNECT_AMOUNT", n.NW_GET_CHAIN_CONNECT_AMOUNT),
    ("NW_GET_GROUP_BY_CHAINID", n.NW_GET_GROUP_BY_CHAINID),
    ("NW_GET_GROUPS", n.NW_GET_GROUPS),
    ("NW_GET_MAIN_NET_MAGIC_NUMBER", n.NW_GET_MAIN_NET_MAGIC_NUMBER),
    ("NW_GET_NODES", n.NW_GET_NODES),
    ("NW_GET_SEEDS", n.NW_GET_SEEDS),
    ("NW_INFO", n.NW_INFO),
    ("NW_NODES", n.NW_NODES),
    ("NW_PROTOCOL_REGISTER", n.NW_PROTOCOL_REGISTER),
    ("NW_RECONNECT", n.NW_RECONNECT),
    ("NW_SEND_PEERS_MSG", n.NW_SEND_PEERS_MSG),
    ("NW_UPDATE_NODE_INFO", n.NW_UPDATE_NODE_INFO),
    ("PARAM_TEST_CMD", n.PARAM_TEST_CMD),
    ("PROTOCOL_PRIORITY_REGISTER", n.PROTOCOL_PRIORITY_REGISTER),
    ("PROTOCOL_VERSION_CHANGE", n.PROTOCOL_VERSION_CHANGE),
    ("RECEIVE_PACKING_BLOCK", n.RECEIVE_PACKING_BLOCK),
    ("RECV_CIRCULAT", n.RECV_CIRCULAT),
    ("RECV_CTX_HASH", n.RECV_CTX_HASH),
    ("RECV_CTX", n.RECV_CTX),
    ("RECV_CTX_SIGN", n.RECV_CTX_SIGN),
    ("RECV_CTX_STATE", n.RECV_CTX_STATE),
    ("RECV_OTHER_CTX", n.RECV_OTHER_CTX),
    ("RECV_REGCHAIN", n.RECV_REGCHAIN),
    ("REG_CROSS_ASSET", n.REG_CROSS_ASSET),
    ("REG_CROSSCHAIN", n.REG_CROSSCHAIN),
    ("REGISTER_API", n.REGISTER_API),
    ("REGISTER_MODULE_DEPENDENCIES", n.REGISTER_MODULE_DEPENDENCIES),
    ("REGISTER_PROTOCOL", n.REGISTER_PROTOCOL),
    ("ROLLBACK_BLOCK", n.ROLLBACK_BLOCK),
    ("ROLLBACK_BLOCK_TXS", n.ROLLBACK_BLOCK_TXS),
    ("ROLLBACK_TX_VALIDATE_STATUS", n.ROLLBACK_TX_VALIDATE_STATUS),
    ("ROLLBACK_UNCONFIRM_TX", n.ROLLBACK_UNCONFIRM_TX),
    ("SAVE_BLOCK", n.SAVE_BLOCK),
    ("SCAN_MANAGED_MODULES", n.SCAN_MANAGED_MODULES),
    ("SC_BATCH_BEFORE_END", n.SC_BATCH_BEFORE_END),
    ("SC_BATCH_BEGIN", n.SC_BATCH_BEGIN),
    ("SC_BATCH_END", n.SC_BATCH_END),
    ("SC_CALL", n.SC_CALL),
    ("SC_CALL_VALIDATOR", n.SC_CALL_VALIDATOR),
    ("SC_CONSTRUCTOR", n.SC_CONSTRUCTOR),
    ("SC_CONTRACT_INFO", n.SC_CONTRACT_INFO),
    ("SC_CONTRACT_OFFLINE_TX_HASH_LIST", n.SC_CONTRACT_OFFLINE_TX_HASH_LIST),
    ("SC_CONTRACT_RESULT_LIST", n.SC_CONTRACT_RESULT_LIST),
    ("SC_CONTRACT_RESULT", n.SC_CONTRACT_RESULT),
    ("SC_CONTRACT_TX", n.SC_CONTRACT_TX),
    ("SC_CREATE", n.SC_CREATE),
    ("SC_CREATE_VALIDATOR", n.SC_CREATE_VALIDATOR),
    ("SC_DELETE", n.SC_DELETE),
    ("SC_DELETE_VALIDATOR", n.SC_DELETE_VALIDATOR),
    ("SC_IMPUTED_CALL_GAS", n.SC_IMPUTED_CALL_GAS),
    ("SC_IMPUTED_CREATE_GAS", n.SC_IMPUTED_CREATE_GAS),
    ("SC_INITIAL_ACCOUNT_TOKEN", n.SC_INITIAL_ACCOUNT_TOKEN),
    ("SC_INVOKE_CONTRACT", n.SC_INVOKE_CONTRACT),
    ("SC_INVOKE_VIEW", n.SC_INVOKE_VIEW),
    ("SC_PACKAGE_BATCH_END", n.SC_PACKAGE_BATCH_END),
    ("SC_REGISTER_CM_FOR_CONTRACT", n.SC_REGISTER_CM_FOR_CONTRACT),
    ("SC_TOKEN_ASSETS_LIST", n.SC_TOKEN_ASSETS_LIST),
    ("SC_TOKEN_BALANCE", n.SC_TOKEN_BALANCE),
    ("SC_TOKEN_TRANSFER_LIST", n.SC_TOKEN_TRANSFER_LIST),
    ("SC_TOKEN_TRANSFER", n.SC_TOKEN_TRANSFER),
    ("SC_TRANSFER_FEE", n.SC_TRANSFER_FEE),
    ("SC_TRANSFER", n.SC_TRANSFER),
    ("SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT", n.SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT),
    ("SC_UPLOAD", n.SC_UPLOAD),
    ("SC_VALIDATE_CALL", n.SC_VALIDATE_CALL),
    ("SC_VALIDATE_CREATE", n.SC_VALIDATE_CREATE),
    ("SC_VALIDATE_DELETE", n.SC_VALIDATE_DELETE),
    ("SHUTDOWN_SYSTEM", n.SHUTDOWN_SYSTEM),
    ("STOP_AGENTVALID", n.STOP_AGENTVALID),
    ("STOP_ALL_MODULES", n.STOP_ALL_MODULES),
    ("TX_BACK_PACKABLE_TXS", n.TX_BACK_PACKABLE_TXS),
    ("TX_BASE_VALIDATE", n.TX_BASE_VALIDATE),
    ("TX_BATCH_VERIFY", n.TX_BATCH_VERIFY),
    ("TX_BLOCK_HEIGHT", n.TX_BLOCK_HEIGHT),
    ("TX_BL_STATE", n.TX_BL_STATE),
    ("TX_CLEAN_THREAD", n.TX_CLEAN_THREAD),
    ("TX_COMMIT", n.TX_COMMIT),
    ("TX_COUNT", n.TX_COUNT),
    ("TX_CS_STATE", n.TX_CS_STATE),
    ("TX_GENESIS_SAVE", n.TX_GENESIS_SAVE),
    ("TX_GET_BLOCKTXS_EXTEND", n.TX_GET_BLOCKTXS_EXTEND),
    ("TX_GET_BLOCKTXS", n.TX_GET_BLOCKTXS),
    ("TX_GET_CONFIRMED_TX_CLIENT", n.TX_GET_CONFIRMED_TX_CLIENT),
    ("TX_GET_CONFIRMED_TX", n.TX_GET_CONFIRMED_TX),
    ("TX_GET_NONEXISTENT_UNCONFIRMED_HASHS", n.TX_GET_NONEXISTENT_UNCONFIRMED_HASHS),
    ("TX_GET_SYSTEMTYPES", n.TX_GET_SYSTEMTYPES),
    ("TX_GET_TX_CLIENT", n.TX_GET_TX_CLIENT),
    ("TX_GET_TX", n.TX_GET_TX),
    ("TX_HASH_LIST", n.TX_HASH_LIST),
    ("TX_HASH", n.TX_HASH),
    ("TX_LIST", n.TX_LIST),
    ("TX_NEWTX", n.TX_NEWTX),
    ("TX_PACKABLE_TXS", n.TX_PACKABLE_TXS),
    ("TX_REGISTER", n.TX_REGISTER),
    ("TX_ROLLBACK", n.TX_ROLLBACK),
    ("TX_SAVE", n.TX_SAVE),
    ("NEW_NET_TX_THREAD", n.NEW_NET_TX_THREAD),
    ("TX_VALIDATOR", n.TX_VALIDATOR),
    ("TX_VERIFY_TX", n.TX_VERIFY_TX),
    ("UPDATE_CHAIN_ASSET", n.UPDATE_CHAIN_ASSET),
    ("VERIFY_COINDATA_BATCH_PACKAGED", n.VERIFY_COINDATA_BATCH_PACKAGED),
    ("VERIFY_COINDATA", n.VERIFY_COINDATA),
    ("WITHDRAW_VALID", n.WITHDRAW_VALID)
]
