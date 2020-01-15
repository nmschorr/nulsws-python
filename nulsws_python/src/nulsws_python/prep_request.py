#!/usr/bin/python3.7
# requesttype 2 - return ack +


from nulsws_python.src.nulsws_python.make_very_top import MakeTop
from nulsws_python.src.nulsws_python.nulsws_calls import NulsWsCalls


class PrepRequest(object):

    def prep_request(self, msg_indx, caps_name, configini_d):
        name_d = NulsWsCalls().calls_dict[caps_name]

        request_type = "1"  # 1 or 2 for message requests   2=return ack+
        subs_e_c = "0"  # subscription event_counter
        subs_per = "0"  # subscription period
        subs_rg = "0"  # subscription range
        resp_max = "0"  # response max size range

        newlist = [request_type, subs_e_c, subs_per, subs_rg, resp_max, name_d]

        msg_section_middle = self.make_request_middle(newlist)
        message_section_top = MakeTop.make_very_top(3, msg_indx, configini_d)
        message_section_top.update(msg_section_middle)
        return message_section_top
