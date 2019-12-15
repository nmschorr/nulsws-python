#!/usr/bin/python3.7

from Libraries.nulsws_library import get_TOP_SECTION
from UnusedSoFar.nulsws_USER_static_settings import *
from UnusedSoFar.nulsws_USER_settings import *
from Libraries.Constants.nulsws_CONSTANTS_otherlabels import *
from UserSettings.nulsws_USER_PARAMS import USER_CALLS_WITH_PARAMS as uclist




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
def prep_REQUEST(msg_indx, api_name_tup):  # requesttype 2 - return ack +
    # response
    # onesie either has a second element of a list, or not
    # user_params_list = uc.user_parameters
    api_name = api_name_tup[0]
    api_name_word = api_name_tup[1]
    myparams = []
    msg_section_bottom = ''

    for i in uclist:
        if i[0] == api_name_word:
            myparams = i[1]
            for tup in myparams:
                print(tup[0], tup[1])
            break  # found it

    params_len = len(myparams)
    print("params len: ", params_len)
    if params_len == 0:
        print("doing a 0 params", api_name_tup, ": ", myparams)
        msg_section_bottom = {
            api_name_word:
                {}  # later substitute, needs to be fixed for other vals
        }
    else:
        msg_section_bottom = " { " + api_name_word + ": "
        for x in range(params_len):
            p1 = str(myparams[x][0])
            p2 = str(myparams[x][1])
            openq = "{ "
            closeq = " } "
            colm = ": "
            ddline = f'{openq}{p1}{colm}{p2}{closeq}'
            msg_section_bottom = msg_section_bottom + ddline
            #print()

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
