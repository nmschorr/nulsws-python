#!usr/bin/python3.7

# Messages have a common structure composed of six fields:
# •  ProtocolVersion: version the service to understand,2 numbers, major/minor
# •  MessageID: identifies a request.
# •  Timestamp:  Number  of  seconds  since  epoch January 1,1970
# •  TimeZone: The time zone where the request was originated
# •  MessageType: The message type, these are specified on section 3
# •  MessageData: A Json object with the message payload

# the first object that should be sent - only if the negotiation is ok service may process
# further requests -otherwise a NegotiateConnectionResponse object should be received with
# Status set to 0 (Failure) and disconnect immediately.

# "MessageType": "NegotiateConnection",
# "MessageData": {
#     "CompressionAlgorithm": "zlib",
#     "CompressionRate": "3"

## -- Enter your custom settings data via the library file nulsuserone.py
# Note: Don't use typing.Dict - it can cause json problems when converted
# This file right now is the client only.
# author:  Nancy M Schorr, for Nuls
# December 2, 2019

from time import time, timezone
import json


# {
#   "MessageData":{
#     "CompressionAlgorithm":"zlib",
#     "CompressionRate":"0",
#     "ProtocolVersion":"0.1"
#   },
#   "MessageID":"1569897424187-1",
#   "MessageType":"NegotiateConnection",
#   "TimeZone":"-4",
#   "Timestamp":"1569897424187"
# }
#

## must keep this list updated
__all__ = ["prep_data1", "myprint", "prep_async", "check_answer"]

def prep_data1(c_alg, cr_intstr):
    # return {"Protocol Version": "0.1" "MessageID": m_id, "Timestamp": t_stamp, "TimeZone":
    # tzone,  "MessageType": mtype}

    mid_name = "MessageID"
    ts_name = "Timestamp"
    tz_name = "TimeZone"
    msg_type_label = "MessageType"
    msg_type = "NegotiateConnection"
    msg_data_label = "MessageData"
    ca_label = "CompressionAlgorithm"
    cr_label = "CompressionRate"
    proto_label = "ProtocolVersion"
    the_time = time()
    tz = timezone

    t_stamp = str(int(the_time * 1000))       # change float to int
    m_id = str(int(the_time * 100000))     # change float to int
    tzone = str(int(tz / 3600))   # change float to int to str
    from nulsws_msgtype1 import proto_ver
    jlist = { mid_name: m_id,
              ts_name: t_stamp,
              tz_name: tzone,
              msg_type_label: msg_type,
              msg_data_label: {proto_label: proto_ver, ca_label: c_alg, cr_label: cr_intstr}
             }
    json_str = json.dumps(jlist, separators=(',', ':'))
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
    msg_data_lab = "MessageData"
    msg_negotiate_lab = 'NegotiationStatus'
    mtyp_lab = "MessageType"
    mt_good_answr = "NegotiateConnectionResponse"
    jload = json.loads(answer)
    jds = json.dumps(jload, separators=(':', ','), indent=4)
    print(jds)

    msg_d_answer = jload.get(msg_data_lab)
    mt = jload.get(mtyp_lab)

    if mt == mt_good_answr:
        final_int = msg_d_answer.get(msg_negotiate_lab)
        if final_int == '1':
            print("Negotiate Status was 1. All is good")
            return True
        else:
            return False
