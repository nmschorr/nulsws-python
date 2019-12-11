#Nuls.ac_getAccountList"

from nulsws_labels_request_name import AC_GET_ACCOUNT_LIST
from nulsws_library import prep_TOP_SECTION
import json
from nulsws_labels import *
from nulsws_labels import CHAINID_LABEL, ZERO
from nulsws_labels import msg_data_label

## from user settings:
CHAINID_VAL = 1

def req_AC_GET_ACCOUNT_LIST(mind):   #requesttype 2 - return ack and response
    stat_msg_top = prep_TOP_SECTION(3, mind)

    bottom = {
        msg_data_label: {
            request_type_label: "1",
            subscrip_evnt_ct_label: ZERO,
            subscrip_period_label: ZERO,
            subscriptn_range_label: ZERO,
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
