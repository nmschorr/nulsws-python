#!/usr/bin/python3.7
"""
by Nancy Schorr for Nuls, None),
(December, None),
(2019

"""

from UserSettings.nulsws_SET import *

# change settings to suit
# for use in api calls
# fill in your default params here

my_minsigns, my_inputs, my_outputs, my_remark, my_signaddress = [1, 1, 1, 1, 1]

_1_AC_CREATE_ACCOUNT_chainId = my_chainid
_1_AC_CREATE_ACCOUNT_count = my_chainid
_1_AC_CREATE_ACCOUNT_password = my_password
_2_AC_CREATE_CONTRACT_ACCOUNT_chainId = my_chainid
_3_AC_CREATE_MULTI_SIGN_ACCOUNT_chainId = my_chainid
_3_AC_CREATE_MULTI_SIGN_ACCOUNT_pubKeys = my_pubkeys
_3_AC_CREATE_MULTI_SIGN_ACCOUNT_minSigns = my_minsigns
_4_AC_CREATE_MULTI_SIGN_TRANSFER_chainId = my_chainid
_4_AC_CREATE_MULTI_SIGN_TRANSFER_inputs = my_inputs
_4_AC_CREATE_MULTI_SIGN_TRANSFER_outputs = my_outputs
_4_AC_CREATE_MULTI_SIGN_TRANSFER_remark = my_remark
_4_AC_CREATE_MULTI_SIGN_TRANSFER_signAddress = my_address
_4_AC_CREATE_MULTI_SIGN_TRANSFER_signPassword = my_password
_5_AC_CREATE_OFFLINE_ACCOUNT_chainId = my_chainid
_5_AC_CREATE_OFFLINE_ACCOUNT_count = my_chainid
_5_AC_CREATE_OFFLINE_ACCOUNT_password = my_chainid
_6_AC_EXPORT_ACCOUNT_KEYSTORE_chainId = my_chainid
_6_AC_EXPORT_ACCOUNT_KEYSTORE_address = my_address
_6_AC_EXPORT_ACCOUNT_KEYSTORE_password = my_chainid
_6_AC_EXPORT_ACCOUNT_KEYSTORE_filePath = my_chainid
_7_AC_EXPORT_KEYSTORE_JSON_chainId = my_chainid
_7_AC_EXPORT_KEYSTORE_JSON_address = my_address
_7_AC_EXPORT_KEYSTORE_JSON_password = my_password
_8_AC_GET_ACCOUNT_BYADDRESS_chainId = my_chainid
_8_AC_GET_ACCOUNT_BYADDRESS_address = my_address
_9_AC_GET_ACCOUNT_LIST_chainId = my_chainid
_10_AC_GET_ADDRESS_LIST_chainId = my_chainid
_10_AC_GET_ADDRESS_LIST_pageNumber = my_chainid
_10_AC_GET_ADDRESS_LIST_pageSize = my_chainid
_11_AC_GET_ADDRESS_PREFIX_BY_CHAINID_chainId = my_chainid
_12_AC_GET_ALIASBY_ADDRESS_chainId = my_chainid
_12_AC_GET_ALIASBY_ADDRESS_address = my_address
_14_AC_GET_ALL_PRIKEY_chainId = my_chainid
_14_AC_GET_ALL_PRIKEY_password = my_password
_15_AC_GET_ENCRYPTED_ADDRESS_LIST_chainId = my_chainid
_16_AC_GET_MULTI_SIGN_ACCOUNT_chainId = my_chainid
_16_AC_GET_MULTI_SIGN_ACCOUNT_address = my_address
_17_AC_GET_PUBKEY_chainId = my_chainid
_17_AC_GET_PUBKEY_address = my_address
_17_AC_GET_PUBKEY_password = my_chainid
_18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_chainId = my_chainid
_18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_password = my_chainid
_18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_keyStore = my_chainid
_18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_overwrite = my_chainid
_19_AC_IMPORT_ACCOUNT_BY_PRIKEY_chainId = my_chainid
_19_AC_IMPORT_ACCOUNT_BY_PRIKEY_password = my_password
_19_AC_IMPORT_ACCOUNT_BY_PRIKEY_priKey = my_chainid
_19_AC_IMPORT_ACCOUNT_BY_PRIKEY_overwrite = my_chainid
_20_AC_IS_ALIAS_USABLE_chainId = my_chainid
_20_AC_IS_ALIAS_USABLE_alias = my_chainid
_21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_chainId = my_chainid
_21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_address = my_address
_21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_pubKey = my_chainid
_22_AC_REMOVE_ACCOUNT_chainId = my_chainid
_22_AC_REMOVE_ACCOUNT_address = my_address
_22_AC_REMOVE_ACCOUNT_password = my_chainid
_23_AC_REMOVE_MULTISIGN_ACCOUNT_chainId = my_chainid
_23_AC_REMOVE_MULTISIGN_ACCOUNT_address = my_address
_24_AC_SET_ALIAS_chainId = my_chainid
_24_AC_SET_ALIAS_address = my_address
_24_AC_SET_ALIAS_password = my_chainid
_24_AC_SET_ALIAS_alias = my_chainid
_25_AC_SET_MULTISIGN_ALIAS_chainId = my_chainid
_25_AC_SET_MULTISIGN_ALIAS_address = my_address
_25_AC_SET_MULTISIGN_ALIAS_alias = my_chainid
_25_AC_SET_MULTISIGN_ALIAS_signAddress = my_address
_25_AC_SET_MULTISIGN_ALIAS_signPassword = my_password
_26_AC_SET_REMARK_chainId = my_chainid
_26_AC_SET_REMARK_address = my_address
_26_AC_SET_REMARK_remark = my_chainid
_27_AC_SIGN_BLOCKDIGEST_chainId = my_chainid
_27_AC_SIGN_BLOCKDIGEST_address = my_address
_27_AC_SIGN_BLOCKDIGEST_password = my_chainid
_27_AC_SIGN_BLOCKDIGEST_data = my_chainid
_28_AC_SIGN_DIGEST_chainId = my_chainid
_28_AC_SIGN_DIGEST_address = my_address
_28_AC_SIGN_DIGEST_password = my_chainid
_28_AC_SIGN_DIGEST_data = my_chainid
_29_AC_SIGN_MULTISIGN_TRANSACTION_chainId = my_chainid
_29_AC_SIGN_MULTISIGN_TRANSACTION_tx = my_chainid
_29_AC_SIGN_MULTISIGN_TRANSACTION_signAddress = my_address
_29_AC_SIGN_MULTISIGN_TRANSACTION_signPassword = my_password
_30_AC_TRANSFER_chainId = my_chainid
_30_AC_TRANSFER_inputs = my_chainid
_30_AC_TRANSFER_outputs = my_chainid
_30_AC_TRANSFER_remark = my_chainid
_31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_chainId = my_chainid
_31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_address = my_address
_31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_password = my_chainid
_31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_newPassword = my_chainid
_31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_priKey = my_chainid
_32_AC_UPDATE_PASSWORD_chainId = my_chainid
_32_AC_UPDATE_PASSWORD_address = my_address
_32_AC_UPDATE_PASSWORD_password = my_chainid
_32_AC_UPDATE_PASSWORD_newPassword = my_chainid
_33_AC_VALIDATION_PASSWORD_chainId = my_chainid
_33_AC_VALIDATION_PASSWORD_address = my_address
_33_AC_VALIDATION_PASSWORD_password = my_chainid
_34_AC_VERIFY_SIGN_DATA_pubKey = my_chainid
_34_AC_VERIFY_SIGN_DATA_sig = my_chainid
_34_AC_VERIFY_SIGN_DATA_data = my_chainid
_35_BATCH_VALIDATE_BEGIN_chainId = my_chainid
_36_BLOCK_VALIDATE_chainId = my_chainid
_36_BLOCK_VALIDATE_txList = my_chainid
_38_CANCEL_CROSSCHAIN_chainId = my_chainid
_38_CANCEL_CROSSCHAIN_assetId = my_chainid
_39_CHECK_BLOCK_VERSION_chainId = my_chainid
_39_CHECK_BLOCK_VERSION_extendsData = my_chainid
_40_CM_ASSET_chainId = my_chainid
_40_CM_ASSET_assetId = my_chainid
_41_CM_ASSET_CIRCULATE_COMMIT_chainId = my_chainid
_41_CM_ASSET_CIRCULATE_COMMIT_txList = my_chainid
_41_CM_ASSET_CIRCULATE_COMMIT_blockHeader = my_chainid
_42_CM_ASSET_CIRCULATE_ROLLBACK_chainId = my_chainid
_42_CM_ASSET_CIRCULATE_ROLLBACK_txList = my_chainid
_42_CM_ASSET_CIRCULATE_ROLLBACK_blockHeader = my_chainid
_43_CM_ASSET_CIRCULATE_VALIDATOR_chainId = my_chainid
_43_CM_ASSET_CIRCULATE_VALIDATOR_tx = my_chainid
_44_CM_ASSET_DISABLE_chainId = my_chainid
_44_CM_ASSET_DISABLE_assetId = my_chainid
_44_CM_ASSET_DISABLE_address = my_address
_44_CM_ASSET_DISABLE_password = my_password
_45_CM_ASSET_REG_chainId = my_chainid
_45_CM_ASSET_REG_assetId = my_chainid
_45_CM_ASSET_REG_symbol = my_chainid
_45_CM_ASSET_REG_assetName = my_chainid
_45_CM_ASSET_REG_initNumber = my_chainid
_45_CM_ASSET_REG_decimalPlaces = my_chainid
_45_CM_ASSET_REG_address = my_address
_45_CM_ASSET_REG_password = my_chainid
_46_CM_CHAIN_chainId = my_chainid
_47_CM_CHAIN_ACTIVE_chainId = my_chainid
_47_CM_CHAIN_ACTIVE_chainName = my_chainid
_47_CM_CHAIN_ACTIVE_addressType = my_address
_47_CM_CHAIN_ACTIVE_addressPrefix = my_address
_47_CM_CHAIN_ACTIVE_magicNumber = my_chainid
_47_CM_CHAIN_ACTIVE_minAvailableNodeNum = my_chainid
_47_CM_CHAIN_ACTIVE_assetId = my_chainid
_47_CM_CHAIN_ACTIVE_symbol = my_chainid
_47_CM_CHAIN_ACTIVE_assetName = my_chainid
_47_CM_CHAIN_ACTIVE_initNumber = my_chainid
_47_CM_CHAIN_ACTIVE_decimalPlaces = my_chainid
_47_CM_CHAIN_ACTIVE_address = my_address
_47_CM_CHAIN_ACTIVE_password = my_chainid
_47_CM_CHAIN_ACTIVE_verifierList = my_chainid
_47_CM_CHAIN_ACTIVE_signatureBFTRatio = my_chainid
_47_CM_CHAIN_ACTIVE_maxSignatureCount = my_chainid
_48_CM_CHAIN_REG_chainId = my_chainid
_48_CM_CHAIN_REG_chainName = my_chainid
_48_CM_CHAIN_REG_addressType = my_address
_48_CM_CHAIN_REG_addressPrefix = my_address
_48_CM_CHAIN_REG_magicNumber = my_chainid
_48_CM_CHAIN_REG_minAvailableNodeNum = my_chainid
_48_CM_CHAIN_REG_assetId = my_chainid
_48_CM_CHAIN_REG_symbol = my_chainid
_48_CM_CHAIN_REG_assetName = my_chainid
_48_CM_CHAIN_REG_initNumber = my_chainid
_48_CM_CHAIN_REG_decimalPlaces = my_chainid
_48_CM_CHAIN_REG_address = my_address
_48_CM_CHAIN_REG_password = my_chainid
_48_CM_CHAIN_REG_verifierList = my_chainid
_48_CM_CHAIN_REG_signatureBFTRatio = my_chainid
_48_CM_CHAIN_REG_maxSignatureCount = my_chainid
_49_CM_GET_CHAIN_ASSET_chainId = my_chainid
_49_CM_GET_CHAIN_ASSET_assetChainId = my_chainid
_49_CM_GET_CHAIN_ASSET_assetId = my_chainid
_50_CM_GET_CIRCULATE_CHAIN_ASSET_circulateChainId = my_chainid
_50_CM_GET_CIRCULATE_CHAIN_ASSET_assetChainId = my_chainid
_50_CM_GET_CIRCULATE_CHAIN_ASSET_assetId = my_chainid
_51_COMMIT_BATCH_UNCONFIRMED_TXS_chainId = my_chainid
_51_COMMIT_BATCH_UNCONFIRMED_TXS_txList = my_chainid
_52_COMMIT_BLOCKTXS_chainId = my_chainid
_52_COMMIT_BLOCKTXS_txList = my_chainid
_52_COMMIT_BLOCKTXS_blockHeight = my_chainid
_53_COMMIT_UNCONFIRMEDTX_chainId = my_chainid
_53_COMMIT_UNCONFIRMEDTX_tx = my_chainid
_55_CREATE_AGENT_VALID_chainId = my_chainid
_55_CREATE_AGENT_VALID_tx = my_chainid
_56_CREATE_CROSSTX_chainId = my_chainid
_56_CREATE_CROSSTX_listFrom = my_chainid
_56_CREATE_CROSSTX_listTo = my_chainid
_56_CREATE_CROSSTX_remark = my_chainid
_57_CROSSCHAIN_REGISTER_CHANGE_chainId = my_chainid
_58_CS_ADD_BLOCK_chainId = my_chainid
_58_CS_ADD_BLOCK_blockHeader = my_chainid
_59_CS_ADD_EVIDENCE_RECORD_chainId = my_chainid
_59_CS_ADD_EVIDENCE_RECORD_blockHeader = my_chainid
_59_CS_ADD_EVIDENCE_RECORD_evidenceHeader = my_chainid
_60_CS_CHAIN_ROLLBACK_chainId = my_chainid
_60_CS_CHAIN_ROLLBACK_height = my_chainid
_61_CS_CONTRACT_DEPOSIT_chainId = my_chainid
_61_CS_CONTRACT_DEPOSIT_agentHash = my_chainid
_61_CS_CONTRACT_DEPOSIT_deposit = my_chainid
_61_CS_CONTRACT_DEPOSIT_contractAddress = my_address
_61_CS_CONTRACT_DEPOSIT_contractSender = my_chainid
_61_CS_CONTRACT_DEPOSIT_contractBalance = my_chainid
_61_CS_CONTRACT_DEPOSIT_contractNonce = my_chainid
_61_CS_CONTRACT_DEPOSIT_blockTime = my_chainid
_62_CS_CONTRACT_WITHDRAW_chainId = my_chainid
_62_CS_CONTRACT_WITHDRAW_joinAgentHash = my_chainid
_62_CS_CONTRACT_WITHDRAW_contractAddress = my_address
_62_CS_CONTRACT_WITHDRAW_contractSender = my_chainid
_62_CS_CONTRACT_WITHDRAW_contractBalance = my_chainid
_62_CS_CONTRACT_WITHDRAW_contractNonce = my_chainid
_62_CS_CONTRACT_WITHDRAW_blockTime = my_chainid
_63_CS_CREATE_AGENT_chainId = my_chainid
_63_CS_CREATE_AGENT_agentAddress = my_address
_63_CS_CREATE_AGENT_packingAddress = my_address
_63_CS_CREATE_AGENT_rewardAddress = my_address
_63_CS_CREATE_AGENT_commissionRate = my_chainid
_63_CS_CREATE_AGENT_deposit = my_chainid
_63_CS_CREATE_AGENT_password = my_chainid
_64_CS_CREATE_CONTRACT_AGENT_chainId = my_chainid
_64_CS_CREATE_CONTRACT_AGENT_packingAddress = my_address
_64_CS_CREATE_CONTRACT_AGENT_deposit = my_chainid
_64_CS_CREATE_CONTRACT_AGENT_commissionRate = my_chainid
_64_CS_CREATE_CONTRACT_AGENT_contractAddress = my_address
_64_CS_CREATE_CONTRACT_AGENT_contractSender = my_chainid
_64_CS_CREATE_CONTRACT_AGENT_contractBalance = my_chainid
_64_CS_CREATE_CONTRACT_AGENT_contractNonce = my_chainid
_64_CS_CREATE_CONTRACT_AGENT_blockTime = my_chainid
_65_CS_CREATE_MULTI_AGENT_chainId = my_chainid
_65_CS_CREATE_MULTI_AGENT_agentAddress = my_address
_65_CS_CREATE_MULTI_AGENT_packingAddress = my_address
_65_CS_CREATE_MULTI_AGENT_rewardAddress = my_address
_65_CS_CREATE_MULTI_AGENT_commissionRate = my_chainid
_65_CS_CREATE_MULTI_AGENT_deposit = my_chainid
_65_CS_CREATE_MULTI_AGENT_password = my_chainid
_65_CS_CREATE_MULTI_AGENT_signAddress = my_address
_66_CS_DEPOSIT_TOAGENT_chainId = my_chainid
_66_CS_DEPOSIT_TOAGENT_address = my_address
_66_CS_DEPOSIT_TOAGENT_agentHash = my_chainid
_66_CS_DEPOSIT_TOAGENT_deposit = my_chainid
_66_CS_DEPOSIT_TOAGENT_password = my_chainid
_67_CS_DOUBLE_SPEND_RECORD_chainId = my_chainid
_67_CS_DOUBLE_SPEND_RECORD_block = my_chainid
_67_CS_DOUBLE_SPEND_RECORD_tx = my_chainid
_68_CS_GET_AGENT_ADDRESS_LIST_chainId = my_chainid
_69_CS_GET_AGENT_CHANGE_INFO_chainId = my_chainid
_70_CS_GET_AGENT_INFO_chainId = my_chainid
_70_CS_GET_AGENT_INFO_agentHash = my_chainid
_71_CS_GET_AGENT_LIST_chainId = my_chainid
_71_CS_GET_AGENT_LIST_pageNumber = my_chainid
_71_CS_GET_AGENT_LIST_pageSize = my_chainid
_71_CS_GET_AGENT_LIST_keyWord = my_chainid
_72_CS_GET_AGENT_STATUS_chainId = my_chainid
_72_CS_GET_AGENT_STATUS_agentHash = my_chainid
_73_CS_GET_CONSENSUS_CONFIG_chainId = my_chainid
_74_CS_GET_CONTRACT_AGENT_INFO_chainId = my_chainid
_74_CS_GET_CONTRACT_AGENT_INFO_agentHash = my_chainid
_74_CS_GET_CONTRACT_AGENT_INFO_contractAddress = my_address
_74_CS_GET_CONTRACT_AGENT_INFO_contractSender = my_chainid
_75_CS_GET_CONTRACT_DEPOSIT_INFO_chainId = my_chainid
_75_CS_GET_CONTRACT_DEPOSIT_INFO_joinAgentHash = my_chainid
_75_CS_GET_CONTRACT_DEPOSIT_INFO_contractAddress = my_address
_75_CS_GET_CONTRACT_DEPOSIT_INFO_contractSender = my_chainid
_76_CS_GET_DEPOSIT_LIST_chainId = my_chainid
_76_CS_GET_DEPOSIT_LIST_pageNumber = my_chainid
_76_CS_GET_DEPOSIT_LIST_pageSize = my_chainid
_76_CS_GET_DEPOSIT_LIST_address = my_address
_76_CS_GET_DEPOSIT_LIST_agentHash = my_chainid
_77_CS_GET_INFO_chainId = my_chainid
_77_CS_GET_INFO_address = my_address
_78_CS_GET_PACKER_INFO_chainId = my_chainid
_79_CS_GET_PUBLISH_LIST_chainId = my_chainid
_79_CS_GET_PUBLISH_LIST_address = my_address
_79_CS_GET_PUBLISH_LIST_type = my_chainid
_80_CS_GET_ROUND_INFO_chainId = my_chainid
_81_CS_GET_ROUND_MEMBER_LIST_chainId = my_chainid
_81_CS_GET_ROUND_MEMBER_LIST_extend = my_chainid
_82_CS_GET_SEED_NODE_INFO_chainId = my_chainid
_83_CS_GET_WHOLEINFO_chainId = my_chainid
_84_CS_MULTI_DEPOSIT_chainId = my_chainid
_84_CS_MULTI_DEPOSIT_address = my_address
_84_CS_MULTI_DEPOSIT_agentHash = my_chainid
_84_CS_MULTI_DEPOSIT_deposit = my_chainid
_84_CS_MULTI_DEPOSIT_password = my_chainid
_84_CS_MULTI_DEPOSIT_signAddress = my_address
_85_CS_MULTI_WITHDRAW_chainId = my_chainid
_85_CS_MULTI_WITHDRAW_address = my_address
_85_CS_MULTI_WITHDRAW_txHash = my_chainid
_85_CS_MULTI_WITHDRAW_password = my_chainid
_85_CS_MULTI_WITHDRAW_signAddress = my_address
_86_CS_RANDOM_RAW_SEEDS_COUNT_chainId = my_chainid
_86_CS_RANDOM_RAW_SEEDS_COUNT_height = my_chainid
_86_CS_RANDOM_RAW_SEEDS_COUNT_count = my_chainid
_87_CS_RANDOM_RAW_SEEDS_HEIGHT_chainId = my_chainid
_87_CS_RANDOM_RAW_SEEDS_HEIGHT_startHeight = my_chainid
_87_CS_RANDOM_RAW_SEEDS_HEIGHT_endHeight = my_chainid
_88_CS_RANDOM_SEED_COUNT_chainId = my_chainid
_88_CS_RANDOM_SEED_COUNT_height = my_chainid
_88_CS_RANDOM_SEED_COUNT_count = my_chainid
_88_CS_RANDOM_SEED_COUNT_algorithm = my_chainid
_89_CS_RANDOM_SEED_HEIGHT_chainId = my_chainid
_89_CS_RANDOM_SEED_HEIGHT_startHeight = my_chainid
_89_CS_RANDOM_SEED_HEIGHT_endHeight = my_chainid
_89_CS_RANDOM_SEED_HEIGHT_algorithm = my_chainid
_90_CS_RECEIVE_HEADERLIST_chainId = my_chainid
_90_CS_RECEIVE_HEADERLIST_headerList = my_chainid
_91_CS_RUN_CHAIN_chainId = my_chainid
_92_CS_RUN_MAINCHAIN_chainId = my_chainid
_93_CS_STOPAGENT_chainId = my_chainid
_93_CS_STOPAGENT_address = my_address
_93_CS_STOPAGENT_password = my_chainid
_94_CS_STOP_AGENT_chainId = my_chainid
_94_CS_STOP_AGENT_address = my_address
_94_CS_STOP_AGENT_password = my_chainid
_95_CS_STOPCHAIN_chainId = my_chainid
_96_CS_STOP_CHAIN_chainId = my_chainid
_97_CS_STOP_CONTRACT_AGENT_chainId = my_chainid
_97_CS_STOP_CONTRACT_AGENT_contractAddress = my_address
_97_CS_STOP_CONTRACT_AGENT_contractSender = my_chainid
_97_CS_STOP_CONTRACT_AGENT_contractBalance = my_chainid
_97_CS_STOP_CONTRACT_AGENT_contractNonce = my_chainid
_97_CS_STOP_CONTRACT_AGENT_blockTime = my_chainid
_98_CS_STOP_MULTI_AGENT_chainId = my_chainid
_98_CS_STOP_MULTI_AGENT_address = my_address
_98_CS_STOP_MULTI_AGENT_password = my_chainid
_98_CS_STOP_MULTI_AGENT_signAddress = my_address
_99_CS_TRIGGER_COINBASE_CONTRACT_chainId = my_chainid
_99_CS_TRIGGER_COINBASE_CONTRACT_tx = my_chainid
_99_CS_TRIGGER_COINBASE_CONTRACT_blockHeader = my_chainid
_99_CS_TRIGGER_COINBASE_CONTRACT_stateRoot = my_chainid
_100_CS_UPDATE_AGENT_CONSENSUS_STATUS_chainId = my_chainid
_101_CS_UPDATE_AGENT_STATUS_chainId = my_chainid
_101_CS_UPDATE_AGENT_STATUS_status = my_chainid
_102_CS_VALIDBLOCK_chainId = my_chainid
_102_CS_VALIDBLOCK_download = my_chainid
_102_CS_VALIDBLOCK_block = my_chainid
_103_CS_WITHDRAW_chainId = my_chainid
_103_CS_WITHDRAW_address = my_address
_103_CS_WITHDRAW_txHash = my_chainid
_103_CS_WITHDRAW_password = my_chainid
_104_DEPOSIT_VALID_chainId = my_chainid
_104_DEPOSIT_VALID_tx = my_chainid
_105_GET_ASSETS_BY_ID_chainId = my_chainid
_105_GET_ASSETS_BY_ID_assetIds = my_chainid
_106_GET_BALANCE_chainId = my_chainid
_106_GET_BALANCE_assetChainId = my_chainid
_106_GET_BALANCE_assetId = my_chainid
_106_GET_BALANCE_address = my_address
_107_GET_BALANCE_NONCE_chainId = my_chainid
_107_GET_BALANCE_NONCE_assetChainId = my_chainid
_107_GET_BALANCE_NONCE_assetId = my_chainid
_107_GET_BALANCE_NONCE_address = my_address
_107_GET_BALANCE_NONCE_isConfirmed = my_chainid
_108_GET_BLOCK_BY_HASH_chainId = my_chainid
_108_GET_BLOCK_BY_HASH_hash = my_chainid
_109_GET_BLOCK_BY_HEIGHT_chainId = my_chainid
_109_GET_BLOCK_BY_HEIGHT_height = my_chainid
_110_GET_BLOCKHEADER_BY_HASH_chainId = my_chainid
_110_GET_BLOCKHEADER_BY_HASH_hash = my_chainid
_111_GET_BLOCKHEADER_BY_HEIGHT_chainId = my_chainid
_111_GET_BLOCKHEADER_BY_HEIGHT_height = my_chainid
_112_GET_BLOCKHEADER_PO_BY_HASH_chainId = my_chainid
_112_GET_BLOCKHEADER_PO_BY_HASH_hash = my_chainid
_113_GET_BLOCKHEADER_POBY_HEIGHT_chainId = my_chainid
_113_GET_BLOCKHEADER_POBY_HEIGHT_height = my_chainid
_114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_chainId = my_chainid
_114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_begin = my_chainid
_114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_end = my_chainid
_115_GET_BLOCKHEADERS_FOR_PROTOCOL_chainId = my_chainid
_115_GET_BLOCKHEADERS_FOR_PROTOCOL_interval = my_chainid
_116_GET_BYZANTINE_COUNT_chainId = my_chainid
_117_GET_CIRCULAT_chainId = my_chainid
_117_GET_CIRCULAT_nodeId = my_chainid
_117_GET_CIRCULAT_messageBody = my_chainid
_119_GET_CROSSTX_STATE_chainId = my_chainid
_119_GET_CROSSTX_STATE_txHash = my_chainid
_120_GET_CTX_chainId = my_chainid
_120_GET_CTX_nodeId = my_chainid
_120_GET_CTX_messageBody = my_chainid
_121_GET_CTX_STATE_chainId = my_chainid
_121_GET_CTX_STATE_nodeId = my_chainid
_121_GET_CTX_STATE_messageBody = my_chainid
_122_GET_FRIEND_CHAIN_CIRCULATE_chainId = my_chainid
_122_GET_FRIEND_CHAIN_CIRCULATE_assetIds = my_chainid
_123_GET_LATEST_BLOCKHEADERS_chainId = my_chainid
_123_GET_LATEST_BLOCKHEADERS_size = my_chainid
_124_GET_LATEST_ROUND_BLOCKHEADERS_chainId = my_chainid
_124_GET_LATEST_ROUND_BLOCKHEADERS_round = my_chainid
_125_GET_NONCE_chainId = my_chainid
_125_GET_NONCE_assetChainId = my_chainid
_125_GET_NONCE_assetId = my_chainid
_125_GET_NONCE_address = my_address
_125_GET_NONCE_isConfirmed = my_chainid
_126_GET_OTHERCTX_chainId = my_chainid
_126_GET_OTHERCTX_nodeId = my_chainid
_126_GET_OTHERCTX_messageBody = my_chainid
_128_GET_ROUND_BLOCKHEADERS_chainId = my_chainid
_128_GET_ROUND_BLOCKHEADERS_height = my_chainid
_128_GET_ROUND_BLOCKHEADERS_round = my_chainid
_129_GET_STATUS_chainId = my_chainid
_130_GET_VERSION_chainId = my_chainid
_131_INFO_chainId = my_chainid
_132_LATEST_BLOCK_chainId = my_chainid
_133_LATEST_BLOCKHEADER_chainId = my_chainid
_134_LATEST_BLOCKHEADER_PO_chainId = my_chainid
_135_LATEST_HEIGHT_chainId = my_chainid
_137_MSG_PROCESS_chainId = my_chainid
_137_MSG_PROCESS_nodeId = my_chainid
_137_MSG_PROCESS_cmd = my_chainid
_137_MSG_PROCESS_messageBody = my_chainid
_138_NEW_BLOCK_HEIGHT_chainId = my_chainid
_138_NEW_BLOCK_HEIGHT_height = my_chainid
_139_NW_ACTIVE_CROSS_chainId = my_chainid
_139_NW_ACTIVE_CROSS_maxOut = my_chainid
_139_NW_ACTIVE_CROSS_maxIn = my_chainid
_139_NW_ACTIVE_CROSS_seedIps = my_chainid
_140_NW_ADD_NODES_chainId = my_chainid
_140_NW_ADD_NODES_isCross = my_chainid
_140_NW_ADD_NODES_nodes = my_chainid
_141_NW_BROADCAST_chainId = my_chainid
_141_NW_BROADCAST_excludeNodes = my_chainid
_141_NW_BROADCAST_messageBody = my_chainid
_141_NW_BROADCAST_command = my_chainid
_141_NW_BROADCAST_isCross = my_chainid
_141_NW_BROADCAST_percent = my_chainid
_142_NW_CREATE_NODEGROUP_chainId = my_chainid
_142_NW_CREATE_NODEGROUP_magicNumber = my_chainid
_142_NW_CREATE_NODEGROUP_maxOut = my_chainid
_142_NW_CREATE_NODEGROUP_maxIn = my_chainid
_142_NW_CREATE_NODEGROUP_minAvailableCount = my_chainid
_142_NW_CREATE_NODEGROUP_isCrossGroup = my_chainid
_143_NW_DEL_NODES_chainId = my_chainid
_143_NW_DEL_NODES_nodes = my_chainid
_144_NW_GET_CHAIN_CONNECT_AMOUNT_chainId = my_chainid
_144_NW_GET_CHAIN_CONNECT_AMOUNT_isCross = my_chainid
_145_NW_GET_GROUP_BY_CHAINID_chainId = my_chainid
_146_NW_GET_GROUPS_startPage = my_chainid
_146_NW_GET_GROUPS_pageSize = my_chainid
_147_NW_GET_NODES_chainId = my_chainid
_147_NW_GET_NODES_state = my_chainid
_147_NW_GET_NODES_isCross = my_chainid
_147_NW_GET_NODES_startPage = my_chainid
_147_NW_GET_NODES_pageSize = my_chainid
_149_NW_INFO_chainId = my_chainid
_150_NW_NODES_chainId = my_chainid
_151_NW_PROTOCOL_REGISTER_role = my_chainid
_151_NW_PROTOCOL_REGISTER_protocolCmds = my_chainid
_152_NW_RECONNECT_chainId = my_chainid
_153_NW_SEND_PEERS_MSG_chainId = my_chainid
_153_NW_SEND_PEERS_MSG_nodes = my_chainid
_153_NW_SEND_PEERS_MSG_messageBody = my_chainid
_153_NW_SEND_PEERS_MSG_command = my_chainid
_154_NW_UPDATE_NODE_INFO_chainId = my_chainid
_154_NW_UPDATE_NODE_INFO_nodeId = my_chainid
_154_NW_UPDATE_NODE_INFO_blockHeight = my_chainid
_154_NW_UPDATE_NODE_INFO_blockHash = my_chainid
_155_PARAM_TEST_CMD_intCount = my_chainid
_155_PARAM_TEST_CMD_byteCount = my_chainid
_155_PARAM_TEST_CMD_shortCount = my_chainid
_155_PARAM_TEST_CMD_longCount = my_chainid
_156_PROTOCOL_VERSION_CHANGE_chainId = my_chainid
_156_PROTOCOL_VERSION_CHANGE_protocolVersion = my_chainid
_157_RECEIVE_PACKING_BLOCK_chainId = my_chainid
_157_RECEIVE_PACKING_BLOCK_block = my_chainid
_158_RECV_CIRCULAT_chainId = my_chainid
_158_RECV_CIRCULAT_nodeId = my_chainid
_158_RECV_CIRCULAT_messageBody = my_chainid
_159_RECV_CTX_chainId = my_chainid
_159_RECV_CTX_nodeId = my_chainid
_159_RECV_CTX_messageBody = my_chainid
_160_RECV_CTX_HASH_chainId = my_chainid
_160_RECV_CTX_HASH_nodeId = my_chainid
_160_RECV_CTX_HASH_messageBody = my_chainid
_161_RECV_CTX_SIGN_chainId = my_chainid
_161_RECV_CTX_SIGN_nodeId = my_chainid
_161_RECV_CTX_SIGN_messageBody = my_chainid
_162_RECV_CTX_STATE_chainId = my_chainid
_162_RECV_CTX_STATE_nodeId = my_chainid
_162_RECV_CTX_STATE_messageBody = my_chainid
_163_RECV_OTHER_CTX_chainId = my_chainid
_163_RECV_OTHER_CTX_nodeId = my_chainid
_163_RECV_OTHER_CTX_messageBody = my_chainid
_164_RECV_REGCHAIN_chainId = my_chainid
_164_RECV_REGCHAIN_nodeId = my_chainid
_164_RECV_REGCHAIN_messageBody = my_chainid
_166_REGISTER_PROTOCOL_chainId = my_chainid
_166_REGISTER_PROTOCOL_moduleCode = my_chainid
_166_REGISTER_PROTOCOL_list = my_chainid
_167_ROLLBACK_BLOCK_TXS_chainId = my_chainid
_167_ROLLBACK_BLOCK_TXS_txList = my_chainid
_167_ROLLBACK_BLOCK_TXS_blockHeight = my_chainid
_168_ROLLBACK_UNCONFIRM_TX_chainId = my_chainid
_168_ROLLBACK_UNCONFIRM_TX_tx = my_chainid
_169_ROLLBACK_BLOCK_chainId = my_chainid
_169_ROLLBACK_BLOCK_blockHeader = my_chainid
_170_ROLLBACK_TX_VALIDATE_STATUS_chainId = my_chainid
_170_ROLLBACK_TX_VALIDATE_STATUS_tx = my_chainid
_171_SAVE_BLOCK_chainId = my_chainid
_171_SAVE_BLOCK_blockHeader = my_chainid
_172_SC_BATCH_BEFORE_END_chainId = my_chainid
_172_SC_BATCH_BEFORE_END_blockType = my_chainid
_172_SC_BATCH_BEFORE_END_blockHeight = my_chainid
_173_SC_BATCH_BEGIN_chainId = my_chainid
_173_SC_BATCH_BEGIN_blockType = my_chainid
_173_SC_BATCH_BEGIN_blockHeight = my_chainid
_173_SC_BATCH_BEGIN_blockTime = my_chainid
_173_SC_BATCH_BEGIN_packingAddress = my_address
_173_SC_BATCH_BEGIN_preStateRoot = my_chainid
_174_SC_BATCH_END_chainId = my_chainid
_174_SC_BATCH_END_blockHeight = my_chainid
_175_SC_CALL_chainId = my_chainid
_175_SC_CALL_sender = my_chainid
_175_SC_CALL_password = my_chainid
_175_SC_CALL_value = my_chainid
_175_SC_CALL_gasLimit = my_chainid
_175_SC_CALL_price = my_chainid
_175_SC_CALL_contractAddress = my_address
_175_SC_CALL_methodName = my_chainid
_175_SC_CALL_methodDesc = my_chainid
_175_SC_CALL_args = my_chainid
_175_SC_CALL_remark = my_chainid
_176_SC_CALL_VALIDATOR_chainId = my_chainid
_176_SC_CALL_VALIDATOR_tx = my_chainid
_177_SC_CONSTRUCTOR_chainId = my_chainid
_177_SC_CONSTRUCTOR_contractCode = my_chainid
_178_SC_CONTRACT_INFO_chainId = my_chainid
_178_SC_CONTRACT_INFO_contractAddress = my_address
_179_SC_CONTRACT_OFFLINE_TX_HASH_LIST_chainId = my_chainid
_179_SC_CONTRACT_OFFLINE_TX_HASH_LIST_blockHash = my_chainid
_180_SC_CONTRACT_RESULT_chainId = my_chainid
_180_SC_CONTRACT_RESULT_hash = my_chainid
_181_SC_CONTRACT_RESULT_LIST_chainId = my_chainid
_181_SC_CONTRACT_RESULT_LIST_hashList = my_chainid
_182_SC_CONTRACT_TX_chainId = my_chainid
_182_SC_CONTRACT_TX_hash = my_chainid
_183_SC_CREATE_chainId = my_chainid
_183_SC_CREATE_sender = my_chainid
_183_SC_CREATE_password = my_chainid
_183_SC_CREATE_alias = my_chainid
_183_SC_CREATE_gasLimit = my_chainid
_183_SC_CREATE_price = my_chainid
_183_SC_CREATE_contractCode = my_chainid
_183_SC_CREATE_args = my_chainid
_183_SC_CREATE_remark = my_chainid
_184_SC_CREATE_VALIDATOR_chainId = my_chainid
_184_SC_CREATE_VALIDATOR_tx = my_chainid
_185_SC_DELETE_chainId = my_chainid
_185_SC_DELETE_sender = my_chainid
_185_SC_DELETE_password = my_chainid
_185_SC_DELETE_contractAddress = my_address
_185_SC_DELETE_remark = my_chainid
_186_SC_DELETE_VALIDATOR_chainId = my_chainid
_186_SC_DELETE_VALIDATOR_tx = my_chainid
_187_SC_IMPUTED_CALL_GAS_chainId = my_chainid
_187_SC_IMPUTED_CALL_GAS_sender = my_chainid
_187_SC_IMPUTED_CALL_GAS_value = my_chainid
_187_SC_IMPUTED_CALL_GAS_contractAddress = my_address
_187_SC_IMPUTED_CALL_GAS_methodName = my_chainid
_187_SC_IMPUTED_CALL_GAS_methodDesc = my_chainid
_187_SC_IMPUTED_CALL_GAS_args = my_chainid
_188_SC_IMPUTED_CREATE_GAS_chainId = my_chainid
_188_SC_IMPUTED_CREATE_GAS_sender = my_chainid
_188_SC_IMPUTED_CREATE_GAS_contractCode = my_chainid
_188_SC_IMPUTED_CREATE_GAS_args = my_chainid
_189_SC_INITIAL_ACCOUNT_TOKEN_chainId = my_chainid
_189_SC_INITIAL_ACCOUNT_TOKEN_address = my_address
_190_SC_INVOKE_CONTRACT_chainId = my_chainid
_190_SC_INVOKE_CONTRACT_blockType = my_chainid
_190_SC_INVOKE_CONTRACT_tx = my_chainid
_191_SC_INVOKE_VIEW_chainId = my_chainid
_191_SC_INVOKE_VIEW_contractAddress = my_address
_191_SC_INVOKE_VIEW_methodName = my_chainid
_191_SC_INVOKE_VIEW_methodDesc = my_chainid
_191_SC_INVOKE_VIEW_args = my_chainid
_192_SC_PACKAGE_BATCH_END_chainId = my_chainid
_192_SC_PACKAGE_BATCH_END_blockHeight = my_chainid
_193_SC_TOKEN_ASSETS_LIST_chainId = my_chainid
_193_SC_TOKEN_ASSETS_LIST_address = my_address
_193_SC_TOKEN_ASSETS_LIST_pageNumber = my_chainid
_193_SC_TOKEN_ASSETS_LIST_pageSize = my_chainid
_194_SC_TOKEN_BALANCE_chainId = my_chainid
_194_SC_TOKEN_BALANCE_contractAddress = my_address
_194_SC_TOKEN_BALANCE_address = my_address
_195_SC_TOKEN_TRANSFER_chainId = my_chainid
_195_SC_TOKEN_TRANSFER_address = my_address
_195_SC_TOKEN_TRANSFER_toAddress = my_address
_195_SC_TOKEN_TRANSFER_contractAddress = my_address
_195_SC_TOKEN_TRANSFER_password = my_chainid
_195_SC_TOKEN_TRANSFER_amount = my_chainid
_195_SC_TOKEN_TRANSFER_remark = my_chainid
_196_SC_TOKEN_TRANSFER_LIST_chainId = my_chainid
_196_SC_TOKEN_TRANSFER_LIST_address = my_address
_196_SC_TOKEN_TRANSFER_LIST_pageNumber = my_chainid
_196_SC_TOKEN_TRANSFER_LIST_pageSize = my_chainid
_197_SC_TRANSFER_chainId = my_chainid
_197_SC_TRANSFER_address = my_address
_197_SC_TRANSFER_toAddress = my_address
_197_SC_TRANSFER_password = my_chainid
_197_SC_TRANSFER_amount = my_chainid
_197_SC_TRANSFER_remark = my_chainid
_198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_chainId = my_chainid
_198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_stateRoot = my_chainid
_198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_blockHeight = my_chainid
_198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_contractAddress = my_address
_198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_tx = my_chainid
_199_SC_UPLOAD_chainId = my_chainid
_199_SC_UPLOAD_jarFileData = my_chainid
_200_SC_VALIDATE_CALL_chainId = my_chainid
_200_SC_VALIDATE_CALL_sender = my_chainid
_200_SC_VALIDATE_CALL_value = my_chainid
_200_SC_VALIDATE_CALL_gasLimit = my_chainid
_200_SC_VALIDATE_CALL_price = my_chainid
_200_SC_VALIDATE_CALL_contractAddress = my_address
_200_SC_VALIDATE_CALL_methodName = my_chainid
_200_SC_VALIDATE_CALL_methodDesc = my_chainid
_200_SC_VALIDATE_CALL_args = my_chainid
_201_SC_VALIDATE_CREATE_chainId = my_chainid
_201_SC_VALIDATE_CREATE_sender = my_chainid
_201_SC_VALIDATE_CREATE_gasLimit = my_chainid
_201_SC_VALIDATE_CREATE_price = my_chainid
_201_SC_VALIDATE_CREATE_contractCode = my_chainid
_201_SC_VALIDATE_CREATE_args = my_chainid
_202_SC_VALIDATE_DELETE_chainId = my_chainid
_202_SC_VALIDATE_DELETE_contractAddress = my_address
_203_STOP_AGENTVALID_chainId = my_chainid
_203_STOP_AGENTVALID_tx = my_chainid
_204_TX_COMMIT_chainId = my_chainid
_204_TX_COMMIT_txList = my_chainid
_204_TX_COMMIT_blockHeader = my_chainid
_205_TX_VALIDATOR_chainId = my_chainid
_205_TX_VALIDATOR_txList = my_chainid
_205_TX_VALIDATOR_blockHeader = my_chainid
_206_TX_BACK_PACKABLE_TXS_chainId = my_chainid
_206_TX_BACK_PACKABLE_TXS_txList = my_chainid
_207_TX_BATCH_VERIFY_chainId = my_chainid
_207_TX_BATCH_VERIFY_txList = my_chainid
_207_TX_BATCH_VERIFY_blockHeader = my_chainid
_207_TX_BATCH_VERIFY_preStateRoot = my_chainid
_208_TX_BL_STATE_chainId = my_chainid
_208_TX_BL_STATE_status = my_chainid
_209_TX_BLOCK_HEIGHT_chainId = my_chainid
_209_TX_BLOCK_HEIGHT_height = my_chainid
_210_TX_CS_STATE_chainId = my_chainid
_210_TX_CS_STATE_packaging = my_chainid
_211_TX_GET_BLOCKTXS_chainId = my_chainid
_211_TX_GET_BLOCKTXS_txHashList = my_chainid
_212_TX_GET_BLOCKTXS_EXTEND_chainId = my_chainid
_212_TX_GET_BLOCKTXS_EXTEND_txHashList = my_chainid
_212_TX_GET_BLOCKTXS_EXTEND_allHits = my_chainid
_213_TX_GET_CONFIRMED_TX_chainId = my_chainid
_213_TX_GET_CONFIRMED_TX_txHash = my_chainid
_214_TX_GET_CONFIRMED_TX_CLIENT_chainId = my_chainid
_214_TX_GET_CONFIRMED_TX_CLIENT_txHash = my_chainid
_215_TX_GET_NONEXISTENT_UNCONFIRMED_HASHS_chainId = my_chainid
_215_TX_GET_NONEXISTENT_UNCONFIRMED_HASHS_txHashList = my_chainid
_216_TX_GET_SYSTEMTYPES_chainId = my_chainid
_217_TX_GET_TX_chainId = my_chainid
_217_TX_GET_TX_txHash = my_chainid
_218_TX_GET_TX_CLIENT_chainId = my_chainid
_218_TX_GET_TX_CLIENT_txHash = my_chainid
_219_TX_NEWTX_chainId = my_chainid
_219_TX_NEWTX_tx = my_chainid
_220_TX_PACKABLE_TXS_chainId = my_chainid
_220_TX_PACKABLE_TXS_endTimestamp = my_chainid
_220_TX_PACKABLE_TXS_maxTxDataSize = my_chainid
_220_TX_PACKABLE_TXS_blockTime = my_chainid
_220_TX_PACKABLE_TXS_packingAddress = my_address
_220_TX_PACKABLE_TXS_preStateRoot = my_chainid
_221_TX_REGISTER_chainId = my_chainid
_221_TX_REGISTER_moduleCode = my_chainid
_221_TX_REGISTER_list = my_chainid
_221_TX_REGISTER_delList = my_chainid
_222_TX_ROLLBACK_chainId = my_chainid
_222_TX_ROLLBACK_txHashList = my_chainid
_222_TX_ROLLBACK_blockHeader = my_chainid
_223_TX_SAVE_chainId = my_chainid
_223_TX_SAVE_txList = my_chainid
_223_TX_SAVE_contractList = my_chainid
_223_TX_SAVE_blockHeader = my_chainid
_224_TX_VERIFY_TX_chainId = my_chainid
_224_TX_VERIFY_TX_tx = my_chainid
_225_UPDATE_CHAIN_ASSET_chainId = my_chainid
_225_UPDATE_CHAIN_ASSET_assets = my_chainid
_226_VERIFY_COINDATA_chainId = my_chainid
_226_VERIFY_COINDATA_tx = my_chainid
_227_VERIFY_COINDATA_BATCH_PACKAGED_chainId = my_chainid
_227_VERIFY_COINDATA_BATCH_PACKAGED_txList = my_chainid
_228_WITHDRAW_VALID_chainId = my_chainid
_228_WITHDRAW_VALID_tx = my_chainid

__all__ = ['FALSE', 'MSG_TYPE', 'REMARK', 'RequestType', 'SHORT_MSG', 'TRUE', 'ZERO', 'ZLIB',
           '_100_CS_UPDATE_AGENT_CONSENSUS_STATUS_chainId', '_101_CS_UPDATE_AGENT_STATUS_chainId',
           '_101_CS_UPDATE_AGENT_STATUS_status', '_102_CS_VALIDBLOCK_block', '_102_CS_VALIDBLOCK_chainId',
           '_102_CS_VALIDBLOCK_download', '_103_CS_WITHDRAW_address', '_103_CS_WITHDRAW_chainId',
           '_103_CS_WITHDRAW_password', '_103_CS_WITHDRAW_txHash', '_104_DEPOSIT_VALID_chainId',
           '_104_DEPOSIT_VALID_tx', '_105_GET_ASSETS_BY_ID_assetIds', '_105_GET_ASSETS_BY_ID_chainId',
           '_106_GET_BALANCE_address', '_106_GET_BALANCE_assetChainId', '_106_GET_BALANCE_assetId',
           '_106_GET_BALANCE_chainId', '_107_GET_BALANCE_NONCE_address',
           '_107_GET_BALANCE_NONCE_assetChainId', '_107_GET_BALANCE_NONCE_assetId',
           '_107_GET_BALANCE_NONCE_chainId', '_107_GET_BALANCE_NONCE_isConfirmed',
           '_108_GET_BLOCK_BY_HASH_chainId', '_108_GET_BLOCK_BY_HASH_hash',
           '_109_GET_BLOCK_BY_HEIGHT_chainId', '_109_GET_BLOCK_BY_HEIGHT_height',
           '_10_AC_GET_ADDRESS_LIST_chainId', '_10_AC_GET_ADDRESS_LIST_pageNumber',
           '_10_AC_GET_ADDRESS_LIST_pageSize', '_110_GET_BLOCKHEADER_BY_HASH_chainId',
           '_110_GET_BLOCKHEADER_BY_HASH_hash', '_111_GET_BLOCKHEADER_BY_HEIGHT_chainId',
           '_111_GET_BLOCKHEADER_BY_HEIGHT_height', '_112_GET_BLOCKHEADER_PO_BY_HASH_chainId',
           '_112_GET_BLOCKHEADER_PO_BY_HASH_hash', '_113_GET_BLOCKHEADER_POBY_HEIGHT_chainId',
           '_113_GET_BLOCKHEADER_POBY_HEIGHT_height', '_114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_begin',
           '_114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_chainId', '_114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_end',
           '_115_GET_BLOCKHEADERS_FOR_PROTOCOL_chainId', '_115_GET_BLOCKHEADERS_FOR_PROTOCOL_interval',
           '_116_GET_BYZANTINE_COUNT_chainId', '_117_GET_CIRCULAT_chainId', '_117_GET_CIRCULAT_messageBody',
           '_117_GET_CIRCULAT_nodeId', '_119_GET_CROSSTX_STATE_chainId', '_119_GET_CROSSTX_STATE_txHash',
           '_11_AC_GET_ADDRESS_PREFIX_BY_CHAINID_chainId', '_120_GET_CTX_chainId', '_120_GET_CTX_messageBody',
           '_120_GET_CTX_nodeId', '_121_GET_CTX_STATE_chainId', '_121_GET_CTX_STATE_messageBody',
           '_121_GET_CTX_STATE_nodeId', '_122_GET_FRIEND_CHAIN_CIRCULATE_assetIds',
           '_122_GET_FRIEND_CHAIN_CIRCULATE_chainId', '_123_GET_LATEST_BLOCKHEADERS_chainId',
           '_123_GET_LATEST_BLOCKHEADERS_size', '_124_GET_LATEST_ROUND_BLOCKHEADERS_chainId',
           '_124_GET_LATEST_ROUND_BLOCKHEADERS_round', '_125_GET_NONCE_address',
           '_125_GET_NONCE_assetChainId', '_125_GET_NONCE_assetId', '_125_GET_NONCE_chainId',
           '_125_GET_NONCE_isConfirmed', '_126_GET_OTHERCTX_chainId', '_126_GET_OTHERCTX_messageBody',
           '_126_GET_OTHERCTX_nodeId', '_128_GET_ROUND_BLOCKHEADERS_chainId',
           '_128_GET_ROUND_BLOCKHEADERS_height', '_128_GET_ROUND_BLOCKHEADERS_round',
           '_129_GET_STATUS_chainId', '_12_AC_GET_ALIASBY_ADDRESS_address',
           '_12_AC_GET_ALIASBY_ADDRESS_chainId', '_130_GET_VERSION_chainId', '_131_INFO_chainId',
           '_132_LATEST_BLOCK_chainId', '_133_LATEST_BLOCKHEADER_chainId',
           '_134_LATEST_BLOCKHEADER_PO_chainId', '_135_LATEST_HEIGHT_chainId', '_137_MSG_PROCESS_chainId',
           '_137_MSG_PROCESS_cmd', '_137_MSG_PROCESS_messageBody', '_137_MSG_PROCESS_nodeId',
           '_138_NEW_BLOCK_HEIGHT_chainId', '_138_NEW_BLOCK_HEIGHT_height', '_139_NW_ACTIVE_CROSS_chainId',
           '_139_NW_ACTIVE_CROSS_maxIn', '_139_NW_ACTIVE_CROSS_maxOut', '_139_NW_ACTIVE_CROSS_seedIps',
           '_140_NW_ADD_NODES_chainId', '_140_NW_ADD_NODES_isCross', '_140_NW_ADD_NODES_nodes',
           '_141_NW_BROADCAST_chainId', '_141_NW_BROADCAST_command', '_141_NW_BROADCAST_excludeNodes',
           '_141_NW_BROADCAST_isCross', '_141_NW_BROADCAST_messageBody', '_141_NW_BROADCAST_percent',
           '_142_NW_CREATE_NODEGROUP_chainId', '_142_NW_CREATE_NODEGROUP_isCrossGroup',
           '_142_NW_CREATE_NODEGROUP_magicNumber', '_142_NW_CREATE_NODEGROUP_maxIn',
           '_142_NW_CREATE_NODEGROUP_maxOut', '_142_NW_CREATE_NODEGROUP_minAvailableCount',
           '_143_NW_DEL_NODES_chainId', '_143_NW_DEL_NODES_nodes', '_144_NW_GET_CHAIN_CONNECT_AMOUNT_chainId',
           '_144_NW_GET_CHAIN_CONNECT_AMOUNT_isCross', '_145_NW_GET_GROUP_BY_CHAINID_chainId',
           '_146_NW_GET_GROUPS_pageSize', '_146_NW_GET_GROUPS_startPage', '_147_NW_GET_NODES_chainId',
           '_147_NW_GET_NODES_isCross', '_147_NW_GET_NODES_pageSize', '_147_NW_GET_NODES_startPage',
           '_147_NW_GET_NODES_state', '_149_NW_INFO_chainId', '_14_AC_GET_ALL_PRIKEY_chainId',
           '_14_AC_GET_ALL_PRIKEY_password', '_150_NW_NODES_chainId',
           '_151_NW_PROTOCOL_REGISTER_protocolCmds', '_151_NW_PROTOCOL_REGISTER_role',
           '_152_NW_RECONNECT_chainId', '_153_NW_SEND_PEERS_MSG_chainId', '_153_NW_SEND_PEERS_MSG_command',
           '_153_NW_SEND_PEERS_MSG_messageBody', '_153_NW_SEND_PEERS_MSG_nodes',
           '_154_NW_UPDATE_NODE_INFO_blockHash', '_154_NW_UPDATE_NODE_INFO_blockHeight',
           '_154_NW_UPDATE_NODE_INFO_chainId', '_154_NW_UPDATE_NODE_INFO_nodeId',
           '_155_PARAM_TEST_CMD_byteCount', '_155_PARAM_TEST_CMD_intCount', '_155_PARAM_TEST_CMD_longCount',
           '_155_PARAM_TEST_CMD_shortCount', '_156_PROTOCOL_VERSION_CHANGE_chainId',
           '_156_PROTOCOL_VERSION_CHANGE_protocolVersion', '_157_RECEIVE_PACKING_BLOCK_block',
           '_157_RECEIVE_PACKING_BLOCK_chainId', '_158_RECV_CIRCULAT_chainId',
           '_158_RECV_CIRCULAT_messageBody', '_158_RECV_CIRCULAT_nodeId', '_159_RECV_CTX_chainId',
           '_159_RECV_CTX_messageBody', '_159_RECV_CTX_nodeId', '_15_AC_GET_ENCRYPTED_ADDRESS_LIST_chainId',
           '_160_RECV_CTX_HASH_chainId', '_160_RECV_CTX_HASH_messageBody', '_160_RECV_CTX_HASH_nodeId',
           '_161_RECV_CTX_SIGN_chainId', '_161_RECV_CTX_SIGN_messageBody', '_161_RECV_CTX_SIGN_nodeId',
           '_162_RECV_CTX_STATE_chainId', '_162_RECV_CTX_STATE_messageBody', '_162_RECV_CTX_STATE_nodeId',
           '_163_RECV_OTHER_CTX_chainId', '_163_RECV_OTHER_CTX_messageBody', '_163_RECV_OTHER_CTX_nodeId',
           '_164_RECV_REGCHAIN_chainId', '_164_RECV_REGCHAIN_messageBody', '_164_RECV_REGCHAIN_nodeId',
           '_166_REGISTER_PROTOCOL_chainId', '_166_REGISTER_PROTOCOL_list',
           '_166_REGISTER_PROTOCOL_moduleCode', '_167_ROLLBACK_BLOCK_TXS_blockHeight',
           '_167_ROLLBACK_BLOCK_TXS_chainId', '_167_ROLLBACK_BLOCK_TXS_txList',
           '_168_ROLLBACK_UNCONFIRM_TX_chainId', '_168_ROLLBACK_UNCONFIRM_TX_tx',
           '_169_ROLLBACK_BLOCK_blockHeader', '_169_ROLLBACK_BLOCK_chainId',
           '_16_AC_GET_MULTI_SIGN_ACCOUNT_address', '_16_AC_GET_MULTI_SIGN_ACCOUNT_chainId',
           '_170_ROLLBACK_TX_VALIDATE_STATUS_chainId', '_170_ROLLBACK_TX_VALIDATE_STATUS_tx',
           '_171_SAVE_BLOCK_blockHeader', '_171_SAVE_BLOCK_chainId', '_172_SC_BATCH_BEFORE_END_blockHeight',
           '_172_SC_BATCH_BEFORE_END_blockType', '_172_SC_BATCH_BEFORE_END_chainId',
           '_173_SC_BATCH_BEGIN_blockHeight', '_173_SC_BATCH_BEGIN_blockTime',
           '_173_SC_BATCH_BEGIN_blockType', '_173_SC_BATCH_BEGIN_chainId',
           '_173_SC_BATCH_BEGIN_packingAddress', '_173_SC_BATCH_BEGIN_preStateRoot',
           '_174_SC_BATCH_END_blockHeight', '_174_SC_BATCH_END_chainId', '_175_SC_CALL_args',
           '_175_SC_CALL_chainId', '_175_SC_CALL_contractAddress', '_175_SC_CALL_gasLimit',
           '_175_SC_CALL_methodDesc', '_175_SC_CALL_methodName', '_175_SC_CALL_password',
           '_175_SC_CALL_price', '_175_SC_CALL_remark', '_175_SC_CALL_sender', '_175_SC_CALL_value',
           '_176_SC_CALL_VALIDATOR_chainId', '_176_SC_CALL_VALIDATOR_tx', '_177_SC_CONSTRUCTOR_chainId',
           '_177_SC_CONSTRUCTOR_contractCode', '_178_SC_CONTRACT_INFO_chainId',
           '_178_SC_CONTRACT_INFO_contractAddress', '_179_SC_CONTRACT_OFFLINE_TX_HASH_LIST_blockHash',
           '_179_SC_CONTRACT_OFFLINE_TX_HASH_LIST_chainId', '_17_AC_GET_PUBKEY_address',
           '_17_AC_GET_PUBKEY_chainId', '_17_AC_GET_PUBKEY_password', '_180_SC_CONTRACT_RESULT_chainId',
           '_180_SC_CONTRACT_RESULT_hash', '_181_SC_CONTRACT_RESULT_LIST_chainId',
           '_181_SC_CONTRACT_RESULT_LIST_hashList', '_182_SC_CONTRACT_TX_chainId', '_182_SC_CONTRACT_TX_hash',
           '_183_SC_CREATE_alias', '_183_SC_CREATE_args', '_183_SC_CREATE_chainId',
           '_183_SC_CREATE_contractCode', '_183_SC_CREATE_gasLimit', '_183_SC_CREATE_password',
           '_183_SC_CREATE_price', '_183_SC_CREATE_remark', '_183_SC_CREATE_sender',
           '_184_SC_CREATE_VALIDATOR_chainId', '_184_SC_CREATE_VALIDATOR_tx', '_185_SC_DELETE_chainId',
           '_185_SC_DELETE_contractAddress', '_185_SC_DELETE_password', '_185_SC_DELETE_remark',
           '_185_SC_DELETE_sender', '_186_SC_DELETE_VALIDATOR_chainId', '_186_SC_DELETE_VALIDATOR_tx',
           '_187_SC_IMPUTED_CALL_GAS_args', '_187_SC_IMPUTED_CALL_GAS_chainId',
           '_187_SC_IMPUTED_CALL_GAS_contractAddress', '_187_SC_IMPUTED_CALL_GAS_methodDesc',
           '_187_SC_IMPUTED_CALL_GAS_methodName', '_187_SC_IMPUTED_CALL_GAS_sender',
           '_187_SC_IMPUTED_CALL_GAS_value', '_188_SC_IMPUTED_CREATE_GAS_args',
           '_188_SC_IMPUTED_CREATE_GAS_chainId', '_188_SC_IMPUTED_CREATE_GAS_contractCode',
           '_188_SC_IMPUTED_CREATE_GAS_sender', '_189_SC_INITIAL_ACCOUNT_TOKEN_address',
           '_189_SC_INITIAL_ACCOUNT_TOKEN_chainId', '_18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_chainId',
           '_18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_keyStore', '_18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_overwrite',
           '_18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_password', '_190_SC_INVOKE_CONTRACT_blockType',
           '_190_SC_INVOKE_CONTRACT_chainId', '_190_SC_INVOKE_CONTRACT_tx', '_191_SC_INVOKE_VIEW_args',
           '_191_SC_INVOKE_VIEW_chainId', '_191_SC_INVOKE_VIEW_contractAddress',
           '_191_SC_INVOKE_VIEW_methodDesc', '_191_SC_INVOKE_VIEW_methodName',
           '_192_SC_PACKAGE_BATCH_END_blockHeight', '_192_SC_PACKAGE_BATCH_END_chainId',
           '_193_SC_TOKEN_ASSETS_LIST_address', '_193_SC_TOKEN_ASSETS_LIST_chainId',
           '_193_SC_TOKEN_ASSETS_LIST_pageNumber', '_193_SC_TOKEN_ASSETS_LIST_pageSize',
           '_194_SC_TOKEN_BALANCE_address', '_194_SC_TOKEN_BALANCE_chainId',
           '_194_SC_TOKEN_BALANCE_contractAddress', '_195_SC_TOKEN_TRANSFER_address',
           '_195_SC_TOKEN_TRANSFER_amount', '_195_SC_TOKEN_TRANSFER_chainId',
           '_195_SC_TOKEN_TRANSFER_contractAddress', '_195_SC_TOKEN_TRANSFER_password',
           '_195_SC_TOKEN_TRANSFER_remark', '_195_SC_TOKEN_TRANSFER_toAddress',
           '_196_SC_TOKEN_TRANSFER_LIST_address', '_196_SC_TOKEN_TRANSFER_LIST_chainId',
           '_196_SC_TOKEN_TRANSFER_LIST_pageNumber', '_196_SC_TOKEN_TRANSFER_LIST_pageSize',
           '_197_SC_TRANSFER_address', '_197_SC_TRANSFER_amount', '_197_SC_TRANSFER_chainId',
           '_197_SC_TRANSFER_password', '_197_SC_TRANSFER_remark', '_197_SC_TRANSFER_toAddress',
           '_198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_blockHeight',
           '_198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_chainId',
           '_198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_contractAddress',
           '_198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_stateRoot',
           '_198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_tx', '_199_SC_UPLOAD_chainId',
           '_199_SC_UPLOAD_jarFileData', '_19_AC_IMPORT_ACCOUNT_BY_PRIKEY_chainId',
           '_19_AC_IMPORT_ACCOUNT_BY_PRIKEY_overwrite', '_19_AC_IMPORT_ACCOUNT_BY_PRIKEY_password',
           '_19_AC_IMPORT_ACCOUNT_BY_PRIKEY_priKey', '_1_AC_CREATE_ACCOUNT_chainId',
           '_1_AC_CREATE_ACCOUNT_count', '_1_AC_CREATE_ACCOUNT_password', '_200_SC_VALIDATE_CALL_args',
           '_200_SC_VALIDATE_CALL_chainId', '_200_SC_VALIDATE_CALL_contractAddress',
           '_200_SC_VALIDATE_CALL_gasLimit', '_200_SC_VALIDATE_CALL_methodDesc',
           '_200_SC_VALIDATE_CALL_methodName', '_200_SC_VALIDATE_CALL_price', '_200_SC_VALIDATE_CALL_sender',
           '_200_SC_VALIDATE_CALL_value', '_201_SC_VALIDATE_CREATE_args', '_201_SC_VALIDATE_CREATE_chainId',
           '_201_SC_VALIDATE_CREATE_contractCode', '_201_SC_VALIDATE_CREATE_gasLimit',
           '_201_SC_VALIDATE_CREATE_price', '_201_SC_VALIDATE_CREATE_sender',
           '_202_SC_VALIDATE_DELETE_chainId', '_202_SC_VALIDATE_DELETE_contractAddress',
           '_203_STOP_AGENTVALID_chainId', '_203_STOP_AGENTVALID_tx', '_204_TX_COMMIT_blockHeader',
           '_204_TX_COMMIT_chainId', '_204_TX_COMMIT_txList', '_205_TX_VALIDATOR_blockHeader',
           '_205_TX_VALIDATOR_chainId', '_205_TX_VALIDATOR_txList', '_206_TX_BACK_PACKABLE_TXS_chainId',
           '_206_TX_BACK_PACKABLE_TXS_txList', '_207_TX_BATCH_VERIFY_blockHeader',
           '_207_TX_BATCH_VERIFY_chainId', '_207_TX_BATCH_VERIFY_preStateRoot', '_207_TX_BATCH_VERIFY_txList',
           '_208_TX_BL_STATE_chainId', '_208_TX_BL_STATE_status', '_209_TX_BLOCK_HEIGHT_chainId',
           '_209_TX_BLOCK_HEIGHT_height', '_20_AC_IS_ALIAS_USABLE_alias', '_20_AC_IS_ALIAS_USABLE_chainId',
           '_210_TX_CS_STATE_chainId', '_210_TX_CS_STATE_packaging', '_211_TX_GET_BLOCKTXS_chainId',
           '_211_TX_GET_BLOCKTXS_txHashList', '_212_TX_GET_BLOCKTXS_EXTEND_allHits',
           '_212_TX_GET_BLOCKTXS_EXTEND_chainId', '_212_TX_GET_BLOCKTXS_EXTEND_txHashList',
           '_213_TX_GET_CONFIRMED_TX_chainId', '_213_TX_GET_CONFIRMED_TX_txHash',
           '_214_TX_GET_CONFIRMED_TX_CLIENT_chainId', '_214_TX_GET_CONFIRMED_TX_CLIENT_txHash',
           '_215_TX_GET_NONEXISTENT_UNCONFIRMED_HASHS_chainId',
           '_215_TX_GET_NONEXISTENT_UNCONFIRMED_HASHS_txHashList', '_216_TX_GET_SYSTEMTYPES_chainId',
           '_217_TX_GET_TX_chainId', '_217_TX_GET_TX_txHash', '_218_TX_GET_TX_CLIENT_chainId',
           '_218_TX_GET_TX_CLIENT_txHash', '_219_TX_NEWTX_chainId', '_219_TX_NEWTX_tx',
           '_21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_address', '_21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_chainId',
           '_21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_pubKey', '_220_TX_PACKABLE_TXS_blockTime',
           '_220_TX_PACKABLE_TXS_chainId', '_220_TX_PACKABLE_TXS_endTimestamp',
           '_220_TX_PACKABLE_TXS_maxTxDataSize', '_220_TX_PACKABLE_TXS_packingAddress',
           '_220_TX_PACKABLE_TXS_preStateRoot', '_221_TX_REGISTER_chainId', '_221_TX_REGISTER_delList',
           '_221_TX_REGISTER_list', '_221_TX_REGISTER_moduleCode', '_222_TX_ROLLBACK_blockHeader',
           '_222_TX_ROLLBACK_chainId', '_222_TX_ROLLBACK_txHashList', '_223_TX_SAVE_blockHeader',
           '_223_TX_SAVE_chainId', '_223_TX_SAVE_contractList', '_223_TX_SAVE_txList',
           '_224_TX_VERIFY_TX_chainId', '_224_TX_VERIFY_TX_tx', '_225_UPDATE_CHAIN_ASSET_assets',
           '_225_UPDATE_CHAIN_ASSET_chainId', '_226_VERIFY_COINDATA_chainId', '_226_VERIFY_COINDATA_tx',
           '_227_VERIFY_COINDATA_BATCH_PACKAGED_chainId', '_227_VERIFY_COINDATA_BATCH_PACKAGED_txList',
           '_228_WITHDRAW_VALID_chainId', '_228_WITHDRAW_VALID_tx', '_22_AC_REMOVE_ACCOUNT_address',
           '_22_AC_REMOVE_ACCOUNT_chainId', '_22_AC_REMOVE_ACCOUNT_password',
           '_23_AC_REMOVE_MULTISIGN_ACCOUNT_address', '_23_AC_REMOVE_MULTISIGN_ACCOUNT_chainId',
           '_24_AC_SET_ALIAS_address', '_24_AC_SET_ALIAS_alias', '_24_AC_SET_ALIAS_chainId',
           '_24_AC_SET_ALIAS_password', '_25_AC_SET_MULTISIGN_ALIAS_address',
           '_25_AC_SET_MULTISIGN_ALIAS_alias', '_25_AC_SET_MULTISIGN_ALIAS_chainId',
           '_25_AC_SET_MULTISIGN_ALIAS_signAddress', '_25_AC_SET_MULTISIGN_ALIAS_signPassword',
           '_26_AC_SET_REMARK_address', '_26_AC_SET_REMARK_chainId', '_26_AC_SET_REMARK_remark',
           '_27_AC_SIGN_BLOCKDIGEST_address', '_27_AC_SIGN_BLOCKDIGEST_chainId',
           '_27_AC_SIGN_BLOCKDIGEST_data', '_27_AC_SIGN_BLOCKDIGEST_password', '_28_AC_SIGN_DIGEST_address',
           '_28_AC_SIGN_DIGEST_chainId', '_28_AC_SIGN_DIGEST_data', '_28_AC_SIGN_DIGEST_password',
           '_29_AC_SIGN_MULTISIGN_TRANSACTION_chainId', '_29_AC_SIGN_MULTISIGN_TRANSACTION_signAddress',
           '_29_AC_SIGN_MULTISIGN_TRANSACTION_signPassword', '_29_AC_SIGN_MULTISIGN_TRANSACTION_tx',
           '_2_AC_CREATE_CONTRACT_ACCOUNT_chainId', '_30_AC_TRANSFER_chainId', '_30_AC_TRANSFER_inputs',
           '_30_AC_TRANSFER_outputs', '_30_AC_TRANSFER_remark',
           '_31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_address', '_31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_chainId',
           '_31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_newPassword',
           '_31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_password', '_31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_priKey',
           '_32_AC_UPDATE_PASSWORD_address', '_32_AC_UPDATE_PASSWORD_chainId',
           '_32_AC_UPDATE_PASSWORD_newPassword', '_32_AC_UPDATE_PASSWORD_password',
           '_33_AC_VALIDATION_PASSWORD_address', '_33_AC_VALIDATION_PASSWORD_chainId',
           '_33_AC_VALIDATION_PASSWORD_password', '_34_AC_VERIFY_SIGN_DATA_data',
           '_34_AC_VERIFY_SIGN_DATA_pubKey', '_34_AC_VERIFY_SIGN_DATA_sig',
           '_35_BATCH_VALIDATE_BEGIN_chainId', '_36_BLOCK_VALIDATE_chainId', '_36_BLOCK_VALIDATE_txList',
           '_38_CANCEL_CROSSCHAIN_assetId', '_38_CANCEL_CROSSCHAIN_chainId',
           '_39_CHECK_BLOCK_VERSION_chainId', '_39_CHECK_BLOCK_VERSION_extendsData',
           '_3_AC_CREATE_MULTI_SIGN_ACCOUNT_chainId', '_3_AC_CREATE_MULTI_SIGN_ACCOUNT_minSigns',
           '_3_AC_CREATE_MULTI_SIGN_ACCOUNT_pubKeys', '_40_CM_ASSET_assetId', '_40_CM_ASSET_chainId',
           '_41_CM_ASSET_CIRCULATE_COMMIT_blockHeader', '_41_CM_ASSET_CIRCULATE_COMMIT_chainId',
           '_41_CM_ASSET_CIRCULATE_COMMIT_txList', '_42_CM_ASSET_CIRCULATE_ROLLBACK_blockHeader',
           '_42_CM_ASSET_CIRCULATE_ROLLBACK_chainId', '_42_CM_ASSET_CIRCULATE_ROLLBACK_txList',
           '_43_CM_ASSET_CIRCULATE_VALIDATOR_chainId', '_43_CM_ASSET_CIRCULATE_VALIDATOR_tx',
           '_44_CM_ASSET_DISABLE_address', '_44_CM_ASSET_DISABLE_assetId', '_44_CM_ASSET_DISABLE_chainId',
           '_44_CM_ASSET_DISABLE_password', '_45_CM_ASSET_REG_address', '_45_CM_ASSET_REG_assetId',
           '_45_CM_ASSET_REG_assetName', '_45_CM_ASSET_REG_chainId', '_45_CM_ASSET_REG_decimalPlaces',
           '_45_CM_ASSET_REG_initNumber', '_45_CM_ASSET_REG_password', '_45_CM_ASSET_REG_symbol',
           '_46_CM_CHAIN_chainId', '_47_CM_CHAIN_ACTIVE_address', '_47_CM_CHAIN_ACTIVE_addressPrefix',
           '_47_CM_CHAIN_ACTIVE_addressType', '_47_CM_CHAIN_ACTIVE_assetId', '_47_CM_CHAIN_ACTIVE_assetName',
           '_47_CM_CHAIN_ACTIVE_chainId', '_47_CM_CHAIN_ACTIVE_chainName',
           '_47_CM_CHAIN_ACTIVE_decimalPlaces', '_47_CM_CHAIN_ACTIVE_initNumber',
           '_47_CM_CHAIN_ACTIVE_magicNumber', '_47_CM_CHAIN_ACTIVE_maxSignatureCount',
           '_47_CM_CHAIN_ACTIVE_minAvailableNodeNum', '_47_CM_CHAIN_ACTIVE_password',
           '_47_CM_CHAIN_ACTIVE_signatureBFTRatio', '_47_CM_CHAIN_ACTIVE_symbol',
           '_47_CM_CHAIN_ACTIVE_verifierList', '_48_CM_CHAIN_REG_address', '_48_CM_CHAIN_REG_addressPrefix',
           '_48_CM_CHAIN_REG_addressType', '_48_CM_CHAIN_REG_assetId', '_48_CM_CHAIN_REG_assetName',
           '_48_CM_CHAIN_REG_chainId', '_48_CM_CHAIN_REG_chainName', '_48_CM_CHAIN_REG_decimalPlaces',
           '_48_CM_CHAIN_REG_initNumber', '_48_CM_CHAIN_REG_magicNumber',
           '_48_CM_CHAIN_REG_maxSignatureCount', '_48_CM_CHAIN_REG_minAvailableNodeNum',
           '_48_CM_CHAIN_REG_password', '_48_CM_CHAIN_REG_signatureBFTRatio', '_48_CM_CHAIN_REG_symbol',
           '_48_CM_CHAIN_REG_verifierList', '_49_CM_GET_CHAIN_ASSET_assetChainId',
           '_49_CM_GET_CHAIN_ASSET_assetId', '_49_CM_GET_CHAIN_ASSET_chainId',
           '_4_AC_CREATE_MULTI_SIGN_TRANSFER_chainId', '_4_AC_CREATE_MULTI_SIGN_TRANSFER_inputs',
           '_4_AC_CREATE_MULTI_SIGN_TRANSFER_outputs', '_4_AC_CREATE_MULTI_SIGN_TRANSFER_remark',
           '_4_AC_CREATE_MULTI_SIGN_TRANSFER_signAddress', '_4_AC_CREATE_MULTI_SIGN_TRANSFER_signPassword',
           '_50_CM_GET_CIRCULATE_CHAIN_ASSET_assetChainId', '_50_CM_GET_CIRCULATE_CHAIN_ASSET_assetId',
           '_50_CM_GET_CIRCULATE_CHAIN_ASSET_circulateChainId', '_51_COMMIT_BATCH_UNCONFIRMED_TXS_chainId',
           '_51_COMMIT_BATCH_UNCONFIRMED_TXS_txList', '_52_COMMIT_BLOCKTXS_blockHeight',
           '_52_COMMIT_BLOCKTXS_chainId', '_52_COMMIT_BLOCKTXS_txList', '_53_COMMIT_UNCONFIRMEDTX_chainId',
           '_53_COMMIT_UNCONFIRMEDTX_tx', '_55_CREATE_AGENT_VALID_chainId', '_55_CREATE_AGENT_VALID_tx',
           '_56_CREATE_CROSSTX_chainId', '_56_CREATE_CROSSTX_listFrom', '_56_CREATE_CROSSTX_listTo',
           '_56_CREATE_CROSSTX_remark', '_57_CROSSCHAIN_REGISTER_CHANGE_chainId',
           '_58_CS_ADD_BLOCK_blockHeader', '_58_CS_ADD_BLOCK_chainId',
           '_59_CS_ADD_EVIDENCE_RECORD_blockHeader', '_59_CS_ADD_EVIDENCE_RECORD_chainId',
           '_59_CS_ADD_EVIDENCE_RECORD_evidenceHeader', '_5_AC_CREATE_OFFLINE_ACCOUNT_chainId',
           '_5_AC_CREATE_OFFLINE_ACCOUNT_count', '_5_AC_CREATE_OFFLINE_ACCOUNT_password',
           '_60_CS_CHAIN_ROLLBACK_chainId', '_60_CS_CHAIN_ROLLBACK_height',
           '_61_CS_CONTRACT_DEPOSIT_agentHash', '_61_CS_CONTRACT_DEPOSIT_blockTime',
           '_61_CS_CONTRACT_DEPOSIT_chainId', '_61_CS_CONTRACT_DEPOSIT_contractAddress',
           '_61_CS_CONTRACT_DEPOSIT_contractBalance', '_61_CS_CONTRACT_DEPOSIT_contractNonce',
           '_61_CS_CONTRACT_DEPOSIT_contractSender', '_61_CS_CONTRACT_DEPOSIT_deposit',
           '_62_CS_CONTRACT_WITHDRAW_blockTime', '_62_CS_CONTRACT_WITHDRAW_chainId',
           '_62_CS_CONTRACT_WITHDRAW_contractAddress', '_62_CS_CONTRACT_WITHDRAW_contractBalance',
           '_62_CS_CONTRACT_WITHDRAW_contractNonce', '_62_CS_CONTRACT_WITHDRAW_contractSender',
           '_62_CS_CONTRACT_WITHDRAW_joinAgentHash', '_63_CS_CREATE_AGENT_agentAddress',
           '_63_CS_CREATE_AGENT_chainId', '_63_CS_CREATE_AGENT_commissionRate', '_63_CS_CREATE_AGENT_deposit',
           '_63_CS_CREATE_AGENT_packingAddress', '_63_CS_CREATE_AGENT_password',
           '_63_CS_CREATE_AGENT_rewardAddress', '_64_CS_CREATE_CONTRACT_AGENT_blockTime',
           '_64_CS_CREATE_CONTRACT_AGENT_chainId', '_64_CS_CREATE_CONTRACT_AGENT_commissionRate',
           '_64_CS_CREATE_CONTRACT_AGENT_contractAddress', '_64_CS_CREATE_CONTRACT_AGENT_contractBalance',
           '_64_CS_CREATE_CONTRACT_AGENT_contractNonce', '_64_CS_CREATE_CONTRACT_AGENT_contractSender',
           '_64_CS_CREATE_CONTRACT_AGENT_deposit', '_64_CS_CREATE_CONTRACT_AGENT_packingAddress',
           '_65_CS_CREATE_MULTI_AGENT_agentAddress', '_65_CS_CREATE_MULTI_AGENT_chainId',
           '_65_CS_CREATE_MULTI_AGENT_commissionRate', '_65_CS_CREATE_MULTI_AGENT_deposit',
           '_65_CS_CREATE_MULTI_AGENT_packingAddress', '_65_CS_CREATE_MULTI_AGENT_password',
           '_65_CS_CREATE_MULTI_AGENT_rewardAddress', '_65_CS_CREATE_MULTI_AGENT_signAddress',
           '_66_CS_DEPOSIT_TOAGENT_address', '_66_CS_DEPOSIT_TOAGENT_agentHash',
           '_66_CS_DEPOSIT_TOAGENT_chainId', '_66_CS_DEPOSIT_TOAGENT_deposit',
           '_66_CS_DEPOSIT_TOAGENT_password', '_67_CS_DOUBLE_SPEND_RECORD_block',
           '_67_CS_DOUBLE_SPEND_RECORD_chainId', '_67_CS_DOUBLE_SPEND_RECORD_tx',
           '_68_CS_GET_AGENT_ADDRESS_LIST_chainId', '_69_CS_GET_AGENT_CHANGE_INFO_chainId',
           '_6_AC_EXPORT_ACCOUNT_KEYSTORE_address', '_6_AC_EXPORT_ACCOUNT_KEYSTORE_chainId',
           '_6_AC_EXPORT_ACCOUNT_KEYSTORE_filePath', '_6_AC_EXPORT_ACCOUNT_KEYSTORE_password',
           '_70_CS_GET_AGENT_INFO_agentHash', '_70_CS_GET_AGENT_INFO_chainId',
           '_71_CS_GET_AGENT_LIST_chainId', '_71_CS_GET_AGENT_LIST_keyWord',
           '_71_CS_GET_AGENT_LIST_pageNumber', '_71_CS_GET_AGENT_LIST_pageSize',
           '_72_CS_GET_AGENT_STATUS_agentHash', '_72_CS_GET_AGENT_STATUS_chainId',
           '_73_CS_GET_CONSENSUS_CONFIG_chainId', '_74_CS_GET_CONTRACT_AGENT_INFO_agentHash',
           '_74_CS_GET_CONTRACT_AGENT_INFO_chainId', '_74_CS_GET_CONTRACT_AGENT_INFO_contractAddress',
           '_74_CS_GET_CONTRACT_AGENT_INFO_contractSender', '_75_CS_GET_CONTRACT_DEPOSIT_INFO_chainId',
           '_75_CS_GET_CONTRACT_DEPOSIT_INFO_contractAddress',
           '_75_CS_GET_CONTRACT_DEPOSIT_INFO_contractSender',
           '_75_CS_GET_CONTRACT_DEPOSIT_INFO_joinAgentHash', '_76_CS_GET_DEPOSIT_LIST_address',
           '_76_CS_GET_DEPOSIT_LIST_agentHash', '_76_CS_GET_DEPOSIT_LIST_chainId',
           '_76_CS_GET_DEPOSIT_LIST_pageNumber', '_76_CS_GET_DEPOSIT_LIST_pageSize',
           '_77_CS_GET_INFO_address', '_77_CS_GET_INFO_chainId', '_78_CS_GET_PACKER_INFO_chainId',
           '_79_CS_GET_PUBLISH_LIST_address', '_79_CS_GET_PUBLISH_LIST_chainId',
           '_79_CS_GET_PUBLISH_LIST_type', '_7_AC_EXPORT_KEYSTORE_JSON_address',
           '_7_AC_EXPORT_KEYSTORE_JSON_chainId', '_7_AC_EXPORT_KEYSTORE_JSON_password',
           '_80_CS_GET_ROUND_INFO_chainId', '_81_CS_GET_ROUND_MEMBER_LIST_chainId',
           '_81_CS_GET_ROUND_MEMBER_LIST_extend', '_82_CS_GET_SEED_NODE_INFO_chainId',
           '_83_CS_GET_WHOLEINFO_chainId', '_84_CS_MULTI_DEPOSIT_address', '_84_CS_MULTI_DEPOSIT_agentHash',
           '_84_CS_MULTI_DEPOSIT_chainId', '_84_CS_MULTI_DEPOSIT_deposit', '_84_CS_MULTI_DEPOSIT_password',
           '_84_CS_MULTI_DEPOSIT_signAddress', '_85_CS_MULTI_WITHDRAW_address',
           '_85_CS_MULTI_WITHDRAW_chainId', '_85_CS_MULTI_WITHDRAW_password',
           '_85_CS_MULTI_WITHDRAW_signAddress', '_85_CS_MULTI_WITHDRAW_txHash',
           '_86_CS_RANDOM_RAW_SEEDS_COUNT_chainId', '_86_CS_RANDOM_RAW_SEEDS_COUNT_count',
           '_86_CS_RANDOM_RAW_SEEDS_COUNT_height', '_87_CS_RANDOM_RAW_SEEDS_HEIGHT_chainId',
           '_87_CS_RANDOM_RAW_SEEDS_HEIGHT_endHeight', '_87_CS_RANDOM_RAW_SEEDS_HEIGHT_startHeight',
           '_88_CS_RANDOM_SEED_COUNT_algorithm', '_88_CS_RANDOM_SEED_COUNT_chainId',
           '_88_CS_RANDOM_SEED_COUNT_count', '_88_CS_RANDOM_SEED_COUNT_height',
           '_89_CS_RANDOM_SEED_HEIGHT_algorithm', '_89_CS_RANDOM_SEED_HEIGHT_chainId',
           '_89_CS_RANDOM_SEED_HEIGHT_endHeight', '_89_CS_RANDOM_SEED_HEIGHT_startHeight',
           '_8_AC_GET_ACCOUNT_BYADDRESS_address', '_8_AC_GET_ACCOUNT_BYADDRESS_chainId',
           '_90_CS_RECEIVE_HEADERLIST_chainId', '_90_CS_RECEIVE_HEADERLIST_headerList',
           '_91_CS_RUN_CHAIN_chainId', '_92_CS_RUN_MAINCHAIN_chainId', '_93_CS_STOPAGENT_address',
           '_93_CS_STOPAGENT_chainId', '_93_CS_STOPAGENT_password', '_94_CS_STOP_AGENT_address',
           '_94_CS_STOP_AGENT_chainId', '_94_CS_STOP_AGENT_password', '_95_CS_STOPCHAIN_chainId',
           '_96_CS_STOP_CHAIN_chainId', '_97_CS_STOP_CONTRACT_AGENT_blockTime',
           '_97_CS_STOP_CONTRACT_AGENT_chainId', '_97_CS_STOP_CONTRACT_AGENT_contractAddress',
           '_97_CS_STOP_CONTRACT_AGENT_contractBalance', '_97_CS_STOP_CONTRACT_AGENT_contractNonce',
           '_97_CS_STOP_CONTRACT_AGENT_contractSender', '_98_CS_STOP_MULTI_AGENT_address',
           '_98_CS_STOP_MULTI_AGENT_chainId', '_98_CS_STOP_MULTI_AGENT_password',
           '_98_CS_STOP_MULTI_AGENT_signAddress', '_99_CS_TRIGGER_COINBASE_CONTRACT_blockHeader',
           '_99_CS_TRIGGER_COINBASE_CONTRACT_chainId', '_99_CS_TRIGGER_COINBASE_CONTRACT_stateRoot',
           '_99_CS_TRIGGER_COINBASE_CONTRACT_tx', '_9_AC_GET_ACCOUNT_LIST_chainId',
           'compatible_proto_versions', 'compress_rate_VALUE', 'compress_type_VALUE', 'connect_method',
           'host_req', 'my_account', 'my_address', 'my_addressprefix', 'my_addresstype', 'my_addressval',
           'my_agentaddress', 'my_agenthash', 'my_algorithm', 'my_alias', 'my_allhits', 'my_amount',
           'my_args', 'my_assetchainid', 'my_assetid', 'my_assetids', 'my_assetinfolist', 'my_assetname',
           'my_assets', 'my_begin', 'my_block', 'my_blockhash', 'my_blockheader', 'my_blockheight',
           'my_blocktime', 'my_blocktype', 'my_bytecount', 'my_chainid', 'my_chainname',
           'my_circulatechainid', 'my_cmd', 'my_cmdregisterlistmy_command', 'my_commissionrate',
           'my_contractaddress', 'my_contractbalance', 'my_contractcode', 'my_contractlist',
           'my_contractnonce', 'my_contractsender', 'my_count', 'my_data', 'my_decimalplaces', 'my_dellist',
           'my_deposit', 'my_download', 'my_end', 'my_endheight', 'my_endtimestamp', 'my_evidenceheader',
           'my_excludenodes', 'my_extend', 'my_extendsdata', 'my_filepath', 'my_frestartifrunning',
           'my_gaslimit', 'my_hash', 'my_hashlist', 'my_headerlist', 'my_height', 'my_initnumber',
           'my_inputs', 'my_intcount', 'my_interval', 'my_isconfirmed', 'my_iscross', 'my_iscrossgroup',
           'my_jarfiledata', 'my_joinagenthash', 'my_keystore', 'my_keyword', 'my_list', 'my_listfrom',
           'my_listto', 'my_lmaxcpus', 'my_lmodulename', 'my_lmoduleversion', 'my_longcount',
           'my_magicnumber', 'my_maxin', 'my_maxout', 'my_maxsignaturecount', 'my_maxtxdatasize',
           'my_messagebody', 'my_methoddesc', 'my_methodname', 'my_minavailablecount',
           'my_minavailablenodenum', 'my_minsigns', 'my_modulecode', 'my_newpassword', 'my_nodeid',
           'my_nodes', 'my_outputs', 'my_overwrite', 'my_packaging', 'my_packingaddress', 'my_pagenumber',
           'my_pagesize', 'my_password', 'my_percent', 'my_prefixlist', 'my_prestateroot', 'my_price',
           'my_prikey', 'my_protocolcmds', 'my_protocolversion', 'my_pubkey', 'my_pubkeys', 'my_registertime',
           'my_remark', 'my_rewardaddress', 'my_role', 'my_round', 'my_seedips', 'my_sender', 'my_shortcount',
           'my_sig', 'my_signaddress', 'my_signaturebftratio', 'my_signpassword', 'my_size', 'my_startheight',
           'my_startpage', 'my_state', 'my_stateroot', 'my_status', 'my_symbol', 'my_toaddress', 'my_tx',
           'my_txhash', 'my_txhashlist', 'my_txlist', 'my_type', 'my_usable', 'my_value', 'my_verifierlist',
           'port_req', 'proto_ver', 'request_int', 'res_max_size', 'sub_event_ct', 'sub_period_int',
           'sub_range', 'subscriptionRange', 'websock_url']

# to generate __all__:
# import UserSettings.nulsws_USER_PARAMS as u
# dir(u)
# then remove globals from generated list
