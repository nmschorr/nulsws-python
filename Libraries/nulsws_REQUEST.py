#!/usr/bin/python3.7

from Libraries.nulsws_library import get_TOP_SECTION

from Libraries.Constants.nulsws_CONSTANTS_otherlabels import *
from UserSettings.nulsws_USER_PARAMS import proto_ver

# from UserSettings.nulsws_USER_PARAMS import _USER_PARAMS
# from Libraries.Constants.nulsws_CONSTANTS_PARAM_LABELS import *
from Libraries.Constants.nulsws_CONSTANTS_PARAM_LOOKUP import PARAM_LOOKUP
# from Libraries.Constants.nulsws_CONSTANTS_API_LABELS import *


# -----------prep_NEGOTIATE_data_type1--------------------------------------#
def prep_NEGOTIATE_request(msg_indx):   #return dict
    compress_rate_VALUE = 1
    compress_type_VALUE = "zlib"


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
    MSG_TYPE = 3
    openSQRB = "["
    closeSQRB = "]"
    OPENBRKT = "{ "
    CLOSEBRKT = "}"
    COMMA = ", "
    COLON = ": "
    COLON = ": "
    beginn = " "
    endd = " :{} }"

    api_name = api_name_tup[0]
    api_name_word = api_name_tup[1]
    myparams = []
    msg_section_bottom = ''

    for i in PARAM_LOOKUP:
        if i[0] == api_name_word:
            myparams = i[1]
            for tup in myparams:
                print(tup[0], tup[1])
            break  # found it

    params_len = len(myparams)
    print("params len: ", params_len)
    # -------------------------------------Length One ---------------------------------
    if params_len == 0:
        print("doing a 0 params", api_name, ": ", myparams)
        api_name_word = str(myparams)
        midd: str = api_name_word + ":{}"
        msg_section_bottom.join(f'{OPENBRKT}{midd}{CLOSEBRKT}{closeSQRB}')

    else:
        # msg_section_bottom: str = " [{ " + api_name_word + ": "
        msg_section_bottom = openSQRB

        for x in range(params_len):
            print("doing a 0 params", api_name, ": ", myparams)
            p1 = str(myparams[0][0])
            p2 = str(myparams[0][1])
            midd: str = f"{api_name_word}" + ": "
            msg_section_bottom = f'{openSQRB}{OPENBRKT}{midd}{CLOSEBRKT},'

            ddline = f'{OPENBRKT}{p1}{COLON}{p2}{closeSQRB}'
            msg_section_bottom += ddline
            # print()
        msg_section_bottom = msg_section_bottom + ']'

    msg_section_MIDDLE = get_REQ_MIDDLE(msg_section_bottom)
    message_section_TOP = get_TOP_SECTION(MSG_TYPE, msg_indx)
    message_section_TOP.update(msg_section_MIDDLE)
    print(message_section_TOP)
    return message_section_TOP  # return dict

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
