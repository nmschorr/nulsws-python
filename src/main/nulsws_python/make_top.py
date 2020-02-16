#!/usr/bin/python3.7

from nulsws_python.src.nulsws_python.labels import Labels
from nulsws_python.src.nulsws_python.make_very_top import MakeVeryTop


class MakeTop(object):

    def make_top_m(self, msg_typ, msg_indx, conf_inid):  # must pass in user config.ini dict
        proto_ver = conf_inid.get("proto_ver")

        nd = Labels().labs_field_d
        data_part = {nd.get("msg_data_label"): {
            nd.get("proto_label"): proto_ver,
            nd.get("compress_type_label"): conf_inid.get("compress_type_value"),
            nd.get("compress_rate_label"): conf_inid.get("compress_rate_value")}}

        large_top = MakeVeryTop.make_very_top_m(msg_typ, msg_indx, proto_ver)
        large_top.update(data_part)
        return large_top  # dict

















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
#         "RequestMethods": {
#           {
#             "GetBalance": {
#               "Address": "tNULSeBaMnrs6JKrCy6TQdzYJZkMZJDng7QAsD"
#             }
#           },
#           {
#             "GetHeight": {}
#           }
#         }
#        }
#     }
# “RequestType”: “1”,
# “SubscriptionEventCounter”: “3”,
# “SubscriptionPeriod”: “0”,
# “SubscriptionRange”: “0”,
# “ResponseMaxSize: “0”,