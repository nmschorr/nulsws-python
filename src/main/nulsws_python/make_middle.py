#!/usr/bin/python3.7

from nulsws_python.src.nulsws_python.labels import Labels


class MakeMiddle(object):

    def make_middle_m(self, bottom_d, mid_section_vals=(1, 0, 0, 0, 0)):  # return dict
        n = Labels.labs_field_d

        [rtyp, sevt, sper, srng, rmax] = [*mid_section_vals]

        req_middle_d = {
            n.get("msg_data_label"): {
                n.get("request_type_label"): rtyp,
                n.get("subscrip_evnt_ct_label"): sevt,
                n.get("subscrip_period_label"): sper,
                n.get("subscriptn_range_label"): srng,
                n.get("response_max_size_label"): rmax,
                n.get("req_methods_label"): bottom_d
            }}
        return req_middle_d
