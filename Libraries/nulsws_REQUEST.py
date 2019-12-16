#!/usr/bin/python3.7

from Libraries.nulsws_library import get_TOP_SECTION
from Libraries.Constants.nulsws_CONSTANTS_otherlabels import *
from UserSettings.nulsws_USER_PARAMS import USER_CALLS_DB

from UserSettings.nulsws_SET import *
# import UserSettings.nulsws_USER_PARAMS
# _up = dir(UserSettings.nulsws_USER_PARAMS)


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

def get_REQ_MIDDLE(bottom_part, mid_section_vals=None):   #return dict
    if not mid_section_vals:
        mid_section_vals = [ONE, ZERO, ZERO, ZERO, ZERO] #2 = ack+date
    [MTL, SECL, SPL, SRL, RMS] = [*mid_section_vals]

    REQ_MIDDLE = {
        msg_data_label: {
            msg_type_label: MTL,
            subscrip_evnt_ct_label : SECL,
            subscrip_period_label: SPL,
            subscriptn_range_label: SRL,
            response_max_size_label: RMS,
            req_methods_label: bottom_part
        }}
    return REQ_MIDDLE   #dict

# -----------prep_REQUEST_ONESIE (request) --------------------------------------#
def prep_REQUEST(msg_indx, api_name_tup):  # requesttype 2 - return ack +
    # response either has a second element of a list, or not
    MSG_TYPE = 3
    api_name = api_name_tup[0]
    api_text = api_name_tup[1]
    myparams = []

    kv = USER_CALLS_DB

    for uc in USER_CALLS_DB:
        if uc[0] == api_text:
            myparams = uc[1]   # part two is the params list
            break  # found it

    params_len = len(myparams)
    temp_dict = {}
    e = dict()
    msg_section_bottom = ''
    # -------------------------------------Length One ---------------------------------
    if params_len == 0:
        msg_section_bottom = dict({api_text: e})

    elif params_len > 0:
        for par in range(params_len):
            print("doing multiple params", api_name, ": ", myparams, "paramslen: ", params_len)

            p1 = str(myparams[par][0])
            p2 = str(myparams[par][1])
            temp_dict = dict({p1: p2})

        msg_section_bottom = dict({api_text: e})
        msg_section_bottom.__setitem__(api_text, temp_dict)

    msg_section_MIDDLE = get_REQ_MIDDLE(msg_section_bottom)
    a=0
    message_section_TOP = get_TOP_SECTION(MSG_TYPE, msg_indx)

    message_section_TOP.update(msg_section_MIDDLE)
    print(message_section_TOP)
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
