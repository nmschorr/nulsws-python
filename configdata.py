from typing import Dict


class ConfigData(object):

    def __init__(self):
        pass

    @staticmethod
    def get_fnames() -> Dict:
        f_dict: Dict = {0: 'dataSimple.json', 1: 'dataNegConn1.json', 2: 'dataNegConnResp2.json',
                        3: 'dataRequest3.json', 4: 'dataUnsub4.json', 5: 'dataResp5.json',
                        6: 'dataAck6.json', 7: 'dataRegCompM7.json', 8: 'dataUnregCompM8.json'}
        return f_dict

    @staticmethod
    def get_mdict() -> Dict:
        m_dict: Dict = {0: 'Simple', 1: 'NegotiateConnection',
                        2: 'NegotiateConnectionResponse',
                        3: 'Request', 4: 'Unsubscribe', 5: 'Response', 6: 'Ack',
                        7: 'RegisterCompoundMethod', 8: 'UnregisterCompoundMethod'}
        return m_dict
