#!/usr/bin/python3.7

from nulsws_python.src.nulsws_python.nulsws_library import NulsWsLib
from nulsws_python.src.nulsws_python.nulsws_params import *
from nulsws_python.src.nulsws_python.user_settings.nulsws_settings_one import *


# -----------prep_NEGOTIATE_data_type1--------------------------------------#


class NulsWsRequest(object):
    def __init__(self):
        self.get_times = NulsWsLib.get_times

    def prep_negotiate_request(self, msg_indx):  # return dict
        data_part = {msg_data_label: {
            proto_label: proto_ver,
            compress_type_label: compress_type_VALUE,
            compress_rate_label: compress_rate_VALUE}}
        top_sect = self.make_very_top(1, msg_indx)
        top_sect.update(data_part)
        return top_sect  # dict

    # -----------get_REQ_MIDDLE--------------------------------------#

    def make_very_top(self, msg_type: int, msg_indx):  # this section builds 5 items: #0
        # 0  "ProtocolVersion": "0.1",
        # 1 "MessageID": "1569897424187-1",  #2 "TimeZone": "-4", # 3 "Timestamp": "1569897424187"
        # 4 "MessageType": "NegotiateConnection",
        # msg_type_name = type_name_dict.__getitem__(msg_type)

        msg_type_name = type_name_dict[msg_type]
        t_stamp, tzone, m_id = self.get_times(msg_indx)
        very_top = {proto_label: proto_ver,
                    msg_id_label: m_id,
                    tmstmp_label: t_stamp,
                    tmzone_label: tzone,
                    msg_type_label: msg_type_name}
        return very_top

    # -----------get_REQ_MIDDLE--------------------------------------#

    def make_request_middle(self, mid_section_vals=None):  # return dict
        if not mid_section_vals:
            mid_section_vals = [1, ZERO, ZERO, ZERO, ZERO]  # 2 = ack+date
        [rtt, sec, sp, sr, rms, bottom_part] = [*mid_section_vals]

        req_middle = {
            msg_data_label: {
                request_type_label: rtt,
                subscrip_evnt_ct_label: sec,
                subscrip_period_label: sp,
                subscriptn_range_label: sr,
                response_max_size_label: rms,
                req_methods_label: bottom_part
            }}
        return req_middle  # dict

    # -----------prep_REQUEST_ONESIE (request) --------------------------------------#

    def prep_request(self, msg_indx, caps_name):  # requesttype 2 - return ack +
        import nulsws_python.src.nulsws_python.nulsws_calls as ndb
        callsdb = ndb.NulsWsCalls().calls_dict
        api_params_dict = {}
        api_text_api_params_dict = dict()
        itm = callsdb[caps_name]
        lowercasename = itm[0]
        api_params_dict = dict(itm[1])

        api_text_api_params_dict.update({lowercasename: api_params_dict})

        request_type = "1"  # 1 or 2 for message requests
        subs_e_c = "0"  # subscription event_counter
        subs_per = "0"  # subscription period
        subs_rg = "0"  # subscription range
        resp_max = "0"  # response max size range

        newlist = [request_type, subs_e_c, subs_per, subs_rg, resp_max, api_text_api_params_dict]

        msg_section_middle = self.make_request_middle(newlist)
        message_section_top = self.make_very_top(3, msg_indx)
        message_section_top.update(msg_section_middle)
        return message_section_top  # "'"return dict

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