


-------! ! ! REGULAR response received: 
a={
   "MessageData": {
      "RequestID": "157588462348569-1",
      "ResponseComment": "",
      "ResponseData": {
         "ListAPI": {
            "Nuls.RegisterAPI": {
               "MethodDescription": "Register API",
               "MethodMinEvent": "1",
               "MethodMinPeriod": "0",
               "MethodName": "RegisterAPI",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.ac_addAddressPrefix": {
               "MethodDescription": "\u6dfb\u52a0\u5730\u5740\u524d\u7f00,\u94fe\u7ba1\u7406\u6a21\u5757\u4f1a\u8c03\u7528\u8be5\u63a5\u53e3",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_addAddressPrefix",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "prefixList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_createAccount": {
               "MethodDescription": "\u521b\u5efa\u6307\u5b9a\u4e2a\u6570\u7684\u8d26\u6237/create a specified number of accounts",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_createAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "count",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_createContractAccount": {
               "MethodDescription": "\u521b\u5efa\u667a\u80fd\u5408\u7ea6\u8d26\u6237/create smart contract account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_createContractAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_createMultiSignAccount": {
               "MethodDescription": "\u521b\u5efa\u591a\u7b7e\u8d26\u6237/create a multi sign account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_createMultiSignAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pubKeys",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "minSigns",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_createMultiSignTransfer": {
               "MethodDescription": "\u521b\u5efa\u591a\u7b7e\u5730\u5740\u8f6c\u8d26\u4ea4\u6613/create multi sign transfer",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_createMultiSignTransfer",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "inputs",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "outputs",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signPassword",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_createOfflineAccount": {
               "MethodDescription": "\u521b\u5efa\u79bb\u7ebf\u8d26\u6237, \u8be5\u8d26\u6237\u4e0d\u4fdd\u5b58\u5230\u6570\u636e\u5e93, \u5e76\u5c06\u76f4\u63a5\u8fd4\u56de\u8d26\u6237\u7684\u6240\u6709\u4fe1\u606f/create an offline account, which is not saved to the database and will directly return all information to the account.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_createOfflineAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "count",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_exportAccountKeyStore": {
               "MethodDescription": "\u8d26\u6237\u5907\u4efd\uff0c\u5bfc\u51faAccountKeyStore\u5b57\u7b26\u4e32/export account KeyStore",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_exportAccountKeyStore",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "filePath",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_exportKeyStoreJson": {
               "MethodDescription": "\u5bfc\u51faAccountKeyStore\u5b57\u7b26\u4e32/export account KeyStore json",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_exportKeyStoreJson",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAccountByAddress": {
               "MethodDescription": "\u901a\u8fc7\u5730\u5740\u83b7\u53d6\u8d26\u6237\u4fe1\u606f/get account info according to address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAccountByAddress",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAccountList": {
               "MethodDescription": "\u83b7\u53d6\u6240\u6709\u8d26\u6237\u96c6\u5408,\u5e76\u653e\u5165\u7f13\u5b58/query all account collections and put them in cache",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAccountList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAddressList": {
               "MethodDescription": "\u5206\u9875\u67e5\u8be2\u8d26\u6237\u5730\u5740\u5217\u8868/Paging query account address list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAddressList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAddressPrefixByChainId": {
               "MethodDescription": "\u901a\u8fc7\u94feid\u83b7\u53d6\u5730\u5740\u524d\u7f00",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAddressPrefixByChainId",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAliasByAddress": {
               "MethodDescription": "\u6839\u636e\u5730\u5740\u83b7\u53d6\u522b\u540d/get the alias by address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAliasByAddress",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAllAddressPrefix": {
               "MethodDescription": "\u83b7\u53d6\u6240\u6709\u94fe\u7684\u5730\u5740\u524d\u7f00",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAllAddressPrefix",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.ac_getAllPriKey": {
               "MethodDescription": "\u83b7\u53d6\u6240\u6709\u672c\u5730\u8d26\u6237\u8d26\u6237\u79c1\u94a5\uff0c\u5fc5\u987b\u4fdd\u8bc1\u6240\u6709\u8d26\u6237\u5bc6\u7801\u4e00\u81f4\uff0c\u5982\u679c\u672c\u5730\u8d26\u6237\u4e2d\u7684\u5bc6\u7801\u4e0d\u4e00\u81f4\uff0c\u5c06\u8fd4\u56de\u9519\u8bef\u4fe1\u606f/Get the all local private keys. if the password in the local account is different, the error message will be returned.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAllPriKey",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getEncryptedAddressList": {
               "MethodDescription": "\u83b7\u53d6\u672c\u5730\u52a0\u5bc6\u8d26\u6237\u5217\u8868/Get a list of locally encrypted accounts",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getEncryptedAddressList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getMultiSignAccount": {
               "MethodDescription": "\u6839\u636e\u591a\u7b7e\u8d26\u6237\u5730\u5740\u83b7\u53d6\u5b8c\u6574\u591a\u7b7e\u8d26\u6237/Search for multi-signature account by address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getMultiSignAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getPriKeyByAddress": {
               "MethodDescription": "\u901a\u8fc7\u8d26\u6237\u5730\u5740\u548c\u5bc6\u7801,\u67e5\u8be2\u8d26\u6237\u79c1\u5319/Inquire the account's private key according to the address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getPriKeyByAddress",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getPubKey": {
               "MethodDescription": "\u6839\u636e\u8d26\u6237\u5730\u5740\u548c\u5bc6\u7801,\u67e5\u8be2\u8d26\u6237\u516c\u94a5/Get the account's public key",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getPubKey",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_importAccountByKeystore": {
               "MethodDescription": "\u6839\u636eAccountKeyStore\u5bfc\u5165\u8d26\u6237/Import accounts by AccountKeyStore",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_importAccountByKeystore",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "keyStore",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "overwrite",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_importAccountByPriKey": {
               "MethodDescription": "\u6839\u636e\u79c1\u94a5\u5bfc\u5165\u8d26\u6237/Import accounts by private key",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_importAccountByPriKey",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "priKey",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "overwrite",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_isAliasUsable": {
               "MethodDescription": "\u68c0\u67e5\u522b\u540d\u662f\u5426\u53ef\u7528/check whether the account is usable",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_isAliasUsable",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "alias",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_isMultiSignAccountBuilder": {
               "MethodDescription": "\u9a8c\u8bc1\u662f\u5426\u591a\u7b7e\u8d26\u6237\u7684\u521b\u5efa\u8005\u4e4b\u4e00/Whether it is multiSign account Builder",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_isMultiSignAccountBuilder",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pubKey",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_removeAccount": {
               "MethodDescription": "\u79fb\u9664\u6307\u5b9a\u8d26\u6237/Remove specified account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_removeAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_removeMultiSignAccount": {
               "MethodDescription": "\u79fb\u9664\u591a\u7b7e\u8d26\u6237/remove the multi sign account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_removeMultiSignAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_setAlias": {
               "MethodDescription": "\u8bbe\u7f6e\u522b\u540d/Set the alias of account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_setAlias",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "alias",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_setMultiSignAlias": {
               "MethodDescription": "\u8bbe\u7f6e\u591a\u7b7e\u8d26\u6237\u522b\u540d/set the alias of multi sign account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_setMultiSignAlias",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "alias",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signPassword",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_setRemark": {
               "MethodDescription": "\u4e3a\u8d26\u6237\u8bbe\u7f6e\u5907\u6ce8/Set remark for accounts",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_setRemark",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_signBlockDigest": {
               "MethodDescription": "\u533a\u5757\u6570\u636e\u6458\u8981\u7b7e\u540d/Block data digest signature",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_signBlockDigest",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "data",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_signDigest": {
               "MethodDescription": "\u6570\u636e\u6458\u8981\u7b7e\u540d/Data digest signature",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_signDigest",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "data",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_signMultiSignTransaction": {
               "MethodDescription": "\u591a\u7b7e\u4ea4\u6613\u7b7e\u540d/sign MultiSign Transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_signMultiSignTransaction",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signPassword",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_transfer": {
               "MethodDescription": "\u521b\u5efa\u666e\u901a\u8f6c\u8d26\u4ea4\u6613/create transfer transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_transfer",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "inputs",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "outputs",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_updateOfflineAccountPassword": {
               "MethodDescription": "\u79bb\u7ebf\u8d26\u6237\u4fee\u6539\u5bc6\u7801/Offline account change password",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_updateOfflineAccountPassword",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "newPassword",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "priKey",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_updatePassword": {
               "MethodDescription": "\u6839\u636e\u539f\u5bc6\u7801\u4fee\u6539\u8d26\u6237\u5bc6\u7801/Modify the account password by the original password",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_updatePassword",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "newPassword",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_validationPassword": {
               "MethodDescription": "\u9a8c\u8bc1\u8d26\u6237\u5bc6\u7801\u662f\u5426\u6b63\u786e/Verify that the account password is correct",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_validationPassword",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_verifySignData": {
               "MethodDescription": "\u9a8c\u8bc1\u6570\u636e\u7b7e\u540d/Verification Data Signature",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_verifySignData",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "pubKey",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sig",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "data",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.batchValidateBegin": {
               "MethodDescription": "\u5f00\u59cb\u6279\u91cf\u6253\u5305:\u72b6\u6001\u901a\u77e5",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "batchValidateBegin",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.blockValidate": {
               "MethodDescription": "\u6574\u533a\u5757\u5165\u8d26\u6821\u9a8c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "blockValidate",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cancelCrossChain": {
               "MethodDescription": "\u6307\u5b9a\u94fe\u8d44\u4ea7\u9000\u51fa\u8de8\u94fe/Specified Chain Assets Exit Cross Chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cancelCrossChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.checkBlockVersion": {
               "MethodDescription": "check block version",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "checkBlockVersion",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "extendsData",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.clearUnconfirmTxs": {
               "MethodDescription": "\u6e05\u9664\u6240\u6709\u8d26\u6237\u672a\u786e\u8ba4\u4ea4\u6613",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "clearUnconfirmTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_asset": {
               "MethodDescription": "\u8d44\u4ea7\u6ce8\u518c\u4fe1\u606f\u67e5\u8be2",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_asset",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_assetCirculateCommit": {
               "MethodDescription": "\u67e5\u8be2\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_assetCirculateCommit",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_assetCirculateRollBack": {
               "MethodDescription": "\u67e5\u8be2\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_assetCirculateRollBack",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_assetCirculateValidator": {
               "MethodDescription": "\u67e5\u8be2\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_assetCirculateValidator",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_assetDisable": {
               "MethodDescription": "\u8d44\u4ea7\u6ce8\u9500",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_assetDisable",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_assetReg": {
               "MethodDescription": "\u8d44\u4ea7\u6ce8\u518c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_assetReg",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "symbol",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "initNumber",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "decimalPlaces",
                     "ParameterType": "short",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_chain": {
               "MethodDescription": "\u67e5\u770b\u94fe\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_chain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_chainActive": {
               "MethodDescription": "\u94fe\u66f4\u65b0\u6fc0\u6d3b-\u7528\u4e8e\u5e73\u884c\u94fe\u7684\u8de8\u94fe\u66f4\u65b0\u6fc0\u6d3b\uff08\u6fc0\u6d3b\u4e4b\u524d\u6ce8\u9500\u7684\u94fe\uff09",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_chainActive",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "chainName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "addressType",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "addressPrefix",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "magicNumber",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "minAvailableNodeNum",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "symbol",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "initNumber",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "decimalPlaces",
                     "ParameterType": "short",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "verifierList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signatureBFTRatio",
                     "ParameterType": "Integer",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxSignatureCount",
                     "ParameterType": "Integer",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_chainReg": {
               "MethodDescription": "\u94fe\u6ce8\u518c-\u7528\u4e8e\u5e73\u884c\u94fe\u7684\u8de8\u94fe\u6ce8\u518c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_chainReg",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[3-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "chainName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "addressType",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "addressPrefix",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "magicNumber",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "minAvailableNodeNum",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "symbol",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "initNumber",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "decimalPlaces",
                     "ParameterType": "short",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "verifierList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signatureBFTRatio",
                     "ParameterType": "Integer",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxSignatureCount",
                     "ParameterType": "Integer",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_getChainAsset": {
               "MethodDescription": "\u8d44\u4ea7\u67e5\u770b",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_getChainAsset",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_getChainsSimpleInfo": {
               "MethodDescription": "\u83b7\u53d6\u8de8\u94fe\u5df2\u6ce8\u518c\u94fe\u5217\u8868",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_getChainsSimpleInfo",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.cm_getCirculateChainAsset": {
               "MethodDescription": "\u67e5\u8be2\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_getCirculateChainAsset",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "circulateChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.commitBatchUnconfirmedTxs": {
               "MethodDescription": "\u672a\u786e\u8ba4\u4ea4\u6613\u6279\u91cf\u63d0\u4ea4\u8d26\u672c(\u6821\u9a8c\u5e76\u66f4\u65b0nonce\u503c)",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "commitBatchUnconfirmedTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.commitBlockTxs": {
               "MethodDescription": "\u63d0\u4ea4\u533a\u5757",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "commitBlockTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.commitUnconfirmedTx": {
               "MethodDescription": "\u672a\u786e\u8ba4\u4ea4\u6613\u63d0\u4ea4\u8d26\u672c(\u6821\u9a8c\u5e76\u66f4\u65b0nonce\u503c)",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "commitUnconfirmedTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.connectReady": {
               "MethodDescription": "check module rpc is ready",
               "MethodMinEvent": "1",
               "MethodMinPeriod": "0",
               "MethodName": "connectReady",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nuls.createAgentValid": {
               "MethodDescription": "create agent transaction validate",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "createAgentValid",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.createCrossTx": {
               "MethodDescription": "\u521b\u5efa\u8de8\u94fe\u8f6c\u8d26\u4ea4\u6613/Creating Cross-Chain Transfer Transactions",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "createCrossTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "listFrom",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "listTo",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.crossChainRegisterChange": {
               "MethodDescription": "\u8de8\u94fe\u6ce8\u518c\u4fe1\u606f\u53d8\u66f4/Registered Cross Chain change",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "crossChainRegisterChange",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_addBlock": {
               "MethodDescription": "\u63a5\u6536\u5e76\u7f13\u5b58\u65b0\u533a\u5757/Receiving and caching new blocks",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_addBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_addEvidenceRecord": {
               "MethodDescription": "\u94fe\u5206\u53c9\u8bc1\u636e\u8bb0\u5f55/add evidence record",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_addEvidenceRecord",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "evidenceHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_chainRollBack": {
               "MethodDescription": "\u533a\u5757\u56de\u6eda/chain rollback",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_chainRollBack",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_contractDeposit": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u59d4\u6258\u5171\u8bc6/contract deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_contractDeposit",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractBalance",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractNonce",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_contractWithdraw": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u9000\u51fa\u5171\u8bc6/contract withdraw deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_contractWithdraw",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "joinAgentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractBalance",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractNonce",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_createAgent": {
               "MethodDescription": "\u521b\u5efa\u8282\u70b9\u4ea4\u6613/create agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_createAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packingAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "rewardAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "commissionRate",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_createContractAgent": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u521b\u5efa\u8282\u70b9/contract create agent",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_createContractAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packingAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "commissionRate",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractBalance",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractNonce",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_createMultiAgent": {
               "MethodDescription": "\u591a\u7b7e\u8d26\u6237\u521b\u5efa\u8282\u70b9/Multi-Sign Account create agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_createMultiAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packingAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "rewardAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "commissionRate",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_depositToAgent": {
               "MethodDescription": "\u521b\u5efa\u59d4\u6258\u4ea4\u6613/deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_depositToAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_doubleSpendRecord": {
               "MethodDescription": "\u53cc\u82b1\u4ea4\u6613\u8bb0\u5f55/double spend transaction record ",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_doubleSpendRecord",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "block",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getAgentAddressList": {
               "MethodDescription": "\u83b7\u53d6\u5f53\u524d\u7f51\u7edc\u5171\u8bc6\u8282\u70b9\u51fa\u5757\u5730\u5740\u5217\u8868\u6216\u5219\u67e5\u8be2\u6700\u8fd1N\u4e2a\u533a\u5757\u7684\u51fa\u5757\u5730\u5740/Get all node out-of-block addresses or specify N block out-of-block designations",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getAgentAddressList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getAgentChangeInfo": {
               "MethodDescription": "get seed nodes list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getAgentChangeInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getAgentInfo": {
               "MethodDescription": "\u67e5\u8be2\u6307\u70b9\u8282\u70b9\u8282\u70b9\u8be6\u7ec6\u4fe1\u606f/Query pointer node details",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getAgentInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getAgentList": {
               "MethodDescription": "\u67e5\u8be2\u5f53\u524d\u7f51\u7edc\u4e2d\u7684\u5171\u8bc6\u8282\u70b9\u5217\u8868/Query the list of consensus nodes in the current network",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getAgentList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "keyWord",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getAgentStatus": {
               "MethodDescription": "\u67e5\u8be2\u6307\u5b9a\u5171\u8bc6\u8282\u70b9\u72b6\u6001/query the specified consensus node status 1.0",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getAgentStatus",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getConsensusConfig": {
               "MethodDescription": "\u83b7\u53d6\u5171\u8bc6\u6a21\u5757\u914d\u7f6e\u4fe1\u606f/get consensus config",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getConsensusConfig",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getContractAgentInfo": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u8282\u70b9/contract get agent info",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getContractAgentInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getContractDepositInfo": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u67e5\u8be2\u6307\u5b9a\u8d26\u6237\u59d4\u6258\u4fe1\u606f/Intelligent Contract Query for Assigned Account Delegation Information",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getContractDepositInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "joinAgentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getDepositList": {
               "MethodDescription": "\u67e5\u8be2\u6307\u5b9a\u8d26\u6237\u6216\u6307\u5b9a\u8282\u70b9\u7684\u59d4\u6258\u4fe1\u606f/Query delegation information for a specified account or node",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getDepositList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getInfo": {
               "MethodDescription": "\u67e5\u8be2\u6307\u5b9a\u8d26\u6237\u5171\u8bc6\u6570\u636e/query consensus information for specified accounts",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getNodePackingAddress": {
               "MethodDescription": "\u83b7\u53d6\u5f53\u524d\u8282\u70b9\u51fa\u5757\u5730\u5740/Get the current node's out-of-block address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getNodePackingAddress",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getPackerInfo": {
               "MethodDescription": "\u83b7\u53d6\u5f53\u524d\u8282\u70b9\u7684\u51fa\u5757\u8d26\u6237\u4fe1\u606f/modifying the Packing State of Nodes",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getPackerInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getPublishList": {
               "MethodDescription": "\u67e5\u8be2\u7ea2\u9ec4\u724c\u8bb0\u5f55/query punish list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getPublishList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "type",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getRoundInfo": {
               "MethodDescription": "\u83b7\u53d6\u5f53\u524d\u8f6e\u6b21\u4fe1\u606f/get current round information",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getRoundInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getRoundMemberList": {
               "MethodDescription": "\u67e5\u8be2\u6307\u5b9a\u533a\u5757\u6240\u5728\u8f6e\u6b21\u7684\u6210\u5458\u5217\u8868/Query the membership list of the specified block's rounds",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getRoundMemberList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "extend",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getSeedNodeInfo": {
               "MethodDescription": "\u83b7\u53d6\u79cd\u5b50\u8282\u70b9\u4fe1\u606f/get seed node info",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getSeedNodeInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getWholeInfo": {
               "MethodDescription": "\u67e5\u8be2\u5168\u7f51\u5171\u8bc6\u6570\u636e/query the consensus information of the whole network",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getWholeInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_multiDeposit": {
               "MethodDescription": "\u591a\u7b7e\u8d26\u6237\u59d4\u6258\u5171\u8bc6/Multi-Sign Account deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_multiDeposit",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_multiWithdraw": {
               "MethodDescription": "\u591a\u7b7e\u8d26\u6237\u9000\u51fa\u5171\u8bc6/Multi-Sign Account withdraw deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_multiWithdraw",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_random_raw_seeds_count": {
               "MethodDescription": "\u6839\u636e\u9ad8\u5ea6\u67e5\u627e\u539f\u59cb\u79cd\u5b50\u5217\u8868\u5e76\u8fd4\u56de",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_random_raw_seeds_count",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "count",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_random_raw_seeds_height": {
               "MethodDescription": "\u6839\u636e\u9ad8\u5ea6\u533a\u95f4\u67e5\u8be2\u539f\u59cb\u79cd\u5b50\u5217\u8868\u5e76\u8fd4\u56de",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_random_raw_seeds_height",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "startHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "endHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_random_seed_count": {
               "MethodDescription": "\u6839\u636e\u9ad8\u5ea6\u548c\u539f\u59cb\u79cd\u5b50\u4e2a\u6570\u751f\u6210\u4e00\u4e2a\u968f\u673a\u79cd\u5b50\u5e76\u8fd4\u56de",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_random_seed_count",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "count",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "algorithm",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_random_seed_height": {
               "MethodDescription": "\u6839\u636e\u9ad8\u5ea6\u533a\u95f4\u751f\u6210\u4e00\u4e2a\u968f\u673a\u79cd\u5b50\u5e76\u8fd4\u56de",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_random_seed_height",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "startHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "endHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "algorithm",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_receiveHeaderList": {
               "MethodDescription": "\u63a5\u6536\u5e76\u7f13\u5b58\u533a\u5757\u5217\u8868/Receive and cache block lists",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_receiveHeaderList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "headerList",
                     "ParameterType": "List<String>",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_runChain": {
               "MethodDescription": "Running a sub chain 1.0",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_runChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_runMainChain": {
               "MethodDescription": "run main chain 1.0",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_runMainChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_stopAgent": {
               "MethodDescription": "\u6ce8\u9500\u8282\u70b9/stop agent",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_stopAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_stopChain": {
               "MethodDescription": "stop a chain 1.0",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_stopChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_stopContractAgent": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u6ce8\u9500\u8282\u70b9/contract stop agent",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_stopContractAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractBalance",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractNonce",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_stopMultiAgent": {
               "MethodDescription": "\u591a\u7b7e\u8d26\u6237\u6ce8\u9500\u8282\u70b9/Multi-Sign Account stop agent",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_stopMultiAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_triggerCoinBaseContract": {
               "MethodDescription": "\u4ea4\u6613\u6a21\u5757\u89e6\u53d1CoinBase\u667a\u80fd\u5408\u7ea6/trigger coin base contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_triggerCoinBaseContract",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "stateRoot",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_updateAgentConsensusStatus": {
               "MethodDescription": "\u4fee\u6539\u8282\u70b9\u5171\u8bc6\u72b6\u6001/modifying the Node Consensus State",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_updateAgentConsensusStatus",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_updateAgentStatus": {
               "MethodDescription": "\u4fee\u6539\u8282\u70b9\u6253\u5305\u72b6\u6001/modifying the Packing State of Nodes",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_updateAgentStatus",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "status",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_validBlock": {
               "MethodDescription": "\u9a8c\u8bc1\u533a\u5757/verify block correctness",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_validBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "download",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "block",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_withdraw": {
               "MethodDescription": "\u9000\u51fa\u59d4\u6258\u4ea4\u6613/withdraw deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_withdraw",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.depositValid": {
               "MethodDescription": "deposit agent transaction validate",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "depositValid",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getAssetsById": {
               "MethodDescription": "\u67e5\u8be2\u94fe\u4e0b\u6307\u5b9a\u8d44\u4ea7\u96c6\u5408\u7684\u91d1\u989d\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getAssetsById",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetIds",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBalance": {
               "MethodDescription": "\u83b7\u53d6\u8d26\u6237\u8d44\u4ea7(\u5df2\u5165\u533a\u5757)",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBalance",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBalanceNonce": {
               "MethodDescription": "\u83b7\u53d6\u8d26\u6237\u8d44\u4ea7\u4f59\u989d\u4e0eNONCE\u503c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBalanceNonce",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isConfirmed",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockByHash": {
               "MethodDescription": "get a block by hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockByHash",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockByHeight": {
               "MethodDescription": "get a block by height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockByHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeaderByHash": {
               "MethodDescription": "get a block header by hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeaderByHash",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeaderByHeight": {
               "MethodDescription": "get a block header by height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeaderByHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeaderPoByHash": {
               "MethodDescription": "get a block header po by hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeaderPoByHash",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeaderPoByHeight": {
               "MethodDescription": "get a block header po by height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeaderPoByHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeadersByHeightRange": {
               "MethodDescription": "get the block headers according to the height range",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeadersByHeightRange",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "begin",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "end",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeadersForProtocol": {
               "MethodDescription": "get block headers for protocol upgrade module",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeadersForProtocol",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "interval",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getByzantineCount": {
               "MethodDescription": "\u67e5\u8be2\u5f53\u524d\u7b7e\u540d\u62dc\u5360\u5ead\u6700\u5c0f\u901a\u8fc7\u6570\u91cf/\u67e5\u8be2\u5f53\u524d\u7b7e\u540d\u62dc\u5360\u5ead\u6700\u5c0f\u901a\u8fc7\u6570\u91cf",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getByzantineCount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getChains": {
               "MethodDescription": "cancel Cross Chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getChains",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getCirculat": {
               "MethodDescription": "\u67e5\u8be2\u672c\u94fe\u8d44\u4ea7\u4fe1\u606f\u6d88\u606f/get chain circulation",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getCirculat",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getCrossChainInfos": {
               "MethodDescription": "\u83b7\u53d6\u8de8\u94fe\u6ce8\u518c\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getCrossChainInfos",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.getCrossTxState": {
               "MethodDescription": "\u67e5\u8be2\u8de8\u94fe\u4ea4\u6613\u5904\u7406\u72b6\u6001/get cross transaction process state",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getCrossTxState",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getCtx": {
               "MethodDescription": "\u94fe\u5185\u8282\u70b9\u5411\u672c\u8282\u70b9\u83b7\u53d6\u5b8c\u6210\u8de8\u94fe\u4ea4\u6613/The intra-chain node acquires and completes the cross-chain transaction from its own node",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getCtx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getCtxState": {
               "MethodDescription": "\u83b7\u53d6\u8de8\u94fe\u4ea4\u6613\u5904\u7406\u72b6\u6001/Getting the state of cross-chain transaction processing",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getCtxState",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getFreezeList": {
               "MethodDescription": "\u5206\u9875\u83b7\u53d6\u8d26\u6237\u9501\u5b9a\u8d44\u4ea7\u5217\u8868",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getFreezeList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getFriendChainCirculate": {
               "MethodDescription": "\u83b7\u53d6\u53cb\u94fe\u8d44\u4ea7\u4fe1\u606f/Access to Friendship Chain Asset Information",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getFriendChainCirculate",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetIds",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getLatestBlockHeaders": {
               "MethodDescription": "get the latest number of block headers",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getLatestBlockHeaders",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "size",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getLatestRoundBlockHeaders": {
               "MethodDescription": "get the latest several rounds of block headers",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getLatestRoundBlockHeaders",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "round",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getNonce": {
               "MethodDescription": "\u83b7\u53d6\u8d26\u6237\u8d44\u4ea7NONCE\u503c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getNonce",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isConfirmed",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getOtherCtx": {
               "MethodDescription": "\u8de8\u94fe\u8282\u70b9\u5411\u672c\u8282\u70b9\u83b7\u53d6\u5b8c\u6574\u4ea4\u6613/Cross-chain nodes obtain complete transactions from their own nodes",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getOtherCtx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getRegisteredChainInfoList": {
               "MethodDescription": "\u67e5\u8be2\u5728\u4e3b\u7f51\u4e0a\u6ce8\u518c\u8de8\u94fe\u7684\u94fe\u4fe1\u606f/Query for cross-chain chain information registered on the main network",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getRegisteredChainInfoList",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.getRoundBlockHeaders": {
               "MethodDescription": "get the latest several rounds of block headers",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getRoundBlockHeaders",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "round",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getStatus": {
               "MethodDescription": "receive the new packaged block",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getStatus",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getVersion": {
               "MethodDescription": "get mainnet version",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getVersion",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.info": {
               "MethodDescription": "returns network node height and local node height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "info",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.latestBlock": {
               "MethodDescription": "the latest block of master chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "latestBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.latestBlockHeader": {
               "MethodDescription": "the latest block header of master chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "latestBlockHeader",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.latestBlockHeaderPo": {
               "MethodDescription": "the latest block header po of master chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "latestBlockHeaderPo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.latestHeight": {
               "MethodDescription": "the latest height of master chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "latestHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.listenerDependenciesReady": {
               "MethodDescription": "notify module is ready",
               "MethodMinEvent": "1",
               "MethodMinPeriod": "0",
               "MethodName": "listenerDependenciesReady",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nuls.msgProcess": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "msgProcess",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "cmd",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.newApiModuleCrossTx": {
               "MethodDescription": "\u63a5\u6536API_MODULE\u7ec4\u88c5\u7684\u8de8\u94fe\u4ea4\u6613/Receiving cross-chain transactions assembled by API_MODULE",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "newApiModuleCrossTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.newBlockHeight": {
               "MethodDescription": "\u94fe\u533a\u5757\u9ad8\u5ea6\u53d8\u66f4/receive new block height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "newBlockHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_activeCross": {
               "MethodDescription": "\u8de8\u94fe\u534f\u8bae\u6a21\u5757\u6fc0\u6d3b\u8de8\u94fe",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_activeCross",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxOut",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxIn",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "seedIps",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_addNodes": {
               "MethodDescription": "\u589e\u52a0\u5f85\u8fde\u63a5\u8282\u70b9",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_addNodes",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isCross",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodes",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_broadcast": {
               "MethodDescription": "\u5e7f\u64ad\u6d88\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_broadcast",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "excludeNodes",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "command",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isCross",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "percent",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_createNodeGroup": {
               "MethodDescription": "\u4e3b\u7f51\u521b\u5efa\u8de8\u94fe\u7f51\u7edc\u6216\u8005\u94fe\u5de5\u5382\u521b\u5efa\u94fe",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_createNodeGroup",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "magicNumber",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxOut",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxIn",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "minAvailableCount",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isCrossGroup",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_currentTimeMillis": {
               "MethodDescription": "\u83b7\u53d6\u8282\u70b9\u7f51\u7edc\u65f6\u95f4",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_currentTimeMillis",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.nw_delNodeGroup": {
               "MethodDescription": "\u5220\u9664\u6307\u5b9a\u7f51\u7edc\u7ec4",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_delNodeGroup",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_delNodes": {
               "MethodDescription": "\u5220\u9664\u8282\u70b9\u7ec4\u8282\u70b9",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_delNodes",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodes",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_getChainConnectAmount": {
               "MethodDescription": "\u83b7\u53d6\u6307\u5b9a\u7f51\u7edc\u7ec4\u53ef\u8fde\u63a5\u6570\u91cf",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getChainConnectAmount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isCross",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_getGroupByChainId": {
               "MethodDescription": "\u83b7\u53d6\u8282\u70b9\u7ec4\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getGroupByChainId",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_getGroups": {
               "MethodDescription": "\u5206\u9875\u83b7\u53d6\u7f51\u7edc\u7ec4\u4fe1\u606f,startPage\u4e0epageSize \u90fd\u4e3a0\u65f6\uff0c\u4e0d\u5206\u9875\uff0c\u8fd4\u56de\u6240\u6709\u7f51\u7edc\u7ec4\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getGroups",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "startPage",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_getMainMagicNumber": {
               "MethodDescription": "\u67e5\u770b\u4e3b\u7f51\u7684\u9b54\u6cd5\u53c2\u6570",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getMainMagicNumber",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.nw_getNodes": {
               "MethodDescription": "\u5206\u9875\u67e5\u770b\u8fde\u63a5\u8282\u70b9\u4fe1\u606f,startPage\u4e0epageSize \u90fd\u4e3a0\u65f6\uff0c\u4e0d\u5206\u9875\uff0c\u8fd4\u56de\u6240\u6709\u8282\u70b9\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getNodes",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "state",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isCross",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "startPage",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_getSeeds": {
               "MethodDescription": "\u67e5\u770b\u8de8\u94fe\u7f51\u7edc\u63d0\u4f9b\u7684\u79cd\u5b50\u8282\u70b9",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getSeeds",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.nw_info": {
               "MethodDescription": "\u83b7\u53d6\u8282\u70b9\u7f51\u7edc\u57fa\u672c\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_info",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_nodes": {
               "MethodDescription": "\u83b7\u53d6\u7f51\u7edc\u8fde\u63a5\u8282\u70b9\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_nodes",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_protocolRegister": {
               "MethodDescription": "\u6a21\u5757\u534f\u8bae\u6307\u4ee4\u6ce8\u518c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_protocolRegister",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "role",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "protocolCmds",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_reconnect": {
               "MethodDescription": "\u672c\u5730\u7f51\u7edc\u91cd\u542f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_reconnect",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_sendPeersMsg": {
               "MethodDescription": "\u5411\u6307\u5b9a\u8282\u70b9\u53d1\u9001\u6d88\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_sendPeersMsg",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodes",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "command",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_updateNodeInfo": {
               "MethodDescription": "\u66f4\u65b0\u8fde\u63a5\u8282\u70b9\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_updateNodeInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.paramTestCmd": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "paramTestCmd",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "intCount",
                     "ParameterType": "int",
                     "ParameterValidRange": "[0,65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "byteCount",
                     "ParameterType": "byte",
                     "ParameterValidRange": "[-128,127]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "shortCount",
                     "ParameterType": "short",
                     "ParameterValidRange": "[0,32767]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "longCount",
                     "ParameterType": "long",
                     "ParameterValidRange": "[0,55555555]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.protocolRegisterWithPriority": {
               "MethodDescription": "\u6a21\u5757\u534f\u8bae\u6307\u4ee4\u6ce8\u518c\uff0c\u5e26\u6709\u4f18\u5148\u7ea7\u53c2\u6570",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "protocolRegisterWithPriority",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "role",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "protocolCmds",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.protocolVersionChange": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "protocolVersionChange",
               "MethodScope": "private",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "protocolVersion",
                     "ParameterType": "short",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.receivePackingBlock": {
               "MethodDescription": "receive the new packaged block",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "receivePackingBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "block",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvCirculat": {
               "MethodDescription": "\u63a5\u6536\u5176\u4ed6\u94fe\u8282\u70b9\u53d1\u9001\u7684\u8d44\u4ea7\u4fe1\u606f/Receiving asset information sent by other link nodes",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvCirculat",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvCtx": {
               "MethodDescription": "\u63a5\u6536\u672c\u94fe\u8282\u70b9\u5e7f\u64ad\u7684\u5b8c\u6574\u4ea4\u6613/Complete Transaction for Receiving Broadcast from Local Chain Nodes",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvCtx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvCtxHash": {
               "MethodDescription": "\u63a5\u6536\u8de8\u94fe\u8282\u70b9\u5e7f\u64ad\u7684\u4ea4\u6613Hash/Transaction Hash receiving cross-link node broadcasting",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvCtxHash",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvCtxSign": {
               "MethodDescription": "\u63a5\u6536\u94fe\u5185\u8282\u70b9\u5e7f\u64ad\u7684\u4ea4\u6613\u7b7e\u540d/Transaction signature for broadcasting in receiving chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvCtxSign",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvCtxState": {
               "MethodDescription": "\u8de8\u94fe\u4ea4\u6613\u5904\u7406\u72b6\u6001\u6d88\u606f/receive cross transaction state",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvCtxState",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvOtherCtx": {
               "MethodDescription": "\u63a5\u6536\u8de8\u94fe\u8282\u70b9\u5e7f\u64ad\u7684\u5b8c\u6574\u4ea4\u6613/Receiving Complete Transactions for Cross-Chain Node Broadcasting",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvOtherCtx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvRegChain": {
               "MethodDescription": "\u63a5\u6536\u5230\u4e3b\u7f51\u8fd4\u56de\u7684\u5df2\u6ce8\u518c\u8de8\u94fe\u4ea4\u6613\u7684\u94fe\u4fe1\u606f/Receiving chain information of registered cross-chain transactions returned from the main network",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvRegChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.registerAsset": {
               "MethodDescription": "\u94fe\u6ce8\u518c\u8de8\u94fe/register Cross Chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "registerAsset",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "symbol",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "usable",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "decimalPlaces",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.registerCrossChain": {
               "MethodDescription": "\u94fe\u6ce8\u518c\u8de8\u94fe/register Cross Chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "registerCrossChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "chainName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "minAvailableNodeNum",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetInfoList",
                     "ParameterType": "List<AssetInfo>",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "registerTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.registerModuleDependencies": {
               "MethodDescription": "Register module followerList",
               "MethodMinEvent": "1",
               "MethodMinPeriod": "0",
               "MethodName": "registerModuleDependencies",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nuls.registerProtocol": {
               "MethodDescription": "register protocol",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "registerProtocol",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "moduleCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "list",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.rollBackBlockTxs": {
               "MethodDescription": "\u533a\u5757\u56de\u6eda",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "rollBackBlockTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.rollBackUnconfirmTx": {
               "MethodDescription": "\u56de\u6eda\u63d0\u4ea4\u7684\u672a\u786e\u8ba4\u4ea4\u6613",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "rollBackUnconfirmTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.rollbackBlock": {
               "MethodDescription": "rollback block header",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "rollbackBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.rollbackTxValidateStatus": {
               "MethodDescription": "\u56de\u6eda\u6253\u5305\u6821\u9a8c\u72b6\u6001",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "rollbackTxValidateStatus",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.saveBlock": {
               "MethodDescription": "save block header",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "saveBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_account_contracts": {
               "MethodDescription": "\u8d26\u6237\u7684\u5408\u7ea6\u5730\u5740\u5217\u8868/account contract list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_account_contracts",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_batch_before_end": {
               "MethodDescription": "\u4ea4\u6613\u6a21\u5757\u6253\u5305\u5b8c\u4ea4\u6613\uff0c\u5728\u505a\u7edf\u4e00\u9a8c\u8bc1\u524d\uff0c\u901a\u77e5\u5408\u7ea6\u6a21\u5757\uff0c\u5408\u7ea6\u6a21\u5757\u505c\u6b62\u63a5\u6536\u4ea4\u6613\uff0c\u5f00\u59cb\u5f02\u6b65\u5904\u7406\u8fd9\u4e2a\u6279\u6b21\u7684\u7ed3\u679c/batch before end",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_batch_before_end",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockType",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_batch_begin": {
               "MethodDescription": "\u6267\u884c\u5408\u7ea6\u4e00\u4e2a\u6279\u6b21\u7684\u5f00\u59cb\u901a\u77e5\uff0c\u751f\u6210\u5f53\u524d\u6279\u6b21\u7684\u4fe1\u606f/batch begin",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_batch_begin",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockType",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packingAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "preStateRoot",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_batch_end": {
               "MethodDescription": "\u901a\u77e5\u5f53\u524d\u6279\u6b21\u7ed3\u675f\u5e76\u8fd4\u56de\u7ed3\u679c/batch end",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_batch_end",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_call": {
               "MethodDescription": "call contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_call",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "value",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "gasLimit",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "price",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodDesc",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_call_validator": {
               "MethodDescription": "call contract validator",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_call_validator",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_constructor": {
               "MethodDescription": "contract code constructor",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_constructor",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_contract_info": {
               "MethodDescription": "\u5408\u7ea6\u4fe1\u606f\u8be6\u60c5/contract info",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_contract_info",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_contract_offline_tx_hash_list": {
               "MethodDescription": "\u8fd4\u56de\u6307\u5b9a\u533a\u5757\u4e2d\u5408\u7ea6\u751f\u6210\u4ea4\u6613\uff08\u5408\u7ea6\u8fd4\u56deGAS\u4ea4\u6613\u9664\u5916\uff09\u7684hash\u5217\u8868\uff08\u5408\u7ea6\u65b0\u751f\u6210\u7684\u4ea4\u6613\u9664\u5408\u7ea6\u8fd4\u56deGAS\u4ea4\u6613\u5916\uff0c\u4e0d\u4fdd\u5b58\u5230\u533a\u5757\u4e2d\uff0c\u5408\u7ea6\u6a21\u5757\u4fdd\u5b58\u4e86\u8fd9\u4e9b\u4ea4\u6613\u548c\u6307\u5b9a\u533a\u5757\u7684\u5173\u7cfb\uff09/contract offline tx hash list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_contract_offline_tx_hash_list",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_contract_result": {
               "MethodDescription": "contract result",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_contract_result",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_contract_result_list": {
               "MethodDescription": "contract result list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_contract_result_list",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hashList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_contract_tx": {
               "MethodDescription": "\u5408\u7ea6\u4ea4\u6613/contract tx",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_contract_tx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_create": {
               "MethodDescription": "\u53d1\u5e03\u5408\u7ea6/create contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_create",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "alias",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "gasLimit",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "price",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_create_validator": {
               "MethodDescription": "create contract validator",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_create_validator",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_delete": {
               "MethodDescription": "delete contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_delete",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_delete_validator": {
               "MethodDescription": "delete contract validator",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_delete_validator",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_imputed_call_gas": {
               "MethodDescription": "imputed call gas",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_imputed_call_gas",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "value",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodDesc",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_imputed_create_gas": {
               "MethodDescription": "\u9884\u4f30\u53d1\u5e03\u5408\u7ea6\u6d88\u8017\u7684GAS/imputed create gas",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_imputed_create_gas",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_initial_account_token": {
               "MethodDescription": "\u521d\u59cb\u5316\u8d26\u6237token\u4fe1\u606f\uff0c\u8282\u70b9\u5bfc\u5165\u8d26\u6237\u65f6\u8c03\u7528/initial account token",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_initial_account_token",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_invoke_contract": {
               "MethodDescription": "\u6279\u6b21\u901a\u77e5\u5f00\u59cb\u540e\uff0c\u4e00\u7b14\u4e00\u7b14\u6267\u884c\u5408\u7ea6/invoke contract one by one",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_invoke_contract",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockType",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_invoke_view": {
               "MethodDescription": "invoke view contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_invoke_view",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodDesc",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_package_batch_end": {
               "MethodDescription": "\u6253\u5305\u7ed3\u675f - \u901a\u77e5\u5f53\u524d\u6279\u6b21\u7ed3\u675f\u5e76\u8fd4\u56de\u7ed3\u679c/batch end",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_package_batch_end",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_register_cmd_for_contract": {
               "MethodDescription": "\u5176\u4ed6\u6a21\u5757\u5411\u5408\u7ea6\u6a21\u5757\u6ce8\u518c\u53ef\u88ab\u5408\u7ea6\u8c03\u7528\u7684\u547d\u4ee4\uff0c\u6ce8\u518c\u540e\uff0c\u53ef\u5728\u5408\u7ea6\u4ee3\u7801\u5185\u8c03\u7528\u6ce8\u518c\u7684\u547d\u4ee4/register cmd for contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_register_cmd_for_contract",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "moduleCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "cmdRegisterList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_token_assets_list": {
               "MethodDescription": "token\u8d44\u4ea7\u96c6\u5408/token assets list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_token_assets_list",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_token_balance": {
               "MethodDescription": "NRC20\u4ee3\u5e01\u4f59\u989d\u8be6\u60c5/NRC20-token balance",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_token_balance",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_token_transfer": {
               "MethodDescription": "NRC20-token\u8f6c\u8d26/transfer NRC20-token from address to toAddress",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_token_transfer",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "toAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "amount",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_token_transfer_list": {
               "MethodDescription": "token\u8f6c\u8d26\u4ea4\u6613\u5217\u8868/token transfer list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_token_transfer_list",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_transfer": {
               "MethodDescription": "\u4ece\u8d26\u6237\u5730\u5740\u5411\u5408\u7ea6\u5730\u5740\u8f6c\u8d26(\u4e3b\u94fe\u8d44\u4ea7)/transfer NULS from sender to contract address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_transfer",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "toAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "amount",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_trigger_payable_for_consensus_contract": {
               "MethodDescription": "\u5171\u8bc6\u5956\u52b1\u6536\u76ca\u5730\u5740\u662f\u5408\u7ea6\u5730\u5740\u65f6\uff0c\u4f1a\u89e6\u53d1\u5408\u7ea6\u7684_payable(String[][] args)\u65b9\u6cd5\uff0c\u53c2\u6570\u662f\u8282\u70b9\u6536\u76ca\u5730\u5740\u660e\u7ec6<br>args[0] = new String[]{address, amount}<br>...<br>/trigger payable for consensus contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_trigger_payable_for_consensus_contract",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "stateRoot",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "Long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_upload": {
               "MethodDescription": "\u5408\u7ea6\u4ee3\u7801jar\u5305\u4e0a\u4f20/upload",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_upload",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "jarFileData",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_validate_call": {
               "MethodDescription": "validate call contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_validate_call",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "value",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "gasLimit",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "price",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodDesc",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_validate_create": {
               "MethodDescription": "\u9a8c\u8bc1\u53d1\u5e03\u5408\u7ea6/validate create contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_validate_create",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "gasLimit",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "price",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_validate_delete": {
               "MethodDescription": "validate delete contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_validate_delete",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.stopAgentValid": {
               "MethodDescription": "stop agent transaction validate",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "stopAgentValid",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.txCommit": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "txCommit",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.txRollback": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "txRollback",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.txValidator": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "txValidator",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_backPackableTxs": {
               "MethodDescription": "\u5171\u8bc6\u6a21\u5757\u628a\u4e0d\u80fd\u6253\u5305\u7684\u4ea4\u6613\u8fd8\u56de\u6765\uff0c\u91cd\u65b0\u52a0\u5165\u5f85\u6253\u5305\u5217\u8868/back packaged transactions",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_backPackableTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_batchVerify": {
               "MethodDescription": "\u9a8c\u8bc1\u533a\u5757\u6240\u6709\u4ea4\u6613/Verify all transactions in the block",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_batchVerify",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "preStateRoot",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_bl_state": {
               "MethodDescription": "\u8bbe\u7f6e\u8282\u70b9\u533a\u5757\u540c\u6b65\u72b6\u6001(\u7531\u533a\u5757\u6a21\u5757\u8bbe\u7f6e)/Set the node block state",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_bl_state",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "status",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_blockHeight": {
               "MethodDescription": "\u63a5\u6536\u6700\u65b0\u533a\u5757\u9ad8\u5ea6/Receive the latest block height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_blockHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_cs_state": {
               "MethodDescription": "\u8bbe\u7f6e\u8282\u70b9\u6253\u5305\u72b6\u6001(\u7531\u5171\u8bc6\u6a21\u5757\u8bbe\u7f6e)/Set the node packaging state",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_cs_state",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packaging",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_gengsisSave": {
               "MethodDescription": "\u4fdd\u5b58\u521b\u4e16\u5757\u7684\u4ea4\u6613/Save the transactions of the Genesis block ",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_gengsisSave",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getBlockTxs": {
               "MethodDescription": "\u83b7\u53d6\u533a\u5757\u7684\u5b8c\u6574\u4ea4\u6613\uff0c\u5982\u679c\u6ca1\u6709\u67e5\u8be2\u5230\uff0c\u6216\u8005\u67e5\u8be2\u5230\u7684\u4e0d\u662f\u533a\u5757\u5b8c\u6574\u7684\u4ea4\u6613\u6570\u636e\uff0c\u5219\u8fd4\u56de\u7a7a\u96c6\u5408/Get block transactions",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getBlockTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHashList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getBlockTxsExtend": {
               "MethodDescription": "\u6839\u636ehash\u5217\u8868\uff0c\u83b7\u53d6\u4ea4\u6613\uff0c\u5148\u67e5\u672a\u786e\u8ba4\uff0c\u518d\u67e5\u5df2\u786e\u8ba4/Get transactions by hashs",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getBlockTxsExtend",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHashList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "allHits",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getConfirmedTx": {
               "MethodDescription": "\u6839\u636ehash\u83b7\u53d6\u5df2\u786e\u8ba4\u4ea4\u6613(\u53ea\u67e5\u5df2\u786e\u8ba4)/Get confirmed transaction by tx hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getConfirmedTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getConfirmedTxClient": {
               "MethodDescription": "\u6839\u636ehash\u83b7\u53d6\u5df2\u786e\u8ba4\u4ea4\u6613(\u53ea\u67e5\u5df2\u786e\u8ba4)/Get confirmed transaction by tx hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getConfirmedTxClient",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getNonexistentUnconfirmedHashs": {
               "MethodDescription": "\u67e5\u8be2\u4f20\u5165\u7684\u4ea4\u6613hash\u4e2d,\u4e0d\u5728\u672a\u786e\u8ba4\u5e93\u4e2d\u7684\u4ea4\u6613hash/Get nonexistent unconfirmed transaction hashs",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getNonexistentUnconfirmedHashs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHashList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getSystemTypes": {
               "MethodDescription": "\u83b7\u53d6\u6240\u6709\u7cfb\u7edf\u4ea4\u6613\u7c7b\u578b/Get system transaction types",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getSystemTypes",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getTx": {
               "MethodDescription": "\u6839\u636ehash\u83b7\u53d6\u4ea4\u6613, \u5148\u67e5\u672a\u786e\u8ba4, \u67e5\u4e0d\u5230\u518d\u67e5\u5df2\u786e\u8ba4/Get transaction by tx hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getTxClient": {
               "MethodDescription": "\u6839\u636ehash\u83b7\u53d6\u4ea4\u6613\uff0c\u5148\u67e5\u672a\u786e\u8ba4\uff0c\u67e5\u4e0d\u5230\u518d\u67e5\u5df2\u786e\u8ba4/Get transaction by tx hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getTxClient",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_newTx": {
               "MethodDescription": "\u63a5\u6536\u672c\u5730\u65b0\u4ea4\u6613/receive a new transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_newTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_packableTxs": {
               "MethodDescription": "\u83b7\u53d6\u53ef\u6253\u5305\u7684\u4ea4\u6613\u96c6/returns a list of packaged transactions",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_packableTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "endTimestamp",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxTxDataSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packingAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "preStateRoot",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_register": {
               "MethodDescription": "\u6ce8\u518c\u6a21\u5757\u4ea4\u6613/Register module transactions",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_register",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "moduleCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "list",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "delList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_rollback": {
               "MethodDescription": "\u56de\u6eda\u533a\u5757\u7684\u4ea4\u6613/transaction rollback",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_rollback",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHashList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_save": {
               "MethodDescription": "\u4fdd\u5b58\u65b0\u533a\u5757\u7684\u4ea4\u6613/Save the confirmed transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_save",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_verifyTx": {
               "MethodDescription": "\u9a8c\u8bc1\u4ea4\u6613\u63a5\u53e3\uff0c\u5305\u62ec\u542b\u57fa\u7840\u9a8c\u8bc1\u3001\u9a8c\u8bc1\u5668\u3001\u8d26\u672c\u9a8c\u8bc1/Verify transation",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_verifyTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.updateChainAsset": {
               "MethodDescription": "\u67e5\u8be2\u66f4\u65b0\u6d41\u901a\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "updateChainAsset",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assets",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.verifyCoinData": {
               "MethodDescription": "\u672a\u786e\u8ba4\u4ea4\u6613\u6821\u9a8c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "verifyCoinData",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.verifyCoinDataBatchPackaged": {
               "MethodDescription": "\u6253\u5305\u4ea4\u6613\u6821\u9a8c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "verifyCoinDataBatchPackaged",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.withdrawValid": {
               "MethodDescription": "withdraw deposit agent transaction validate",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "withdrawValid",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nulstar.ForwardMessage": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ForwardMessage",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nulstar.GetCPUInfo": {
               "MethodDescription": "Query information about CPU",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "GetCPUInfo",
               "MethodScope": "admin",
               "Parameters": [
                  {
                     "ParameterName": "lMaxCPUs",
                     "ParameterType": "int"
                  }
               ]
            },
            "Nulstar.GetConsolidatedAPI": {
               "MethodDescription": "",
               "MethodMinEvent": "1",
               "MethodMinPeriod": "0",
               "MethodName": "GetConsolidatedAPI",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nulstar.GetRAMInfo": {
               "MethodDescription": "Query information about RAM memory",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "GetRAMInfo",
               "MethodScope": "admin",
               "Parameters": []
            },
            "Nulstar.ListAPI": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ListAPI",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nulstar.RegisterAPI": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "RegisterAPI",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nulstar.checkupdates": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "checkupdates",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nulstar.scanmanagedmodules": {
               "MethodDescription": "Searches and reads the configuration file Module.ncf in the directory hierarchy.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "scanmanagedmodules",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nulstar.shutdownsystem": {
               "MethodDescription": "Stops the system enterily.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "shutdownsystem",
               "MethodScope": "admin",
               "Parameters": []
            },
            "Nulstar.startallmodules": {
               "MethodDescription": "Starts modules of the desired namespace, if blank then all available modules are started.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "startallmodules",
               "MethodScope": "private",
               "Parameters": [
                  {
                     "ParameterName": "fRestartIfRunning",
                     "ParameterType": "bool",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nulstar.startmodule": {
               "MethodDescription": "Starts the specified module.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "startmodule",
               "MethodScope": "private",
               "Parameters": [
                  {
                     "ParameterName": "lModuleName",
                     "ParameterType": "QString",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "lModuleVersion",
                     "ParameterType": "QString",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "fRestartIfRunning",
                     "ParameterType": "bool",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nulstar.stopallmodules": {
               "MethodDescription": "Stops all modules belonging to the specified namespace, if blank it stops all modules that are currently running.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "stopallmodules",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nulstar.stopmodule": {
               "MethodDescription": "Stops the specified module.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "stopmodule",
               "MethodScope": "private",
               "Parameters": [
                  {
                     "ParameterName": "lModuleName",
                     "ParameterType": "QString",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "lModuleVersion",
                     "ParameterType": "QString",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            }
         }
      },
      "ResponseErrorCode": "",
      "ResponseMaxSize": "0",
      "ResponseProcessingTime": "1",
      "ResponseStatus": 0
   },
   "MessageID": "1575848916688-8",
   "MessageType": "Response",
   "TimeZone": "-8",
   "Timestamp": "1575884636505"
}
--------------end Regular request--------------------------------

Process finished with exit code 0
/usr/local/bin/python3.7 /home/admin/workspace/pywebsockets/nulsws_client.py
the url:   ws://127.0.0.1:7772
* * * First message going out- Negotiate: 
{
   "ProtocolVersion": "0.1",
   "MessageID": "157588462348558-1",
   "Timestamp": 157588462348558,
   "TimeZone": 8,
   "MessageType": "NegotiateConnection",
   "MessageData": {
      "ProtocolVersion": "0.1",
      "CompressionAlgorithm": "zlib",
      "CompressionRate": 0
   }
}
! ! ! Negotiate response is this: 
{
   "MessageData": {
      "NegotiationComment": "Negotiation successful!",
      "NegotiationStatus": "1",
      "RequestID": "157588462348558-1"
   },
   "MessageID": "1575848916688-5",
   "MessageType": "NegotiateConnectionResponse",
   "TimeZone": "-8",
   "Timestamp": "1575884626493"
}
------end Negotiate----------------------------------------
* * * _REGISTER_ message going out: 
{
   "ProtocolVersion": "0.1",
   "MessageID": "157588462348564-1",
   "Timestamp": 157588462348564,
   "TimeZone": 8,
   "MessageType": "Request",
   "MessageData": {
      "RequestAck": "0",
      "RequestMethods": {
         "RegisterAPI": {
            "Abbreviation": "NSTM",
            "ConnectionInformation": {
               "IP": "127.0.0.1",
               "Port": "7775"
            },
            "Dependencies": {},
            "Methods": [
               {
                  "MethodDescription": "Query information about CPU",
                  "MethodMinEvent": "0",
                  "MethodMinPeriod": "0",
                  "MethodName": "GetCPUInfo",
                  "MethodScope": "admin",
                  "Parameters": [
                     {
                        "ParameterName": "lMaxCPUs",
                        "ParameterType": "int"
                     }
                  ]
               },
               {
                  "MethodDescription": "Query information about RAM memory",
                  "MethodMinEvent": "0",
                  "MethodMinPeriod": "0",
                  "MethodName": "GetRAMInfo",
                  "MethodScope": "admin",
                  "Parameters": []
               }
            ],
            "ModuleDomain": "Nulstar",
            "ModuleName": "StatsManager",
            "ModuleRoles": {
               "Role_StatsManager": [
                  "0.1"
               ]
            },
            "ModuleVersion": "0.1.0"
         }
      },
      "ResponseMaxSize": "0",
      "SubscriptionEventCounter": "0",
      "SubscriptionPeriod": "0",
      "SubscriptionRange": ""
   }
}
msg just recieved
-------! ! ! _REGISTER_ response received: 
{
   "MessageData": {
      "RequestID": "157588462348564-1",
      "ResponseComment": "",
      "ResponseData": {
         "RegisterAPI": {}
      },
      "ResponseErrorCode": "",
      "ResponseMaxSize": "0",
      "ResponseProcessingTime": "46",
      "ResponseStatus": 0
   },
   "MessageID": "1575848916688-7",
   "MessageType": "Response",
   "TimeZone": "-8",
   "Timestamp": "1575884631545"
}
-----------end _REGISTER_-----------------------------------
* * * REGULAR message going out: 
{
   "ProtocolVersion": "0.1",
   "MessageID": "157588462348569-1",
   "Timestamp": 157588462348569,
   "TimeZone": 8,
   "MessageType": "Request",
   "MessageData": {
      "RequestType": "2",
      "SubscriptionEventCounter": "0",
      "SubscriptionPeriod": "0",
      "SubscriptionRange": "0",
      "ResponseMaxSize": "0",
      "RequestMethods": {
         "ListAPI": {}
      }
   }
}
* * * Sending Regular request going out:

-------! ! ! REGULAR response received: 
{
   "MessageData": {
      "RequestID": "157588462348569-1",
      "ResponseComment": "",
      "ResponseData": {
         "ListAPI": {
            "Nuls.RegisterAPI": {
               "MethodDescription": "Register API",
               "MethodMinEvent": "1",
               "MethodMinPeriod": "0",
               "MethodName": "RegisterAPI",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.ac_addAddressPrefix": {
               "MethodDescription": "\u6dfb\u52a0\u5730\u5740\u524d\u7f00,\u94fe\u7ba1\u7406\u6a21\u5757\u4f1a\u8c03\u7528\u8be5\u63a5\u53e3",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_addAddressPrefix",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "prefixList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_createAccount": {
               "MethodDescription": "\u521b\u5efa\u6307\u5b9a\u4e2a\u6570\u7684\u8d26\u6237/create a specified number of accounts",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_createAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "count",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_createContractAccount": {
               "MethodDescription": "\u521b\u5efa\u667a\u80fd\u5408\u7ea6\u8d26\u6237/create smart contract account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_createContractAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_createMultiSignAccount": {
               "MethodDescription": "\u521b\u5efa\u591a\u7b7e\u8d26\u6237/create a multi sign account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_createMultiSignAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pubKeys",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "minSigns",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_createMultiSignTransfer": {
               "MethodDescription": "\u521b\u5efa\u591a\u7b7e\u5730\u5740\u8f6c\u8d26\u4ea4\u6613/create multi sign transfer",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_createMultiSignTransfer",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "inputs",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "outputs",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signPassword",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_createOfflineAccount": {
               "MethodDescription": "\u521b\u5efa\u79bb\u7ebf\u8d26\u6237, \u8be5\u8d26\u6237\u4e0d\u4fdd\u5b58\u5230\u6570\u636e\u5e93, \u5e76\u5c06\u76f4\u63a5\u8fd4\u56de\u8d26\u6237\u7684\u6240\u6709\u4fe1\u606f/create an offline account, which is not saved to the database and will directly return all information to the account.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_createOfflineAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "count",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_exportAccountKeyStore": {
               "MethodDescription": "\u8d26\u6237\u5907\u4efd\uff0c\u5bfc\u51faAccountKeyStore\u5b57\u7b26\u4e32/export account KeyStore",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_exportAccountKeyStore",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "filePath",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_exportKeyStoreJson": {
               "MethodDescription": "\u5bfc\u51faAccountKeyStore\u5b57\u7b26\u4e32/export account KeyStore json",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_exportKeyStoreJson",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAccountByAddress": {
               "MethodDescription": "\u901a\u8fc7\u5730\u5740\u83b7\u53d6\u8d26\u6237\u4fe1\u606f/get account info according to address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAccountByAddress",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAccountList": {
               "MethodDescription": "\u83b7\u53d6\u6240\u6709\u8d26\u6237\u96c6\u5408,\u5e76\u653e\u5165\u7f13\u5b58/query all account collections and put them in cache",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAccountList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAddressList": {
               "MethodDescription": "\u5206\u9875\u67e5\u8be2\u8d26\u6237\u5730\u5740\u5217\u8868/Paging query account address list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAddressList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAddressPrefixByChainId": {
               "MethodDescription": "\u901a\u8fc7\u94feid\u83b7\u53d6\u5730\u5740\u524d\u7f00",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAddressPrefixByChainId",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAliasByAddress": {
               "MethodDescription": "\u6839\u636e\u5730\u5740\u83b7\u53d6\u522b\u540d/get the alias by address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAliasByAddress",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getAllAddressPrefix": {
               "MethodDescription": "\u83b7\u53d6\u6240\u6709\u94fe\u7684\u5730\u5740\u524d\u7f00",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAllAddressPrefix",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.ac_getAllPriKey": {
               "MethodDescription": "\u83b7\u53d6\u6240\u6709\u672c\u5730\u8d26\u6237\u8d26\u6237\u79c1\u94a5\uff0c\u5fc5\u987b\u4fdd\u8bc1\u6240\u6709\u8d26\u6237\u5bc6\u7801\u4e00\u81f4\uff0c\u5982\u679c\u672c\u5730\u8d26\u6237\u4e2d\u7684\u5bc6\u7801\u4e0d\u4e00\u81f4\uff0c\u5c06\u8fd4\u56de\u9519\u8bef\u4fe1\u606f/Get the all local private keys. if the password in the local account is different, the error message will be returned.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getAllPriKey",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getEncryptedAddressList": {
               "MethodDescription": "\u83b7\u53d6\u672c\u5730\u52a0\u5bc6\u8d26\u6237\u5217\u8868/Get a list of locally encrypted accounts",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getEncryptedAddressList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getMultiSignAccount": {
               "MethodDescription": "\u6839\u636e\u591a\u7b7e\u8d26\u6237\u5730\u5740\u83b7\u53d6\u5b8c\u6574\u591a\u7b7e\u8d26\u6237/Search for multi-signature account by address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getMultiSignAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getPriKeyByAddress": {
               "MethodDescription": "\u901a\u8fc7\u8d26\u6237\u5730\u5740\u548c\u5bc6\u7801,\u67e5\u8be2\u8d26\u6237\u79c1\u5319/Inquire the account's private key according to the address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getPriKeyByAddress",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_getPubKey": {
               "MethodDescription": "\u6839\u636e\u8d26\u6237\u5730\u5740\u548c\u5bc6\u7801,\u67e5\u8be2\u8d26\u6237\u516c\u94a5/Get the account's public key",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_getPubKey",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_importAccountByKeystore": {
               "MethodDescription": "\u6839\u636eAccountKeyStore\u5bfc\u5165\u8d26\u6237/Import accounts by AccountKeyStore",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_importAccountByKeystore",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "keyStore",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "overwrite",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_importAccountByPriKey": {
               "MethodDescription": "\u6839\u636e\u79c1\u94a5\u5bfc\u5165\u8d26\u6237/Import accounts by private key",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_importAccountByPriKey",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "priKey",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "overwrite",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_isAliasUsable": {
               "MethodDescription": "\u68c0\u67e5\u522b\u540d\u662f\u5426\u53ef\u7528/check whether the account is usable",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_isAliasUsable",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "alias",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_isMultiSignAccountBuilder": {
               "MethodDescription": "\u9a8c\u8bc1\u662f\u5426\u591a\u7b7e\u8d26\u6237\u7684\u521b\u5efa\u8005\u4e4b\u4e00/Whether it is multiSign account Builder",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_isMultiSignAccountBuilder",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pubKey",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_removeAccount": {
               "MethodDescription": "\u79fb\u9664\u6307\u5b9a\u8d26\u6237/Remove specified account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_removeAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_removeMultiSignAccount": {
               "MethodDescription": "\u79fb\u9664\u591a\u7b7e\u8d26\u6237/remove the multi sign account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_removeMultiSignAccount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_setAlias": {
               "MethodDescription": "\u8bbe\u7f6e\u522b\u540d/Set the alias of account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_setAlias",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "alias",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_setMultiSignAlias": {
               "MethodDescription": "\u8bbe\u7f6e\u591a\u7b7e\u8d26\u6237\u522b\u540d/set the alias of multi sign account",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_setMultiSignAlias",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "alias",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signPassword",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_setRemark": {
               "MethodDescription": "\u4e3a\u8d26\u6237\u8bbe\u7f6e\u5907\u6ce8/Set remark for accounts",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_setRemark",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_signBlockDigest": {
               "MethodDescription": "\u533a\u5757\u6570\u636e\u6458\u8981\u7b7e\u540d/Block data digest signature",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_signBlockDigest",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "data",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_signDigest": {
               "MethodDescription": "\u6570\u636e\u6458\u8981\u7b7e\u540d/Data digest signature",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_signDigest",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "data",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_signMultiSignTransaction": {
               "MethodDescription": "\u591a\u7b7e\u4ea4\u6613\u7b7e\u540d/sign MultiSign Transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_signMultiSignTransaction",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signPassword",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_transfer": {
               "MethodDescription": "\u521b\u5efa\u666e\u901a\u8f6c\u8d26\u4ea4\u6613/create transfer transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_transfer",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "inputs",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "outputs",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_updateOfflineAccountPassword": {
               "MethodDescription": "\u79bb\u7ebf\u8d26\u6237\u4fee\u6539\u5bc6\u7801/Offline account change password",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_updateOfflineAccountPassword",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "newPassword",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "priKey",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_updatePassword": {
               "MethodDescription": "\u6839\u636e\u539f\u5bc6\u7801\u4fee\u6539\u8d26\u6237\u5bc6\u7801/Modify the account password by the original password",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_updatePassword",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "newPassword",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_validationPassword": {
               "MethodDescription": "\u9a8c\u8bc1\u8d26\u6237\u5bc6\u7801\u662f\u5426\u6b63\u786e/Verify that the account password is correct",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_validationPassword",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.ac_verifySignData": {
               "MethodDescription": "\u9a8c\u8bc1\u6570\u636e\u7b7e\u540d/Verification Data Signature",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ac_verifySignData",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "pubKey",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sig",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "data",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.batchValidateBegin": {
               "MethodDescription": "\u5f00\u59cb\u6279\u91cf\u6253\u5305:\u72b6\u6001\u901a\u77e5",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "batchValidateBegin",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.blockValidate": {
               "MethodDescription": "\u6574\u533a\u5757\u5165\u8d26\u6821\u9a8c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "blockValidate",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cancelCrossChain": {
               "MethodDescription": "\u6307\u5b9a\u94fe\u8d44\u4ea7\u9000\u51fa\u8de8\u94fe/Specified Chain Assets Exit Cross Chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cancelCrossChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.checkBlockVersion": {
               "MethodDescription": "check block version",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "checkBlockVersion",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "extendsData",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.clearUnconfirmTxs": {
               "MethodDescription": "\u6e05\u9664\u6240\u6709\u8d26\u6237\u672a\u786e\u8ba4\u4ea4\u6613",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "clearUnconfirmTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_asset": {
               "MethodDescription": "\u8d44\u4ea7\u6ce8\u518c\u4fe1\u606f\u67e5\u8be2",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_asset",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_assetCirculateCommit": {
               "MethodDescription": "\u67e5\u8be2\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_assetCirculateCommit",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_assetCirculateRollBack": {
               "MethodDescription": "\u67e5\u8be2\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_assetCirculateRollBack",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_assetCirculateValidator": {
               "MethodDescription": "\u67e5\u8be2\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_assetCirculateValidator",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_assetDisable": {
               "MethodDescription": "\u8d44\u4ea7\u6ce8\u9500",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_assetDisable",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_assetReg": {
               "MethodDescription": "\u8d44\u4ea7\u6ce8\u518c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_assetReg",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "symbol",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "initNumber",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "decimalPlaces",
                     "ParameterType": "short",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_chain": {
               "MethodDescription": "\u67e5\u770b\u94fe\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_chain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_chainActive": {
               "MethodDescription": "\u94fe\u66f4\u65b0\u6fc0\u6d3b-\u7528\u4e8e\u5e73\u884c\u94fe\u7684\u8de8\u94fe\u66f4\u65b0\u6fc0\u6d3b\uff08\u6fc0\u6d3b\u4e4b\u524d\u6ce8\u9500\u7684\u94fe\uff09",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_chainActive",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "chainName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "addressType",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "addressPrefix",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "magicNumber",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "minAvailableNodeNum",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "symbol",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "initNumber",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "decimalPlaces",
                     "ParameterType": "short",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "verifierList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signatureBFTRatio",
                     "ParameterType": "Integer",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxSignatureCount",
                     "ParameterType": "Integer",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_chainReg": {
               "MethodDescription": "\u94fe\u6ce8\u518c-\u7528\u4e8e\u5e73\u884c\u94fe\u7684\u8de8\u94fe\u6ce8\u518c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_chainReg",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[3-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "chainName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "addressType",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "addressPrefix",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "magicNumber",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "minAvailableNodeNum",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "symbol",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "initNumber",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "decimalPlaces",
                     "ParameterType": "short",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "verifierList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signatureBFTRatio",
                     "ParameterType": "Integer",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxSignatureCount",
                     "ParameterType": "Integer",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_getChainAsset": {
               "MethodDescription": "\u8d44\u4ea7\u67e5\u770b",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_getChainAsset",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cm_getChainsSimpleInfo": {
               "MethodDescription": "\u83b7\u53d6\u8de8\u94fe\u5df2\u6ce8\u518c\u94fe\u5217\u8868",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_getChainsSimpleInfo",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.cm_getCirculateChainAsset": {
               "MethodDescription": "\u67e5\u8be2\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cm_getCirculateChainAsset",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "circulateChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.commitBatchUnconfirmedTxs": {
               "MethodDescription": "\u672a\u786e\u8ba4\u4ea4\u6613\u6279\u91cf\u63d0\u4ea4\u8d26\u672c(\u6821\u9a8c\u5e76\u66f4\u65b0nonce\u503c)",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "commitBatchUnconfirmedTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.commitBlockTxs": {
               "MethodDescription": "\u63d0\u4ea4\u533a\u5757",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "commitBlockTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.commitUnconfirmedTx": {
               "MethodDescription": "\u672a\u786e\u8ba4\u4ea4\u6613\u63d0\u4ea4\u8d26\u672c(\u6821\u9a8c\u5e76\u66f4\u65b0nonce\u503c)",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "commitUnconfirmedTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.connectReady": {
               "MethodDescription": "check module rpc is ready",
               "MethodMinEvent": "1",
               "MethodMinPeriod": "0",
               "MethodName": "connectReady",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nuls.createAgentValid": {
               "MethodDescription": "create agent transaction validate",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "createAgentValid",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.createCrossTx": {
               "MethodDescription": "\u521b\u5efa\u8de8\u94fe\u8f6c\u8d26\u4ea4\u6613/Creating Cross-Chain Transfer Transactions",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "createCrossTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "listFrom",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "listTo",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.crossChainRegisterChange": {
               "MethodDescription": "\u8de8\u94fe\u6ce8\u518c\u4fe1\u606f\u53d8\u66f4/Registered Cross Chain change",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "crossChainRegisterChange",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_addBlock": {
               "MethodDescription": "\u63a5\u6536\u5e76\u7f13\u5b58\u65b0\u533a\u5757/Receiving and caching new blocks",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_addBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_addEvidenceRecord": {
               "MethodDescription": "\u94fe\u5206\u53c9\u8bc1\u636e\u8bb0\u5f55/add evidence record",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_addEvidenceRecord",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "evidenceHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_chainRollBack": {
               "MethodDescription": "\u533a\u5757\u56de\u6eda/chain rollback",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_chainRollBack",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_contractDeposit": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u59d4\u6258\u5171\u8bc6/contract deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_contractDeposit",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractBalance",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractNonce",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_contractWithdraw": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u9000\u51fa\u5171\u8bc6/contract withdraw deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_contractWithdraw",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "joinAgentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractBalance",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractNonce",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_createAgent": {
               "MethodDescription": "\u521b\u5efa\u8282\u70b9\u4ea4\u6613/create agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_createAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packingAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "rewardAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "commissionRate",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_createContractAgent": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u521b\u5efa\u8282\u70b9/contract create agent",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_createContractAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packingAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "commissionRate",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractBalance",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractNonce",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_createMultiAgent": {
               "MethodDescription": "\u591a\u7b7e\u8d26\u6237\u521b\u5efa\u8282\u70b9/Multi-Sign Account create agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_createMultiAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packingAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "rewardAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "commissionRate",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_depositToAgent": {
               "MethodDescription": "\u521b\u5efa\u59d4\u6258\u4ea4\u6613/deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_depositToAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_doubleSpendRecord": {
               "MethodDescription": "\u53cc\u82b1\u4ea4\u6613\u8bb0\u5f55/double spend transaction record ",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_doubleSpendRecord",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "block",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getAgentAddressList": {
               "MethodDescription": "\u83b7\u53d6\u5f53\u524d\u7f51\u7edc\u5171\u8bc6\u8282\u70b9\u51fa\u5757\u5730\u5740\u5217\u8868\u6216\u5219\u67e5\u8be2\u6700\u8fd1N\u4e2a\u533a\u5757\u7684\u51fa\u5757\u5730\u5740/Get all node out-of-block addresses or specify N block out-of-block designations",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getAgentAddressList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getAgentChangeInfo": {
               "MethodDescription": "get seed nodes list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getAgentChangeInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getAgentInfo": {
               "MethodDescription": "\u67e5\u8be2\u6307\u70b9\u8282\u70b9\u8282\u70b9\u8be6\u7ec6\u4fe1\u606f/Query pointer node details",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getAgentInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getAgentList": {
               "MethodDescription": "\u67e5\u8be2\u5f53\u524d\u7f51\u7edc\u4e2d\u7684\u5171\u8bc6\u8282\u70b9\u5217\u8868/Query the list of consensus nodes in the current network",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getAgentList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "keyWord",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getAgentStatus": {
               "MethodDescription": "\u67e5\u8be2\u6307\u5b9a\u5171\u8bc6\u8282\u70b9\u72b6\u6001/query the specified consensus node status 1.0",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getAgentStatus",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getConsensusConfig": {
               "MethodDescription": "\u83b7\u53d6\u5171\u8bc6\u6a21\u5757\u914d\u7f6e\u4fe1\u606f/get consensus config",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getConsensusConfig",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getContractAgentInfo": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u8282\u70b9/contract get agent info",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getContractAgentInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getContractDepositInfo": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u67e5\u8be2\u6307\u5b9a\u8d26\u6237\u59d4\u6258\u4fe1\u606f/Intelligent Contract Query for Assigned Account Delegation Information",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getContractDepositInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "joinAgentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getDepositList": {
               "MethodDescription": "\u67e5\u8be2\u6307\u5b9a\u8d26\u6237\u6216\u6307\u5b9a\u8282\u70b9\u7684\u59d4\u6258\u4fe1\u606f/Query delegation information for a specified account or node",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getDepositList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getInfo": {
               "MethodDescription": "\u67e5\u8be2\u6307\u5b9a\u8d26\u6237\u5171\u8bc6\u6570\u636e/query consensus information for specified accounts",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getNodePackingAddress": {
               "MethodDescription": "\u83b7\u53d6\u5f53\u524d\u8282\u70b9\u51fa\u5757\u5730\u5740/Get the current node's out-of-block address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getNodePackingAddress",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getPackerInfo": {
               "MethodDescription": "\u83b7\u53d6\u5f53\u524d\u8282\u70b9\u7684\u51fa\u5757\u8d26\u6237\u4fe1\u606f/modifying the Packing State of Nodes",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getPackerInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getPublishList": {
               "MethodDescription": "\u67e5\u8be2\u7ea2\u9ec4\u724c\u8bb0\u5f55/query punish list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getPublishList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "type",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getRoundInfo": {
               "MethodDescription": "\u83b7\u53d6\u5f53\u524d\u8f6e\u6b21\u4fe1\u606f/get current round information",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getRoundInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getRoundMemberList": {
               "MethodDescription": "\u67e5\u8be2\u6307\u5b9a\u533a\u5757\u6240\u5728\u8f6e\u6b21\u7684\u6210\u5458\u5217\u8868/Query the membership list of the specified block's rounds",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getRoundMemberList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "extend",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getSeedNodeInfo": {
               "MethodDescription": "\u83b7\u53d6\u79cd\u5b50\u8282\u70b9\u4fe1\u606f/get seed node info",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getSeedNodeInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_getWholeInfo": {
               "MethodDescription": "\u67e5\u8be2\u5168\u7f51\u5171\u8bc6\u6570\u636e/query the consensus information of the whole network",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_getWholeInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_multiDeposit": {
               "MethodDescription": "\u591a\u7b7e\u8d26\u6237\u59d4\u6258\u5171\u8bc6/Multi-Sign Account deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_multiDeposit",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "agentHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "deposit",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_multiWithdraw": {
               "MethodDescription": "\u591a\u7b7e\u8d26\u6237\u9000\u51fa\u5171\u8bc6/Multi-Sign Account withdraw deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_multiWithdraw",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_random_raw_seeds_count": {
               "MethodDescription": "\u6839\u636e\u9ad8\u5ea6\u67e5\u627e\u539f\u59cb\u79cd\u5b50\u5217\u8868\u5e76\u8fd4\u56de",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_random_raw_seeds_count",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "count",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_random_raw_seeds_height": {
               "MethodDescription": "\u6839\u636e\u9ad8\u5ea6\u533a\u95f4\u67e5\u8be2\u539f\u59cb\u79cd\u5b50\u5217\u8868\u5e76\u8fd4\u56de",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_random_raw_seeds_height",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "startHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "endHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_random_seed_count": {
               "MethodDescription": "\u6839\u636e\u9ad8\u5ea6\u548c\u539f\u59cb\u79cd\u5b50\u4e2a\u6570\u751f\u6210\u4e00\u4e2a\u968f\u673a\u79cd\u5b50\u5e76\u8fd4\u56de",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_random_seed_count",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "count",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "algorithm",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_random_seed_height": {
               "MethodDescription": "\u6839\u636e\u9ad8\u5ea6\u533a\u95f4\u751f\u6210\u4e00\u4e2a\u968f\u673a\u79cd\u5b50\u5e76\u8fd4\u56de",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_random_seed_height",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "startHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "endHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "algorithm",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_receiveHeaderList": {
               "MethodDescription": "\u63a5\u6536\u5e76\u7f13\u5b58\u533a\u5757\u5217\u8868/Receive and cache block lists",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_receiveHeaderList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "headerList",
                     "ParameterType": "List<String>",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_runChain": {
               "MethodDescription": "Running a sub chain 1.0",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_runChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_runMainChain": {
               "MethodDescription": "run main chain 1.0",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_runMainChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_stopAgent": {
               "MethodDescription": "\u6ce8\u9500\u8282\u70b9/stop agent",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_stopAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_stopChain": {
               "MethodDescription": "stop a chain 1.0",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_stopChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_stopContractAgent": {
               "MethodDescription": "\u667a\u80fd\u5408\u7ea6\u6ce8\u9500\u8282\u70b9/contract stop agent",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_stopContractAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractSender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractBalance",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractNonce",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_stopMultiAgent": {
               "MethodDescription": "\u591a\u7b7e\u8d26\u6237\u6ce8\u9500\u8282\u70b9/Multi-Sign Account stop agent",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_stopMultiAgent",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "signAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_triggerCoinBaseContract": {
               "MethodDescription": "\u4ea4\u6613\u6a21\u5757\u89e6\u53d1CoinBase\u667a\u80fd\u5408\u7ea6/trigger coin base contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_triggerCoinBaseContract",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "stateRoot",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_updateAgentConsensusStatus": {
               "MethodDescription": "\u4fee\u6539\u8282\u70b9\u5171\u8bc6\u72b6\u6001/modifying the Node Consensus State",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_updateAgentConsensusStatus",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_updateAgentStatus": {
               "MethodDescription": "\u4fee\u6539\u8282\u70b9\u6253\u5305\u72b6\u6001/modifying the Packing State of Nodes",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_updateAgentStatus",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "status",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_validBlock": {
               "MethodDescription": "\u9a8c\u8bc1\u533a\u5757/verify block correctness",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_validBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "download",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "block",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.cs_withdraw": {
               "MethodDescription": "\u9000\u51fa\u59d4\u6258\u4ea4\u6613/withdraw deposit agent transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "cs_withdraw",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.depositValid": {
               "MethodDescription": "deposit agent transaction validate",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "depositValid",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getAssetsById": {
               "MethodDescription": "\u67e5\u8be2\u94fe\u4e0b\u6307\u5b9a\u8d44\u4ea7\u96c6\u5408\u7684\u91d1\u989d\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getAssetsById",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetIds",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBalance": {
               "MethodDescription": "\u83b7\u53d6\u8d26\u6237\u8d44\u4ea7(\u5df2\u5165\u533a\u5757)",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBalance",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBalanceNonce": {
               "MethodDescription": "\u83b7\u53d6\u8d26\u6237\u8d44\u4ea7\u4f59\u989d\u4e0eNONCE\u503c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBalanceNonce",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isConfirmed",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockByHash": {
               "MethodDescription": "get a block by hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockByHash",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockByHeight": {
               "MethodDescription": "get a block by height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockByHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeaderByHash": {
               "MethodDescription": "get a block header by hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeaderByHash",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeaderByHeight": {
               "MethodDescription": "get a block header by height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeaderByHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeaderPoByHash": {
               "MethodDescription": "get a block header po by hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeaderPoByHash",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeaderPoByHeight": {
               "MethodDescription": "get a block header po by height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeaderPoByHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeadersByHeightRange": {
               "MethodDescription": "get the block headers according to the height range",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeadersByHeightRange",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "begin",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "end",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getBlockHeadersForProtocol": {
               "MethodDescription": "get block headers for protocol upgrade module",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getBlockHeadersForProtocol",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "interval",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getByzantineCount": {
               "MethodDescription": "\u67e5\u8be2\u5f53\u524d\u7b7e\u540d\u62dc\u5360\u5ead\u6700\u5c0f\u901a\u8fc7\u6570\u91cf/\u67e5\u8be2\u5f53\u524d\u7b7e\u540d\u62dc\u5360\u5ead\u6700\u5c0f\u901a\u8fc7\u6570\u91cf",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getByzantineCount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getChains": {
               "MethodDescription": "cancel Cross Chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getChains",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getCirculat": {
               "MethodDescription": "\u67e5\u8be2\u672c\u94fe\u8d44\u4ea7\u4fe1\u606f\u6d88\u606f/get chain circulation",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getCirculat",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getCrossChainInfos": {
               "MethodDescription": "\u83b7\u53d6\u8de8\u94fe\u6ce8\u518c\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getCrossChainInfos",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.getCrossTxState": {
               "MethodDescription": "\u67e5\u8be2\u8de8\u94fe\u4ea4\u6613\u5904\u7406\u72b6\u6001/get cross transaction process state",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getCrossTxState",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getCtx": {
               "MethodDescription": "\u94fe\u5185\u8282\u70b9\u5411\u672c\u8282\u70b9\u83b7\u53d6\u5b8c\u6210\u8de8\u94fe\u4ea4\u6613/The intra-chain node acquires and completes the cross-chain transaction from its own node",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getCtx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getCtxState": {
               "MethodDescription": "\u83b7\u53d6\u8de8\u94fe\u4ea4\u6613\u5904\u7406\u72b6\u6001/Getting the state of cross-chain transaction processing",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getCtxState",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getFreezeList": {
               "MethodDescription": "\u5206\u9875\u83b7\u53d6\u8d26\u6237\u9501\u5b9a\u8d44\u4ea7\u5217\u8868",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getFreezeList",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getFriendChainCirculate": {
               "MethodDescription": "\u83b7\u53d6\u53cb\u94fe\u8d44\u4ea7\u4fe1\u606f/Access to Friendship Chain Asset Information",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getFriendChainCirculate",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetIds",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getLatestBlockHeaders": {
               "MethodDescription": "get the latest number of block headers",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getLatestBlockHeaders",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "size",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getLatestRoundBlockHeaders": {
               "MethodDescription": "get the latest several rounds of block headers",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getLatestRoundBlockHeaders",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "round",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getNonce": {
               "MethodDescription": "\u83b7\u53d6\u8d26\u6237\u8d44\u4ea7NONCE\u503c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getNonce",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetChainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isConfirmed",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getOtherCtx": {
               "MethodDescription": "\u8de8\u94fe\u8282\u70b9\u5411\u672c\u8282\u70b9\u83b7\u53d6\u5b8c\u6574\u4ea4\u6613/Cross-chain nodes obtain complete transactions from their own nodes",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getOtherCtx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getRegisteredChainInfoList": {
               "MethodDescription": "\u67e5\u8be2\u5728\u4e3b\u7f51\u4e0a\u6ce8\u518c\u8de8\u94fe\u7684\u94fe\u4fe1\u606f/Query for cross-chain chain information registered on the main network",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getRegisteredChainInfoList",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.getRoundBlockHeaders": {
               "MethodDescription": "get the latest several rounds of block headers",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getRoundBlockHeaders",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "round",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getStatus": {
               "MethodDescription": "receive the new packaged block",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getStatus",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.getVersion": {
               "MethodDescription": "get mainnet version",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "getVersion",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.info": {
               "MethodDescription": "returns network node height and local node height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "info",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.latestBlock": {
               "MethodDescription": "the latest block of master chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "latestBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.latestBlockHeader": {
               "MethodDescription": "the latest block header of master chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "latestBlockHeader",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.latestBlockHeaderPo": {
               "MethodDescription": "the latest block header po of master chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "latestBlockHeaderPo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.latestHeight": {
               "MethodDescription": "the latest height of master chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "latestHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.listenerDependenciesReady": {
               "MethodDescription": "notify module is ready",
               "MethodMinEvent": "1",
               "MethodMinPeriod": "0",
               "MethodName": "listenerDependenciesReady",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nuls.msgProcess": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "msgProcess",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "cmd",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.newApiModuleCrossTx": {
               "MethodDescription": "\u63a5\u6536API_MODULE\u7ec4\u88c5\u7684\u8de8\u94fe\u4ea4\u6613/Receiving cross-chain transactions assembled by API_MODULE",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "newApiModuleCrossTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.newBlockHeight": {
               "MethodDescription": "\u94fe\u533a\u5757\u9ad8\u5ea6\u53d8\u66f4/receive new block height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "newBlockHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_activeCross": {
               "MethodDescription": "\u8de8\u94fe\u534f\u8bae\u6a21\u5757\u6fc0\u6d3b\u8de8\u94fe",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_activeCross",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxOut",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxIn",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "seedIps",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_addNodes": {
               "MethodDescription": "\u589e\u52a0\u5f85\u8fde\u63a5\u8282\u70b9",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_addNodes",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isCross",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodes",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_broadcast": {
               "MethodDescription": "\u5e7f\u64ad\u6d88\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_broadcast",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "excludeNodes",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "command",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isCross",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "percent",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_createNodeGroup": {
               "MethodDescription": "\u4e3b\u7f51\u521b\u5efa\u8de8\u94fe\u7f51\u7edc\u6216\u8005\u94fe\u5de5\u5382\u521b\u5efa\u94fe",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_createNodeGroup",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "magicNumber",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxOut",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxIn",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "minAvailableCount",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isCrossGroup",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_currentTimeMillis": {
               "MethodDescription": "\u83b7\u53d6\u8282\u70b9\u7f51\u7edc\u65f6\u95f4",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_currentTimeMillis",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.nw_delNodeGroup": {
               "MethodDescription": "\u5220\u9664\u6307\u5b9a\u7f51\u7edc\u7ec4",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_delNodeGroup",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_delNodes": {
               "MethodDescription": "\u5220\u9664\u8282\u70b9\u7ec4\u8282\u70b9",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_delNodes",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodes",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_getChainConnectAmount": {
               "MethodDescription": "\u83b7\u53d6\u6307\u5b9a\u7f51\u7edc\u7ec4\u53ef\u8fde\u63a5\u6570\u91cf",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getChainConnectAmount",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isCross",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_getGroupByChainId": {
               "MethodDescription": "\u83b7\u53d6\u8282\u70b9\u7ec4\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getGroupByChainId",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_getGroups": {
               "MethodDescription": "\u5206\u9875\u83b7\u53d6\u7f51\u7edc\u7ec4\u4fe1\u606f,startPage\u4e0epageSize \u90fd\u4e3a0\u65f6\uff0c\u4e0d\u5206\u9875\uff0c\u8fd4\u56de\u6240\u6709\u7f51\u7edc\u7ec4\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getGroups",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "startPage",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_getMainMagicNumber": {
               "MethodDescription": "\u67e5\u770b\u4e3b\u7f51\u7684\u9b54\u6cd5\u53c2\u6570",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getMainMagicNumber",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.nw_getNodes": {
               "MethodDescription": "\u5206\u9875\u67e5\u770b\u8fde\u63a5\u8282\u70b9\u4fe1\u606f,startPage\u4e0epageSize \u90fd\u4e3a0\u65f6\uff0c\u4e0d\u5206\u9875\uff0c\u8fd4\u56de\u6240\u6709\u8282\u70b9\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getNodes",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "state",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "isCross",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "startPage",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_getSeeds": {
               "MethodDescription": "\u67e5\u770b\u8de8\u94fe\u7f51\u7edc\u63d0\u4f9b\u7684\u79cd\u5b50\u8282\u70b9",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_getSeeds",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nuls.nw_info": {
               "MethodDescription": "\u83b7\u53d6\u8282\u70b9\u7f51\u7edc\u57fa\u672c\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_info",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_nodes": {
               "MethodDescription": "\u83b7\u53d6\u7f51\u7edc\u8fde\u63a5\u8282\u70b9\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_nodes",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_protocolRegister": {
               "MethodDescription": "\u6a21\u5757\u534f\u8bae\u6307\u4ee4\u6ce8\u518c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_protocolRegister",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "role",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "protocolCmds",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_reconnect": {
               "MethodDescription": "\u672c\u5730\u7f51\u7edc\u91cd\u542f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_reconnect",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_sendPeersMsg": {
               "MethodDescription": "\u5411\u6307\u5b9a\u8282\u70b9\u53d1\u9001\u6d88\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_sendPeersMsg",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodes",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "command",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.nw_updateNodeInfo": {
               "MethodDescription": "\u66f4\u65b0\u8fde\u63a5\u8282\u70b9\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "nw_updateNodeInfo",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.paramTestCmd": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "paramTestCmd",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "intCount",
                     "ParameterType": "int",
                     "ParameterValidRange": "[0,65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "byteCount",
                     "ParameterType": "byte",
                     "ParameterValidRange": "[-128,127]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "shortCount",
                     "ParameterType": "short",
                     "ParameterValidRange": "[0,32767]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "longCount",
                     "ParameterType": "long",
                     "ParameterValidRange": "[0,55555555]",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.protocolRegisterWithPriority": {
               "MethodDescription": "\u6a21\u5757\u534f\u8bae\u6307\u4ee4\u6ce8\u518c\uff0c\u5e26\u6709\u4f18\u5148\u7ea7\u53c2\u6570",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "protocolRegisterWithPriority",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "role",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "protocolCmds",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.protocolVersionChange": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "protocolVersionChange",
               "MethodScope": "private",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "protocolVersion",
                     "ParameterType": "short",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.receivePackingBlock": {
               "MethodDescription": "receive the new packaged block",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "receivePackingBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "block",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvCirculat": {
               "MethodDescription": "\u63a5\u6536\u5176\u4ed6\u94fe\u8282\u70b9\u53d1\u9001\u7684\u8d44\u4ea7\u4fe1\u606f/Receiving asset information sent by other link nodes",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvCirculat",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvCtx": {
               "MethodDescription": "\u63a5\u6536\u672c\u94fe\u8282\u70b9\u5e7f\u64ad\u7684\u5b8c\u6574\u4ea4\u6613/Complete Transaction for Receiving Broadcast from Local Chain Nodes",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvCtx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvCtxHash": {
               "MethodDescription": "\u63a5\u6536\u8de8\u94fe\u8282\u70b9\u5e7f\u64ad\u7684\u4ea4\u6613Hash/Transaction Hash receiving cross-link node broadcasting",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvCtxHash",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvCtxSign": {
               "MethodDescription": "\u63a5\u6536\u94fe\u5185\u8282\u70b9\u5e7f\u64ad\u7684\u4ea4\u6613\u7b7e\u540d/Transaction signature for broadcasting in receiving chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvCtxSign",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvCtxState": {
               "MethodDescription": "\u8de8\u94fe\u4ea4\u6613\u5904\u7406\u72b6\u6001\u6d88\u606f/receive cross transaction state",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvCtxState",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvOtherCtx": {
               "MethodDescription": "\u63a5\u6536\u8de8\u94fe\u8282\u70b9\u5e7f\u64ad\u7684\u5b8c\u6574\u4ea4\u6613/Receiving Complete Transactions for Cross-Chain Node Broadcasting",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvOtherCtx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.recvRegChain": {
               "MethodDescription": "\u63a5\u6536\u5230\u4e3b\u7f51\u8fd4\u56de\u7684\u5df2\u6ce8\u518c\u8de8\u94fe\u4ea4\u6613\u7684\u94fe\u4fe1\u606f/Receiving chain information of registered cross-chain transactions returned from the main network",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "recvRegChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "nodeId",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "messageBody",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.registerAsset": {
               "MethodDescription": "\u94fe\u6ce8\u518c\u8de8\u94fe/register Cross Chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "registerAsset",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "symbol",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "usable",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "decimalPlaces",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.registerCrossChain": {
               "MethodDescription": "\u94fe\u6ce8\u518c\u8de8\u94fe/register Cross Chain",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "registerCrossChain",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "chainName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "minAvailableNodeNum",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assetInfoList",
                     "ParameterType": "List<AssetInfo>",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "registerTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.registerModuleDependencies": {
               "MethodDescription": "Register module followerList",
               "MethodMinEvent": "1",
               "MethodMinPeriod": "0",
               "MethodName": "registerModuleDependencies",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nuls.registerProtocol": {
               "MethodDescription": "register protocol",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "registerProtocol",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "moduleCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "list",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.rollBackBlockTxs": {
               "MethodDescription": "\u533a\u5757\u56de\u6eda",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "rollBackBlockTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.rollBackUnconfirmTx": {
               "MethodDescription": "\u56de\u6eda\u63d0\u4ea4\u7684\u672a\u786e\u8ba4\u4ea4\u6613",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "rollBackUnconfirmTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.rollbackBlock": {
               "MethodDescription": "rollback block header",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "rollbackBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.rollbackTxValidateStatus": {
               "MethodDescription": "\u56de\u6eda\u6253\u5305\u6821\u9a8c\u72b6\u6001",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "rollbackTxValidateStatus",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.saveBlock": {
               "MethodDescription": "save block header",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "saveBlock",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_account_contracts": {
               "MethodDescription": "\u8d26\u6237\u7684\u5408\u7ea6\u5730\u5740\u5217\u8868/account contract list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_account_contracts",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_batch_before_end": {
               "MethodDescription": "\u4ea4\u6613\u6a21\u5757\u6253\u5305\u5b8c\u4ea4\u6613\uff0c\u5728\u505a\u7edf\u4e00\u9a8c\u8bc1\u524d\uff0c\u901a\u77e5\u5408\u7ea6\u6a21\u5757\uff0c\u5408\u7ea6\u6a21\u5757\u505c\u6b62\u63a5\u6536\u4ea4\u6613\uff0c\u5f00\u59cb\u5f02\u6b65\u5904\u7406\u8fd9\u4e2a\u6279\u6b21\u7684\u7ed3\u679c/batch before end",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_batch_before_end",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockType",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_batch_begin": {
               "MethodDescription": "\u6267\u884c\u5408\u7ea6\u4e00\u4e2a\u6279\u6b21\u7684\u5f00\u59cb\u901a\u77e5\uff0c\u751f\u6210\u5f53\u524d\u6279\u6b21\u7684\u4fe1\u606f/batch begin",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_batch_begin",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockType",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packingAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "preStateRoot",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_batch_end": {
               "MethodDescription": "\u901a\u77e5\u5f53\u524d\u6279\u6b21\u7ed3\u675f\u5e76\u8fd4\u56de\u7ed3\u679c/batch end",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_batch_end",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_call": {
               "MethodDescription": "call contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_call",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "value",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "gasLimit",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "price",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodDesc",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_call_validator": {
               "MethodDescription": "call contract validator",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_call_validator",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_constructor": {
               "MethodDescription": "contract code constructor",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_constructor",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_contract_info": {
               "MethodDescription": "\u5408\u7ea6\u4fe1\u606f\u8be6\u60c5/contract info",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_contract_info",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_contract_offline_tx_hash_list": {
               "MethodDescription": "\u8fd4\u56de\u6307\u5b9a\u533a\u5757\u4e2d\u5408\u7ea6\u751f\u6210\u4ea4\u6613\uff08\u5408\u7ea6\u8fd4\u56deGAS\u4ea4\u6613\u9664\u5916\uff09\u7684hash\u5217\u8868\uff08\u5408\u7ea6\u65b0\u751f\u6210\u7684\u4ea4\u6613\u9664\u5408\u7ea6\u8fd4\u56deGAS\u4ea4\u6613\u5916\uff0c\u4e0d\u4fdd\u5b58\u5230\u533a\u5757\u4e2d\uff0c\u5408\u7ea6\u6a21\u5757\u4fdd\u5b58\u4e86\u8fd9\u4e9b\u4ea4\u6613\u548c\u6307\u5b9a\u533a\u5757\u7684\u5173\u7cfb\uff09/contract offline tx hash list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_contract_offline_tx_hash_list",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_contract_result": {
               "MethodDescription": "contract result",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_contract_result",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_contract_result_list": {
               "MethodDescription": "contract result list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_contract_result_list",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hashList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_contract_tx": {
               "MethodDescription": "\u5408\u7ea6\u4ea4\u6613/contract tx",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_contract_tx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "hash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_create": {
               "MethodDescription": "\u53d1\u5e03\u5408\u7ea6/create contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_create",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "alias",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "gasLimit",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "price",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_create_validator": {
               "MethodDescription": "create contract validator",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_create_validator",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_delete": {
               "MethodDescription": "delete contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_delete",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_delete_validator": {
               "MethodDescription": "delete contract validator",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_delete_validator",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_imputed_call_gas": {
               "MethodDescription": "imputed call gas",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_imputed_call_gas",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "value",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodDesc",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_imputed_create_gas": {
               "MethodDescription": "\u9884\u4f30\u53d1\u5e03\u5408\u7ea6\u6d88\u8017\u7684GAS/imputed create gas",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_imputed_create_gas",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_initial_account_token": {
               "MethodDescription": "\u521d\u59cb\u5316\u8d26\u6237token\u4fe1\u606f\uff0c\u8282\u70b9\u5bfc\u5165\u8d26\u6237\u65f6\u8c03\u7528/initial account token",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_initial_account_token",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_invoke_contract": {
               "MethodDescription": "\u6279\u6b21\u901a\u77e5\u5f00\u59cb\u540e\uff0c\u4e00\u7b14\u4e00\u7b14\u6267\u884c\u5408\u7ea6/invoke contract one by one",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_invoke_contract",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockType",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_invoke_view": {
               "MethodDescription": "invoke view contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_invoke_view",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodDesc",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_package_batch_end": {
               "MethodDescription": "\u6253\u5305\u7ed3\u675f - \u901a\u77e5\u5f53\u524d\u6279\u6b21\u7ed3\u675f\u5e76\u8fd4\u56de\u7ed3\u679c/batch end",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_package_batch_end",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_register_cmd_for_contract": {
               "MethodDescription": "\u5176\u4ed6\u6a21\u5757\u5411\u5408\u7ea6\u6a21\u5757\u6ce8\u518c\u53ef\u88ab\u5408\u7ea6\u8c03\u7528\u7684\u547d\u4ee4\uff0c\u6ce8\u518c\u540e\uff0c\u53ef\u5728\u5408\u7ea6\u4ee3\u7801\u5185\u8c03\u7528\u6ce8\u518c\u7684\u547d\u4ee4/register cmd for contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_register_cmd_for_contract",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "moduleCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "cmdRegisterList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_token_assets_list": {
               "MethodDescription": "token\u8d44\u4ea7\u96c6\u5408/token assets list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_token_assets_list",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_token_balance": {
               "MethodDescription": "NRC20\u4ee3\u5e01\u4f59\u989d\u8be6\u60c5/NRC20-token balance",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_token_balance",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_token_transfer": {
               "MethodDescription": "NRC20-token\u8f6c\u8d26/transfer NRC20-token from address to toAddress",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_token_transfer",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "toAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "amount",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_token_transfer_list": {
               "MethodDescription": "token\u8f6c\u8d26\u4ea4\u6613\u5217\u8868/token transfer list",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_token_transfer_list",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageNumber",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "pageSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_transfer": {
               "MethodDescription": "\u4ece\u8d26\u6237\u5730\u5740\u5411\u5408\u7ea6\u5730\u5740\u8f6c\u8d26(\u4e3b\u94fe\u8d44\u4ea7)/transfer NULS from sender to contract address",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_transfer",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "address",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "toAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "password",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "amount",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "remark",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_trigger_payable_for_consensus_contract": {
               "MethodDescription": "\u5171\u8bc6\u5956\u52b1\u6536\u76ca\u5730\u5740\u662f\u5408\u7ea6\u5730\u5740\u65f6\uff0c\u4f1a\u89e6\u53d1\u5408\u7ea6\u7684_payable(String[][] args)\u65b9\u6cd5\uff0c\u53c2\u6570\u662f\u8282\u70b9\u6536\u76ca\u5730\u5740\u660e\u7ec6<br>args[0] = new String[]{address, amount}<br>...<br>/trigger payable for consensus contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_trigger_payable_for_consensus_contract",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "stateRoot",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeight",
                     "ParameterType": "Long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_upload": {
               "MethodDescription": "\u5408\u7ea6\u4ee3\u7801jar\u5305\u4e0a\u4f20/upload",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_upload",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "jarFileData",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_validate_call": {
               "MethodDescription": "validate call contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_validate_call",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "value",
                     "ParameterType": "BigInteger",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "gasLimit",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "price",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodName",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "methodDesc",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_validate_create": {
               "MethodDescription": "\u9a8c\u8bc1\u53d1\u5e03\u5408\u7ea6/validate create contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_validate_create",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "gasLimit",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "price",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "args",
                     "ParameterType": "Object[]",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.sc_validate_delete": {
               "MethodDescription": "validate delete contract",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "sc_validate_delete",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "sender",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.stopAgentValid": {
               "MethodDescription": "stop agent transaction validate",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "stopAgentValid",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.txCommit": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "txCommit",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.txRollback": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "txRollback",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.txValidator": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "txValidator",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_backPackableTxs": {
               "MethodDescription": "\u5171\u8bc6\u6a21\u5757\u628a\u4e0d\u80fd\u6253\u5305\u7684\u4ea4\u6613\u8fd8\u56de\u6765\uff0c\u91cd\u65b0\u52a0\u5165\u5f85\u6253\u5305\u5217\u8868/back packaged transactions",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_backPackableTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_batchVerify": {
               "MethodDescription": "\u9a8c\u8bc1\u533a\u5757\u6240\u6709\u4ea4\u6613/Verify all transactions in the block",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_batchVerify",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "preStateRoot",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_bl_state": {
               "MethodDescription": "\u8bbe\u7f6e\u8282\u70b9\u533a\u5757\u540c\u6b65\u72b6\u6001(\u7531\u533a\u5757\u6a21\u5757\u8bbe\u7f6e)/Set the node block state",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_bl_state",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "status",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_blockHeight": {
               "MethodDescription": "\u63a5\u6536\u6700\u65b0\u533a\u5757\u9ad8\u5ea6/Receive the latest block height",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_blockHeight",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "height",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_cs_state": {
               "MethodDescription": "\u8bbe\u7f6e\u8282\u70b9\u6253\u5305\u72b6\u6001(\u7531\u5171\u8bc6\u6a21\u5757\u8bbe\u7f6e)/Set the node packaging state",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_cs_state",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packaging",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_gengsisSave": {
               "MethodDescription": "\u4fdd\u5b58\u521b\u4e16\u5757\u7684\u4ea4\u6613/Save the transactions of the Genesis block ",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_gengsisSave",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getBlockTxs": {
               "MethodDescription": "\u83b7\u53d6\u533a\u5757\u7684\u5b8c\u6574\u4ea4\u6613\uff0c\u5982\u679c\u6ca1\u6709\u67e5\u8be2\u5230\uff0c\u6216\u8005\u67e5\u8be2\u5230\u7684\u4e0d\u662f\u533a\u5757\u5b8c\u6574\u7684\u4ea4\u6613\u6570\u636e\uff0c\u5219\u8fd4\u56de\u7a7a\u96c6\u5408/Get block transactions",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getBlockTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHashList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getBlockTxsExtend": {
               "MethodDescription": "\u6839\u636ehash\u5217\u8868\uff0c\u83b7\u53d6\u4ea4\u6613\uff0c\u5148\u67e5\u672a\u786e\u8ba4\uff0c\u518d\u67e5\u5df2\u786e\u8ba4/Get transactions by hashs",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getBlockTxsExtend",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHashList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "allHits",
                     "ParameterType": "boolean",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getConfirmedTx": {
               "MethodDescription": "\u6839\u636ehash\u83b7\u53d6\u5df2\u786e\u8ba4\u4ea4\u6613(\u53ea\u67e5\u5df2\u786e\u8ba4)/Get confirmed transaction by tx hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getConfirmedTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getConfirmedTxClient": {
               "MethodDescription": "\u6839\u636ehash\u83b7\u53d6\u5df2\u786e\u8ba4\u4ea4\u6613(\u53ea\u67e5\u5df2\u786e\u8ba4)/Get confirmed transaction by tx hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getConfirmedTxClient",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getNonexistentUnconfirmedHashs": {
               "MethodDescription": "\u67e5\u8be2\u4f20\u5165\u7684\u4ea4\u6613hash\u4e2d,\u4e0d\u5728\u672a\u786e\u8ba4\u5e93\u4e2d\u7684\u4ea4\u6613hash/Get nonexistent unconfirmed transaction hashs",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getNonexistentUnconfirmedHashs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHashList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getSystemTypes": {
               "MethodDescription": "\u83b7\u53d6\u6240\u6709\u7cfb\u7edf\u4ea4\u6613\u7c7b\u578b/Get system transaction types",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getSystemTypes",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getTx": {
               "MethodDescription": "\u6839\u636ehash\u83b7\u53d6\u4ea4\u6613, \u5148\u67e5\u672a\u786e\u8ba4, \u67e5\u4e0d\u5230\u518d\u67e5\u5df2\u786e\u8ba4/Get transaction by tx hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_getTxClient": {
               "MethodDescription": "\u6839\u636ehash\u83b7\u53d6\u4ea4\u6613\uff0c\u5148\u67e5\u672a\u786e\u8ba4\uff0c\u67e5\u4e0d\u5230\u518d\u67e5\u5df2\u786e\u8ba4/Get transaction by tx hash",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_getTxClient",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHash",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_newTx": {
               "MethodDescription": "\u63a5\u6536\u672c\u5730\u65b0\u4ea4\u6613/receive a new transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_newTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_packableTxs": {
               "MethodDescription": "\u83b7\u53d6\u53ef\u6253\u5305\u7684\u4ea4\u6613\u96c6/returns a list of packaged transactions",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_packableTxs",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "endTimestamp",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "maxTxDataSize",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockTime",
                     "ParameterType": "long",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "packingAddress",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "preStateRoot",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_register": {
               "MethodDescription": "\u6ce8\u518c\u6a21\u5757\u4ea4\u6613/Register module transactions",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_register",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "moduleCode",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "list",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "delList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_rollback": {
               "MethodDescription": "\u56de\u6eda\u533a\u5757\u7684\u4ea4\u6613/transaction rollback",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_rollback",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txHashList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_save": {
               "MethodDescription": "\u4fdd\u5b58\u65b0\u533a\u5757\u7684\u4ea4\u6613/Save the confirmed transaction",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_save",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "contractList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "blockHeader",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.tx_verifyTx": {
               "MethodDescription": "\u9a8c\u8bc1\u4ea4\u6613\u63a5\u53e3\uff0c\u5305\u62ec\u542b\u57fa\u7840\u9a8c\u8bc1\u3001\u9a8c\u8bc1\u5668\u3001\u8d26\u672c\u9a8c\u8bc1/Verify transation",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "tx_verifyTx",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.updateChainAsset": {
               "MethodDescription": "\u67e5\u8be2\u66f4\u65b0\u6d41\u901a\u8d44\u4ea7\u4fe1\u606f",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "updateChainAsset",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "assets",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.verifyCoinData": {
               "MethodDescription": "\u672a\u786e\u8ba4\u4ea4\u6613\u6821\u9a8c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "verifyCoinData",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.verifyCoinDataBatchPackaged": {
               "MethodDescription": "\u6253\u5305\u4ea4\u6613\u6821\u9a8c",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "verifyCoinDataBatchPackaged",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "[1-65535]",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "txList",
                     "ParameterType": "List",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nuls.withdrawValid": {
               "MethodDescription": "withdraw deposit agent transaction validate",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "withdrawValid",
               "MethodScope": "public",
               "Parameters": [
                  {
                     "ParameterName": "chainId",
                     "ParameterType": "int",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "tx",
                     "ParameterType": "String",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nulstar.ForwardMessage": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ForwardMessage",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nulstar.GetCPUInfo": {
               "MethodDescription": "Query information about CPU",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "GetCPUInfo",
               "MethodScope": "admin",
               "Parameters": [
                  {
                     "ParameterName": "lMaxCPUs",
                     "ParameterType": "int"
                  }
               ]
            },
            "Nulstar.GetConsolidatedAPI": {
               "MethodDescription": "",
               "MethodMinEvent": "1",
               "MethodMinPeriod": "0",
               "MethodName": "GetConsolidatedAPI",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nulstar.GetRAMInfo": {
               "MethodDescription": "Query information about RAM memory",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "GetRAMInfo",
               "MethodScope": "admin",
               "Parameters": []
            },
            "Nulstar.ListAPI": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "ListAPI",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nulstar.RegisterAPI": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "RegisterAPI",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nulstar.checkupdates": {
               "MethodDescription": "",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "checkupdates",
               "MethodScope": "public",
               "Parameters": []
            },
            "Nulstar.scanmanagedmodules": {
               "MethodDescription": "Searches and reads the configuration file Module.ncf in the directory hierarchy.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "scanmanagedmodules",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nulstar.shutdownsystem": {
               "MethodDescription": "Stops the system enterily.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "shutdownsystem",
               "MethodScope": "admin",
               "Parameters": []
            },
            "Nulstar.startallmodules": {
               "MethodDescription": "Starts modules of the desired namespace, if blank then all available modules are started.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "startallmodules",
               "MethodScope": "private",
               "Parameters": [
                  {
                     "ParameterName": "fRestartIfRunning",
                     "ParameterType": "bool",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nulstar.startmodule": {
               "MethodDescription": "Starts the specified module.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "startmodule",
               "MethodScope": "private",
               "Parameters": [
                  {
                     "ParameterName": "lModuleName",
                     "ParameterType": "QString",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "lModuleVersion",
                     "ParameterType": "QString",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "fRestartIfRunning",
                     "ParameterType": "bool",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            },
            "Nulstar.stopallmodules": {
               "MethodDescription": "Stops all modules belonging to the specified namespace, if blank it stops all modules that are currently running.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "stopallmodules",
               "MethodScope": "private",
               "Parameters": []
            },
            "Nulstar.stopmodule": {
               "MethodDescription": "Stops the specified module.",
               "MethodMinEvent": "0",
               "MethodMinPeriod": "0",
               "MethodName": "stopmodule",
               "MethodScope": "private",
               "Parameters": [
                  {
                     "ParameterName": "lModuleName",
                     "ParameterType": "QString",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  },
                  {
                     "ParameterName": "lModuleVersion",
                     "ParameterType": "QString",
                     "ParameterValidRange": "",
                     "ParameterValidRegExp": ""
                  }
               ]
            }
         }
      },
      "ResponseErrorCode": "",
      "ResponseMaxSize": "0",
      "ResponseProcessingTime": "1",
      "ResponseStatus": 0
   },
   "MessageID": "1575848916688-8",
   "MessageType": "Response",
   "TimeZone": "-8",
   "Timestamp": "1575884636505"
}
--------------end Regular request--------------------------------

Process finished with exit code 0

