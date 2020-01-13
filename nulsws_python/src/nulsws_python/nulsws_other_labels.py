#!/usr/bin/python3.7
"""
by Nancy Schorr for Nuls-io
January 2020

"""

type_name_dict = {0: 'None', 1: 'NegotiateConnection',
                  2: 'NegotiateConnectionResponse',
                  3: 'Request', 4: 'Unsubscribe', 5: 'Response', 6: 'Ack',
                  7: 'RegisterCompoundMethod', 8: 'UnregisterCompoundMethod'}

compress_type_label = "CompressionAlgorithm"
compress_rate_label = "CompressionRate"
msg_data_label = "MessageData"
msg_id_label = "MessageID"
msg_type_label = "MessageType"
negotiate_conn_label = "NegotiateConnection"
negotiate_stat_label = 'NegotiationStatus'
negotiate_conn_resp_label = "NegotiateConnectionResponse"
proto_label = "ProtocolVersion"
tmstmp_label = "Timestamp"
tmzone_label = "TimeZone"
request_label = "Request"
request_internalid_label = "RequestInternalID"
request_date_label = "RequestDate"
request_time_label = "RequestTime"
json_seps = (',', ':')

request_type_label = "RequestType"
subscrip_evnt_ct_label = "SubscriptionEventCounter"
subscrip_period_label = "SubscriptionPeriod"
subscriptn_range_label = "SubscriptionRange"
req_methods_label = "RequestMethods"
get_bal_label = "GetBalance"
response_max_size_label = "ResponseMaxSize"
address_label = "Address"
get_height_label = "GetHeight"

ZERO = "0"
ONE = "1"
CHAINID_LABEL = "chainId"

# reason for labels: all uppers is easier for the user to use correctly because of mixed case in values


class NulsWsParams(object):
    param_dict = {
        "ADDRESS": "address",
        "ADDRESSPREFIX": "addressPrefix",
        "ADDRESSTYPE": "addressType",
        "AGENTADDRESS": "agentAddress",
        "AGENTHASH": "agentHash",
        "ALGORITHM": "algorithm",
        "ALIAS": "alias",
        "ALLHITS": "allHits",
        "AMOUNT": "amount",
        "ARGS": "args",
        "ASSETCHAINID": "assetChainId",
        "ASSETID": "assetId",
        "ASSETIDS": "assetIds",
        "ASSETINFOLIST": "assetInfoList",
        "ASSETNAME": "assetName",
        "ASSETS": "assets",
        "BEGIN": "begin",
        "BLOCK": "block",
        "BLOCKHASH": "blockHash",
        "BLOCKHEADER": "blockHeader",
        "BLOCKHEIGHT": "blockHeight",
        "BLOCKTIME": "blockTime",
        "BLOCKTYPE": "blockType",
        "BYTECOUNT": "byteCount",
        "CHAINID": "chainId",
        "CHAINNAME": "chainName",
        "CIRCULATECHAINID": "circulateChainId",
        "CMD": "cmd",
        "CMDREGISTERLIST": "cmdRegisterList",
        "COMMAND": "command",
        "COMMISSIONRATE": "commissionRate",
        "CONTRACTADDRESS": "contractAddress",
        "CONTRACTBALANCE": "contractBalance",
        "CONTRACTCODE": "contractCode",
        "CONTRACTLIST": "contractList",
        "CONTRACTNONCE": "contractNonce",
        "CONTRACTSENDER": "contractSender",
        "COUNT": "count",
        "DATA": "data",
        "DECIMALPLACES": "decimalPlaces",
        "DELLIST": "delList",
        "DEPOSIT": "deposit",
        "DOWNLOAD": "download",
        "END": "end",
        "ENDHEIGHT": "endHeight",
        "ENDTIMESTAMP": "endTimestamp",
        "EVIDENCEHEADER": "evidenceHeader",
        "EXCLUDENODES": "excludeNodes",
        "EXTEND": "extend",
        "EXTENDSDATA": "extendsData",
        "FRESTARTIFRUNNING": "fRestartIfRunning",
        "FILEPATH": "filePath",
        "GASLIMIT": "gasLimit",
        "HASH": "hash",
        "HASHLIST": "hashList",
        "HEADERLIST": "headerList",
        "HEIGHT": "height",
        "INITNUMBER": "initNumber",
        "INPUTS": "inputs",
        "INTCOUNT": "intCount",
        "INTERVAL": "interval",
        "ISCONFIRMED": "isConfirmed",
        "ISCROSS": "isCross",
        "ISCROSSGROUP": "isCrossGroup",
        "JARFILEDATA": "jarFileData",
        "JOINAGENTHASH": "joinAgentHash",
        "KEYSTORE": "keyStore",
        "KEYWORD": "keyWord",
        "LMAXCPUS": "lMaxCPUs",
        "LMODULENAME": "lModuleName",
        "LMODULEVERSION": "lModuleVersion",
        "LIST": "list",
        "LISTFROM": "listFrom",
        "LISTTO": "listTo",
        "LONGCOUNT": "longCount",
        "MAGICNUMBER": "magicNumber",
        "MAXIN": "maxIn",
        "MAXOUT": "maxOut",
        "MAXSIGNATURECOUNT": "maxSignatureCount",
        "MAXTXDATASIZE": "maxTxDataSize",
        "MESSAGEBODY": "messageBody",
        "METHODDESC": "methodDesc",
        "METHODNAME": "methodName",
        "MINAVAILABLECOUNT": "minAvailableCount",
        "MINAVAILABLENODENUM": "minAvailableNodeNum",
        "MINSIGNS": "minSigns",
        "MODULECODE": "moduleCode",
        "NEWPASSWORD": "newPassword",
        "NODEID": "nodeId",
        "NODES": "nodes",
        "OUTPUTS": "outputs",
        "OVERWRITE": "overwrite",
        "PACKAGING": "packaging",
        "PACKINGADDRESS": "packingAddress",
        "PAGENUMBER": "pageNumber",
        "PAGESIZE": "pageSize",
        "PASSWORD": "password",
        "PERCENT": "percent",
        "PRESTATEROOT": "preStateRoot",
        "PREFIXLIST": "prefixList",
        "PRIKEY": "priKey",
        "PRICE": "price",
        "PROTOCOLCMDS": "protocolCmds",
        "PROTOCOLVERSION": "protocolVersion",
        "PUBKEY": "pubKey",
        "PUBKEYS": "pubKeys",
        "REGISTERTIME": "registerTime",
        "REMARK": "remark",
        "REWARDADDRESS": "rewardAddress",
        "ROLE": "role",
        "ROUND": "round",
        "SEEDIPS": "seedIps",
        "SENDER": "sender",
        "SHORTCOUNT": "shortCount",
        "SIG": "sig",
        "SIGNADDRESS": "signAddress",
        "SIGNPASSWORD": "signPassword",
        "SIGNATUREBFTRATIO": "signatureBFTRatio",
        "SIZE": "size",
        "STARTHEIGHT": "startHeight",
        "STARTPAGE": "startPage",
        "STATE": "state",
        "STATEROOT": "stateRoot",
        "STATUS": "status",
        "SYMBOL": "symbol",
        "TOADDRESS": "toAddress",
        "TX": "tx",
        "TXHASH": "txHash",
        "TXHASHLIST": "txHashList",
        "TXLIST": "txList",
        "TYPE": "type",
        "USABLE": "usable",
        "VALUE": "value",
        "VERIFIERLIST": "verifierList",
        "PREFIXLIST": "prefixList"
    }


__all__ = ['CHAINID_LABEL', 'ONE', 'ZERO', 'address_label', 'compress_rate_label',
           'compress_type_label', 'get_bal_label', 'get_height_label', 'json_seps', 'msg_data_label',
           'msg_id_label',
           'msg_type_label', 'negotiate_conn_label', 'negotiate_conn_resp_label', 'negotiate_stat_label',
           'proto_label',
           'req_methods_label', 'request_date_label', 'request_internalid_label', 'request_label',
           'request_time_label',
           'request_type_label', 'response_max_size_label', 'subscrip_evnt_ct_label', 'subscrip_period_label',
           'subscriptn_range_label', 'tmstmp_label', 'tmzone_label', 'type_name_dict']





# to generate __all__:
# import libraries.constants.nulsws_CONSTANTS_otherlabels as u
# dir(u)
# then remove globals
