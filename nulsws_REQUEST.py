#!/usr/bin/python3.7

from nulsws_library import get_TOP_SECTION
from nulsws_CONSTANTS_otherlabels import *
from nulsws_USER_static_settings import *
from nulsws_USER_settings import *
from nulsws_USER_CHOICE import onesy_label

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
def prep_REQUEST_ONESIE_NO_params(msg_indx, onesie):  # requesttype 2 - return ack + response
    MSG_TYPE = 3
    count = 2
    try:
        both = onesie[1][0]
    except:
        count = 1

    if count == 2:
        msg_section_bottom = { onesie[0]: both }
    else:
        msg_section_bottom = { onesie[0]: []  }

    msg_section_MIDDLE = get_REQ_MIDDLE(msg_section_bottom)
    message_section_TOP = get_TOP_SECTION(MSG_TYPE, msg_indx)
    message_section_TOP.update(msg_section_MIDDLE)
    return message_section_TOP   # return dict

# ----------- end library file --------------------------------------#




# msg_section_middle = {
    #     "MessageData": {
    #         "RequestType": "2",
    #         "SubscriptionEventCounter": "0",
    #         "SubscriptionPeriod": "0",
    #         "SubscriptionRange": "0",
    #         "ResponseMaxSize": "0",
    #         "RequestMethods":
    #           {


# "ListAPI": #works!
# "cm_getChainsSimpleInfo":   #works!
# "getRegisteredChainInfoList" :  {}   #works
# "nw_getSeeds": {}  # works!
# "nw_getMainMagicNumber": {}  #  works!
# "nw_currentTimeMillis": {}  # works!
# "cs_getConsensusConfig" : { "chainId": 1} #works