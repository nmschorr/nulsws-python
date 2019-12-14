#!usr/bin/python3.7


"""
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
  "ProtocolVersion":"0.1",
  "MessageID":"1569897424187-1",
  "MessageType":"NegotiateConnection",
  "TimeZone":"-4",
  "Timestamp":"1569897424187",
  "MessageData":{
    "CompressionAlgorithm":"zlib",
    "CompressionRate":"0",
    "ProtocolVersion":"0.1"
  },
}

Compression Rate can be values 0 through 9.
Compression Algorithm is normally "zlib"

 -- Enter your custom settings data via the library file 'nulsws_msgtype1.py'.

Note: Don't use typing.Dict - it can cause json problems when converted.

This file right now provides support for the the client only.

"""

import json
from time import time, timezone
from json import dumps as json_dumps
from Libraries.Constants.nulsws_CONSTANTS_otherlabels import msg_data_label, type_name_dict, tmzone_label, msg_id_label, \
    msg_type_label, negotiate_stat_label, negotiate_conn_resp_label, proto_label, tmstmp_label
from UserSettings.nulsws_USER_static_settings import proto_ver
import inspect


def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]
# -----------get_times--------------------------------------#

def get_times(msg_index=1):
    t_stamp = int(time() * 100000)  # change float to int
    tzone = int(timezone / 3600)  # change float to int to str
    m_id = str(t_stamp) + "-" + str(msg_index)
    return t_stamp, tzone, m_id


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


# -----------check_json_answer--------------------------------------#

def check_json_answer(answer) -> bool:
    jload = json.loads(answer)
    json_prt(jload, "check answer jds value= ")
    msg_d_answer = jload.get(msg_data_label)
    mt = jload.get(msg_type_label)
    if mt == negotiate_conn_resp_label:
        final_int = msg_d_answer.get(negotiate_stat_label)
        if final_int == '1':
            print("Negotiate Status was 1. All is good")
            return True
        else:
            return False


# -----------myprint--------------------------------------#

def myprint(x, y=None, debug=True):
    if debug:
        print(x) if not y else print(str(x) + ' ' + str(y))


# -----------json_prt--------------------------------------#

def json_prt(json_str, str_msg, debug=True):
    if not isinstance(json_str, dict):
        json_str = json.loads(json_str)
    if debug:
        if str_msg:
            aname = ''.join(str_msg)
            # print(aname)
            print(aname + str(json_dumps(json_str, indent=3)))
        else:
            myprint("nothing returned")





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
