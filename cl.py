
##### python 3.7

# class WebSocketClientConnection(simple_httpclient._HTTPConnection):
"""WebSocket client connection.

This class should not be instantiated directly; use the
`websocket_connect` function instead.
"""
# Override `on_message` to handle incoming messages, and use
# `write_message` to send messages to the client.

# NegotiateConnection,
# NegotiateConnectionResponse,  Request,  Unsubscribe,  Response,  Ack,
# RegisterCompoundMethod and UnregisterCompoundMethod.

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

# This file reads the datafile as in dataRequest or dataNegotiateConnection
# converts it into JSON format and sends it to the server.


from tornado.websocket import websocket_connect, WebSocketClosedError
from tornado.websocket import WebSocketHandler
#from typing import Dict, List, AnyStr  ## using Dict messes up json so don't use! but it will
# create
                             ## and ordered Dict

from typing import Dict
import json
import json.encoder
import asyncio
from datetime import datetime
import string, random
from configdata import ConfigData

class NulsWebsocket(WebSocketHandler):

    def __init__(self):
        method: str = "ws://"
        host: str = "127.0.0.1"
        port = "9006"
        sport = "7771"
        dport = "18003"
        self.my_url: str = ''.join([method, host, ":", port])
        print("the url:  ", self.my_url)
        self.connection = None
        self.tstamp: str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        self.m_id: str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
        cd = ConfigData()
        self.fndict: Dict = cd.get_fnames()
        self.mdict: Dict = cd.get_mdict()

    def get_top(self, msg_type: int) -> dict:
        mtype = self.mdict.get(msg_type)
        return {"MessageID": self.m_id, "Timestamp": self.tstamp, "TimeZone": -8,"MessageType":
            mtype}

    def read_data_file(self, mtyp: int):
        fname: str = self.fndict.get(mtyp)
        print("filename is: ", fname)
        with open(fname, 'r') as f:
            mdd = json.load(f).get("MessageData")
        mainpart = self.get_top(mtyp)
        mainpart.update({"MessageData": mdd})  ## add bottom part
        return mainpart

    async def connect_serve(self, the_type)-> None :
        try:
            self.connection = await websocket_connect(self.my_url)
            msg_d = self.read_data_file(the_type)
            print("sending: ", json.dumps(msg_d))
            resp = await self.connection.write_message(json.dumps(msg_d))
            print("Waiting for response...")
            answer = await self.connection.read_message()
            print("Received answer!  :  ", answer)
        except WebSocketClosedError as e:
            print(e)

    async def ws_runner(self):
        mtype = 8
        await self.connect_serve(mtype)                       # in same dir as program

    def main(self):
        asyncio.run(self.ws_runner(), debug=True)   # starts event loop


if __name__ == "__main__":
    w = NulsWebsocket()
    w.main()

    # origtop_info = {"ProtocolVersion": '1.0', "MessageID": m_id, "Timestamp": ts, "TimeZone":
    #     -8, "MessageType": mtype}

    # def mypretty(self, jsonfile):
    #     print(json.dumps(jsonfile, indent=4))
    # async def first_connect(self, mtype)-> None :
    #     try:
    #         self.connection = await websocket_connect(self.my_url)
    #         await self.connection.write_message(u"helloThere!")
    #         answer = await self.connection.read_message()
    #         print("Received answer!  :  ", answer)
    #     except WebSocketClosedError as e:
    #         print(e)



