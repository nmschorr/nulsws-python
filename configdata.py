from typing import Dict


class ConfigData(object):

    def __init__(self):
        pass

    def get_fnames(self) -> Dict:
        f_dict: Dict = {0: 'dataSimple.ncf', 1: 'dataNegConn1.ncf', 2: 'dataNegConnResp2.ncf',
                             3: 'dataRequest3.ncf', 4: 'dataUnsub4.ncf', 5: 'dataResp5.ncf',
                             6: 'dataAck6.ncf', 7: 'dataRegCompM7.ncf', 8: 'dataUnregCompM8.ncf'}
        return f_dict

    def get_mdict(self) -> Dict:
        m_dict: Dict = {0: 'Simple', 1: 'NegotiateConnection',
                             2: 'NegotiateConnectionResponse',
                             3: 'Request', 4: 'Unsubscribe', 5: 'Response', 6: 'Ack',
                             7: 'RegisterCompoundMethod', 8: 'UnregisterCompoundMethod'}
        return m_dict
