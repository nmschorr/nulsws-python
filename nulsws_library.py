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
from time import time, timezone
from nulsws_msgtype1 import proto_ver

msg_id_label = "MessageID"
tmstmp_label = "Timestamp"
tmzone_label = "TimeZone"
msg_type_label = "MessageType"
negotiate_conn_label = "NegotiateConnection"
msg_data_label = "MessageData"
ca_label = "CompressionAlgorithm"
cr_label = "CompressionRate"
proto_label = "ProtocolVersion"
msg_data_label = "MessageData"
negotiate_stat_label = 'NegotiationStatus'
negotiate_conn_resp = "NegotiateConnectionResponse"
tz = timezone
json_seps = (',', ':')


## must keep this list updated
__all__ = ["prep_data1", "myprint", "prep_async", "check_answer"]

def prep_data1(c_alg, cr_intstr):
    the_time = time()
    t_stamp = str(int(the_time * 1000))       # change float to int
    m_id = str(int(the_time * 100000))     # change float to int
    tzone = str(int(tz / 3600))   # change float to int to str
    jlist = { msg_id_label: m_id,
              tmstmp_label : t_stamp,
              tmzone_label: tzone,
              msg_type_label: negotiate_conn_label,
              msg_data_label: {proto_label: proto_ver, ca_label: c_alg, cr_label: cr_intstr}
             }
    json_str = json.dumps(jlist, separators=json_seps)



    return json_str

def myprint( x, y=None):
    debug = True
    if y is not None:
        x = x + ' ' + y
    if debug:
        print(x)

def prep_async( t_vars):
    ztype = t_vars[0]
    zcomp = t_vars[1]
    good_msg = "all is good, was 1, ok to continue"

    if ztype != 'zlib':  # neg_conn
        ztype = 'zlib'
    return ztype, zcomp, good_msg

def check_answer(answer) -> bool:

    jload = json.loads(answer)
    jds = json.dumps(jload, separators=(':', ','), indent=4)
    print(jds)

    msg_d_answer = jload.get(msg_data_label)
    mt = jload.get(msg_type_label)

    if mt == negotiate_conn_resp:
        final_int = msg_d_answer.get(negotiate_stat_label)
        if final_int == '1':
            print("Negotiate Status was 1. All is good")
            return True
        else:
            return False
