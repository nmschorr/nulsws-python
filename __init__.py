#!/usr/bin/python3.7


# This file makes this directory a module
# import each function here and name it so it is available within the module

# from .nulsws_library import *
# from .nulsws_msgtype1 import port1, websock_url1, connect_method1, compression_type1, comp_int1



# from .nulsws_library, .nulsws_msgtype1 import * will import these:

# (keep this list up to date)
# __all__ = ["check_answer", "prep_async", "prep_data1", "port1", "connect_method1", "websock_url1",
#            "compression_type1", "comp_int1"]

from nulsws_library import get_times, prep_TOP_SECTION, check_json_answer, myprint
from nulsws_labels import address_label, compress_rate_label, compress_type_label, \
    get_bal_label, get_height_label, json_seps, msg_data_label, msg_id_label, \
    msg_type_label, negotiate_conn_label, negotiate_conn_resp_label, negotiate_stat_label, \
    proto_label, req_methods_label, request_date_label, request_internalid_label, request_label, \
    request_type_label, request_time_label, response_max_size_label, \
    subscriptn_range_label, subscrip_evnt_ct_label, subscrip_period_label, tmstmp_label, tmzone_label

# __ALL__ = [get_times, prep_TOP_SECTION, check_json_answer, myprint, address_label, \
#            compress_rate_label, compress_type_label, get_bal_label, get_height_label, json_seps,
#            msg_data_label, \
#            msg_id_label, msg_type_label, negotiate_conn_label, negotiate_conn_resp_label,
#            negotiate_stat_label, \
#            proto_label, req_method_label, request_date_label, request_internalid_label,
#            request_label, \
#            request_t_label, request_time_label, response_max_size_label, sub_rg_label,
# \
#            subscrip_evnt_ct_label, subscrip_period_label, tmstmp_label, tmzone_label]
