#!usr/bin/python3.7

# All messages will have a common base structure composed of six fields:
# •  ProtocolVersion: Represents the protocol version that the caller needs the
# service to understand, it is composed by two numbers, major and minor and
# follows semantic rules, which means that if the major number is different the
# connection is refused, if the minor number varies then a successful
# connection can be established.
# •  MessageID: This is a string that identifies a request. Its length should not
# surpass 256 characters.
# •  Timestamp:  Number  of  seconds  since  epoch  (January  1,  1970
# at 00:00:00 GMT)
# •  TimeZone: The time zone where the request was originated and it is
# represented as a number between -12 and 12
# •  MessageType: The message type, these are specified on section 3]
# •  MessageData: A Json object that holds the payload of the message.

# Note: be careful with typing.Dict - it can cause json problems when converted

# the first object that should be sent - only if the negotiation is ok service may process
# further requests -otherwise a NegotiateConnectionResponse object should be received with
# Status set to 0 (Failure) and disconnect immediately.
# "MessageType": "NegotiateConnection",
# "MessageData": {
#     "CompressionAlgorithm": "zlib",
#     "CompressionRate": "3"

## -- Enter your custom settings data via the library file nulsuserone.py


from tornado.websocket import websocket_connect, WebSocketClosedError
from json import load, dumps
from asyncio import run
from time import time, timezone
import nulsuserone
import json

class NulsWebsocket(object):
    def __init__(self):
        self.ws_url = nulsuserone.my_url
        self.myprint("the url:  ", self.ws_url)

    def prep_data1(self, c_alg, cr_intstr):
        the_time = time()
        tz = timezone
        mid_name = "MessageID"
        ts_name = "Timestamp"
        tz_name = "TimeZone"
        msg_type_label = "MessageType"
        msg_type = "NegotiateConnection"
        msg_data_label = "MessageData"
        ca_label = "CompressionAlgorithm"
        cr_label = "CompressionRate"


        t_stamp = str(int(the_time * 1000))       # change float to int
        m_id = str(int(the_time * 100000))     # change float to int
        tzone = str(int(tz / 3600))   # change float to int to str
        jlist = { mid_name: m_id,
                  ts_name: t_stamp,
                  tz_name: tzone,
                  msg_type_label: msg_type,
                  msg_data_label: {ca_label : c_alg, cr_label : cr_intstr}
                 }
        return jlist
                #return {"MessageID": m_id, "Timestamp": t_stamp, "TimeZone": tzone, "MessageType": mtype}

    def myprint(self, x, y=None):
        debug = True
        if y is not None:
            x = x + ' ' + y
        if debug == True:
            print(x)

    # def one_lib(self, comp_name = 'zlib', comp_int = 3):
    #     self.send_negotiate_conn()

    async def connect_serve1(self, t_vars):
        ztype = t_vars[0]
        zcomp = str(t_vars[1])

        try:
            if ztype != 'zlib':  # neg_conn
                ztype = 'zlib'
            connection = await websocket_connect(nulsuserone.my_url )
                ### only continue if connection is ok
            js_list = self.prep_data1(ztype, zcomp)
            json_str = json.dumps(js_list, separators=(',', ':'))

            self.myprint('sending: ', json_str)
            resp = await connection.write_message(json_str)
            if (resp is not None) and (len(resp) > 0):
                self.myprint("Got response: ", resp)
            self.myprint("Waiting for data...")
            answer = await connection.read_message()
            print("Received answer from blockchain")
            j = json.loads(answer)

            print(j)
            mtyp_lab = "MessageType"
            mt = j.get(mtyp_lab)
            mt_good_answr = "NegotiateConnectionResponse"
            if mt == mt_good_answr:
                msg_data_lab = "MessageData"
                msg_d_answer = j.get(msg_data_lab)
                msg_negotiate_lab = 'NegotiationStatus'

                final_int = msg_d_answer.get(msg_negotiate_lab)
                print("all is good")
                return final_int
        except WebSocketClosedError as e:
            print(e)

    async def ws_runner(self, mtype, varss):
        if mtype == 1:
            await self.connect_serve1(varss)                       # in same dir as

    def main(self):
        m_type = nulsuserone.mtype
        comp_t = nulsuserone.comp_type
        comp_int = nulsuserone.comp_int
        vars_list = [comp_t, comp_int]
        run(self.ws_runner(m_type, vars_list), debug=True)   # starts event loop


n = NulsWebsocket()
n.main()
## -- enter user data via the library file nulsuserone.py

