#!/usr/bin/python3.7
"""
by Nancy Schorr for Nuls, None),
(December, None),
(2019

"""

from nulsws_python.src.nulsws_python.user_settings.nulsws_settings_one import *

# change user_settings to suit
# for use in api calls
# fill in your default params here


class UserSettings(object):
    my_minsigns, my_inputs, my_outputs, my_remark, my_signaddress = [1, 1, 1, 1, 1]

    z0_ADD_ADDRESS_PREFIX_prefix = my_addressprefix
    z1_AC_CREATE_ACCOUNT_chainId = my_chainid
    z1_AC_CREATE_ACCOUNT_count = my_chainid
    z1_AC_CREATE_ACCOUNT_password = my_password
    z2_AC_CREATE_CONTRACT_ACCOUNT_chainId = my_chainid
    z3_AC_CREATE_MULTI_SIGN_ACCOUNT_chainId = my_chainid
    z3_AC_CREATE_MULTI_SIGN_ACCOUNT_pubKeys = my_pubkeys
    z3_AC_CREATE_MULTI_SIGN_ACCOUNT_minSigns = my_minsigns
    z4_AC_CREATE_MULTI_SIGN_TRANSFER_chainId = my_chainid
    z4_AC_CREATE_MULTI_SIGN_TRANSFER_inputs = my_inputs
    z4_AC_CREATE_MULTI_SIGN_TRANSFER_outputs = my_outputs
    z4_AC_CREATE_MULTI_SIGN_TRANSFER_remark = my_remark
    z4_AC_CREATE_MULTI_SIGN_TRANSFER_signAddress = my_address
    z4_AC_CREATE_MULTI_SIGN_TRANSFER_signPassword = my_password
    z5_AC_CREATE_OFFLINE_ACCOUNT_chainId = my_chainid
    z5_AC_CREATE_OFFLINE_ACCOUNT_count = my_chainid
    z5_AC_CREATE_OFFLINE_ACCOUNT_password = my_chainid
    z6_AC_EXPORT_ACCOUNT_KEYSTORE_chainId = my_chainid
    z6_AC_EXPORT_ACCOUNT_KEYSTORE_address = my_address
    z6_AC_EXPORT_ACCOUNT_KEYSTORE_password = my_chainid
    z6_AC_EXPORT_ACCOUNT_KEYSTORE_filePath = my_chainid
    z7_AC_EXPORT_KEYSTORE_JSON_chainId = my_chainid
    z7_AC_EXPORT_KEYSTORE_JSON_address = my_address
    z7_AC_EXPORT_KEYSTORE_JSON_password = my_password
    z8_AC_GET_ACCOUNT_BYADDRESS_chainId = my_chainid
    z8_AC_GET_ACCOUNT_BYADDRESS_address = my_address
    z9_AC_GET_ACCOUNT_LIST_chainId = my_chainid
    z10_AC_GET_ADDRESS_LIST_chainId = my_chainid
    z10_AC_GET_ADDRESS_LIST_pageNumber = my_chainid
    z10_AC_GET_ADDRESS_LIST_pageSize = my_chainid
    z11_AC_GET_ADDRESS_PREFIX_BY_CHAINID_chainId = my_chainid
    z12_AC_GET_ALIASBY_ADDRESS_chainId = my_chainid
    z12_AC_GET_ALIASBY_ADDRESS_address = my_address
    z13_AC_GET_ALL_ADDRESS_PREFIX_chainId = my_chainid

    z14_AC_GET_ALL_PRIKEY_chainId = my_chainid

    z14_AC_GET_ALL_PRIKEY_password = my_password
    z15_AC_GET_ENCRYPTED_ADDRESS_LIST_chainId = my_chainid
    z16_AC_GET_MULTI_SIGN_ACCOUNT_chainId = my_chainid
    z16_AC_GET_MULTI_SIGN_ACCOUNT_address = my_address
    z17_AC_GET_PUBKEY_chainId = my_chainid
    z17_AC_GET_PUBKEY_address = my_address
    z17_AC_GET_PUBKEY_password = my_chainid
    z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_chainId = my_chainid
    z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_password = my_chainid
    z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_keyStore = my_chainid
    z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_overwrite = my_chainid
    z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_chainId = my_chainid
    z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_password = my_password
    z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_priKey = my_chainid
    z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_overwrite = my_chainid
    z20_AC_IS_ALIAS_USABLE_chainId = my_chainid
    z20_AC_IS_ALIAS_USABLE_alias = my_chainid
    z21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_chainId = my_chainid
    z21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_address = my_address
    z21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_pubKey = my_chainid
    z22_AC_REMOVE_ACCOUNT_chainId = my_chainid
    z22_AC_REMOVE_ACCOUNT_address = my_address
    z22_AC_REMOVE_ACCOUNT_password = my_chainid
    z23_AC_REMOVE_MULTISIGN_ACCOUNT_chainId = my_chainid
    z23_AC_REMOVE_MULTISIGN_ACCOUNT_address = my_address
    z24_AC_SET_ALIAS_chainId = my_chainid
    z24_AC_SET_ALIAS_address = my_address
    z24_AC_SET_ALIAS_password = my_chainid
    z24_AC_SET_ALIAS_alias = my_chainid
    z25_AC_SET_MULTISIGN_ALIAS_chainId = my_chainid
    z25_AC_SET_MULTISIGN_ALIAS_address = my_address
    z25_AC_SET_MULTISIGN_ALIAS_alias = my_chainid
    z25_AC_SET_MULTISIGN_ALIAS_signAddress = my_address
    z25_AC_SET_MULTISIGN_ALIAS_signPassword = my_password
    z26_AC_SET_REMARK_chainId = my_chainid
    z26_AC_SET_REMARK_address = my_address
    z26_AC_SET_REMARK_remark = my_chainid
    z27_AC_SIGN_BLOCKDIGEST_chainId = my_chainid
    z27_AC_SIGN_BLOCKDIGEST_address = my_address
    z27_AC_SIGN_BLOCKDIGEST_password = my_chainid
    z27_AC_SIGN_BLOCKDIGEST_data = my_chainid
    z28_AC_SIGN_DIGEST_chainId = my_chainid
    z28_AC_SIGN_DIGEST_address = my_address
    z28_AC_SIGN_DIGEST_password = my_chainid
    z28_AC_SIGN_DIGEST_data = my_chainid
    z29_AC_SIGN_MULTISIGN_TRANSACTION_chainId = my_chainid
    z29_AC_SIGN_MULTISIGN_TRANSACTION_tx = my_chainid
    z29_AC_SIGN_MULTISIGN_TRANSACTION_signAddress = my_address
    z29_AC_SIGN_MULTISIGN_TRANSACTION_signPassword = my_password
    z30_AC_TRANSFER_chainId = my_chainid
    z30_AC_TRANSFER_inputs = my_chainid
    z30_AC_TRANSFER_outputs = my_chainid
    z30_AC_TRANSFER_remark = my_chainid
    z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_chainId = my_chainid
    z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_address = my_address
    z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_password = my_chainid
    z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_newPassword = my_chainid
    z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_priKey = my_chainid
    z32_AC_UPDATE_PASSWORD_chainId = my_chainid
    z32_AC_UPDATE_PASSWORD_address = my_address
    z32_AC_UPDATE_PASSWORD_password = my_chainid
    z32_AC_UPDATE_PASSWORD_newPassword = my_chainid
    z33_AC_VALIDATION_PASSWORD_chainId = my_chainid
    z33_AC_VALIDATION_PASSWORD_address = my_address
    z33_AC_VALIDATION_PASSWORD_password = my_chainid
    z34_AC_VERIFY_SIGN_DATA_pubKey = my_chainid
    z34_AC_VERIFY_SIGN_DATA_sig = my_chainid
    z34_AC_VERIFY_SIGN_DATA_data = my_chainid
    z35_BATCH_VALIDATE_BEGIN_chainId = my_chainid
    z36_BLOCK_VALIDATE_chainId = my_chainid
    z36_BLOCK_VALIDATE_txList = my_chainid
    z38_CANCEL_CROSSCHAIN_chainId = my_chainid
    z38_CANCEL_CROSSCHAIN_assetId = my_chainid
    z39_CHECK_BLOCK_VERSION_chainId = my_chainid
    z39_CHECK_BLOCK_VERSION_extendsData = my_chainid
    z40_CM_ASSET_chainId = my_chainid
    z40_CM_ASSET_assetId = my_chainid
    z41_CM_ASSET_CIRCULATE_COMMIT_chainId = my_chainid
    z41_CM_ASSET_CIRCULATE_COMMIT_txList = my_chainid
    z41_CM_ASSET_CIRCULATE_COMMIT_blockHeader = my_chainid
    z42_CM_ASSET_CIRCULATE_ROLLBACK_chainId = my_chainid
    z42_CM_ASSET_CIRCULATE_ROLLBACK_txList = my_chainid
    z42_CM_ASSET_CIRCULATE_ROLLBACK_blockHeader = my_chainid
    z43_CM_ASSET_CIRCULATE_VALIDATOR_chainId = my_chainid
    z43_CM_ASSET_CIRCULATE_VALIDATOR_tx = my_chainid
    z44_CM_ASSET_DISABLE_chainId = my_chainid
    z44_CM_ASSET_DISABLE_assetId = my_chainid
    z44_CM_ASSET_DISABLE_address = my_address
    z44_CM_ASSET_DISABLE_password = my_password
    z45_CM_ASSET_REG_chainId = my_chainid
    z45_CM_ASSET_REG_assetId = my_chainid
    z45_CM_ASSET_REG_symbol = my_chainid
    z45_CM_ASSET_REG_assetName = my_chainid
    z45_CM_ASSET_REG_initNumber = my_chainid
    z45_CM_ASSET_REG_decimalPlaces = my_chainid
    z45_CM_ASSET_REG_address = my_address
    z45_CM_ASSET_REG_password = my_chainid
    z46_CM_CHAIN_chainId = my_chainid
    z47_CM_CHAIN_ACTIVE_chainId = my_chainid
    z47_CM_CHAIN_ACTIVE_chainName = my_chainid
    z47_CM_CHAIN_ACTIVE_addressType = my_address
    z47_CM_CHAIN_ACTIVE_addressPrefix = my_address
    z47_CM_CHAIN_ACTIVE_magicNumber = my_chainid
    z47_CM_CHAIN_ACTIVE_minAvailableNodeNum = my_chainid
    z47_CM_CHAIN_ACTIVE_assetId = my_chainid
    z47_CM_CHAIN_ACTIVE_symbol = my_chainid
    z47_CM_CHAIN_ACTIVE_assetName = my_chainid
    z47_CM_CHAIN_ACTIVE_initNumber = my_chainid
    z47_CM_CHAIN_ACTIVE_decimalPlaces = my_chainid
    z47_CM_CHAIN_ACTIVE_address = my_address
    z47_CM_CHAIN_ACTIVE_password = my_chainid
    z47_CM_CHAIN_ACTIVE_verifierList = my_chainid
    z47_CM_CHAIN_ACTIVE_signatureBFTRatio = my_chainid
    z47_CM_CHAIN_ACTIVE_maxSignatureCount = my_chainid
    z48_CM_CHAIN_REG_chainId = my_chainid
    z48_CM_CHAIN_REG_chainName = my_chainid
    z48_CM_CHAIN_REG_addressType = my_address
    z48_CM_CHAIN_REG_addressPrefix = my_address
    z48_CM_CHAIN_REG_magicNumber = my_chainid
    z48_CM_CHAIN_REG_minAvailableNodeNum = my_chainid
    z48_CM_CHAIN_REG_assetId = my_chainid
    z48_CM_CHAIN_REG_symbol = my_chainid
    z48_CM_CHAIN_REG_assetName = my_chainid
    z48_CM_CHAIN_REG_initNumber = my_chainid
    z48_CM_CHAIN_REG_decimalPlaces = my_chainid
    z48_CM_CHAIN_REG_address = my_address
    z48_CM_CHAIN_REG_password = my_chainid
    z48_CM_CHAIN_REG_verifierList = my_chainid
    z48_CM_CHAIN_REG_signatureBFTRatio = my_chainid
    z48_CM_CHAIN_REG_maxSignatureCount = my_chainid
    z49_CM_GET_CHAIN_ASSET_chainId = my_chainid
    z49_CM_GET_CHAIN_ASSET_assetChainId = my_chainid
    z49_CM_GET_CHAIN_ASSET_assetId = my_chainid
    z50_CM_GET_CIRCULATE_CHAIN_ASSET_circulateChainId = my_chainid
    z50_CM_GET_CIRCULATE_CHAIN_ASSET_assetChainId = my_chainid
    z50_CM_GET_CIRCULATE_CHAIN_ASSET_assetId = my_chainid
    z51_COMMIT_BATCH_UNCONFIRMED_TXS_chainId = my_chainid
    z51_COMMIT_BATCH_UNCONFIRMED_TXS_txList = my_chainid
    z52_COMMIT_BLOCKTXS_chainId = my_chainid
    z52_COMMIT_BLOCKTXS_txList = my_chainid
    z52_COMMIT_BLOCKTXS_blockHeight = my_chainid
    z53_COMMIT_UNCONFIRMEDTX_chainId = my_chainid
    z53_COMMIT_UNCONFIRMEDTX_tx = my_chainid
    z55_CREATE_AGENT_VALID_chainId = my_chainid
    z55_CREATE_AGENT_VALID_tx = my_chainid
    z56_CREATE_CROSSTX_chainId = my_chainid
    z56_CREATE_CROSSTX_listFrom = my_chainid
    z56_CREATE_CROSSTX_listTo = my_chainid
    z56_CREATE_CROSSTX_remark = my_chainid
    z57_CROSSCHAIN_REGISTER_CHANGE_chainId = my_chainid
    z58_CS_ADD_BLOCK_chainId = my_chainid
    z58_CS_ADD_BLOCK_blockHeader = my_chainid
    z59_CS_ADD_EVIDENCE_RECORD_chainId = my_chainid
    z59_CS_ADD_EVIDENCE_RECORD_blockHeader = my_chainid
    z59_CS_ADD_EVIDENCE_RECORD_evidenceHeader = my_chainid
    z60_CS_CHAIN_ROLLBACK_chainId = my_chainid
    z60_CS_CHAIN_ROLLBACK_height = my_chainid
    z61_CS_CONTRACT_DEPOSIT_chainId = my_chainid
    z61_CS_CONTRACT_DEPOSIT_agentHash = my_chainid
    z61_CS_CONTRACT_DEPOSIT_deposit = my_chainid
    z61_CS_CONTRACT_DEPOSIT_contractAddress = my_address
    z61_CS_CONTRACT_DEPOSIT_contractSender = my_chainid
    z61_CS_CONTRACT_DEPOSIT_contractBalance = my_chainid
    z61_CS_CONTRACT_DEPOSIT_contractNonce = my_chainid
    z61_CS_CONTRACT_DEPOSIT_blockTime = my_chainid
    z62_CS_CONTRACT_WITHDRAW_chainId = my_chainid
    z62_CS_CONTRACT_WITHDRAW_joinAgentHash = my_chainid
    z62_CS_CONTRACT_WITHDRAW_contractAddress = my_address
    z62_CS_CONTRACT_WITHDRAW_contractSender = my_chainid
    z62_CS_CONTRACT_WITHDRAW_contractBalance = my_chainid
    z62_CS_CONTRACT_WITHDRAW_contractNonce = my_chainid
    z62_CS_CONTRACT_WITHDRAW_blockTime = my_chainid
    z63_CS_CREATE_AGENT_chainId = my_chainid
    z63_CS_CREATE_AGENT_agentAddress = my_address
    z63_CS_CREATE_AGENT_packingAddress = my_address
    z63_CS_CREATE_AGENT_rewardAddress = my_address
    z63_CS_CREATE_AGENT_commissionRate = my_chainid
    z63_CS_CREATE_AGENT_deposit = my_chainid
    z63_CS_CREATE_AGENT_password = my_chainid
    z64_CS_CREATE_CONTRACT_AGENT_chainId = my_chainid
    z64_CS_CREATE_CONTRACT_AGENT_packingAddress = my_address
    z64_CS_CREATE_CONTRACT_AGENT_deposit = my_chainid
    z64_CS_CREATE_CONTRACT_AGENT_commissionRate = my_chainid
    z64_CS_CREATE_CONTRACT_AGENT_contractAddress = my_address
    z64_CS_CREATE_CONTRACT_AGENT_contractSender = my_chainid
    z64_CS_CREATE_CONTRACT_AGENT_contractBalance = my_chainid
    z64_CS_CREATE_CONTRACT_AGENT_contractNonce = my_chainid
    z64_CS_CREATE_CONTRACT_AGENT_blockTime = my_chainid
    z65_CS_CREATE_MULTI_AGENT_chainId = my_chainid
    z65_CS_CREATE_MULTI_AGENT_agentAddress = my_address
    z65_CS_CREATE_MULTI_AGENT_packingAddress = my_address
    z65_CS_CREATE_MULTI_AGENT_rewardAddress = my_address
    z65_CS_CREATE_MULTI_AGENT_commissionRate = my_chainid
    z65_CS_CREATE_MULTI_AGENT_deposit = my_chainid
    z65_CS_CREATE_MULTI_AGENT_password = my_chainid
    z65_CS_CREATE_MULTI_AGENT_signAddress = my_address
    z66_CS_DEPOSIT_TOAGENT_chainId = my_chainid
    z66_CS_DEPOSIT_TOAGENT_address = my_address
    z66_CS_DEPOSIT_TOAGENT_agentHash = my_chainid
    z66_CS_DEPOSIT_TOAGENT_deposit = my_chainid
    z66_CS_DEPOSIT_TOAGENT_password = my_chainid
    z67_CS_DOUBLE_SPEND_RECORD_chainId = my_chainid
    z67_CS_DOUBLE_SPEND_RECORD_block = my_chainid
    z67_CS_DOUBLE_SPEND_RECORD_tx = my_chainid
    z68_CS_GET_AGENT_ADDRESS_LIST_chainId = my_chainid
    z69_CS_GET_AGENT_CHANGE_INFO_chainId = my_chainid
    z70_CS_GET_AGENT_INFO_chainId = my_chainid
    z70_CS_GET_AGENT_INFO_agentHash = my_chainid
    z71_CS_GET_AGENT_LIST_chainId = my_chainid
    z71_CS_GET_AGENT_LIST_pageNumber = my_chainid
    z71_CS_GET_AGENT_LIST_pageSize = my_chainid
    z71_CS_GET_AGENT_LIST_keyWord = my_chainid
    z72_CS_GET_AGENT_STATUS_chainId = my_chainid
    z72_CS_GET_AGENT_STATUS_agentHash = my_chainid
    z73_CS_GET_CONSENSUS_CONFIG_chainId = my_chainid
    z74_CS_GET_CONTRACT_AGENT_INFO_chainId = my_chainid
    z74_CS_GET_CONTRACT_AGENT_INFO_agentHash = my_chainid
    z74_CS_GET_CONTRACT_AGENT_INFO_contractAddress = my_address
    z74_CS_GET_CONTRACT_AGENT_INFO_contractSender = my_chainid
    z75_CS_GET_CONTRACT_DEPOSIT_INFO_chainId = my_chainid
    z75_CS_GET_CONTRACT_DEPOSIT_INFO_joinAgentHash = my_chainid
    z75_CS_GET_CONTRACT_DEPOSIT_INFO_contractAddress = my_address
    z75_CS_GET_CONTRACT_DEPOSIT_INFO_contractSender = my_chainid
    z76_CS_GET_DEPOSIT_LIST_chainId = my_chainid
    z76_CS_GET_DEPOSIT_LIST_pageNumber = my_chainid
    z76_CS_GET_DEPOSIT_LIST_pageSize = my_chainid
    z76_CS_GET_DEPOSIT_LIST_address = my_address
    z76_CS_GET_DEPOSIT_LIST_agentHash = my_chainid
    z77_CS_GET_INFO_chainId = my_chainid
    z77_CS_GET_INFO_address = my_address
    z78_CS_GET_PACKER_INFO_chainId = my_chainid
    z79_CS_GET_PUBLISH_LIST_chainId = my_chainid
    z79_CS_GET_PUBLISH_LIST_address = my_address
    z79_CS_GET_PUBLISH_LIST_type = my_chainid
    z80_CS_GET_ROUND_INFO_chainId = my_chainid
    z81_CS_GET_ROUND_MEMBER_LIST_chainId = my_chainid
    z81_CS_GET_ROUND_MEMBER_LIST_extend = my_chainid
    z82_CS_GET_SEED_NODE_INFO_chainId = my_chainid
    z83_CS_GET_WHOLEINFO_chainId = my_chainid
    z84_CS_MULTI_DEPOSIT_chainId = my_chainid
    z84_CS_MULTI_DEPOSIT_address = my_address
    z84_CS_MULTI_DEPOSIT_agentHash = my_chainid
    z84_CS_MULTI_DEPOSIT_deposit = my_chainid
    z84_CS_MULTI_DEPOSIT_password = my_chainid
    z84_CS_MULTI_DEPOSIT_signAddress = my_address
    z85_CS_MULTI_WITHDRAW_chainId = my_chainid
    z85_CS_MULTI_WITHDRAW_address = my_address
    z85_CS_MULTI_WITHDRAW_txHash = my_chainid
    z85_CS_MULTI_WITHDRAW_password = my_chainid
    z85_CS_MULTI_WITHDRAW_signAddress = my_address
    z86_CS_RANDOM_RAW_SEEDS_COUNT_chainId = my_chainid
    z86_CS_RANDOM_RAW_SEEDS_COUNT_height = my_chainid
    z86_CS_RANDOM_RAW_SEEDS_COUNT_count = my_chainid
    z87_CS_RANDOM_RAW_SEEDS_HEIGHT_chainId = my_chainid
    z87_CS_RANDOM_RAW_SEEDS_HEIGHT_startHeight = my_chainid
    z87_CS_RANDOM_RAW_SEEDS_HEIGHT_endHeight = my_chainid
    z88_CS_RANDOM_SEED_COUNT_chainId = my_chainid
    z88_CS_RANDOM_SEED_COUNT_height = my_chainid
    z88_CS_RANDOM_SEED_COUNT_count = my_chainid
    z88_CS_RANDOM_SEED_COUNT_algorithm = my_chainid
    z89_CS_RANDOM_SEED_HEIGHT_chainId = my_chainid
    z89_CS_RANDOM_SEED_HEIGHT_startHeight = my_chainid
    z89_CS_RANDOM_SEED_HEIGHT_endHeight = my_chainid
    z89_CS_RANDOM_SEED_HEIGHT_algorithm = my_chainid
    z90_CS_RECEIVE_HEADERLIST_chainId = my_chainid
    z90_CS_RECEIVE_HEADERLIST_headerList = my_chainid
    z91_CS_RUN_CHAIN_chainId = my_chainid
    z92_CS_RUN_MAINCHAIN_chainId = my_chainid
    z93_CS_STOPAGENT_chainId = my_chainid
    z93_CS_STOPAGENT_address = my_address
    z93_CS_STOPAGENT_password = my_chainid
    z94_CS_STOP_AGENT_chainId = my_chainid
    z94_CS_STOP_AGENT_address = my_address
    z94_CS_STOP_AGENT_password = my_chainid
    z95_CS_STOPCHAIN_chainId = my_chainid
    z96_CS_STOP_CHAIN_chainId = my_chainid
    z97_CS_STOP_CONTRACT_AGENT_chainId = my_chainid
    z97_CS_STOP_CONTRACT_AGENT_contractAddress = my_address
    z97_CS_STOP_CONTRACT_AGENT_contractSender = my_chainid
    z97_CS_STOP_CONTRACT_AGENT_contractBalance = my_chainid
    z97_CS_STOP_CONTRACT_AGENT_contractNonce = my_chainid
    z97_CS_STOP_CONTRACT_AGENT_blockTime = my_chainid
    z98_CS_STOP_MULTI_AGENT_chainId = my_chainid
    z98_CS_STOP_MULTI_AGENT_address = my_address
    z98_CS_STOP_MULTI_AGENT_password = my_chainid
    z98_CS_STOP_MULTI_AGENT_signAddress = my_address
    z99_CS_TRIGGER_COINBASE_CONTRACT_chainId = my_chainid
    z99_CS_TRIGGER_COINBASE_CONTRACT_tx = my_chainid
    z99_CS_TRIGGER_COINBASE_CONTRACT_blockHeader = my_chainid
    z99_CS_TRIGGER_COINBASE_CONTRACT_stateRoot = my_chainid
    z100_CS_UPDATE_AGENT_CONSENSUS_STATUS_chainId = my_chainid
    z101_CS_UPDATE_AGENT_STATUS_chainId = my_chainid
    z101_CS_UPDATE_AGENT_STATUS_status = my_chainid
    z102_CS_VALIDBLOCK_chainId = my_chainid
    z102_CS_VALIDBLOCK_download = my_chainid
    z102_CS_VALIDBLOCK_block = my_chainid
    z103_CS_WITHDRAW_chainId = my_chainid
    z103_CS_WITHDRAW_address = my_address
    z103_CS_WITHDRAW_txHash = my_chainid
    z103_CS_WITHDRAW_password = my_chainid
    z104_DEPOSIT_VALID_chainId = my_chainid
    z104_DEPOSIT_VALID_tx = my_chainid
    z105_GET_ASSETS_BY_ID_chainId = my_chainid
    z105_GET_ASSETS_BY_ID_assetIds = my_chainid
    z106_GET_BALANCE_chainId = my_chainid
    z106_GET_BALANCE_assetChainId = my_chainid
    z106_GET_BALANCE_assetId = my_chainid
    z106_GET_BALANCE_address = my_address
    z107_GET_BALANCE_NONCE_chainId = my_chainid
    z107_GET_BALANCE_NONCE_assetChainId = my_chainid
    z107_GET_BALANCE_NONCE_assetId = my_chainid
    z107_GET_BALANCE_NONCE_address = my_address
    z107_GET_BALANCE_NONCE_isConfirmed = my_chainid
    z108_GET_BLOCK_BY_HASH_chainId = my_chainid
    z108_GET_BLOCK_BY_HASH_hash = my_chainid
    z109_GET_BLOCK_BY_HEIGHT_chainId = my_chainid
    z109_GET_BLOCK_BY_HEIGHT_height = my_chainid
    z110_GET_BLOCKHEADER_BY_HASH_chainId = my_chainid
    z110_GET_BLOCKHEADER_BY_HASH_hash = my_chainid
    z111_GET_BLOCKHEADER_BY_HEIGHT_chainId = my_chainid
    z111_GET_BLOCKHEADER_BY_HEIGHT_height = my_chainid
    z112_GET_BLOCKHEADER_PO_BY_HASH_chainId = my_chainid
    z112_GET_BLOCKHEADER_PO_BY_HASH_hash = my_chainid
    z113_GET_BLOCKHEADER_POBY_HEIGHT_chainId = my_chainid
    z113_GET_BLOCKHEADER_POBY_HEIGHT_height = my_chainid
    z114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_chainId = my_chainid
    z114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_begin = my_chainid
    z114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_end = my_chainid
    z115_GET_BLOCKHEADERS_FOR_PROTOCOL_chainId = my_chainid
    z115_GET_BLOCKHEADERS_FOR_PROTOCOL_interval = my_chainid
    z116_GET_BYZANTINE_COUNT_chainId = my_chainid
    z117_GET_CIRCULAT_chainId = my_chainid
    z117_GET_CIRCULAT_nodeId = my_chainid
    z117_GET_CIRCULAT_messageBody = my_chainid
    z119_GET_CROSSTX_STATE_chainId = my_chainid
    z119_GET_CROSSTX_STATE_txHash = my_chainid
    z120_GET_CTX_chainId = my_chainid
    z120_GET_CTX_nodeId = my_chainid
    z120_GET_CTX_messageBody = my_chainid
    z121_GET_CTX_STATE_chainId = my_chainid
    z121_GET_CTX_STATE_nodeId = my_chainid
    z121_GET_CTX_STATE_messageBody = my_chainid
    z122_GET_FRIEND_CHAIN_CIRCULATE_chainId = my_chainid
    z122_GET_FRIEND_CHAIN_CIRCULATE_assetIds = my_chainid
    z123_GET_LATEST_BLOCKHEADERS_chainId = my_chainid
    z123_GET_LATEST_BLOCKHEADERS_size = my_chainid
    z124_GET_LATEST_ROUND_BLOCKHEADERS_chainId = my_chainid
    z124_GET_LATEST_ROUND_BLOCKHEADERS_round = my_chainid
    z125_GET_NONCE_chainId = my_chainid
    z125_GET_NONCE_assetChainId = my_chainid
    z125_GET_NONCE_assetId = my_chainid
    z125_GET_NONCE_address = my_address
    z125_GET_NONCE_isConfirmed = my_chainid
    z126_GET_OTHERCTX_chainId = my_chainid
    z126_GET_OTHERCTX_nodeId = my_chainid
    z126_GET_OTHERCTX_messageBody = my_chainid
    z128_GET_ROUND_BLOCKHEADERS_chainId = my_chainid
    z128_GET_ROUND_BLOCKHEADERS_height = my_chainid
    z128_GET_ROUND_BLOCKHEADERS_round = my_chainid
    z129_GET_STATUS_chainId = my_chainid
    z130_GET_VERSION_chainId = my_chainid
    z131_INFO_chainId = my_chainid
    z132_LATEST_BLOCK_chainId = my_chainid
    z133_LATEST_BLOCKHEADER_chainId = my_chainid
    z134_LATEST_BLOCKHEADER_PO_chainId = my_chainid
    z135_LATEST_HEIGHT_chainId = my_chainid
    z137_MSG_PROCESS_chainId = my_chainid
    z137_MSG_PROCESS_nodeId = my_chainid
    z137_MSG_PROCESS_cmd = my_chainid
    z137_MSG_PROCESS_messageBody = my_chainid
    z138_NEW_BLOCK_HEIGHT_chainId = my_chainid
    z138_NEW_BLOCK_HEIGHT_height = my_chainid
    z139_NW_ACTIVE_CROSS_chainId = my_chainid
    z139_NW_ACTIVE_CROSS_maxOut = my_chainid
    z139_NW_ACTIVE_CROSS_maxIn = my_chainid
    z139_NW_ACTIVE_CROSS_seedIps = my_chainid
    z140_NW_ADD_NODES_chainId = my_chainid
    z140_NW_ADD_NODES_isCross = my_chainid
    z140_NW_ADD_NODES_nodes = my_chainid
    z141_NW_BROADCAST_chainId = my_chainid
    z141_NW_BROADCAST_excludeNodes = my_chainid
    z141_NW_BROADCAST_messageBody = my_chainid
    z141_NW_BROADCAST_command = my_chainid
    z141_NW_BROADCAST_isCross = my_chainid
    z141_NW_BROADCAST_percent = my_chainid
    z142_NW_CREATE_NODEGROUP_chainId = my_chainid
    z142_NW_CREATE_NODEGROUP_magicNumber = my_chainid
    z142_NW_CREATE_NODEGROUP_maxOut = my_chainid
    z142_NW_CREATE_NODEGROUP_maxIn = my_chainid
    z142_NW_CREATE_NODEGROUP_minAvailableCount = my_chainid
    z142_NW_CREATE_NODEGROUP_isCrossGroup = my_chainid
    z143_NW_DEL_NODES_chainId = my_chainid
    z143_NW_DEL_NODES_nodes = my_chainid
    z144_NW_GET_CHAIN_CONNECT_AMOUNT_chainId = my_chainid
    z144_NW_GET_CHAIN_CONNECT_AMOUNT_isCross = my_chainid
    z145_NW_GET_GROUP_BY_CHAINID_chainId = my_chainid
    z146_NW_GET_GROUPS_startPage = my_chainid
    z146_NW_GET_GROUPS_pageSize = my_chainid
    z147_NW_GET_NODES_chainId = my_chainid
    z147_NW_GET_NODES_state = my_chainid
    z147_NW_GET_NODES_isCross = my_chainid
    z147_NW_GET_NODES_startPage = my_chainid
    z147_NW_GET_NODES_pageSize = my_chainid
    z149_NW_INFO_chainId = my_chainid
    z150_NW_NODES_chainId = my_chainid
    z151_NW_PROTOCOL_REGISTER_role = my_chainid
    z151_NW_PROTOCOL_REGISTER_protocolCmds = my_chainid
    z152_NW_RECONNECT_chainId = my_chainid
    z153_NW_SEND_PEERS_MSG_chainId = my_chainid
    z153_NW_SEND_PEERS_MSG_nodes = my_chainid
    z153_NW_SEND_PEERS_MSG_messageBody = my_chainid
    z153_NW_SEND_PEERS_MSG_command = my_chainid
    z154_NW_UPDATE_NODE_INFO_chainId = my_chainid
    z154_NW_UPDATE_NODE_INFO_nodeId = my_chainid
    z154_NW_UPDATE_NODE_INFO_blockHeight = my_chainid
    z154_NW_UPDATE_NODE_INFO_blockHash = my_chainid
    z155_PARAM_TEST_CMD_intCount = my_chainid
    z155_PARAM_TEST_CMD_byteCount = my_chainid
    z155_PARAM_TEST_CMD_shortCount = my_chainid
    z155_PARAM_TEST_CMD_longCount = my_chainid
    z156_PROTOCOL_VERSION_CHANGE_chainId = my_chainid
    z156_PROTOCOL_VERSION_CHANGE_protocolVersion = my_chainid
    z157_RECEIVE_PACKING_BLOCK_chainId = my_chainid
    z157_RECEIVE_PACKING_BLOCK_block = my_chainid
    z158_RECV_CIRCULAT_chainId = my_chainid
    z158_RECV_CIRCULAT_nodeId = my_chainid
    z158_RECV_CIRCULAT_messageBody = my_chainid
    z159_RECV_CTX_chainId = my_chainid
    z159_RECV_CTX_nodeId = my_chainid
    z159_RECV_CTX_messageBody = my_chainid
    z160_RECV_CTX_HASH_chainId = my_chainid
    z160_RECV_CTX_HASH_nodeId = my_chainid
    z160_RECV_CTX_HASH_messageBody = my_chainid
    z161_RECV_CTX_SIGN_chainId = my_chainid
    z161_RECV_CTX_SIGN_nodeId = my_chainid
    z161_RECV_CTX_SIGN_messageBody = my_chainid
    z162_RECV_CTX_STATE_chainId = my_chainid
    z162_RECV_CTX_STATE_nodeId = my_chainid
    z162_RECV_CTX_STATE_messageBody = my_chainid
    z163_RECV_OTHER_CTX_chainId = my_chainid
    z163_RECV_OTHER_CTX_nodeId = my_chainid
    z163_RECV_OTHER_CTX_messageBody = my_chainid
    z164_RECV_REGCHAIN_chainId = my_chainid
    z164_RECV_REGCHAIN_nodeId = my_chainid
    z164_RECV_REGCHAIN_messageBody = my_chainid
    z166_REGISTER_PROTOCOL_chainId = my_chainid
    z166_REGISTER_PROTOCOL_moduleCode = my_chainid
    z166_REGISTER_PROTOCOL_list = my_chainid
    z167_ROLLBACK_BLOCK_TXS_chainId = my_chainid
    z167_ROLLBACK_BLOCK_TXS_txList = my_chainid
    z167_ROLLBACK_BLOCK_TXS_blockHeight = my_chainid
    z168_ROLLBACK_UNCONFIRM_TX_chainId = my_chainid
    z168_ROLLBACK_UNCONFIRM_TX_tx = my_chainid
    z169_ROLLBACK_BLOCK_chainId = my_chainid
    z169_ROLLBACK_BLOCK_blockHeader = my_chainid
    z170_ROLLBACK_TX_VALIDATE_STATUS_chainId = my_chainid
    z170_ROLLBACK_TX_VALIDATE_STATUS_tx = my_chainid
    z171_SAVE_BLOCK_chainId = my_chainid
    z171_SAVE_BLOCK_blockHeader = my_chainid
    z172_SC_BATCH_BEFORE_END_chainId = my_chainid
    z172_SC_BATCH_BEFORE_END_blockType = my_chainid
    z172_SC_BATCH_BEFORE_END_blockHeight = my_chainid
    z173_SC_BATCH_BEGIN_chainId = my_chainid
    z173_SC_BATCH_BEGIN_blockType = my_chainid
    z173_SC_BATCH_BEGIN_blockHeight = my_chainid
    z173_SC_BATCH_BEGIN_blockTime = my_chainid
    z173_SC_BATCH_BEGIN_packingAddress = my_address
    z173_SC_BATCH_BEGIN_preStateRoot = my_chainid
    z174_SC_BATCH_END_chainId = my_chainid
    z174_SC_BATCH_END_blockHeight = my_chainid
    z175_SC_CALL_chainId = my_chainid
    z175_SC_CALL_sender = my_chainid
    z175_SC_CALL_password = my_chainid
    z175_SC_CALL_value = my_chainid
    z175_SC_CALL_gasLimit = my_chainid
    z175_SC_CALL_price = my_chainid
    z175_SC_CALL_contractAddress = my_address
    z175_SC_CALL_methodName = my_chainid
    z175_SC_CALL_methodDesc = my_chainid
    z175_SC_CALL_args = my_chainid
    z175_SC_CALL_remark = my_chainid
    z176_SC_CALL_VALIDATOR_chainId = my_chainid
    z176_SC_CALL_VALIDATOR_tx = my_chainid
    z177_SC_CONSTRUCTOR_chainId = my_chainid
    z177_SC_CONSTRUCTOR_contractCode = my_chainid
    z178_SC_CONTRACT_INFO_chainId = my_chainid
    z178_SC_CONTRACT_INFO_contractAddress = my_address
    z179_SC_CONTRACT_OFFLINE_TX_HASH_LIST_chainId = my_chainid
    z179_SC_CONTRACT_OFFLINE_TX_HASH_LIST_blockHash = my_chainid
    z180_SC_CONTRACT_RESULT_chainId = my_chainid
    z180_SC_CONTRACT_RESULT_hash = my_chainid
    z181_SC_CONTRACT_RESULT_LIST_chainId = my_chainid
    z181_SC_CONTRACT_RESULT_LIST_hashList = my_chainid
    z182_SC_CONTRACT_TX_chainId = my_chainid
    z182_SC_CONTRACT_TX_hash = my_chainid
    z183_SC_CREATE_chainId = my_chainid
    z183_SC_CREATE_sender = my_chainid
    z183_SC_CREATE_password = my_chainid
    z183_SC_CREATE_alias = my_chainid
    z183_SC_CREATE_gasLimit = my_chainid
    z183_SC_CREATE_price = my_chainid
    z183_SC_CREATE_contractCode = my_chainid
    z183_SC_CREATE_args = my_chainid
    z183_SC_CREATE_remark = my_chainid
    z184_SC_CREATE_VALIDATOR_chainId = my_chainid
    z184_SC_CREATE_VALIDATOR_tx = my_chainid
    z185_SC_DELETE_chainId = my_chainid
    z185_SC_DELETE_sender = my_chainid
    z185_SC_DELETE_password = my_chainid
    z185_SC_DELETE_contractAddress = my_address
    z185_SC_DELETE_remark = my_chainid
    z186_SC_DELETE_VALIDATOR_chainId = my_chainid
    z186_SC_DELETE_VALIDATOR_tx = my_chainid
    z187_SC_IMPUTED_CALL_GAS_chainId = my_chainid
    z187_SC_IMPUTED_CALL_GAS_sender = my_chainid
    z187_SC_IMPUTED_CALL_GAS_value = my_chainid
    z187_SC_IMPUTED_CALL_GAS_contractAddress = my_address
    z187_SC_IMPUTED_CALL_GAS_methodName = my_chainid
    z187_SC_IMPUTED_CALL_GAS_methodDesc = my_chainid
    z187_SC_IMPUTED_CALL_GAS_args = my_chainid
    z188_SC_IMPUTED_CREATE_GAS_chainId = my_chainid
    z188_SC_IMPUTED_CREATE_GAS_sender = my_chainid
    z188_SC_IMPUTED_CREATE_GAS_contractCode = my_chainid
    z188_SC_IMPUTED_CREATE_GAS_args = my_chainid
    z189_SC_INITIAL_ACCOUNT_TOKEN_chainId = my_chainid
    z189_SC_INITIAL_ACCOUNT_TOKEN_address = my_address
    z190_SC_INVOKE_CONTRACT_chainId = my_chainid
    z190_SC_INVOKE_CONTRACT_blockType = my_chainid
    z190_SC_INVOKE_CONTRACT_tx = my_chainid
    z191_SC_INVOKE_VIEW_chainId = my_chainid
    z191_SC_INVOKE_VIEW_contractAddress = my_address
    z191_SC_INVOKE_VIEW_methodName = my_chainid
    z191_SC_INVOKE_VIEW_methodDesc = my_chainid
    z191_SC_INVOKE_VIEW_args = my_chainid
    z192_SC_PACKAGE_BATCH_END_chainId = my_chainid
    z192_SC_PACKAGE_BATCH_END_blockHeight = my_chainid
    z193_SC_TOKEN_ASSETS_LIST_chainId = my_chainid
    z193_SC_TOKEN_ASSETS_LIST_address = my_address
    z193_SC_TOKEN_ASSETS_LIST_pageNumber = my_chainid
    z193_SC_TOKEN_ASSETS_LIST_pageSize = my_chainid
    z194_SC_TOKEN_BALANCE_chainId = my_chainid
    z194_SC_TOKEN_BALANCE_contractAddress = my_address
    z194_SC_TOKEN_BALANCE_address = my_address
    z195_SC_TOKEN_TRANSFER_chainId = my_chainid
    z195_SC_TOKEN_TRANSFER_address = my_address
    z195_SC_TOKEN_TRANSFER_toAddress = my_address
    z195_SC_TOKEN_TRANSFER_contractAddress = my_address
    z195_SC_TOKEN_TRANSFER_password = my_chainid
    z195_SC_TOKEN_TRANSFER_amount = my_chainid
    z195_SC_TOKEN_TRANSFER_remark = my_chainid
    z196_SC_TOKEN_TRANSFER_LIST_chainId = my_chainid
    z196_SC_TOKEN_TRANSFER_LIST_address = my_address
    z196_SC_TOKEN_TRANSFER_LIST_pageNumber = my_chainid
    z196_SC_TOKEN_TRANSFER_LIST_pageSize = my_chainid
    z197_SC_TRANSFER_chainId = my_chainid
    z197_SC_TRANSFER_address = my_address
    z197_SC_TRANSFER_toAddress = my_address
    z197_SC_TRANSFER_password = my_chainid
    z197_SC_TRANSFER_amount = my_chainid
    z197_SC_TRANSFER_remark = my_chainid
    z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_chainId = my_chainid
    z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_stateRoot = my_chainid
    z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_blockHeight = my_chainid
    z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_contractAddress = my_address
    z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_tx = my_chainid
    z199_SC_UPLOAD_chainId = my_chainid
    z199_SC_UPLOAD_jarFileData = my_chainid
    z200_SC_VALIDATE_CALL_chainId = my_chainid
    z200_SC_VALIDATE_CALL_sender = my_chainid
    z200_SC_VALIDATE_CALL_value = my_chainid
    z200_SC_VALIDATE_CALL_gasLimit = my_chainid
    z200_SC_VALIDATE_CALL_price = my_chainid
    z200_SC_VALIDATE_CALL_contractAddress = my_address
    z200_SC_VALIDATE_CALL_methodName = my_chainid
    z200_SC_VALIDATE_CALL_methodDesc = my_chainid
    z200_SC_VALIDATE_CALL_args = my_chainid
    z201_SC_VALIDATE_CREATE_chainId = my_chainid
    z201_SC_VALIDATE_CREATE_sender = my_chainid
    z201_SC_VALIDATE_CREATE_gasLimit = my_chainid
    z201_SC_VALIDATE_CREATE_price = my_chainid
    z201_SC_VALIDATE_CREATE_contractCode = my_chainid
    z201_SC_VALIDATE_CREATE_args = my_chainid
    z202_SC_VALIDATE_DELETE_chainId = my_chainid
    z202_SC_VALIDATE_DELETE_contractAddress = my_address
    z203_STOP_AGENTVALID_chainId = my_chainid
    z203_STOP_AGENTVALID_tx = my_chainid
    z204_TX_COMMIT_chainId = my_chainid
    z204_TX_COMMIT_txList = my_chainid
    z204_TX_COMMIT_blockHeader = my_chainid
    z205_TX_VALIDATOR_chainId = my_chainid
    z205_TX_VALIDATOR_txList = my_chainid
    z205_TX_VALIDATOR_blockHeader = my_chainid
    z206_TX_BACK_PACKABLE_TXS_chainId = my_chainid
    z206_TX_BACK_PACKABLE_TXS_txList = my_chainid
    z207_TX_BATCH_VERIFY_chainId = my_chainid
    z207_TX_BATCH_VERIFY_txList = my_chainid
    z207_TX_BATCH_VERIFY_blockHeader = my_chainid
    z207_TX_BATCH_VERIFY_preStateRoot = my_chainid
    z208_TX_BL_STATE_chainId = my_chainid
    z208_TX_BL_STATE_status = my_chainid
    z209_TX_BLOCK_HEIGHT_chainId = my_chainid
    z209_TX_BLOCK_HEIGHT_height = my_chainid
    z210_TX_CS_STATE_chainId = my_chainid
    z210_TX_CS_STATE_packaging = my_chainid
    z211_TX_GET_BLOCKTXS_chainId = my_chainid
    z211_TX_GET_BLOCKTXS_txHashList = my_chainid
    z212_TX_GET_BLOCKTXS_EXTEND_chainId = my_chainid
    z212_TX_GET_BLOCKTXS_EXTEND_txHashList = my_chainid
    z212_TX_GET_BLOCKTXS_EXTEND_allHits = my_chainid
    z213_TX_GET_CONFIRMED_TX_chainId = my_chainid
    z213_TX_GET_CONFIRMED_TX_txHash = my_chainid
    z214_TX_GET_CONFIRMED_TX_CLIENT_chainId = my_chainid
    z214_TX_GET_CONFIRMED_TX_CLIENT_txHash = my_chainid
    z215_TX_GET_NONEXISTENT_UNCONFIRMED_HASHS_chainId = my_chainid
    z215_TX_GET_NONEXISTENT_UNCONFIRMED_HASHS_txHashList = my_chainid
    z216_TX_GET_SYSTEMTYPES_chainId = my_chainid
    z217_TX_GET_TX_chainId = my_chainid
    z217_TX_GET_TX_txHash = my_chainid
    z218_TX_GET_TX_CLIENT_chainId = my_chainid
    z218_TX_GET_TX_CLIENT_txHash = my_chainid
    z219_TX_NEWTX_chainId = my_chainid
    z219_TX_NEWTX_tx = my_chainid
    z220_TX_PACKABLE_TXS_chainId = my_chainid
    z220_TX_PACKABLE_TXS_endTimestamp = my_chainid
    z220_TX_PACKABLE_TXS_maxTxDataSize = my_chainid
    z220_TX_PACKABLE_TXS_blockTime = my_chainid
    z220_TX_PACKABLE_TXS_packingAddress = my_address
    z220_TX_PACKABLE_TXS_preStateRoot = my_chainid
    z221_TX_REGISTER_chainId = my_chainid
    z221_TX_REGISTER_moduleCode = my_chainid
    z221_TX_REGISTER_list = my_chainid
    z221_TX_REGISTER_delList = my_chainid
    z222_TX_ROLLBACK_chainId = my_chainid
    z222_TX_ROLLBACK_txHashList = my_chainid
    z222_TX_ROLLBACK_blockHeader = my_chainid
    z223_TX_SAVE_chainId = my_chainid
    z223_TX_SAVE_txList = my_chainid
    z223_TX_SAVE_contractList = my_chainid
    z223_TX_SAVE_blockHeader = my_chainid
    z224_TX_VERIFY_TX_chainId = my_chainid
    z224_TX_VERIFY_TX_tx = my_chainid
    z225_UPDATE_CHAIN_ASSET_chainId = my_chainid
    z225_UPDATE_CHAIN_ASSET_assets = my_chainid
    z226_VERIFY_COINDATA_chainId = my_chainid
    z226_VERIFY_COINDATA_tx = my_chainid
    z227_VERIFY_COINDATA_BATCH_PACKAGED_chainId = my_chainid
    z227_VERIFY_COINDATA_BATCH_PACKAGED_txList = my_chainid
    z228_WITHDRAW_VALID_chainId = my_chainid
    z228_WITHDRAW_VALID_tx = my_chainid

    # the following were added after the above numbers were created. The consist of 1000 + the
    # number that it should have been approximately

    z1017_AC_GET_PRIKEY_BY_ADDRESS__chainId = my_chainid
    z1017_AC_GET_PRIKEY_BY_ADDRESS_address = my_address
    z1017_AC_GET_PRIKEY_BY_ADDRESS_password = my_password

#
# __all__ = ['FALSE', 'request_type_one_or_two', 'REMARK', 'RequestType', 'SHORT_MSG', 'TRUE', 'ZERO', 'ZLIB',
#          'compatible_proto_versions', 'compress_rate_VALUE', 'compress_type_VALUE', 'connect_method',
#          'host_req', 'my_account', 'my_address', 'my_addressprefix', 'my_addresstype', 'my_addressval',
#          'my_agentaddress', 'my_agenthash', 'my_algorithm', 'my_alias', 'my_allhits', 'my_amount', 'my_args',
#          'my_assetchainid', 'my_assetid', 'my_assetids', 'my_assetinfolist', 'my_assetname', 'my_assets',
#          'my_begin', 'my_block', 'my_blockhash', 'my_blockheader', 'my_blockheight', 'my_blocktime',
#            'my_blocktype', 'my_bytecount', 'my_chainid', 'my_chainname', 'my_circulatechainid', 'my_cmd',
#            'my_cmdregisterlistmy_command', 'my_commissionrate', 'my_contractaddress', 'my_contractbalance',
#            'my_contractcode', 'my_contractlist', 'my_contractnonce', 'my_contractsender', 'my_count', 'my_data',
#            'my_decimalplaces', 'my_dellist', 'my_deposit', 'my_download', 'my_end', 'my_endheight',
#            'my_endtimestamp', 'my_evidenceheader', 'my_excludenodes', 'my_extend', 'my_extendsdata',
#            'my_filepath', 'my_frestartifrunning', 'my_gaslimit', 'my_hash', 'my_hashlist', 'my_headerlist',
#            'my_height', 'my_initnumber', 'my_inputs', 'my_intcount', 'my_interval', 'my_isconfirmed',
#            'my_iscross', 'my_iscrossgroup', 'my_jarfiledata', 'my_joinagenthash', 'my_keystore', 'my_keyword',
#            'my_list', 'my_listfrom', 'my_listto', 'my_lmaxcpus', 'my_lmodulename', 'my_lmoduleversion',
#            'my_longcount', 'my_magicnumber', 'my_maxin', 'my_maxout', 'my_maxsignaturecount',
#            'my_maxtxdatasize', 'my_messagebody', 'my_methoddesc', 'my_methodname', 'my_minavailablecount',
#            'my_minavailablenodenum', 'my_minsigns', 'my_modulecode', 'my_newpassword', 'my_nodeid', 'my_nodes',
#            'my_outputs', 'my_overwrite', 'my_packaging', 'my_packingaddress', 'my_pagenumber', 'my_pagesize',
#            'my_password', 'my_percent', 'my_prefixlist', 'my_prestateroot', 'my_price', 'my_prikey',
#            'my_protocolcmds', 'my_protocolversion', 'my_pubkey', 'my_pubkeys', 'my_registertime', 'my_remark',
#            'my_rewardaddress', 'my_role', 'my_round', 'my_seedips', 'my_sender', 'my_shortcount', 'my_sig',
#            'my_signaddress', 'my_signaturebftratio', 'my_signpassword', 'my_size', 'my_startheight',
#            'my_startpage', 'my_state', 'my_stateroot', 'my_status', 'my_symbol', 'my_toaddress', 'my_tx',
#            'my_txhash', 'my_txhashlist', 'my_txlist', 'my_type', 'my_usable', 'my_value', 'my_verifierlist',
#            'port_req', 'proto_ver', 'request_int', 'res_max_size', 'sub_event_ct', 'sub_period_int',
#            'sub_range', 'subscriptionRange', 'websock_url', 'z100_CS_UPDATE_AGENT_CONSENSUS_STATUS_chainId',
#            'z101_CS_UPDATE_AGENT_STATUS_chainId', 'z101_CS_UPDATE_AGENT_STATUS_status',
#            'z102_CS_VALIDBLOCK_block', 'z102_CS_VALIDBLOCK_chainId', 'z102_CS_VALIDBLOCK_download',
#            'z103_CS_WITHDRAW_address', 'z103_CS_WITHDRAW_chainId', 'z103_CS_WITHDRAW_password',
#            'z103_CS_WITHDRAW_txHash', 'z104_DEPOSIT_VALID_chainId', 'z104_DEPOSIT_VALID_tx',
#            'z105_GET_ASSETS_BY_ID_assetIds', 'z105_GET_ASSETS_BY_ID_chainId', 'z106_GET_BALANCE_address',
#            'z106_GET_BALANCE_assetChainId', 'z106_GET_BALANCE_assetId', 'z106_GET_BALANCE_chainId',
#            'z107_GET_BALANCE_NONCE_address', 'z107_GET_BALANCE_NONCE_assetChainId',
#            'z107_GET_BALANCE_NONCE_assetId', 'z107_GET_BALANCE_NONCE_chainId',
#            'z107_GET_BALANCE_NONCE_isConfirmed', 'z108_GET_BLOCK_BY_HASH_chainId',
#            'z108_GET_BLOCK_BY_HASH_hash', 'z109_GET_BLOCK_BY_HEIGHT_chainId', 'z109_GET_BLOCK_BY_HEIGHT_height',
#            'z10_AC_GET_ADDRESS_LIST_chainId', 'z10_AC_GET_ADDRESS_LIST_pageNumber',
#            'z10_AC_GET_ADDRESS_LIST_pageSize', 'z110_GET_BLOCKHEADER_BY_HASH_chainId',
#            'z110_GET_BLOCKHEADER_BY_HASH_hash', 'z111_GET_BLOCKHEADER_BY_HEIGHT_chainId',
#            'z111_GET_BLOCKHEADER_BY_HEIGHT_height', 'z112_GET_BLOCKHEADER_PO_BY_HASH_chainId',
#            'z112_GET_BLOCKHEADER_PO_BY_HASH_hash', 'z113_GET_BLOCKHEADER_POBY_HEIGHT_chainId',
#            'z113_GET_BLOCKHEADER_POBY_HEIGHT_height', 'z114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_begin',
#            'z114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_chainId', 'z114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_end',
#            'z115_GET_BLOCKHEADERS_FOR_PROTOCOL_chainId', 'z115_GET_BLOCKHEADERS_FOR_PROTOCOL_interval',
#            'z116_GET_BYZANTINE_COUNT_chainId', 'z117_GET_CIRCULAT_chainId', 'z117_GET_CIRCULAT_messageBody',
#            'z117_GET_CIRCULAT_nodeId', 'z119_GET_CROSSTX_STATE_chainId', 'z119_GET_CROSSTX_STATE_txHash',
#            'z11_AC_GET_ADDRESS_PREFIX_BY_CHAINID_chainId', 'z120_GET_CTX_chainId', 'z120_GET_CTX_messageBody',
#            'z120_GET_CTX_nodeId', 'z121_GET_CTX_STATE_chainId', 'z121_GET_CTX_STATE_messageBody',
#            'z121_GET_CTX_STATE_nodeId', 'z122_GET_FRIEND_CHAIN_CIRCULATE_assetIds',
#            'z122_GET_FRIEND_CHAIN_CIRCULATE_chainId', 'z123_GET_LATEST_BLOCKHEADERS_chainId',
#            'z123_GET_LATEST_BLOCKHEADERS_size', 'z124_GET_LATEST_ROUND_BLOCKHEADERS_chainId',
#            'z124_GET_LATEST_ROUND_BLOCKHEADERS_round', 'z125_GET_NONCE_address', 'z125_GET_NONCE_assetChainId',
#            'z125_GET_NONCE_assetId', 'z125_GET_NONCE_chainId', 'z125_GET_NONCE_isConfirmed',
#            'z126_GET_OTHERCTX_chainId', 'z126_GET_OTHERCTX_messageBody', 'z126_GET_OTHERCTX_nodeId',
#            'z128_GET_ROUND_BLOCKHEADERS_chainId', 'z128_GET_ROUND_BLOCKHEADERS_height',
#            'z128_GET_ROUND_BLOCKHEADERS_round', 'z129_GET_STATUS_chainId', 'z12_AC_GET_ALIASBY_ADDRESS_address',
#            'z12_AC_GET_ALIASBY_ADDRESS_chainId', 'z130_GET_VERSION_chainId', 'z131_INFO_chainId',
#            'z132_LATEST_BLOCK_chainId', 'z133_LATEST_BLOCKHEADER_chainId', 'z134_LATEST_BLOCKHEADER_PO_chainId',
#            'z135_LATEST_HEIGHT_chainId', 'z137_MSG_PROCESS_chainId', 'z137_MSG_PROCESS_cmd',
#            'z137_MSG_PROCESS_messageBody', 'z137_MSG_PROCESS_nodeId', 'z138_NEW_BLOCK_HEIGHT_chainId',
#            'z138_NEW_BLOCK_HEIGHT_height', 'z139_NW_ACTIVE_CROSS_chainId', 'z139_NW_ACTIVE_CROSS_maxIn',
#            'z139_NW_ACTIVE_CROSS_maxOut', 'z139_NW_ACTIVE_CROSS_seedIps', 'z140_NW_ADD_NODES_chainId',
#            'z140_NW_ADD_NODES_isCross', 'z140_NW_ADD_NODES_nodes', 'z141_NW_BROADCAST_chainId',
#            'z141_NW_BROADCAST_command', 'z141_NW_BROADCAST_excludeNodes', 'z141_NW_BROADCAST_isCross',
#            'z141_NW_BROADCAST_messageBody', 'z141_NW_BROADCAST_percent', 'z142_NW_CREATE_NODEGROUP_chainId',
#            'z142_NW_CREATE_NODEGROUP_isCrossGroup', 'z142_NW_CREATE_NODEGROUP_magicNumber',
#            'z142_NW_CREATE_NODEGROUP_maxIn', 'z142_NW_CREATE_NODEGROUP_maxOut',
#            'z142_NW_CREATE_NODEGROUP_minAvailableCount', 'z143_NW_DEL_NODES_chainId', 'z143_NW_DEL_NODES_nodes',
#            'z144_NW_GET_CHAIN_CONNECT_AMOUNT_chainId', 'z144_NW_GET_CHAIN_CONNECT_AMOUNT_isCross',
#            'z145_NW_GET_GROUP_BY_CHAINID_chainId', 'z146_NW_GET_GROUPS_pageSize',
#            'z146_NW_GET_GROUPS_startPage', 'z147_NW_GET_NODES_chainId', 'z147_NW_GET_NODES_isCross',
#            'z147_NW_GET_NODES_pageSize', 'z147_NW_GET_NODES_startPage', 'z147_NW_GET_NODES_state',
#            'z149_NW_INFO_chainId', 'z14_AC_GET_ALL_PRIKEY_chainId', 'z14_AC_GET_ALL_PRIKEY_password',
#            'z150_NW_NODES_chainId', 'z151_NW_PROTOCOL_REGISTER_protocolCmds', 'z151_NW_PROTOCOL_REGISTER_role',
#            'z152_NW_RECONNECT_chainId', 'z153_NW_SEND_PEERS_MSG_chainId', 'z153_NW_SEND_PEERS_MSG_command',
#            'z153_NW_SEND_PEERS_MSG_messageBody', 'z153_NW_SEND_PEERS_MSG_nodes',
#            'z154_NW_UPDATE_NODE_INFO_blockHash', 'z154_NW_UPDATE_NODE_INFO_blockHeight',
#            'z154_NW_UPDATE_NODE_INFO_chainId', 'z154_NW_UPDATE_NODE_INFO_nodeId',
#            'z155_PARAM_TEST_CMD_byteCount', 'z155_PARAM_TEST_CMD_intCount', 'z155_PARAM_TEST_CMD_longCount',
#            'z155_PARAM_TEST_CMD_shortCount', 'z156_PROTOCOL_VERSION_CHANGE_chainId',
#            'z156_PROTOCOL_VERSION_CHANGE_protocolVersion', 'z157_RECEIVE_PACKING_BLOCK_block',
#            'z157_RECEIVE_PACKING_BLOCK_chainId', 'z158_RECV_CIRCULAT_chainId', 'z158_RECV_CIRCULAT_messageBody',
#            'z158_RECV_CIRCULAT_nodeId', 'z159_RECV_CTX_chainId', 'z159_RECV_CTX_messageBody',
#            'z159_RECV_CTX_nodeId', 'z15_AC_GET_ENCRYPTED_ADDRESS_LIST_chainId', 'z160_RECV_CTX_HASH_chainId',
#            'z160_RECV_CTX_HASH_messageBody', 'z160_RECV_CTX_HASH_nodeId', 'z161_RECV_CTX_SIGN_chainId',
#            'z161_RECV_CTX_SIGN_messageBody', 'z161_RECV_CTX_SIGN_nodeId', 'z162_RECV_CTX_STATE_chainId',
#            'z162_RECV_CTX_STATE_messageBody', 'z162_RECV_CTX_STATE_nodeId', 'z163_RECV_OTHER_CTX_chainId',
#            'z163_RECV_OTHER_CTX_messageBody', 'z163_RECV_OTHER_CTX_nodeId', 'z164_RECV_REGCHAIN_chainId',
#            'z164_RECV_REGCHAIN_messageBody', 'z164_RECV_REGCHAIN_nodeId', 'z166_REGISTER_PROTOCOL_chainId',
#            'z166_REGISTER_PROTOCOL_list', 'z166_REGISTER_PROTOCOL_moduleCode',
#            'z167_ROLLBACK_BLOCK_TXS_blockHeight', 'z167_ROLLBACK_BLOCK_TXS_chainId',
#            'z167_ROLLBACK_BLOCK_TXS_txList', 'z168_ROLLBACK_UNCONFIRM_TX_chainId',
#            'z168_ROLLBACK_UNCONFIRM_TX_tx', 'z169_ROLLBACK_BLOCK_blockHeader', 'z169_ROLLBACK_BLOCK_chainId',
#            'z16_AC_GET_MULTI_SIGN_ACCOUNT_address', 'z16_AC_GET_MULTI_SIGN_ACCOUNT_chainId',
#            'z170_ROLLBACK_TX_VALIDATE_STATUS_chainId', 'z170_ROLLBACK_TX_VALIDATE_STATUS_tx',
#            'z171_SAVE_BLOCK_blockHeader', 'z171_SAVE_BLOCK_chainId', 'z172_SC_BATCH_BEFORE_END_blockHeight',
#            'z172_SC_BATCH_BEFORE_END_blockType', 'z172_SC_BATCH_BEFORE_END_chainId',
#            'z173_SC_BATCH_BEGIN_blockHeight', 'z173_SC_BATCH_BEGIN_blockTime', 'z173_SC_BATCH_BEGIN_blockType',
#            'z173_SC_BATCH_BEGIN_chainId', 'z173_SC_BATCH_BEGIN_packingAddress',
#            'z173_SC_BATCH_BEGIN_preStateRoot', 'z174_SC_BATCH_END_blockHeight', 'z174_SC_BATCH_END_chainId',
#            'z175_SC_CALL_args', 'z175_SC_CALL_chainId', 'z175_SC_CALL_contractAddress', 'z175_SC_CALL_gasLimit',
#            'z175_SC_CALL_methodDesc', 'z175_SC_CALL_methodName', 'z175_SC_CALL_password', 'z175_SC_CALL_price',
#            'z175_SC_CALL_remark', 'z175_SC_CALL_sender', 'z175_SC_CALL_value', 'z176_SC_CALL_VALIDATOR_chainId',
#            'z176_SC_CALL_VALIDATOR_tx', 'z177_SC_CONSTRUCTOR_chainId', 'z177_SC_CONSTRUCTOR_contractCode',
#            'z178_SC_CONTRACT_INFO_chainId', 'z178_SC_CONTRACT_INFO_contractAddress',
#            'z179_SC_CONTRACT_OFFLINE_TX_HASH_LIST_blockHash', 'z179_SC_CONTRACT_OFFLINE_TX_HASH_LIST_chainId',
#            'z17_AC_GET_PUBKEY_address', 'z17_AC_GET_PUBKEY_chainId', 'z17_AC_GET_PUBKEY_password',
#            'z180_SC_CONTRACT_RESULT_chainId', 'z180_SC_CONTRACT_RESULT_hash',
#            'z181_SC_CONTRACT_RESULT_LIST_chainId', 'z181_SC_CONTRACT_RESULT_LIST_hashList',
#            'z182_SC_CONTRACT_TX_chainId', 'z182_SC_CONTRACT_TX_hash', 'z183_SC_CREATE_alias',
#            'z183_SC_CREATE_args', 'z183_SC_CREATE_chainId', 'z183_SC_CREATE_contractCode',
#            'z183_SC_CREATE_gasLimit', 'z183_SC_CREATE_password', 'z183_SC_CREATE_price',
#            'z183_SC_CREATE_remark', 'z183_SC_CREATE_sender', 'z184_SC_CREATE_VALIDATOR_chainId',
#            'z184_SC_CREATE_VALIDATOR_tx', 'z185_SC_DELETE_chainId', 'z185_SC_DELETE_contractAddress',
#            'z185_SC_DELETE_password', 'z185_SC_DELETE_remark', 'z185_SC_DELETE_sender',
#            'z186_SC_DELETE_VALIDATOR_chainId', 'z186_SC_DELETE_VALIDATOR_tx', 'z187_SC_IMPUTED_CALL_GAS_args',
#            'z187_SC_IMPUTED_CALL_GAS_chainId', 'z187_SC_IMPUTED_CALL_GAS_contractAddress',
#            'z187_SC_IMPUTED_CALL_GAS_methodDesc', 'z187_SC_IMPUTED_CALL_GAS_methodName',
#            'z187_SC_IMPUTED_CALL_GAS_sender', 'z187_SC_IMPUTED_CALL_GAS_value',
#            'z188_SC_IMPUTED_CREATE_GAS_args', 'z188_SC_IMPUTED_CREATE_GAS_chainId',
#            'z188_SC_IMPUTED_CREATE_GAS_contractCode', 'z188_SC_IMPUTED_CREATE_GAS_sender',
#            'z189_SC_INITIAL_ACCOUNT_TOKEN_address', 'z189_SC_INITIAL_ACCOUNT_TOKEN_chainId',
#            'z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_chainId', 'z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_keyStore',
#            'z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_overwrite', 'z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_password',
#            'z190_SC_INVOKE_CONTRACT_blockType', 'z190_SC_INVOKE_CONTRACT_chainId', 'z190_SC_INVOKE_CONTRACT_tx',
#            'z191_SC_INVOKE_VIEW_args', 'z191_SC_INVOKE_VIEW_chainId', 'z191_SC_INVOKE_VIEW_contractAddress',
#            'z191_SC_INVOKE_VIEW_methodDesc', 'z191_SC_INVOKE_VIEW_methodName',
#            'z192_SC_PACKAGE_BATCH_END_blockHeight', 'z192_SC_PACKAGE_BATCH_END_chainId',
#            'z193_SC_TOKEN_ASSETS_LIST_address', 'z193_SC_TOKEN_ASSETS_LIST_chainId',
#            'z193_SC_TOKEN_ASSETS_LIST_pageNumber', 'z193_SC_TOKEN_ASSETS_LIST_pageSize',
#            'z194_SC_TOKEN_BALANCE_address', 'z194_SC_TOKEN_BALANCE_chainId',
#            'z194_SC_TOKEN_BALANCE_contractAddress', 'z195_SC_TOKEN_TRANSFER_address',
#            'z195_SC_TOKEN_TRANSFER_amount', 'z195_SC_TOKEN_TRANSFER_chainId',
#            'z195_SC_TOKEN_TRANSFER_contractAddress', 'z195_SC_TOKEN_TRANSFER_password',
#            'z195_SC_TOKEN_TRANSFER_remark', 'z195_SC_TOKEN_TRANSFER_toAddress',
#            'z196_SC_TOKEN_TRANSFER_LIST_address', 'z196_SC_TOKEN_TRANSFER_LIST_chainId',
#            'z196_SC_TOKEN_TRANSFER_LIST_pageNumber', 'z196_SC_TOKEN_TRANSFER_LIST_pageSize',
#            'z197_SC_TRANSFER_address', 'z197_SC_TRANSFER_amount', 'z197_SC_TRANSFER_chainId',
#            'z197_SC_TRANSFER_password', 'z197_SC_TRANSFER_remark', 'z197_SC_TRANSFER_toAddress',
#            'z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_blockHeight',
#            'z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_chainId',
#            'z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_contractAddress',
#            'z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_stateRoot',
#            'z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_tx', 'z199_SC_UPLOAD_chainId',
#            'z199_SC_UPLOAD_jarFileData', 'z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_chainId',
#            'z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_overwrite', 'z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_password',
#            'z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_priKey', 'z1_AC_CREATE_ACCOUNT_chainId',
#            'z1_AC_CREATE_ACCOUNT_count', 'z1_AC_CREATE_ACCOUNT_password', 'z200_SC_VALIDATE_CALL_args',
#            'z200_SC_VALIDATE_CALL_chainId', 'z200_SC_VALIDATE_CALL_contractAddress',
#            'z200_SC_VALIDATE_CALL_gasLimit', 'z200_SC_VALIDATE_CALL_methodDesc',
#            'z200_SC_VALIDATE_CALL_methodName', 'z200_SC_VALIDATE_CALL_price', 'z200_SC_VALIDATE_CALL_sender',
#            'z200_SC_VALIDATE_CALL_value', 'z201_SC_VALIDATE_CREATE_args', 'z201_SC_VALIDATE_CREATE_chainId',
#            'z201_SC_VALIDATE_CREATE_contractCode', 'z201_SC_VALIDATE_CREATE_gasLimit',
#            'z201_SC_VALIDATE_CREATE_price', 'z201_SC_VALIDATE_CREATE_sender', 'z202_SC_VALIDATE_DELETE_chainId',
#            'z202_SC_VALIDATE_DELETE_contractAddress', 'z203_STOP_AGENTVALID_chainId', 'z203_STOP_AGENTVALID_tx',
#            'z204_TX_COMMIT_blockHeader', 'z204_TX_COMMIT_chainId', 'z204_TX_COMMIT_txList',
#            'z205_TX_VALIDATOR_blockHeader', 'z205_TX_VALIDATOR_chainId', 'z205_TX_VALIDATOR_txList',
#            'z206_TX_BACK_PACKABLE_TXS_chainId', 'z206_TX_BACK_PACKABLE_TXS_txList',
#            'z207_TX_BATCH_VERIFY_blockHeader', 'z207_TX_BATCH_VERIFY_chainId',
#            'z207_TX_BATCH_VERIFY_preStateRoot', 'z207_TX_BATCH_VERIFY_txList', 'z208_TX_BL_STATE_chainId',
#            'z208_TX_BL_STATE_status', 'z209_TX_BLOCK_HEIGHT_chainId', 'z209_TX_BLOCK_HEIGHT_height',
#            'z20_AC_IS_ALIAS_USABLE_alias', 'z20_AC_IS_ALIAS_USABLE_chainId', 'z210_TX_CS_STATE_chainId',
#            'z210_TX_CS_STATE_packaging', 'z211_TX_GET_BLOCKTXS_chainId', 'z211_TX_GET_BLOCKTXS_txHashList',
#            'z212_TX_GET_BLOCKTXS_EXTEND_allHits', 'z212_TX_GET_BLOCKTXS_EXTEND_chainId',
#            'z212_TX_GET_BLOCKTXS_EXTEND_txHashList', 'z213_TX_GET_CONFIRMED_TX_chainId',
#            'z213_TX_GET_CONFIRMED_TX_txHash', 'z214_TX_GET_CONFIRMED_TX_CLIENT_chainId',
#            'z214_TX_GET_CONFIRMED_TX_CLIENT_txHash', 'z215_TX_GET_NONEXISTENT_UNCONFIRMED_HASHS_chainId',
#            'z215_TX_GET_NONEXISTENT_UNCONFIRMED_HASHS_txHashList', 'z216_TX_GET_SYSTEMTYPES_chainId',
#            'z217_TX_GET_TX_chainId', 'z217_TX_GET_TX_txHash', 'z218_TX_GET_TX_CLIENT_chainId',
#            'z218_TX_GET_TX_CLIENT_txHash', 'z219_TX_NEWTX_chainId', 'z219_TX_NEWTX_tx',
#            'z21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_address', 'z21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_chainId',
#            'z21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_pubKey', 'z220_TX_PACKABLE_TXS_blockTime',
#            'z220_TX_PACKABLE_TXS_chainId', 'z220_TX_PACKABLE_TXS_endTimestamp',
#            'z220_TX_PACKABLE_TXS_maxTxDataSize', 'z220_TX_PACKABLE_TXS_packingAddress',
#            'z220_TX_PACKABLE_TXS_preStateRoot', 'z221_TX_REGISTER_chainId', 'z221_TX_REGISTER_delList',
#            'z221_TX_REGISTER_list', 'z221_TX_REGISTER_moduleCode', 'z222_TX_ROLLBACK_blockHeader',
#            'z222_TX_ROLLBACK_chainId', 'z222_TX_ROLLBACK_txHashList', 'z223_TX_SAVE_blockHeader',
#            'z223_TX_SAVE_chainId', 'z223_TX_SAVE_contractList', 'z223_TX_SAVE_txList',
#            'z224_TX_VERIFY_TX_chainId', 'z224_TX_VERIFY_TX_tx', 'z225_UPDATE_CHAIN_ASSET_assets',
#            'z225_UPDATE_CHAIN_ASSET_chainId', 'z226_VERIFY_COINDATA_chainId', 'z226_VERIFY_COINDATA_tx',
#            'z227_VERIFY_COINDATA_BATCH_PACKAGED_chainId', 'z227_VERIFY_COINDATA_BATCH_PACKAGED_txList',
#            'z228_WITHDRAW_VALID_chainId', 'z228_WITHDRAW_VALID_tx', 'z22_AC_REMOVE_ACCOUNT_address',
#            'z22_AC_REMOVE_ACCOUNT_chainId', 'z22_AC_REMOVE_ACCOUNT_password',
#            'z23_AC_REMOVE_MULTISIGN_ACCOUNT_address', 'z23_AC_REMOVE_MULTISIGN_ACCOUNT_chainId',
#            'z24_AC_SET_ALIAS_address', 'z24_AC_SET_ALIAS_alias', 'z24_AC_SET_ALIAS_chainId',
#            'z24_AC_SET_ALIAS_password', 'z25_AC_SET_MULTISIGN_ALIAS_address',
#            'z25_AC_SET_MULTISIGN_ALIAS_alias', 'z25_AC_SET_MULTISIGN_ALIAS_chainId',
#            'z25_AC_SET_MULTISIGN_ALIAS_signAddress', 'z25_AC_SET_MULTISIGN_ALIAS_signPassword',
#            'z26_AC_SET_REMARK_address', 'z26_AC_SET_REMARK_chainId', 'z26_AC_SET_REMARK_remark',
#            'z27_AC_SIGN_BLOCKDIGEST_address', 'z27_AC_SIGN_BLOCKDIGEST_chainId', 'z27_AC_SIGN_BLOCKDIGEST_data',
#            'z27_AC_SIGN_BLOCKDIGEST_password', 'z28_AC_SIGN_DIGEST_address', 'z28_AC_SIGN_DIGEST_chainId',
#            'z28_AC_SIGN_DIGEST_data', 'z28_AC_SIGN_DIGEST_password',
#            'z29_AC_SIGN_MULTISIGN_TRANSACTION_chainId', 'z29_AC_SIGN_MULTISIGN_TRANSACTION_signAddress',
#            'z29_AC_SIGN_MULTISIGN_TRANSACTION_signPassword', 'z29_AC_SIGN_MULTISIGN_TRANSACTION_tx',
#            'z2_AC_CREATE_CONTRACT_ACCOUNT_chainId', 'z30_AC_TRANSFER_chainId', 'z30_AC_TRANSFER_inputs',
#            'z30_AC_TRANSFER_outputs', 'z30_AC_TRANSFER_remark',
#            'z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_address', 'z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_chainId',
#            'z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_newPassword',
#            'z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_password', 'z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_priKey',
#            'z32_AC_UPDATE_PASSWORD_address', 'z32_AC_UPDATE_PASSWORD_chainId',
#            'z32_AC_UPDATE_PASSWORD_newPassword', 'z32_AC_UPDATE_PASSWORD_password',
#            'z33_AC_VALIDATION_PASSWORD_address', 'z33_AC_VALIDATION_PASSWORD_chainId',
#            'z33_AC_VALIDATION_PASSWORD_password', 'z34_AC_VERIFY_SIGN_DATA_data',
#            'z34_AC_VERIFY_SIGN_DATA_pubKey', 'z34_AC_VERIFY_SIGN_DATA_sig', 'z35_BATCH_VALIDATE_BEGIN_chainId',
#            'z36_BLOCK_VALIDATE_chainId', 'z36_BLOCK_VALIDATE_txList', 'z38_CANCEL_CROSSCHAIN_assetId',
#            'z38_CANCEL_CROSSCHAIN_chainId', 'z39_CHECK_BLOCK_VERSION_chainId',
#            'z39_CHECK_BLOCK_VERSION_extendsData', 'z3_AC_CREATE_MULTI_SIGN_ACCOUNT_chainId',
#            'z3_AC_CREATE_MULTI_SIGN_ACCOUNT_minSigns', 'z3_AC_CREATE_MULTI_SIGN_ACCOUNT_pubKeys',
#            'z40_CM_ASSET_assetId', 'z40_CM_ASSET_chainId', 'z41_CM_ASSET_CIRCULATE_COMMIT_blockHeader',
#            'z41_CM_ASSET_CIRCULATE_COMMIT_chainId', 'z41_CM_ASSET_CIRCULATE_COMMIT_txList',
#            'z42_CM_ASSET_CIRCULATE_ROLLBACK_blockHeader', 'z42_CM_ASSET_CIRCULATE_ROLLBACK_chainId',
#            'z42_CM_ASSET_CIRCULATE_ROLLBACK_txList', 'z43_CM_ASSET_CIRCULATE_VALIDATOR_chainId',
#            'z43_CM_ASSET_CIRCULATE_VALIDATOR_tx', 'z44_CM_ASSET_DISABLE_address',
#            'z44_CM_ASSET_DISABLE_assetId', 'z44_CM_ASSET_DISABLE_chainId', 'z44_CM_ASSET_DISABLE_password',
#            'z45_CM_ASSET_REG_address', 'z45_CM_ASSET_REG_assetId', 'z45_CM_ASSET_REG_assetName',
#            'z45_CM_ASSET_REG_chainId', 'z45_CM_ASSET_REG_decimalPlaces', 'z45_CM_ASSET_REG_initNumber',
#            'z45_CM_ASSET_REG_password', 'z45_CM_ASSET_REG_symbol', 'z46_CM_CHAIN_chainId',
#            'z47_CM_CHAIN_ACTIVE_address', 'z47_CM_CHAIN_ACTIVE_addressPrefix',
#            'z47_CM_CHAIN_ACTIVE_addressType', 'z47_CM_CHAIN_ACTIVE_assetId', 'z47_CM_CHAIN_ACTIVE_assetName',
#            'z47_CM_CHAIN_ACTIVE_chainId', 'z47_CM_CHAIN_ACTIVE_chainName', 'z47_CM_CHAIN_ACTIVE_decimalPlaces',
#            'z47_CM_CHAIN_ACTIVE_initNumber', 'z47_CM_CHAIN_ACTIVE_magicNumber',
#            'z47_CM_CHAIN_ACTIVE_maxSignatureCount', 'z47_CM_CHAIN_ACTIVE_minAvailableNodeNum',
#            'z47_CM_CHAIN_ACTIVE_password', 'z47_CM_CHAIN_ACTIVE_signatureBFTRatio',
#            'z47_CM_CHAIN_ACTIVE_symbol', 'z47_CM_CHAIN_ACTIVE_verifierList', 'z48_CM_CHAIN_REG_address',
#            'z48_CM_CHAIN_REG_addressPrefix', 'z48_CM_CHAIN_REG_addressType', 'z48_CM_CHAIN_REG_assetId',
#            'z48_CM_CHAIN_REG_assetName', 'z48_CM_CHAIN_REG_chainId', 'z48_CM_CHAIN_REG_chainName',
#            'z48_CM_CHAIN_REG_decimalPlaces', 'z48_CM_CHAIN_REG_initNumber', 'z48_CM_CHAIN_REG_magicNumber',
#            'z48_CM_CHAIN_REG_maxSignatureCount', 'z48_CM_CHAIN_REG_minAvailableNodeNum',
#            'z48_CM_CHAIN_REG_password', 'z48_CM_CHAIN_REG_signatureBFTRatio', 'z48_CM_CHAIN_REG_symbol',
#            'z48_CM_CHAIN_REG_verifierList', 'z49_CM_GET_CHAIN_ASSET_assetChainId',
#            'z49_CM_GET_CHAIN_ASSET_assetId', 'z49_CM_GET_CHAIN_ASSET_chainId',
#            'z4_AC_CREATE_MULTI_SIGN_TRANSFER_chainId', 'z4_AC_CREATE_MULTI_SIGN_TRANSFER_inputs',
#            'z4_AC_CREATE_MULTI_SIGN_TRANSFER_outputs', 'z4_AC_CREATE_MULTI_SIGN_TRANSFER_remark',
#            'z4_AC_CREATE_MULTI_SIGN_TRANSFER_signAddress', 'z4_AC_CREATE_MULTI_SIGN_TRANSFER_signPassword',
#            'z50_CM_GET_CIRCULATE_CHAIN_ASSET_assetChainId', 'z50_CM_GET_CIRCULATE_CHAIN_ASSET_assetId',
#            'z50_CM_GET_CIRCULATE_CHAIN_ASSET_circulateChainId', 'z51_COMMIT_BATCH_UNCONFIRMED_TXS_chainId',
#            'z51_COMMIT_BATCH_UNCONFIRMED_TXS_txList', 'z52_COMMIT_BLOCKTXS_blockHeight',
#            'z52_COMMIT_BLOCKTXS_chainId', 'z52_COMMIT_BLOCKTXS_txList', 'z53_COMMIT_UNCONFIRMEDTX_chainId',
#            'z53_COMMIT_UNCONFIRMEDTX_tx', 'z55_CREATE_AGENT_VALID_chainId', 'z55_CREATE_AGENT_VALID_tx',
#            'z56_CREATE_CROSSTX_chainId', 'z56_CREATE_CROSSTX_listFrom', 'z56_CREATE_CROSSTX_listTo',
#            'z56_CREATE_CROSSTX_remark', 'z57_CROSSCHAIN_REGISTER_CHANGE_chainId',
#            'z58_CS_ADD_BLOCK_blockHeader', 'z58_CS_ADD_BLOCK_chainId', 'z59_CS_ADD_EVIDENCE_RECORD_blockHeader',
#            'z59_CS_ADD_EVIDENCE_RECORD_chainId', 'z59_CS_ADD_EVIDENCE_RECORD_evidenceHeader',
#            'z5_AC_CREATE_OFFLINE_ACCOUNT_chainId', 'z5_AC_CREATE_OFFLINE_ACCOUNT_count',
#            'z5_AC_CREATE_OFFLINE_ACCOUNT_password', 'z60_CS_CHAIN_ROLLBACK_chainId',
#            'z60_CS_CHAIN_ROLLBACK_height', 'z61_CS_CONTRACT_DEPOSIT_agentHash',
#            'z61_CS_CONTRACT_DEPOSIT_blockTime', 'z61_CS_CONTRACT_DEPOSIT_chainId',
#            'z61_CS_CONTRACT_DEPOSIT_contractAddress', 'z61_CS_CONTRACT_DEPOSIT_contractBalance',
#            'z61_CS_CONTRACT_DEPOSIT_contractNonce', 'z61_CS_CONTRACT_DEPOSIT_contractSender',
#            'z61_CS_CONTRACT_DEPOSIT_deposit', 'z62_CS_CONTRACT_WITHDRAW_blockTime',
#            'z62_CS_CONTRACT_WITHDRAW_chainId', 'z62_CS_CONTRACT_WITHDRAW_contractAddress',
#            'z62_CS_CONTRACT_WITHDRAW_contractBalance', 'z62_CS_CONTRACT_WITHDRAW_contractNonce',
#            'z62_CS_CONTRACT_WITHDRAW_contractSender', 'z62_CS_CONTRACT_WITHDRAW_joinAgentHash',
#            'z63_CS_CREATE_AGENT_agentAddress', 'z63_CS_CREATE_AGENT_chainId',
#            'z63_CS_CREATE_AGENT_commissionRate', 'z63_CS_CREATE_AGENT_deposit',
#            'z63_CS_CREATE_AGENT_packingAddress', 'z63_CS_CREATE_AGENT_password',
#            'z63_CS_CREATE_AGENT_rewardAddress', 'z64_CS_CREATE_CONTRACT_AGENT_blockTime',
#            'z64_CS_CREATE_CONTRACT_AGENT_chainId', 'z64_CS_CREATE_CONTRACT_AGENT_commissionRate',
#            'z64_CS_CREATE_CONTRACT_AGENT_contractAddress', 'z64_CS_CREATE_CONTRACT_AGENT_contractBalance',
#            'z64_CS_CREATE_CONTRACT_AGENT_contractNonce', 'z64_CS_CREATE_CONTRACT_AGENT_contractSender',
#            'z64_CS_CREATE_CONTRACT_AGENT_deposit', 'z64_CS_CREATE_CONTRACT_AGENT_packingAddress',
#            'z65_CS_CREATE_MULTI_AGENT_agentAddress', 'z65_CS_CREATE_MULTI_AGENT_chainId',
#            'z65_CS_CREATE_MULTI_AGENT_commissionRate', 'z65_CS_CREATE_MULTI_AGENT_deposit',
#            'z65_CS_CREATE_MULTI_AGENT_packingAddress', 'z65_CS_CREATE_MULTI_AGENT_password',
#            'z65_CS_CREATE_MULTI_AGENT_rewardAddress', 'z65_CS_CREATE_MULTI_AGENT_signAddress',
#            'z66_CS_DEPOSIT_TOAGENT_address', 'z66_CS_DEPOSIT_TOAGENT_agentHash',
#            'z66_CS_DEPOSIT_TOAGENT_chainId', 'z66_CS_DEPOSIT_TOAGENT_deposit',
#            'z66_CS_DEPOSIT_TOAGENT_password', 'z67_CS_DOUBLE_SPEND_RECORD_block',
#            'z67_CS_DOUBLE_SPEND_RECORD_chainId', 'z67_CS_DOUBLE_SPEND_RECORD_tx',
#            'z68_CS_GET_AGENT_ADDRESS_LIST_chainId', 'z69_CS_GET_AGENT_CHANGE_INFO_chainId',
#            'z6_AC_EXPORT_ACCOUNT_KEYSTORE_address', 'z6_AC_EXPORT_ACCOUNT_KEYSTORE_chainId',
#            'z6_AC_EXPORT_ACCOUNT_KEYSTORE_filePath', 'z6_AC_EXPORT_ACCOUNT_KEYSTORE_password',
#            'z70_CS_GET_AGENT_INFO_agentHash', 'z70_CS_GET_AGENT_INFO_chainId', 'z71_CS_GET_AGENT_LIST_chainId',
#            'z71_CS_GET_AGENT_LIST_keyWord', 'z71_CS_GET_AGENT_LIST_pageNumber',
#            'z71_CS_GET_AGENT_LIST_pageSize', 'z72_CS_GET_AGENT_STATUS_agentHash',
#            'z72_CS_GET_AGENT_STATUS_chainId', 'z73_CS_GET_CONSENSUS_CONFIG_chainId',
#            'z74_CS_GET_CONTRACT_AGENT_INFO_agentHash', 'z74_CS_GET_CONTRACT_AGENT_INFO_chainId',
#            'z74_CS_GET_CONTRACT_AGENT_INFO_contractAddress', 'z74_CS_GET_CONTRACT_AGENT_INFO_contractSender',
#            'z75_CS_GET_CONTRACT_DEPOSIT_INFO_chainId', 'z75_CS_GET_CONTRACT_DEPOSIT_INFO_contractAddress',
#            'z75_CS_GET_CONTRACT_DEPOSIT_INFO_contractSender', 'z75_CS_GET_CONTRACT_DEPOSIT_INFO_joinAgentHash',
#            'z76_CS_GET_DEPOSIT_LIST_address', 'z76_CS_GET_DEPOSIT_LIST_agentHash',
#            'z76_CS_GET_DEPOSIT_LIST_chainId', 'z76_CS_GET_DEPOSIT_LIST_pageNumber',
#            'z76_CS_GET_DEPOSIT_LIST_pageSize', 'z77_CS_GET_INFO_address', 'z77_CS_GET_INFO_chainId',
#            'z78_CS_GET_PACKER_INFO_chainId', 'z79_CS_GET_PUBLISH_LIST_address',
#            'z79_CS_GET_PUBLISH_LIST_chainId', 'z79_CS_GET_PUBLISH_LIST_type',
#            'z7_AC_EXPORT_KEYSTORE_JSON_address', 'z7_AC_EXPORT_KEYSTORE_JSON_chainId',
#            'z7_AC_EXPORT_KEYSTORE_JSON_password', 'z80_CS_GET_ROUND_INFO_chainId',
#            'z81_CS_GET_ROUND_MEMBER_LIST_chainId', 'z81_CS_GET_ROUND_MEMBER_LIST_extend',
#            'z82_CS_GET_SEED_NODE_INFO_chainId', 'z83_CS_GET_WHOLEINFO_chainId', 'z84_CS_MULTI_DEPOSIT_address',
#            'z84_CS_MULTI_DEPOSIT_agentHash', 'z84_CS_MULTI_DEPOSIT_chainId', 'z84_CS_MULTI_DEPOSIT_deposit',
#            'z84_CS_MULTI_DEPOSIT_password', 'z84_CS_MULTI_DEPOSIT_signAddress', 'z85_CS_MULTI_WITHDRAW_address',
#            'z85_CS_MULTI_WITHDRAW_chainId', 'z85_CS_MULTI_WITHDRAW_password',
#            'z85_CS_MULTI_WITHDRAW_signAddress', 'z85_CS_MULTI_WITHDRAW_txHash',
#            'z86_CS_RANDOM_RAW_SEEDS_COUNT_chainId', 'z86_CS_RANDOM_RAW_SEEDS_COUNT_count',
#            'z86_CS_RANDOM_RAW_SEEDS_COUNT_height', 'z87_CS_RANDOM_RAW_SEEDS_HEIGHT_chainId',
#            'z87_CS_RANDOM_RAW_SEEDS_HEIGHT_endHeight', 'z87_CS_RANDOM_RAW_SEEDS_HEIGHT_startHeight',
#            'z88_CS_RANDOM_SEED_COUNT_algorithm', 'z88_CS_RANDOM_SEED_COUNT_chainId',
#            'z88_CS_RANDOM_SEED_COUNT_count', 'z88_CS_RANDOM_SEED_COUNT_height',
#            'z89_CS_RANDOM_SEED_HEIGHT_algorithm', 'z89_CS_RANDOM_SEED_HEIGHT_chainId',
#            'z89_CS_RANDOM_SEED_HEIGHT_endHeight', 'z89_CS_RANDOM_SEED_HEIGHT_startHeight',
#            'z8_AC_GET_ACCOUNT_BYADDRESS_address', 'z8_AC_GET_ACCOUNT_BYADDRESS_chainId',
#            'z90_CS_RECEIVE_HEADERLIST_chainId', 'z90_CS_RECEIVE_HEADERLIST_headerList',
#            'z91_CS_RUN_CHAIN_chainId', 'z92_CS_RUN_MAINCHAIN_chainId', 'z93_CS_STOPAGENT_address',
#            'z93_CS_STOPAGENT_chainId', 'z93_CS_STOPAGENT_password', 'z94_CS_STOP_AGENT_address',
#            'z94_CS_STOP_AGENT_chainId', 'z94_CS_STOP_AGENT_password', 'z95_CS_STOPCHAIN_chainId',
#            'z96_CS_STOP_CHAIN_chainId', 'z97_CS_STOP_CONTRACT_AGENT_blockTime',
#            'z97_CS_STOP_CONTRACT_AGENT_chainId', 'z97_CS_STOP_CONTRACT_AGENT_contractAddress',
#            'z97_CS_STOP_CONTRACT_AGENT_contractBalance', 'z97_CS_STOP_CONTRACT_AGENT_contractNonce',
#            'z97_CS_STOP_CONTRACT_AGENT_contractSender', 'z98_CS_STOP_MULTI_AGENT_address',
#            'z98_CS_STOP_MULTI_AGENT_chainId', 'z98_CS_STOP_MULTI_AGENT_password',
#            'z98_CS_STOP_MULTI_AGENT_signAddress', 'z99_CS_TRIGGER_COINBASE_CONTRACT_blockHeader',
#            'z99_CS_TRIGGER_COINBASE_CONTRACT_chainId', 'z99_CS_TRIGGER_COINBASE_CONTRACT_stateRoot',
#            'z99_CS_TRIGGER_COINBASE_CONTRACT_tx', 'z9_AC_GET_ACCOUNT_LIST_chainId',
#            'z13_AC_GET_ALL_ADDRESS_PREFIX_chainId', 'z0_ADD_ADDRESS_PREFIX_prefix',
#            'z1017_AC_GET_PRIKEY_BY_ADDRESS__chainId',
#            'z1017_AC_GET_PRIKEY_BY_ADDRESS_address',
#            'z1017_AC_GET_PRIKEY_BY_ADDRESS_password'
#
#            ]


# to generate __all__:
# import user_settings.nulsws_USER_PARAMS as u
# dir(u)
# then remove globals from generated list
