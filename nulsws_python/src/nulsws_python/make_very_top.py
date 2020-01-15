#!/usr/bin/python3.7


from nulsws_python.src.nulsws_python.nulsws_library import NulsWsLib
from nulsws_python.src.nulsws_python.nulsws_labels import NulsWsLabels


# 0  "ProtocolVersion": "0.1",
# 1 "MessageID": "1569897424187-1",  #2 "TimeZone": "-4", # 3 "Timestamp": "1569897424187"
# 4 "MessageType": "NegotiateConnection",
# msg_type_name = labs_type_name_d.__getitem__(msg_type)


class MakeVeryTop(object):
    def __init__(self):
        pass

    @staticmethod
    def make_very_top(msg_type: int, msg_indx: int, proto_ver):
        t_stamp, tzone, m_id = NulsWsLib.get_times(msg_indx)
        msg_type_name = NulsWsLabels.labs_type_name_d[msg_type]

        lab_d = NulsWsLabels().labs_req_field_d

        very_top_d = {lab_d.get("proto_label"): proto_ver,
                      lab_d.get("msg_id_label"): m_id,
                      lab_d.get("tmstmp_label"): t_stamp,
                      lab_d.get("tmzone_label"): tzone,
                      lab_d.get("msg_type_label"): msg_type_name
                      }
        return very_top_d
