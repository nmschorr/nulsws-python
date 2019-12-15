

# for use in api calls



my_address: str =  None
my_addressPrefix: str =  None
my_addressType: str =  None
my_agentAddress: str =  None
my_agentHash: str =  None
my_algorithm: str =  None
my_alias: str =  None
my_allHits: str =  None
my_amount: int =  0  #BigInteger
my_args: str =  None
my_assetChainId: str =  None
my_assetId: str =  None
my_assetIds: str =  None
my_assetInfoList: str =  None
my_assetName: str =  None
my_assets: list =  None   #List
my_begin: str =  None
my_block: str =  None
my_blockHash: str =  0
my_blockHeader: str =  0
my_blockHeight: str =  0
my_blockTime: str =  None
my_blockType: str =  None
my_byteCount: str =  0
my_chainId: int =  1
my_chainName: str =  None
my_circulateChainId: str =  None
my_cmd: str =  None
my_cmdRegisterList: str =  None
my_command: str =  None
my_commissionRate: str =  None
my_contractAddress: str =  None
my_contractBalance: str =  None
my_contractCode: str =  None
my_contractList: str =  None
my_contractNonce: str =  None
my_contractSender: str =  None
my_count: str =  1
my_data: str =  None
my_decimalPlaces: str =  0
my_delList: str =  None
my_deposit: str =  0
my_download: str =  None
my_end: str =  None
my_endHeight: str =  None
my_endTimestamp: str =  None
my_evidenceHeader: str =  None
my_excludeNodes: str =  None
my_extend: str =  None
my_extendsData: str =  0
my_fRestartIfRunning: str =  0
my_filePath: str =  None
my_gasLimit: str =  0
my_hash: str =  0
my_hashList: str =  None
my_headerList: str =  None
my_height: str =  1
my_initNumber: int =  0  #BigInteger
my_inputs: str =  None
my_intCount: str =  0
my_interval: str =  0
my_isConfirmed: str =  None
my_isCross: str =  None
my_isCrossGroup: str =  None
my_jarFileData: str =  None
my_joinAgentHash: str =  None
my_keyStore: str =  None
my_keyWord: str =  None
my_lMaxCPUs: str =  0
my_lModuleName: str =  None
my_lModuleVersion: str =  None
my_list: str =  None
my_listFrom: str =  None
my_listTo: str =  None
my_longCount: int =  0
my_magicNumber: str =  0
my_maxIn: int =  0
my_maxOut: str =  0
my_maxSignatureCount: int =  0  #Integer
my_maxTxDataSize: str =  0
my_messageBody: str =  None
my_methodDesc: str =  None
my_methodName: str =  None
my_minAvailableCount: int =  0
my_minAvailableNodeNum: int =  None
my_minSigns: int =  None
my_moduleCode: str =  None
my_newPassword: str =  None
my_nodeId: int =  None
my_nodes: str =  0
my_outputs: str =  None
my_overwrite: str =  None
my_packaging: str =  None
my_packingAddress: str =  None
my_pageNumber: int =  0
my_pageSize: int =  0
my_password: str =  None
my_percent: int =  None
my_preStateRoot: str =  None
my_prefixList: str =  None
my_priKey: str =  None
my_price: int =  0
my_protocolCmds: str =  None
my_protocolVersion: str =  None
my_pubKey: str =  None
my_pubKeys: list =  None
my_registerTime: str =  None
my_remark: str =  None
my_rewardAddress: str =  None
my_role: str =  None
my_round: str =  None
my_seedIps: str =  None
my_sender: str =  None
my_shortCount: str =  0
my_sig: str =  None
my_signAddress: str =  None
my_signPassword: str =  my_password
my_signatureBFTRatio: int =  None  #Integer
my_size: str =  0
my_startHeight: str =  0
my_startPage: str =  None
my_state: str =  None
my_stateRoot: str =  None
my_status: str =  None
my_symbol: str =  None
my_toAddress: str =  None
my_tx: str =  None
my_txHash: str =  None
my_txHashList: str =  None
my_txList: str =  None
my_type: str =  None
my_usable: str =  None
my_value: int =  None  #BigInteger
my_verifierList: str =  None

b = [
['my_amount', 'BigInteger'],
['my_initNumber', 'BigInteger'],
['my_value', 'BigInteger'],
['my_maxSignatureCount', 'Integer'],
['my_signatureBFTRatio', 'Integer'],
['my_assets', 'List'],
['my_cmdRegisterList', 'List'],
['my_contractList', 'List'],
['my_delList', 'List'],
['my_hashList', 'List'],
['my_inputs', 'List'],
['my_list', 'List'],
['my_listFrom', 'List'],
['my_listTo', 'List'],
['my_outputs', 'List'],
['my_prefixList', 'List'],
['my_protocolCmds', 'List'],
['my_pubKeys', 'List'],
['my_txHashList', 'List'],
['my_txList', 'List'],
['my_verifierList', 'List'],
['my_assetInfoList', 'List<AssetInfo>'],
['my_headerList', 'List<String>'],
['my_args', 'Object[]'],
['my_lModuleName', 'QString'],
['my_lModuleVersion', 'QString'],
['my_address', 'String'],
['my_addressPrefix', 'String'],
['my_agentAddress', 'String'],
['my_agentHash', 'String'],
['my_algorithm', 'String'],
['my_alias', 'String'],
['my_assetIds', 'String'],
['my_assetName', 'String'],
['my_block', 'String'],
['my_blockHash', 'String'],
['my_blockHeader', 'String'],
['my_chainName', 'String'],
['my_cmd', 'String'],
['my_command', 'String'],
['my_contractAddress', 'String'],
['my_contractBalance', 'String'],
['my_contractCode', 'String'],
['my_contractNonce', 'String'],
['my_contractSender', 'String'],
['my_data', 'String'],
['my_deposit', 'String'],
['my_evidenceHeader', 'String'],
['my_excludeNodes', 'String'],
['my_extend', 'String'],
['my_extendsData', 'String'],
['my_filePath', 'String'],
['my_hash', 'String'],
['my_jarFileData', 'String'],
['my_joinAgentHash', 'String'],
['my_keyStore', 'String'],
['my_keyWord', 'String'],
['my_maxOut', 'String'],
['my_messageBody', 'String'],
['my_methodDesc', 'String'],
['my_methodName', 'String'],
['my_moduleCode', 'String'],
['my_newPassword', 'String'],
['my_nodeId', 'String'],
['my_nodes', 'String'],
['my_packingAddress', 'String'],
['my_password', 'String'],
['my_preStateRoot', 'String'],
['my_priKey', 'String'],
['my_pubKey', 'String'],
['my_remark', 'String'],
['my_rewardAddress', 'String'],
['my_role', 'String'],
['my_seedIps', 'String'],
['my_sender', 'String'],
['my_sig', 'String'],
['my_signAddress', 'String'],
['my_signPassword', 'String'],
['my_stateRoot', 'String'],
['my_symbol', 'String'],
['my_toAddress', 'String'],
['my_tx', 'String'],
['my_txHash', 'String'],
['my_fRestartIfRunning', 'bool'],
['my_allHits', 'boolean'],
['my_isConfirmed', 'boolean'],
['my_isCrossGroup', 'boolean'],
['my_overwrite', 'boolean'],
['my_packaging', 'boolean'],
['my_usable', 'boolean'],
['my_byteCount', 'byte'],
['my_addressType', 'int'],
['my_assetChainId', 'int'],
['my_assetId', 'int'],
['my_blockType', 'int'],
['my_chainId', 'int'],
['my_circulateChainId', 'int'],
['my_commissionRate', 'int'],
['my_count', 'int'],
['my_download', 'int'],
['my_height', 'int'],
['my_intCount', 'int'],
['my_interval', 'int'],
['my_isCross', 'int'],
['my_lMaxCPUs', 'int'],
['my_maxIn', 'int'],
['my_maxTxDataSize', 'int'],
['my_minAvailableCount', 'int'],
['my_minAvailableNodeNum', 'int'],
['my_minSigns', 'int'],
['my_pageNumber', 'int'],
['my_pageSize', 'int'],
['my_percent', 'int'],
['my_round', 'int'],
['my_size', 'int'],
['my_startPage', 'int'],
['my_state', 'int'],
['my_status', 'int'],
['my_type', 'int'],
['my_begin', 'long'],
['my_blockHeight', 'long'],
['my_blockTime', 'long'],
['my_end', 'long'],
['my_endHeight', 'long'],
['my_endTimestamp', 'long'],
['my_gasLimit', 'long'],
['my_longCount', 'long'],
['my_magicNumber', 'long'],
['my_price', 'long'],
['my_registerTime', 'long'],
['my_startHeight', 'long'],
['my_decimalPlaces', 'short'],
['my_protocolVersion', 'short'],
['my_shortCount', 'short']
]

a = [
['amount', 'BigInteger'],
['initNumber', 'BigInteger'],
['value', 'BigInteger'],
['maxSignatureCount', 'Integer'],
['signatureBFTRatio', 'Integer'],
['assets', 'List'],
['cmdRegisterList', 'List'],
['contractList', 'List'],
['delList', 'List'],
['hashList', 'List'],
['inputs', 'List'],
['list', 'List'],
['listFrom', 'List'],
['listTo', 'List'],
['outputs', 'List'],
['prefixList', 'List'],
['protocolCmds', 'List'],
['pubKeys', 'List'],
['txHashList', 'List'],
['txList', 'List'],
['verifierList', 'List'],
['assetInfoList', 'List<AssetInfo>'],
['headerList', 'List<String>'],
['args', 'Object[]'],
['lModuleName', 'QString'],
['lModuleVersion', 'QString'],
['address', 'String'],
['addressPrefix', 'String'],
['agentAddress', 'String'],
['agentHash', 'String'],
['algorithm', 'String'],
['alias', 'String'],
['assetIds', 'String'],
['assetName', 'String'],
['block', 'String'],
['blockHash', 'String'],
['blockHeader', 'String'],
['chainName', 'String'],
['cmd', 'String'],
['command', 'String'],
['contractAddress', 'String'],
['contractBalance', 'String'],
['contractCode', 'String'],
['contractNonce', 'String'],
['contractSender', 'String'],
['data', 'String'],
['deposit', 'String'],
['evidenceHeader', 'String'],
['excludeNodes', 'String'],
['extend', 'String'],
['extendsData', 'String'],
['filePath', 'String'],
['hash', 'String'],
['jarFileData', 'String'],
['joinAgentHash', 'String'],
['keyStore', 'String'],
['keyWord', 'String'],
['maxOut', 'String'],
['messageBody', 'String'],
['methodDesc', 'String'],
['methodName', 'String'],
['moduleCode', 'String'],
['newPassword', 'String'],
['nodeId', 'String'],
['nodes', 'String'],
['packingAddress', 'String'],
['password', 'String'],
['preStateRoot', 'String'],
['priKey', 'String'],
['pubKey', 'String'],
['remark', 'String'],
['rewardAddress', 'String'],
['role', 'String'],
['seedIps', 'String'],
['sender', 'String'],
['sig', 'String'],
['signAddress', 'String'],
['signPassword', 'String'],
['stateRoot', 'String'],
['symbol', 'String'],
['toAddress', 'String'],
['tx', 'String'],
['txHash', 'String'],
['fRestartIfRunning', 'bool'],
['allHits', 'boolean'],
['isConfirmed', 'boolean'],
['isCrossGroup', 'boolean'],
['overwrite', 'boolean'],
['packaging', 'boolean'],
['usable', 'boolean'],
['byteCount', 'byte'],
['addressType', 'int'],
['assetChainId', 'int'],
['assetId', 'int'],
['blockType', 'int'],
['chainId', 'int'],
['circulateChainId', 'int'],
['commissionRate', 'int'],
['count', 'int'],
['download', 'int'],
['height', 'int'],
['intCount', 'int'],
['interval', 'int'],
['isCross', 'int'],
['lMaxCPUs', 'int'],
['maxIn', 'int'],
['maxTxDataSize', 'int'],
['minAvailableCount', 'int'],
['minAvailableNodeNum', 'int'],
['minSigns', 'int'],
['pageNumber', 'int'],
['pageSize', 'int'],
['percent', 'int'],
['round', 'int'],
['size', 'int'],
['startPage', 'int'],
['state', 'int'],
['status', 'int'],
['type', 'int'],
['begin', 'long'],
['blockHeight', 'long'],
['blockTime', 'long'],
['end', 'long'],
['endHeight', 'long'],
['endTimestamp', 'long'],
['gasLimit', 'long'],
['longCount', 'long'],
['magicNumber', 'long'],
['price', 'long'],
['registerTime', 'long'],
['startHeight', 'long'],
['decimalPlaces', 'short'],
['protocolVersion', 'short'],
['shortCount', 'short']
]

__ALL__ : str =   ['my_address', 'my_addressPrefix', 'my_addressType', 'my_agentAddress', 'my_agentHash',
           'my_algorithm', 'my_alias', 'my_allHits', 'my_amount', 'my_args', 'my_assetChainId', 'my_assetId',
           'my_assetIds', 'my_assetInfoList', 'my_assetName', 'my_assets', 'my_begin', 'my_block',
           'my_blockHash', 'my_blockHeader', 'my_blockHeight', 'my_blockTime', 'my_blockType', 'my_byteCount',
           'my_chainId', 'my_chainName', 'my_circulateChainId', 'my_cmd', 'my_cmdRegisterList', 'my_command',
           'my_commissionRate', 'my_contractAddress', 'my_contractBalance', 'my_contractCode',
           'my_contractList', 'my_contractNonce', 'my_contractSender', 'my_count', 'my_data',
           'my_decimalPlaces', 'my_delList', 'my_deposit', 'my_download', 'my_end', 'my_endHeight',
           'my_endTimestamp', 'my_evidenceHeader', 'my_excludeNodes', 'my_extend', 'my_extendsData',
           'my_fRestartIfRunning', 'my_filePath', 'my_gasLimit', 'my_hash', 'my_hashList', 'my_headerList',
           'my_height', 'my_initNumber', 'my_inputs', 'my_intCount', 'my_interval', 'my_isConfirmed',
           'my_isCross', 'my_isCrossGroup', 'my_jarFileData', 'my_joinAgentHash', 'my_keyStore', 'my_keyWord',
           'my_lMaxCPUs', 'my_lModuleName', 'my_lModuleVersion', 'my_list', 'my_listFrom', 'my_listTo',
           'my_longCount', 'my_magicNumber', 'my_maxIn', 'my_maxOut', 'my_maxSignatureCount',
           'my_maxTxDataSize', 'my_messageBody', 'my_methodDesc', 'my_methodName', 'my_minAvailableCount',
           'my_minAvailableNodeNum', 'my_minSigns', 'my_moduleCode', 'my_newPassword', 'my_nodeId',
           'my_nodes', 'my_outputs', 'my_overwrite', 'my_packaging', 'my_packingAddress', 'my_pageNumber',
           'my_pageSize', 'my_password', 'my_percent', 'my_preStateRoot', 'my_prefixList', 'my_priKey',
           'my_price', 'my_protocolCmds', 'my_protocolVersion', 'my_pubKey', 'my_pubKeys', 'my_registerTime',
           'my_remark', 'my_rewardAddress', 'my_role', 'my_round', 'my_seedIps', 'my_sender', 'my_shortCount',
           'my_sig', 'my_signAddress', 'my_signPassword', 'my_signatureBFTRatio', 'my_size', 'my_startHeight',
           'my_startPage', 'my_state', 'my_stateRoot', 'my_status', 'my_symbol', 'my_toAddress', 'my_tx',
           'my_txHash', 'my_txHashList', 'my_txList', 'my_type', 'my_usable', 'my_value', 'my_verifierList']
