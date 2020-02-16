#!/usr/bin/python3.7
# requesttype 2 - return ack +


from src.modules.nulsws_python.calls_d import CallsD
from src.modules.nulsws_python.make_middle import MakeMiddle
from src.modules.nulsws_python.make_top import MakeTop


class RequestPrep(object):

    def prep_request(self, msg_type, msg_indx, caps_name, configini_d):
        mtop_obj = MakeTop()
        mid_obj = MakeMiddle()
        bottom_sect = CallsD().calls_dict[caps_name]

        request_type = "1"  # 1 or 2 for message requests   2=return ack+
        subs_e_c = "0"  # subscription event_counter
        subs_per = "0"  # subscription period
        subs_rg = "0"  # subscription range
        resp_max = "0"  # response max size range
        middle_sect = (request_type, subs_e_c, subs_per, subs_rg, resp_max)

        mid_plus_bottom_section = mid_obj.make_middle_m(bottom_sect, middle_sect)
        full_request = mtop_obj.make_top_m(msg_type, msg_indx, configini_d)
        full_request.update(mid_plus_bottom_section)
        return full_request
