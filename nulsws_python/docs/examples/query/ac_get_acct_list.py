#!/usr/bin/python3.7
#
# Nuls.ac_getAccountList"


import json
from nulsws_python.src.nulsws_python.nulsws_request import get_top_section
from nulsws_python.src.nulsws_python.user_settings.nulsws_settings_two import *
from nulsws_python.src.nulsws_python.constants.nulsws_api_labels import NulswsApiLabel
from nulsws_python.src.nulsws_python.constants.nulsws_other_labels import *


class AcGetAcctList(object):

    def __init__(self):
        self.chainid_val = 1
        self.n = NulswsApiLabel()

    def req_ac_get_account_list(self, m_index):  #
        stat_msg_top = get_top_section(3, m_index)   # 3 is a Request

        bottom = {
            msg_data_label: {
                request_type_label: "1",       # 1 = normal response only
                subscrip_evnt_ct_label: ZERO,   # not implemented yet in Nulstar
                subscrip_period_label: ZERO,    # not implemented yet in Nulstar
                subscriptn_range_label: ZERO,    # not implemented yet in Nulstar
                response_max_size_label: ZERO,
                req_methods_label:
                    {
                        self.n.AC_GET_ACCOUNT_LIST: {CHAINID_LABEL: self.chainid_val}
                    }
            }}
        stat_msg_top.update(bottom)
        return json.dumps(stat_msg_top)


if __name__ == '__main__':
    ac = AcGetAcctList()
    ac.req_ac_get_account_list()




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
