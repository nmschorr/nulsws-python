#!/usr/bin/python3.7

import json

<<<<<<< HEAD:libraries/nulsws_request.py
from libraries.constants.nulsws_name_pairs import NamePairs
import libraries.constants.nulsws_calls_db  # import class for calls_list
from libraries.constants.nulsws_otherlabels import *
from user_settings.nulsws_settings import *
import libraries.nulsws_library
from libraries.nulsws_library import NulswsLibrary as nulib


=======
from Libraries.Constants.Dictionaires.nulsws_NAME_PAIRS import NAME_PAIRS
from Libraries.Constants.nulsws_CONSTANTS_otherlabels import *
from UserSettings.nulsws_SET import *
import Libraries.Constants.CLASSES.nulsws_cls_PARAMS  # import class for USER_CALLS_DB
import Libraries.nulsws_library
# -----------prep_NEGOTIATE_data_type1--------------------------------------#
>>>>>>> master:Libraries/nulsws_REQUEST.py

# -----------prep_NEGOTIATE_data_type1--------------------------------------#

def prep_NEGOTIATE_request(msg_indx):   #return dict
    data_part = { msg_data_label: {
                  proto_label: proto_ver,
                  compress_type_label: compress_type_VALUE,
                  compress_rate_label: compress_rate_VALUE}}
    top_sect = get_top_section(1, msg_indx)
    top_sect.update(data_part)
    return top_sect   # dict

# -----------get_REQ_MIDDLE--------------------------------------#

def get_top_section(msg_type: int, msg_indx):  # this section builds 5 items: #0
    # 0  "ProtocolVersion": "0.1",
    # 1 "MessageID": "1569897424187-1",  #2 "TimeZone": "-4",   #3 "Timestamp": "1569897424187"
<<<<<<< HEAD:libraries/nulsws_request.py
    # 4 "MessageType": "NegotiateConnection",
    # msg_type_name = type_name_dict.__getitem__(msg_type)

    msg_type_name = type_name_dict[msg_type]

    t_stamp, tzone, m_id = nulib.get_times(msg_indx)
=======
    # #4 "MessageType": "NegotiateConnection",
    msg_type_name = type_name_dict.__getitem__(msg_type)
    t_stamp, tzone, m_id = Libraries.nulsws_library.Nulsws_Library.get_times(msg_indx)
>>>>>>> master:Libraries/nulsws_REQUEST.py
    top_part = {proto_label: proto_ver,
                msg_id_label: m_id,
                tmstmp_label: t_stamp,
                tmzone_label: tzone,
                msg_type_label: msg_type_name}
    return top_part

# -----------get_REQ_MIDDLE--------------------------------------#

def get_request_middle(mid_section_vals=None):   #return dict
    if not mid_section_vals:
        mid_section_vals = [1, ZERO, ZERO, ZERO, ZERO] #2 = ack+date
    [RT, SEC, SP, SR, RMS, bottom_part] = [*mid_section_vals]

    req_middle = {
        msg_data_label: {
            request_type_label: RT,
            subscrip_evnt_ct_label : SEC,
            subscrip_period_label: SP,
            subscriptn_range_label: SR,
            response_max_size_label: RMS,
            req_methods_label: bottom_part
        }}
    return req_middle   #dict

# -----------prep_REQUEST_ONESIE (request) --------------------------------------#
def prep_REQUEST(msg_indx, api_name):  # requesttype 2 - return ack +

    param = libraries.constants.nulsws_calls_db.nulsws_params
    user_calls_db = param.calls_list
    name_list =  NamePairs.name_pairs_list

    # response either has a second element of a list, or not
    api_name_tup = [i for i in name_list if i[1] == api_name][0]
    api_text = api_name_tup[1]
    api_params_dict = {}
    api_text_api_params_dict = dict()
    try:
        api_params_list = [val[1] for val in user_calls_db if val[0] == api_text]

        api_params_dict = dict(api_params_list[0])
    except:
        pass

    api_text_api_params_dict.update({api_text: api_params_dict})

    request_type = "2"  # 1 or 2 for message requests
    subs_e_c = "0"     # subscription event_counter
    subs_per = "0"      # subscription period
    subs_rg = "0"      # subscription range
    resp_max = "0"    # response max size range

    newlist = [request_type, subs_e_c, subs_per, subs_rg, resp_max, api_text_api_params_dict]

    msg_section_middle = get_request_middle(newlist)
    message_section_top = get_top_section(3, msg_indx)
    message_section_top.update(msg_section_middle)
    print(json.dumps(message_section_top, indent=2))
    return message_section_top  # "'"return dict

# ----------- end library file --------------------------------------#








# ---------------- Example -------------------------------------------------------------------

#
# Example of type 3 message:
# {
#     "ProtocolVersion": "0.1.0"
#     "MessageID": m_id,
#     "TimeZone": tzone,
#     "Timestamp": t_stamp
#     "MessageType": "Request",
#     "MessageData": {
#         "RequestType": "1",
#         "SubscriptionEventCounter": "0",
#         "SubscriptionPeriod": "1",
#         "SubscriptionRange": "[100]",
#         "ResponseMaxSize": "0",
#         "RequestMethods": [
#           {
#             "GetBalance": {
#               "Address": "tNULSeBaMnrs6JKrCy6TQdzYJZkMZJDng7QAsD"
#             }
#           },
#           {
#             "GetHeight": {}
#           }
#         ]
#        }
#     }