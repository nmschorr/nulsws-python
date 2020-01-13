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

 -- Enter your custom user_settings data via the library file 'nulsws_msgtype1.py'.

Note: Don't use typing.Dict - it can cause json problems when converted.

This file right now provides support for the the client only.

"""

import json
from json import dumps as json_dumps
from time import time, timezone

from nulsws_python.src.nulsws_python.nulsws_other_labels import msg_data_label, msg_type_label, \
    negotiate_stat_label, negotiate_conn_resp_label


class NulsWsLib(object):

    # -----------get_times--------------------------------------#

    @classmethod
    def get_times(cls, msg_index: int):
        t_stamp = int(time() * 100000)  # change float to int
        tzone = int(timezone / 3600)  # change float to int to str
        m_id = str(t_stamp) + "-" + str(msg_index)
        t_stamp = str(t_stamp)
        return t_stamp, str(tzone), m_id

    # -----------check_json_answer--------------------------------------#

    def check_json_answer(self, answer) -> bool:
        jload = json.loads(answer)
        self.json_prt(jload, "check answer jds value= ")
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

    @classmethod
    def myprint(cls, x, y=None, debug=True):
        if debug:
            print(x) if not y else print(str(x) + ' ' + str(y))

    # -----------json_prt--------------------------------------#
    @classmethod
    def json_prt(cls, json_str, str_msg="", debug=True):
        if not isinstance(json_str, dict):
            json_str = json.loads(json_str)
        if debug:
            if str_msg:
                aname = ''.join(str_msg)
                print(aname + str(json_dumps(json_str, indent=3)))
            else:
                NulsWsLib.myprint(0, "nothing returned")

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
