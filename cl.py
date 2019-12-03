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

    @staticmethod
    def get_top(msg_type: int) -> dict:
        the_time = time()
        tz = timezone

        t_stamp = str(int(the_time * 1000))       # change float to int
        m_id = str(int(the_time * 100000))     # change float to int
        tzone = str(int(tz / 3600))   # change float to int to str
        mtype = ' '
        return {"MessageID": m_id, "Timestamp": t_stamp, "TimeZone": tzone, "MessageType": mtype}

    @staticmethod
    def make_bottom_part1(c_alg: str, cr_intstr: str):
        mt_name = "MessageType"
        mtype = "NegotiateConnection"
        md_name = "MessageData"
        c_alg_name = "CompressionAlgorithm"
        cr_name = "CompressionRate"
        plist = [ { mt_name : mtype, md_name : { c_alg_name : c_alg, cr_name : cr_intstr} } ]
        jsds = json.dumps(plist , separators=(',', ':'))
        print(jsds)
        return jsds

    def prep_data1(self, ztype, zcomp):
        all_parts = self.get_top(1)
        bottom_part = NulsWebsocket.make_bottom_part1(ztype, str(zcomp))
        all_parts.update({'MessageData': bottom_part})     # adding bottom
        all_together = ''.join(all_parts)
        self.myprint('all_parts:  ', all_together)
        return all_together

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
        zcomp = t_vars[1]

        try:
            if ztype != 'zlib':  # neg_conn
                ztype = 'zlib'
            # if zcomp != 3:  # neg_conn
            #     zcomp = 3
            the_url = nulsuserone.my_url
            connection = await websocket_connect(the_url)
            ### only continue if connection is ok
            msg_d = self.prep_data1(ztype, zcomp)
            self.myprint('sending: ', dumps(msg_d))
            resp = await connection.write_message(dumps(msg_d))
            if (resp is not None) and (len(resp) > 0):
                self.myprint("Got response: ", resp)
            self.myprint("Waiting for data...")
            answer = await connection.read_message()
            # waiting for a resp of: type: NegotiateConnectionResponse; NegotiationStatus=1; 1=good

            if answer is not None:
                print("Received answer!  :  ", answer)
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

