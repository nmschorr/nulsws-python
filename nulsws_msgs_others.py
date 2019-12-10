

import json
from nulsws_usersets_negt_type1 import proto_ver, compress_type_negt, comp_rate_negt
from nulsws_library import prep_TOP_SECTION, json_prt
from nulsws_staticvals import *

#-----------prep_NEGOTIATE_data_type1--------------------------------------#
def prep_NEGOTIATE_data_type1(mind):
        # this section has any number of items depending on the msg type
    top_sect = prep_TOP_SECTION(1, mind)
    data_part = { msg_data_label: {
                  proto_label: proto_ver,
                  compress_type_label: compress_type_negt,
                  compress_rate_label: comp_rate_negt}}
    top_sect.update(data_part)
    json_str = json.dumps(top_sect, separators=json_seps)
    return json_str


#-----------prep_data_REQUEST_type3--------------------------------------#

def prep_data_REQUEST_type3(mind):   #requesttype 2 - return ack and response
    stat_msg_top = prep_TOP_SECTION(3, mind)

    bottom = {
        "MessageData": {
            "RequestType": "2",
            "SubscriptionEventCounter": "0",
            "SubscriptionPeriod": "0",
            "SubscriptionRange": "0",
            "ResponseMaxSize": "0",
            "RequestMethods":
              {
                  # "ListAPI": #works!
                  #"cm_getChainsSimpleInfo":   #works!
                  #"getRegisteredChainInfoList" :  {}   #works
                  #"nw_getSeeds" : {}      # works!
                  #"nw_getMainMagicNumber": {}  #  works!
                  #"nw_currentTimeMillis": {}  # works!
                  #"cs_getConsensusConfig" : { "chainId": 1} #works


              }
          } }

    stat_msg_top.update(bottom)
    return json.dumps(stat_msg_top)
