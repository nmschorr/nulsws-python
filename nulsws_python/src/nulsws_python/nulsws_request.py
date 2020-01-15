#!/usr/bin/python3.7

from nulsws_python.src.nulsws_python.nulsws_labels import NulsWsLabels
from nulsws_python.src.nulsws_python.make_very_top import MakeTop


class NulsWsRequest(object):

    def __init__(self):
        self.labs_param = NulsWsLabels().labs_req_field_d
        self.labs_type_name_d = NulsWsLabels().labs_type_name_d

    def prep_negotiate_request(self, msg_indx, cfid):  # return dict
        
        nd = self.labs_param
        data_part = {nd.get("msg_data_label"): {
            nd.get("proto_label"): cfid.get("proto_ver"),
            nd.get("compress_type_label"): cfid.get("compress_type_value"),
            nd.get("compress_rate_label"): cfid.get("compress_rate_value")}}

        top_sect = MakeTop.make_very_top(1, msg_indx, cfid)
        top_sect.update(data_part)
        return top_sect  # dict

    def make_request_middle(self, mid_section_vals=None):  # return dict
        nnn = self.labs_param
        zero = nnn.get("ZERO")
        if not mid_section_vals:
            mid_section_vals = [1, zero, zero, zero, zero]  # 2 = ack+date
        [rtt, sec, sp, sr, rms, bottom_part] = [*mid_section_vals]

        def f(x):
            return n.get(x)

        # need labs_req_field_d
        n = NulsWsLabels.labs_req_field_d

        z = f("msg_data_label")
        req_middle = {
            n.get("msg_data_label"): {
                n.get("request_type_label"): rtt,
                n.get("subscrip_evnt_ct_label"): sec,
                n.get("subscrip_period_label"): sp,
                n.get("subscriptn_range_label"): sr,
                n.get("response_max_size_label"): rms,
                n.get("req_methods_label"): bottom_part
            }}
        return req_middle  # dict




# ----------- end library file --------------------------------------#


















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