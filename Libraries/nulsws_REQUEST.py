#!/usr/bin/python3.7

from Libraries.nulsws_library import get_times
from Libraries.Constants.nulsws_CONSTANTS_otherlabels import *
from UserSettings.nulsws_SET import *
from UserSettings.nulsws_USER_PARAMS import USER_CALLS_DB
import json

# -----------prep_NEGOTIATE_data_type1--------------------------------------#
def prep_NEGOTIATE_request(msg_indx):   #return dict
    # this section has any number of items depending on the msg type
    top_sect = get_TOP_SECTION(1, msg_indx)
    data_part = { msg_data_label: {
                  proto_label: proto_ver,
                  compress_type_label: compress_type_VALUE,
                  compress_rate_label: compress_rate_VALUE}}
    top_sect.update(data_part)
    return top_sect   # dict

# -----------get_REQ_MIDDLE--------------------------------------#

def get_TOP_SECTION(msg_type: int, msg_indx):  # this section builds 5 items: #0
    # 0  "ProtocolVersion": "0.1",
    # 1 "MessageID": "1569897424187-1",  #2 "TimeZone": "-4",   #3 "Timestamp": "1569897424187"
    # #4 "MessageType": "NegotiateConnection",
    msg_type_name = type_name_dict.__getitem__(msg_type)
    t_stamp, tzone, m_id = get_times(msg_indx)
    top_part = {proto_label: proto_ver,
                msg_id_label: m_id,
                tmstmp_label: t_stamp,
                tmzone_label: tzone,
                msg_type_label: msg_type_name}
    return top_part

# -----------get_REQ_MIDDLE--------------------------------------#

def get_REQ_MIDDLE(bottom_part, mid_section_vals=None):   #return dict
    if not mid_section_vals:
        mid_section_vals = [1, ZERO, ZERO, ZERO, ZERO] #2 = ack+date

    [RT, SEC, SP, SR, RMS] = [*mid_section_vals]

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
def prep_REQUEST(msg_indx, api_name_tup):  # requesttype 2 - return ack +
    # response either has a second element of a list, or not
    MSG_TYPE = 3  # for request
    api_name = api_name_tup[0]
    api_text = api_name_tup[1]
    myparams = []

    for uc in USER_CALLS_DB:
        if uc[0] == api_text:
            myparams = uc[1]   # part two is the params list
            break  # found it

    params_len = len(myparams)
   # bottom_group = list()
    bottom_group = dict()

    pdict = dict([])
    # -------------------------------------Length One ---------------------------------

    if params_len > 0:
        for t_item in range(params_len):
            print("doing multiple params", api_name, ": ", myparams, "paramslen: ", params_len)
            p1 = str(myparams[t_item][0])
            p2 = str(myparams[t_item][1])
            pdict.update({p1: p2})

    bottom_group.__setitem__(0, {api_text: pdict})    #this is the last item of six
    # bottom_dict = dict({api_text : pdict })
    request_type = "2"  # 1 or 2 for message requests
    subscrip_e_ct = ""   #subscrip_evnt_ct
    subscrip_period = ""
    subscrip_rng = ""
    response_max_size = ""

    newlist = [request_type, subscrip_e_ct, subscrip_period, subscrip_rng, response_max_size]

    msg_section_MIDDLE = get_REQ_MIDDLE(bottom_group, newlist)

    message_section_TOP = get_TOP_SECTION(MSG_TYPE, msg_indx)
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
