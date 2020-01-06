# Nuls.ac_getAccountList"


import json

# from libraries.nulsws_REQUEST import AC_GET_ACCOUNT_LIST
from libraries.nulsws_request import get_top_section
from libraries.Constants.nulsws_otherlabels import *

## from user settings:

CHAINID_VAL = 1


def req_AC_GET_ACCOUNT_LIST(mind):  #
    stat_msg_top = get_top_section(3, mind)   # 3 is a Request

    bottom = {
        msg_data_label: {
            request_type_label: "1",       # 1 = normal response only
            subscrip_evnt_ct_label: ZERO,   # not implemented yet in Nulstar
            subscrip_period_label: ZERO,    # not implemented yet in Nulstar
            subscriptn_range_label: ZERO,    # not implemented yet in Nulstar
            response_max_size_label: ZERO,
            req_methods_label:
                {
                    AC_GET_ACCOUNT_LIST: {CHAINID_LABEL: CHAINID_VAL}
                }
        }}
    stat_msg_top.update(bottom)
    return json.dumps(stat_msg_top)






# "Nuls.ac_getAccountList": {
#     "MethodDescription": "\u83b7\u53d6\u6240\u6709\u8d26\u6237\u96c6\u5408,\u5e76\u653e\u5165\u7f13\u5b58/query all account collections and put them in cache",
#     "MethodMinEvent": "0",
#     "MethodMinPeriod": "0",
#     "MethodName": "ac_getAccountList",
#     "MethodScope": "public",
#     "Parameters": [
#         {
#             "ParameterName": "chainId",
#             "ParameterType": "int",
#             "ParameterValidRange": "",
#             "ParameterValidRegExp": ""
#         }
#     ]
# },
