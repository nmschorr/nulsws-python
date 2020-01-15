#!/usr/bin/python3.7

from nulsws_python.src.nulsws_python.nulsws_library import NulsWsLib
from nulsws_python.src.nulsws_python.nulsws_labels import NulsWsLabels
from nulsws_python.src.nulsws_python.make_very_top import MakeTop


# from nulsws_python.src.nulsws_python.user_settings.nulsws_user_set import NulsWsUserSet
# just pass the dict1 into this file via methods

class NulsWsRequest(object):

    # -----------prep_NEGOTIATE_data_type1--------------------------------------#

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

    # -----------get_REQ_MIDDLE--------------------------------------#



    # -----------get_REQ_MIDDLE--------------------------------------#

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
        rf = NulsWsLabels.labs_req_field_d

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

    # -----------prep_REQUEST_ONESIE (request) --------------------------------------#

    def prep_request(self, msg_indx, caps_name, dd):  # requesttype 2 - return ack +
        import nulsws_python.src.nulsws_python.nulsws_calls as ndb
        callsdb = ndb.NulsWsCalls().calls_dict
        api_text_api_params_dict = dict()
        itm_d: dict = callsdb[caps_name]

        api_text_api_params_dict.update(itm_d)

        request_type = "1"  # 1 or 2 for message requests
        subs_e_c = "0"  # subscription event_counter
        subs_per = "0"  # subscription period
        subs_rg = "0"  # subscription range
        resp_max = "0"  # response max size range

        newlist = [request_type, subs_e_c, subs_per, subs_rg, resp_max, api_text_api_params_dict]

        msg_section_middle = self.make_request_middle(newlist)
        message_section_top = MakeTop.make_very_top(3, msg_indx, dd)
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