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
import random
from time import time, timezone
from nulsws_msgtype1 import proto_ver
from nulsws_msgtype1 import compress_type1, comp_rate1

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
json_seps = (',', ':')
json_d = None

# message type - data
m_dict: dict = {0: 'None', 1: 'NegotiateConnection',
                2: 'NegotiateConnectionResponse',
                3: 'Request', 4: 'Unsubscribe', 5: 'Response', 6: 'Ack',
                7: 'RegisterCompoundMethod', 8: 'UnregisterCompoundMethod'}

## must keep this list updated

def do_math():
    rand = random.random()
    ws_rand = round(rand * 100000)
    rand_ending = str(int(ws_rand))

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
    x = m_dict.__getitem__(msg_type)
    t_stamp, tzone, m_id= do_math()
    top_part = { msg_id_label: m_id,
              tmstmp_label : t_stamp,
              tmzone_label: tzone,
              msg_type_label: x}
    return top_part

#-------------------------------------------------#
def prep_data_type1():
    # this section has any number of items depending on the msg type
    top_sect = prep_header_section(1)
    compress_rate = "0"
    data_part = {msg_data_label: {proto_label: proto_ver,
                                  compress_type_label: compress_type1,
                                  compress_rate_label: comp_rate1}}
    top_sect.update(data_part)
    json_str = json.dumps(top_sect, separators=json_seps)
    return json_str

#-------------------------------------------------#


def prep_data_type3():
    # this section has any number of items depending on the msg type
    top_sect = prep_header_section(3)
    request_int = 1
    sub_event_ct = 0
    sub_period_int = 1
    sub_range = "[100]"
    res_max_size = 0

    # labels:
    request_t_label = "RequestType"
    subscription_eventct_label = "SubscriptionEventCounter"
    subscription_period_label= "SubscriptionPeriod"
    sub_rg_label = "SubscriptionRange"
    req_method_label = "RequestMethods"
    get_bal_label = "GetBalance"
    get_addy_label = "Address"
    get_height_label = "GetHeight"
    response_max_size_label = "ResponseMaxSize"
    address_label = "Address"
    get_height_label =  "GetHeight"
    data_height = {get_height_label: {}}


    address_val = "NULSd6Hge7xHDnvsSpnzbR2gWHd31zJ1How11"  ## from user file

    data_getbalance = {  get_bal_label : {
                address_label : address_val
    } }


    rquest_list = [data_getbalance, data_height]
    req_methods_sec =  { req_method_label: rquest_list }

    data_part = { request_t_label: str(request_int),
                     subscription_eventct_label  : str(sub_event_ct),
                     subscription_period_label: str(sub_period_int),
                     sub_rg_label: sub_range,
                      response_max_size_label : str(res_max_size)
                      }



    data_part.update(req_methods_sec)

    msg_data_sect = { msg_data_label : data_part }


    top_sect.update(msg_data_sect)
    jds = json.dumps(top_sect, indent=4)
    print(jds)
    #exit()

    json_str = json.dumps(top_sect)
    print(json_str)
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
    if y is not None:
        x = x + ' ' + y
    if debug:
        print(x)
