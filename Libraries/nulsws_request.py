#!/usr/bin/python3.7

import json

from Libraries.Constants.classes.nulsws_NAME_PAIRS import NAME_PAIRS
from Libraries.Constants.nulsws_otherlabels import *
from UserSettings.nulsws_settings import *
import Libraries.Constants.classes.nulsws_calls_DB  # import class for USER_CALLS_DB
import Libraries.nulsws_library as nulib
# -----------prep_NEGOTIATE_data_type1--------------------------------------#


def prep_NEGOTIATE_request(msg_indx):   #return dict
    data_part = { msg_data_label: {
                  proto_label: proto_ver,
                  compress_type_label: compress_type_VALUE,
                  compress_rate_label: compress_rate_VALUE}}
    top_sect = get_TOP_SECTION(1, msg_indx)
    top_sect.update(data_part)
    return top_sect   # dict

# -----------get_REQ_MIDDLE--------------------------------------#

def get_TOP_SECTION(msg_type: int, msg_indx):  # this section builds 5 items: #0
    # 0  "ProtocolVersion": "0.1",
    # 1 "MessageID": "1569897424187-1",  #2 "TimeZone": "-4",   #3 "Timestamp": "1569897424187"
    # #4 "MessageType": "NegotiateConnection",
    #msg_type_name = type_name_dict.__getitem__(msg_type)

    msg_type_name = type_name_dict[msg_type]
    t_stamp, tzone, m_id = nulib.get_times(msg_indx)
    top_part = {proto_label: proto_ver,
                msg_id_label: m_id,
                tmstmp_label: t_stamp,
                tmzone_label: tzone,
                msg_type_label: msg_type_name}
    return top_part

# -----------get_REQ_MIDDLE--------------------------------------#

def get_REQ_MIDDLE(mid_section_vals=None):   #return dict
    if not mid_section_vals:
        mid_section_vals = [1, ZERO, ZERO, ZERO, ZERO] #2 = ack+date
    [RT, SEC, SP, SR, RMS, bottom_part] = [*mid_section_vals]

    REQ_MIDDLE = {
        msg_data_label: {
            request_type_label: RT,
            subscrip_evnt_ct_label : SEC,
            subscrip_period_label: SP,
            subscriptn_range_label: SR,
            response_max_size_label: RMS,
            req_methods_label: bottom_part
        }}
    return REQ_MIDDLE   #dict

# -----------prep_REQUEST_ONESIE (request) --------------------------------------#
def prep_REQUEST(msg_indx, api_name):  # requesttype 2 - return ack +
    # import Libraries.constants.CLASSES.nulsws_cls_PARAMS  # import class for USER_CALLS_DB

    param_object = Libraries.Constants.classes.nulsws_calls_DB.nulsws_Cls_Prm()
    USER_CALLS_DB = param_object.USER_CALLS_DB

    # response either has a second element of a list, or not
    api_name_tup = [i for i in NAME_PAIRS if i[1] == api_name][0]
    api_text = api_name_tup[1]
    API_params_dict = {}
    API_text_API_PARAMS_dict = dict()
    try:
        API_params_LIST = [val[1] for val in USER_CALLS_DB if val[0] == api_text]

        API_params_dict = dict(API_params_LIST[0])
    except:
        pass

    API_text_API_PARAMS_dict.update({api_text: API_params_dict})

    request_type = "2"  # 1 or 2 for message requests
    subs_e_c = "0"     # subscription event_counter
    subs_per = "0"      # subscription period
    subs_rg = "0"      # subscription range
    resp_max = "0"    # response max size range

    newlist = [request_type, subs_e_c, subs_per, subs_rg, resp_max, API_text_API_PARAMS_dict]

    msg_section_MIDDLE = get_REQ_MIDDLE(newlist)
    message_section_TOP = get_TOP_SECTION(3, msg_indx)
    message_section_TOP.update(msg_section_MIDDLE)
    print(json.dumps(message_section_TOP, indent=2))
    return message_section_TOP  # "'"return dict

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
