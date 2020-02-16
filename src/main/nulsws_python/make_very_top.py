#!/usr/bin/python3.7


from nulsws_python.src.nulsws_python.routines import Routines
from nulsws_python.src.nulsws_python.labels import Labels

# 0  "ProtocolVersion": "0.1",
# 1 "MessageID": "1569897424187-1",  #2 "TimeZone": "-4",
# 3 "Timestamp": "1569897424187"
# 4 "MessageType": "NegotiateConnection",
# msg_type_name = labs_type_d.__getitem__(msg_type)


class MakeVeryTop(object):

    @staticmethod
    def make_very_top_m(msg_type: int, msg_indx: int, proto_ver: str):
        t_stamp, tzone, m_id = Routines.get_times(msg_indx)
        msg_type_name = Labels.labs_type_d[msg_type]

        lab_d = Labels().labs_field_d

        very_top_d = {lab_d.get("proto_label"): proto_ver,
                      lab_d.get("msg_id_label"): m_id,
                      lab_d.get("tmstmp_label"): t_stamp,
                      lab_d.get("tmzone_label"): tzone,
                      lab_d.get("msg_type_label"): msg_type_name
                      }
        return very_top_d
