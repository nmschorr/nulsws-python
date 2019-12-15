#!/usr/bin/python3.7

from Libraries.nulsws_library import get_TOP_SECTION
from UserSettings.nulsws_USER_static_settings import *
from UserSettings.nulsws_USER_settings import *
from Libraries.Constants.nulsws_CONSTANTS_otherlabels import *
from Libraries.Constants.nulsws_CONSTANTS_API_LABELS import *
from Libraries.Constants.nulsws_CONSTANTS_PARAM_LABELS import *
from UserSettings.nulsws_USER_PARAMS import user_calls_list as uclist




# -----------prep_NEGOTIATE_data_type1--------------------------------------#
def prep_NEGOTIATE_data_type1(msg_indx):   #return dict
        # this section has any number of items depending on the msg type
    top_sect = get_TOP_SECTION(1, msg_indx)
    data_part = { msg_data_label: {
                  proto_label: proto_ver,
                  compress_type_label: compress_type_VALUE,
                  compress_rate_label: compress_rate_VALUE}}
    top_sect.update(data_part)
    return top_sect   # dict

# -----------get_REQ_MIDDLE--------------------------------------#
    # set mid_section_vals in user library file
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
def prep_REQUEST_ONESIE_NO_params_or_just_ONE(msg_indx, api_name_tup):  # requesttype 2 - return ack +
    # response
    # onesie either has a second element of a list, or not
    # user_params_list = uc.user_parameters
    api_name = api_name_tup[0]
    api_name_word = api_name_tup[1]
    myvarslist = []

    for i in uclist:
        if i[0] == api_name_word:
            myvarslist = i[1]
            for tup in myvarslist:
                print(tup[0], tup[1])
                break

    msg_section_bottom = ''
    params_len = len(myvarslist)
    if params_len == 0:
        msg_section_bottom = {
            api_name:
                {}  # later substitute, needs to be fixed for other vals
        }
    if params_len == 1:
        msg_section_bottom = {
            api_name :
                { myvarslist[0][0] : myvarslist[0][1] }   # later substitute, needs to be fixed for
            }

    if params_len == 2:
        msg_section_bottom = {
            api_name:
                [ { myvarslist[0][0]: myvarslist[0][1] },  # later substitute, needs to be fixed for
                { myvarslist[1][0]: myvarslist[1][1] }]  # later substitute, needs to be fixed for

        }
    if params_len == 3:
        msg_section_bottom = {
            api_name:
                [ { myvarslist[0][0]: myvarslist[0][1] },  # later substitute, needs to be fixed for
                { myvarslist[1][0]: myvarslist[1][1] },  # later substitute, needs to be fixed for
                { myvarslist[2][0]: myvarslist[2][1]}]  # later substitute, needs to be fixed for
        }
    msg_section_MIDDLE = get_REQ_MIDDLE(msg_section_bottom)
    message_section_TOP = get_TOP_SECTION(MSG_TYPE, msg_indx)
    message_section_TOP.update(msg_section_MIDDLE)
    return message_section_TOP   # return dict

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
