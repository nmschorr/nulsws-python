#!/usr/bin/python3.7
"""
by Nancy Schorr for Nuls, None),
(December, None),
(2019

"""
from Libraries.Constants.nulsws_CONSTANTS_API_LABELS import *
from Libraries.Constants.nulsws_CONSTANTS_PARAM_LABELS import *

from UserSettings.nulsws_SET import *

# change settings to suit
# for use in api calls
# fill in your default params here

# next step:
# define:  my_minsigns, my_inputs, my_outputs, my_remark, my_signaddress, my_password

my_minsigns, my_inputs, my_outputs, my_remark, my_signaddress = [1,1,1,1,1]

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
_4_AC_CREATE_MULTI_SIGN_TRANSFER_remarks = my_remark
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
_26_AC_SET_REMARK_remarks = my_chainid
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
_30_AC_TRANSFER_remarks = my_chainid
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
_56_CREATE_CROSSTX_remarks = my_chainid
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
_175_SC_CALL_remarks = my_chainid
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
_183_SC_CREATE_remarks = my_chainid
_184_SC_CREATE_VALIDATOR_chainId = my_chainid
_184_SC_CREATE_VALIDATOR_tx = my_chainid
_185_SC_DELETE_chainId = my_chainid
_185_SC_DELETE_sender = my_chainid
_185_SC_DELETE_password = my_chainid
_185_SC_DELETE_contractAddress = my_address
_185_SC_DELETE_remarks = my_chainid
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
_195_SC_TOKEN_TRANSFER_remarks = my_chainid
_196_SC_TOKEN_TRANSFER_LIST_chainId = my_chainid
_196_SC_TOKEN_TRANSFER_LIST_address = my_address
_196_SC_TOKEN_TRANSFER_LIST_pageNumber = my_chainid
_196_SC_TOKEN_TRANSFER_LIST_pageSize = my_chainid
_197_SC_TRANSFER_chainId = my_chainid
_197_SC_TRANSFER_address = my_address
_197_SC_TRANSFER_toAddress = my_address
_197_SC_TRANSFER_password = my_chainid
_197_SC_TRANSFER_amount = my_chainid
_197_SC_TRANSFER_remarks = my_chainid
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



# list of lists of tups


USER_CALLS_DB = [
[ #0
REGISTER_API, None],
[ #1
AC_CREATE_ACCOUNT, [
(CHAINID, _1AC_CREATE_ACCOUNT_chainid),
(COUNT, _1AC_CREATE_ACCOUNT_count),
(PASSWORD, _1AC_CREATE_ACCOUNT_password)
]],

[
AC_CREATE_CONTRACT_ACCOUNT, [      #2
(CHAINID, _2AC_CREATE_CONTRACT_ACCOUNT_chainid)
]],

[
AC_CREATE_MULTI_SIGN_ACCOUNT, [     #3
(CHAINID, _3_ACCREATE_MULTI_SIGN_ACCOUNT_chainid),
(PUBKEYS, _3_ACCREATE_MULTI_SIGN_ACCOUNT_pubkeys),
(MINSIGNS, _3_ACCREATE_MULTI_SIGN_ACCOUNT_minsigns)
]],

[
AC_CREATE_MULTI_SIGN_TRANSFER, [     #4
(CHAINID, _4_AC_CREATE_MULTI_SIGN_ACCOUNT_chainid),
(INPUTS, _4_AC_CREATE_MULTI_SIGN_ACCOUNT_inputs),
(OUTPUTS, _4_AC_CREATE_MULTI_SIGN_ACCOUNT_outputs),
(REMARK, _4_AC_CREATE_MULTI_SIGN_ACCOUNT_remark),
(SIGNADDRESS, _4_AC_CREATE_MULTI_SIGN_ACCOUNT_signaddress),
(SIGNPASSWORD, _4_AC_CREATE_MULTI_SIGN_ACCOUNT_signpassword)
]], 

[
AC_CREATE_OFFLINE_ACCOUNT, [      #5
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
(ADDRESS, my_address)
]], 

[
AC_GET_ACCOUNT_LIST, [
(CHAINID, my_chainid)
]], 

[

AC_GET_ADDRESS_LIST, [
(CHAINID, my_chainid),
(PAGENUMBER, 1),
(PAGESIZE, 0)
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
AC_GET_ALL_ADDRESS_PREFIX, []], 

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
(OVERWRITE, TRUE)
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
(REMARK, REMARK)
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
(REMARK, REMARK)
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
BLOCKHEIGHT, []], 

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
(ASSETCHAINID, my_chainid),
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
CONNECT_READY, []], 

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
(REMARK, REMARK)
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
(COUNT, 0),
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
GET_CROSSCHAIN_INFOS, []], 

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
GET_LATEST_ROUND_BLOCKHEADERS,[
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
GET_REGISTERED_CHAIN_INFO_LIST, []], 

[
GET_ROUND_BLOCKHEADERS, [
(CHAINID, my_chainid),
(HEIGHT, ZERO),
(ROUND, ZERO)
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
LATEST_HEIGHT, [
(CHAINID, my_chainid)
]], 

[
LISTENER_DEPENDENCIES_READY, []
], [

MSG_PROCESS,[
(CHAINID, my_chainid),
( NODEID, ZERO),
( CMD, None),
(MESSAGEBODY, None)
]], 

[
NEW_BLOCK_HEIGHT, [
(CHAINID, my_chainid),
(HEIGHT, ZERO)
]], 

[
NW_ACTIVE_CROSS, [
(CHAINID, my_chainid),
( MAXOUT, ZERO),
( MAXIN, ZERO),
( SEEDIPS, None)
]], 

[
NW_ADD_NODES, [
(CHAINID, my_chainid),
( ISCROSS, FALSE),
( NODES, None)
]], 

[
NW_BROADCAST, [
( CHAINID, my_chainid),
( EXCLUDENODES, None),
(MESSAGEBODY, SHORT_MSG),
( COMMAND, None),
( ISCROSS, FALSE),
( PERCENT, ZERO)
]], 

[
NW_CREATE_NODEGROUP, [
( CHAINID, my_chainid),
( MAGICNUMBER, ZERO),
( MAXOUT, ZERO),
( MAXIN, ZERO),
( MINAVAILABLECOUNT, ZERO),
    (ISCROSSGROUP, FALSE)
]], 

[
NW_DEL_NODES, [
( CHAINID, my_chainid),
( NODES, None)
]], 

[
NW_GET_CHAIN_CONNECT_AMOUNT, [
( CHAINID, my_chainid),
( ISCROSS, FALSE)
]], 

[
NW_GET_GROUP_BY_CHAINID,[
( CHAINID, my_chainid)
]],
    
[
NW_GET_GROUPS, [
( STARTPAGE, FALSE),
( PAGESIZE, ZERO)
]],

[
NW_GET_NODES, [
( CHAINID, my_chainid),
( STATE, None),
( ISCROSS, FALSE),
( STARTPAGE, ZERO),
( PAGESIZE, ZERO)
]], 

[
NW_GET_SEEDS, [], 
],

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
   (MESSAGEBODY, SHORT_MSG),
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
( INTCOUNT, ZERO),
( BYTECOUNT, my_count),
( SHORTCOUNT, ZERO),
( LONGCOUNT, ZERO)
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
(MESSAGEBODY, SHORT_MSG)
]], 

[
RECV_CTX, [
( CHAINID, my_chainid),
( NODEID, None),
(MESSAGEBODY, SHORT_MSG)
]], 

[
RECV_CTX_HASH, [
( CHAINID, my_chainid),
( NODEID, None),
(MESSAGEBODY, SHORT_MSG)
]], 

[
RECV_CTX_SIGN, [
( CHAINID, my_chainid),
( NODEID, None),
(MESSAGEBODY, SHORT_MSG)
]], 

[
RECV_CTX_STATE, [
( CHAINID, my_chainid),
( NODEID, None),
(MESSAGEBODY, SHORT_MSG)
]], 

[
RECV_OTHER_CTX, [
( CHAINID, my_chainid),
( NODEID, None),
(MESSAGEBODY, SHORT_MSG)
]], 

[
RECV_REGCHAIN, [
( CHAINID, my_chainid),
( NODEID, None),
(MESSAGEBODY, SHORT_MSG)
]], 

[
REGISTER_MODULE_DEPENDENCIES, []
],

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
(REMARK, SHORT_MSG)
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
( GASLIMIT, ZERO),
( PRICE, None),
( CONTRACTCODE, None),
( ARGS, None),
(REMARK, SHORT_MSG)
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
(REMARK, SHORT_MSG)
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
( CONTRACTADDRESS, my_address),
( ADDRESS, my_address)
]],

[
SC_TOKEN_TRANSFER, [
( CHAINID, my_chainid),
( ADDRESS, my_address),
( TOADDRESS, my_address),
( CONTRACTADDRESS, my_address),
( PASSWORD, None),
( AMOUNT, ZERO),
(REMARK, SHORT_MSG)
]],

[
SC_TOKEN_TRANSFER_LIST, [
( CHAINID, my_chainid),
( ADDRESS, my_address),
( PAGENUMBER, None),
( PAGESIZE, None)
]],

[
SC_TRANSFER, [
( CHAINID, my_chainid),
( ADDRESS, my_address),
( TOADDRESS, None),
( PASSWORD, my_password),
( AMOUNT, None),
(REMARK, SHORT_MSG)
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
FORWARD_MESSAGE, []], 

[
GET_CONSOLIDATEDAPI, []], 

[
CHECK_UPDATES, []], 

[
SCAN_MANAGED_MODULES, []], 

[
SHUTDOWN_SYSTEM, [
]],
[
STOP_ALL_MODULES, None
]
] #end big list

