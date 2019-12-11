

import json
from nulsws_usersets_negt_type1 import proto_ver, compress_type_negt, comp_rate_negt
from nulsws_library import prep_TOP_SECTION
from nulsws_labels import *

#-----------prep_NEGOTIATE_data_type1--------------------------------------#
def prep_NEGOTIATE_data_type1(msg_indx):
        # this section has any number of items depending on the msg type
    top_sect = prep_TOP_SECTION(1, msg_indx)
    data_part = { msg_data_label: {
                  proto_label: proto_ver,
                  compress_type_label: compress_type_negt,
                  compress_rate_label: comp_rate_negt}}
    top_sect.update(data_part)
    json_str = json.dumps(top_sect, separators=json_seps)
    return json_str


#-----------get_REQ_MIDDLE--------------------------------------#

def get_REQ_MIDDLE(mid_section_vals=None):

    if not mid_section_vals:
        mid_section_vals = ["2", ZERO, ZERO, ZERO, ZERO] #2 = ack+date
    [MTL, SECL, SPL, SRL, RMS] = [*mid_section_vals]

    REQ_MIDDLE = {
        msg_data_label: {
            msg_type_label: MTL,
            subscrip_evnt_ct_label : SECL,
            subscrip_period_label: SPL,
            subscriptn_range_label: SRL,
            response_max_size_label: RMS
        }}
    return REQ_MIDDLE

def prep_data_REQUEST_type3(msg_indx):  # requesttype 2 - return ack and
        # response
    onesy_label = "nw_getSeeds"
    MSG_TYPE = 3

    message_section_top = prep_TOP_SECTION(MSG_TYPE, msg_indx)
    msg_section_middle = get_REQ_MIDDLE()
    msg_section_bottom = {
        req_methods_label: {
              onesy_label: {}  # works!
          } }

    msg_section_middle.update(msg_section_bottom)
    message_section_top.update(msg_section_middle)
    return message_section_top   # return dict

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