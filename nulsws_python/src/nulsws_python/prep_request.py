#!/usr/bin/python3.7
# requesttype 2 - return ack +


from nulsws_python.src.nulsws_python.make_very_top import MakeTop
from nulsws_python.src.nulsws_python.nulsws_calls import NulsWsCalls


class PrepRequest(object):

    def prep_request(self, msg_indx, caps_name, configini_d):
        bottom_callsd = NulsWsCalls().calls_dict[caps_name]

        request_type = "1"  # 1 or 2 for message requests   2=return ack+
        subs_e_c = "0"  # subscription event_counter
        subs_per = "0"  # subscription period
        subs_rg = "0"  # subscription range
        resp_max = "0"  # response max size range

        mid_list = [request_type, subs_e_c, subs_per, subs_rg, resp_max]

        msg_section_middle = self.make_request_middle(bottom_callsd, mid_list)
        lg_top = MakeTop.make_top(msg_indx, configini_d)

        lg_top.update(msg_section_middle)
        return lg_top
