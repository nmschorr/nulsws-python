#!usr/bin/python3.7


'''
author:  Nancy M Schorr, for Nuls
December 2, 2019

NEGOTIATE CONNECTION

The first message that should be sent. If this message receives a response of '1', then
service may proceed to further requests.

With a failure, a NegotiateConnectionResponse object will be received with
Status of '0' (Failure) and this service should disconnect immediately.

Messages have a common structure composed of six fields:

•  ProtocolVersion: version the service to understand,2 numbers, major/minor
•  MessageID: identifies a request.
•  Timestamp:  Number  of  seconds  since  epoch January 1,1970
•  TimeZone: The time zone where the request was originated
•  MessageType: The message type, these are specified on section 3
•  MessageData: A Json object with the message payload

Example Negotiate Connection message - order of items doesn't matter when at the same level
{
  "MessageData":{
    "CompressionAlgorithm":"zlib",
    "CompressionRate":"0",
    "ProtocolVersion":"0.1"
  },
  "MessageID":"1569897424187-1",
  "MessageType":"NegotiateConnection",
  "TimeZone":"-4",
  "Timestamp":"1569897424187"
}

Compression Rate can be values 0 through 9.
Compression Algorithm is normally "zlib"

 -- Enter your custom settings data via the library file 'nulsws_msgtype1.py'.

Note: Don't use typing.Dict - it can cause json problems when converted.

This file right now provides support for the the client only.

'''

import json
from random import random
from time import time, timezone
from nulsws_msgtype1 import proto_ver, compress_type1, comp_rate1
from nulsws_staticvals import m_dict, bigtest

compress_type_label = "CompressionAlgorithm"
compress_rate_label = "CompressionRate"
msg_data_label = "MessageData"
msg_id_label = "MessageID"
msg_type_label = "MessageType"
negotiate_conn_label = "NegotiateConnection"
negotiate_stat_label = 'NegotiationStatus'
negotiate_conn_resp_label = "NegotiateConnectionResponse"
proto_label = "ProtocolVersion"
tmstmp_label = "Timestamp"
tmzone_label = "TimeZone"
request_label = "Request"
request_internalid_label = "RequestInternalID"
request_date_label = "RequestDate"
request_time_label = "RequestTime"
json_seps = (',', ':')
json_d = None


def do_math():
    rand_ending = str(int(round(random() * 100000)))

    the_time = time()
    m_id1 = str(int(the_time * 100000))  # change float to int to str
    part_id = m_id1[4:]  # remove the first 4 chars
    m_id = part_id + rand_ending
    tzone = str(int(timezone / 3600))   # change float to int to str
    t_stamp = str(int(the_time * 1000))       # change float to int
    return t_stamp, tzone, m_id

def prep_header_section(msg_type: int):         # this section builds 4 items:
    #1 "MessageID": "1569897424187-1",
    #2 "TimeZone": "-4",
    #3 "Timestamp": "1569897424187"
    #4 "MessageType": "NegotiateConnection",
    msg_type_name = m_dict.__getitem__(msg_type)
    t_stamp, tzone, m_id= do_math()
    top_part = { msg_id_label: m_id,
                    # request_internalid_label: "348022847492",
                    # request_date_label: "2019-12-06",
                    # request_time_label: "19:00:00",
                    tmstmp_label : t_stamp,
                    tmzone_label: tzone,
                    msg_type_label: msg_type_name}
    return top_part

#-----------prep_data_type1--------------------------------------#
def prep_data_type1():
    # this section has any number of items depending on the msg type
    top_sect = prep_header_section(1)
    data_part = {msg_data_label: {
                  proto_label: proto_ver,
                  compress_type_label: compress_type1,
                  compress_rate_label: comp_rate1}}
    top_sect.update(data_part)
    json_str = json.dumps(top_sect, separators=json_seps)
    return json_str

#-----------prep_data_type3--------------------------------------#

def prep_data_type3():
    # this section has any number of items depending on the msg type
    top_sect = prep_header_section(3)

    # values from user defined library/config file
    from nulsws_msgtype3 import sub_event_ct, sub_period_int, sub_range, res_max_size, \
        address_val, msg_type3

    # labels:
    from nulsws_staticvals import request_t_label, sub_rg_label, subscrip_evnt_ct_label, \
        subscrip_period_label, req_method_label, get_bal_label, response_max_size_label, \
        address_label, get_height_label

    data_getbalance = {get_bal_label: { address_label: address_val  }}

    # data_height = {get_height_label: {}}
    #rquest_list = [data_getbalance, {get_height_label: {}}]
    rquest_list = [data_getbalance]
    req_methods_sec = {req_method_label: rquest_list }

    data_part = {request_t_label: str(msg_type3),
                 subscrip_evnt_ct_label: str(sub_event_ct),
                 subscrip_period_label: str(sub_period_int),
                 sub_rg_label: str(sub_range),
                 response_max_size_label: str(res_max_size)
                }

    data_part.update(req_methods_sec)

    msg_data_sect = {msg_data_label: data_part}
    top_sect.update(msg_data_sect)
    #jds = json.dumps(top_sect, indent=4)
    #print(jds)

    #json_str = json.dumps(top_sect)
    #print(json_str)

    jds = json.dumps(bigtest, indent=4)
    print(jds)

    json_str = json.dumps(bigtest)


    return json_str


#   "MessageData": {
#     "RequestType": "1",
#     "SubscriptionEventCounter": "0",
#     "SubscriptionPeriod": "1",
#     "SubscriptionRange": "[100]",
#     "ResponseMaxSize": "0",
#     "RequestMethods": [
#       {
#         "GetBalance": {
#           "Address": "tNULSeBaMnrs6JKrCy6TQdzYJZkMZJDng7QAsD"
#         }
#       },
#       {
#         "GetHeight": {}
#       }
#     ]
#   }
# }

def check_answer(answer) -> bool:
    jload = json.loads(answer)
    jds = json.dumps(jload, separators=(':', ','), indent=4)
    print(jds)
    msg_d_answer = jload.get(msg_data_label)
    mt = jload.get(msg_type_label)
    if mt == negotiate_conn_resp_label:
        final_int = msg_d_answer.get(negotiate_stat_label)
        if final_int == '1':
            print("Negotiate Status was 1. All is good")
            return True
        else:
            return False

def myprint(x, y=None):
    debug = True
    # if y is not None:
    #     x = x + ' ' + y
    # if debug:
    #     print(x)
