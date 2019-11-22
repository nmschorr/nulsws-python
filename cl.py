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

# This file reads the json file as in dataRequest or dataNegotiateConnection
# adds info to it and sends it to the server.
# Note: be careful with typing.Dict - it can cause json problems when converted


from tornado.websocket import websocket_connect, WebSocketClosedError
from typing import Dict
from json import load, dumps
from asyncio import run
from random import choices
from string import ascii_uppercase, digits
from time import time
from configdata import ConfigData as cd


class NulsWebsocket(object):
    def __init__(self):
        method: str = "ws://"
        host: str = "127.0.0.1"
        wport = "9006"
        port = "7771"
        dport = "18003"
        self.my_url: str = ''.join([method, host, ":", port])
        print("the url:  ", self.my_url)

    def get_top(self, msg_type: int) -> dict:
        ts = int(time())
        m_id: str = ''.join(choices(ascii_uppercase + digits, k=15))
        mtype = cd().get_mdict().get(msg_type)
        return {"MessageID": m_id, "Timestamp": ts, "TimeZone": -8, "MessageType": mtype}

    def read_data_file(self, mtyp: int):
        fname: str = cd().get_fnames().get(mtyp)
        print("filename is: ", fname)
        with open(fname, 'r') as f:
            mdd = load(f).get("MessageData")
        mainpart = self.get_top(mtyp)
        mainpart.update({"MessageData": mdd})     # adding bottom part
        return mainpart

    async def connect_serve(self, the_type) -> None:
        try:
            answer = None
            connection = await websocket_connect(self.my_url)
            msg_d = self.read_data_file(the_type)
            print("sending: ", dumps(msg_d))
            resp = await connection.write_message(dumps(msg_d))
            if resp:
                print("Got response: ", resp)
            print("Waiting for data...")
            answer = await connection.read_message()
            if answer is not None:
                print("Received answer!  :  ", answer)
        except WebSocketClosedError as e:
            print(e)

    async def ws_runner(self, mtype):
        await self.connect_serve(mtype)                       # in same dir as program

    def main(self):
        mtype = 1
        run(self.ws_runner(mtype), debug=True)   # starts event loop


if __name__ == "__main__":
    NulsWebsocket().main()
