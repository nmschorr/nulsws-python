
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
import configparser
from datetime import datetime
import string, random

class NulsWebsocket(WebSocketHandler):

    def myswitcher(self, the_type, mytup):
        switcher = {


    if mtyp == 2:  self.read_type2(mytup)

    if mtyp == 3:  self.read_type3(mytup)

    if mtyp == 4: self.read_type4(mytup)

    if mtyp == 5:  self.read_type5(mytup)

    if mtyp == 6: self.read_type6(mytup)

    if mtyp == 7: self.read_type7(mytup)

    if mtyp == 8: self.read_type8(mytup)


    def __init__(self):
        method: str = "ws://"
        host: str = "127.0.0.1"
        port = "9006"
        port = "7771"
        dport = "18003"
        self.my_url: str = ''.join([method, host, ":", port])
        print("the url:  ", self.my_url)
        self.connection = None
        self.timestamp: str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        self.mdict: Dict = self.get_mdict()
        self.filenames: Dict = self.get_fnames()

    def get_fnames(self) -> Dict:
        f_dict: Dict = {0:'dataSimple.ncf', 1: 'dataNegConn1.ncf', 2: 'dataNegConnResp2.ncf',
               3: 'dataRequest3.ncf', 4: 'dataUnsub4.ncf', 5: 'dataResp5.ncf',
               6: 'dataAck6.ncf', 7: 'dataRegCompM7.ncf', 8: 'dataUnregCompM8.ncf'}
        return f_dict

    def get_mdict(self) -> Dict:
        m_dict: Dict = {0:'Simple', 1: 'NegotiateConnection', 2: 'NegotiateConnectionResponse',
                3: 'Request', 4:  'Unsubscribe', 5: 'Response', 6: 'Ack',
                7: 'RegisterCompoundMethod', 8: 'UnregisterCompoundMethod'}
        return m_dict

    async def first_connect(self, mtype)-> None :
        try:
            self.connection = await websocket_connect(self.my_url)
            await self.connection.write_message(u"helloThere!")
            answer = await self.connection.read_message()
            print("Received answer!  :  ", answer)
        except WebSocketClosedError as e:
            print(e)


    async def real_connect(self, the_type)-> None :
        try:
            self.connection = await websocket_connect(self.my_url)
            msg_d = self.read_data_file(the_type)

            jsn = json.dumps(msg_d)
            #jsn = json.JSONEncoder().encode(json.dumps(msg_d))

            resp = await self.connection.write_message(json.dumps(msg_d))
            print("resp:  ", resp)
            answer = await self.connection.read_message()
            print("Received answer!  :  ", answer)
        except WebSocketClosedError as e:
            print(e)


    def get_top_info(self, msg_type: int) -> dict:
        # (5 known properties: "TimeZone", "MessageID", "Timestamp", "MessageType", "MessageData"])

        m_id: str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
        mtype = self.mdict.get(msg_type)
        ts = self.timestamp
        # origtop_info = {"ProtocolVersion": '1.0', "MessageID": m_id, "Timestamp": ts, "TimeZone":
        #     -8, "MessageType": mtype}
        top_info = {"MessageID": m_id, "Timestamp": ts, "TimeZone": -8,"MessageType": mtype}
        return top_info

    def read_type0(self, scts, mdt):   ## this function only for testing
        subhead = dict()
        header: dict = scts.get('top')  ## ordered dict
        header.update({'MessageData': mdt})
        subhead.update(header)
        return subhead

    def read_type2(self, scts, mdt):   ## this function only for testing
        subhead = self.get_top_info(2)
        header: dict = scts.get('top')  ## ordered dict
        header.update({'MessageData': mdt})
        subhead.update(header)
        return subhead

    def read_type3(self, scts, mdta):  ## this function only for testing
        subhead = self.get_top_info(3)
        bal: dict = scts.get('GetBalance')
        reqmeths: dict = scts.get('RequestMethods')
        reqmeths.update({'GetBalance': bal})  # bottom
        mdta.update({'RequestMethods': reqmeths})  # next up
        subhead.update({'MessageData': mdta})
        return subhead

    def read_type4(self, scts, mdta):  ## this function only for testing
        subhead = self.get_top_info(4)
        unsubmeths: dict = scts.get('UnsubscribeMethods')
        mdta.update({'UnsubscribeMethods': unsubmeths})  # next up
        subhead.update({'MessageData': mdta})
        return subhead


    def read_data_file(self, mtyp: int) ->dict:
        filename: str = self.filenames.get(mtyp)
        custom_parser = configparser.RawConfigParser()   ## to preserve case
        custom_parser.optionxform = lambda option: option
        custom_parser.read(filename)
        sects = custom_parser._sections
        mdata: dict = sects.get('MessageData')
        mytup = (sects, mdata)


        if mtyp == 0:
            subhead = self.read_type0(mytup)

        if mtyp == 1:
            subhead = self.get_top_info(mtyp)  ## simple one needs no sub routine
            subhead.update({'MessageData': mdata})

        if mtyp == 2:
            subhead = self.read_type2(mytup)

        if mtyp == 3:
            subhead = self.read_type3(mytup)

        if mtyp == 4:
            subhead = self.read_type4(mytup)

        if mtyp == 5:
            subhead = self.read_type5(mytup)

        if mtyp == 6:
            subhead = self.read_type6(mytup)

        if mtyp == 7:
            subhead = self.read_type7(mytup)

        if mtyp == 8:
            subhead = self.read_type8(mytup)

        print(subhead)
        return subhead

    def mypretty(self, jsonfile):
        print(json.dumps(jsonfile, indent=4))


    async def mytest(self):
        await print()

    async def ws_runner(self):
        mtype = 3
        await self.real_connect(mtype)                       # in same dir as program

    def main(self):
        asyncio.run(self.ws_runner(), debug=True)   # starts event loop


if __name__ == "__main__":
    w = NulsWebsocket()
    w.main()








    # async def rw_msg(self):
    #     try:
    #         await self.connection.write_message(self.data_body)
    #         fun = await self.connection.read_message()
    #         print("message received from server: ", fun)
    #     except WebSocketClosedError as e:
    #         print(e)


    # def get_msg_body(self):
    #     dataj = {
    #         "jsonrpc": "2.0",
    #         "method": "getChainInfo",
    #         "params": [],
    #         "id": 1234
    #     }
    #     db = json.dumps(dataj)
    #     return db
    #
    # async def my_sleep(self, amsg="done sleeping"):
    #     sleep(2)
    #     print(amsg)





    #
    #
    # def big_data(self):
    #     self.bigdata = {
    #         "MessageID": "45sdj8jcf8899ekffEFefee",
    #         "Timestamp": "1542102459",
    #         "TimeZone": "-8",
    #         "MessageType": "Request",
    #         "MessageData": {
    #             "SubscriptionEventCounter": "3",
    #             "SubscriptionPeriod": "0",
    #             "SubscriptionRange": "0",
    #             "ResponseMaxSize": "0",
    #             "RequestMethods": [
    #                 {
    #                 "GetBalance": {
    #                     "Address": "tNULSeBaMnrs6JKrCy6TQdzYJZkMZJDng7QAsD"
    #                 }
    #                 }
    #             ]
    #             }
    #         }
    #
    #


#
#
# ####/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# from tornado.ioloop import IOLoop, PeriodicCallback
# from tornado.websocket import websocket_connect
# from tornado import websocket
#
# # import tornado
# # import tornado.platform
#
#
# class Client(websocket):
#     def __init__(self, url, timeout):
#         self.url = url
#         self.ws = None
#         self.timeout = timeout
#         self.ioloop = IOLoop.instance()
#         #self.connect1()
#         self.ioloop.start()
#
#         send_this = "{ 'POST  HTTP/1.1', 'Host: 127.0.0.1:18003', 'Content-Type: application/json;charset=UTF-8', 'Accept: */*', 'Cache-Control: no-cache' ,'Host: 127.0.0.1:18003', 'Accept-Encoding: gzip deflate' ,'Content-Length: 80' ,'Connection: keep-alive', 'cache-control: no-cache', 'jsonrpc: 2.0' , 'method : getChainInfo',  'params:[]', 'id: 1234' }"
#
#
#
#     def on_open(self):
#         print("WebSocket opened")
#
#     def on_message(self, message):
#         self.write_message(u"You said: " + message)
#
#     def on_close(self):
#         print("WebSocket closed")
#
#     async def open(self):
#         conn = await websocket_connect(url)
#
#         async def proxy_loop():
#             while True:
#                 msg = await conn.read_message()
#                 if msg is None:
#                     break
#                 await self.write_message(msg)
#
#         self.ioloop.IOLoop.current().spawn_callback(proxy_loop)
#
#
# if __name__ == "__main__":
#     method: str = "ws://"
#     host = "localhost"
#     port = "9006"
#     #port = "18003"
#     url : str = ''.join([method, host, ":", port])
#     print(" uri:  ", url)
#     client = Client(url, 5)
#     client.open()
#
#
#




# send_this = '\{ \'POST  HTTP/1.1', 'Host: 127.0.0.1:18003', 'Content-Type: application/json;charset=UTF-8', 'Accept: */*', 'Cache-Control: no-cache' ,'Host: 127.0.0.1:18003', 'Accept-Encoding: gzip deflate' ,'Content-Length: 80' ,'Connection: keep-alive', 'cache-control: no-cache', 'jsonrpc: 2.0' , 'method : getChainInfo',  'params:[]', 'id: 1234' \}'
























# import json
# import asyncio
# from tornado import platform.
#
#
# # OPCODE=TEXT, FIN=0, MSG="Too much "
# from websocket.tests.test_websocket import TRACEABLE
#
#
# class n_socket(object):
#
#     def __init__(self):
#         ws.enableTrace(TRACEABLE)
#
#         self.url: str = "ws://127.0.0.1:7771"
#
#         sock = ws.WebSocket()
#         sock.set_mask_key(_abnf.create_mask_key)
#         self.data = {
#             "MessageID": "45sdj8jcf8899ekffEFefee",
#             "Timestamp": "1542102459",
#             "TimeZone": "-8",
#             "MessageType": "Request",
#             "MessageData": {
#                 "SubscriptionEventCounter": "3",
#                 "SubscriptionPeriod": "0",
#                 "SubscriptionRange": "0",
#                 "ResponseMaxSize": "0",
#                 "RequestMethods": [
#                     {
#                     "GetBalance": {
#                         "Address": "tNULSeBaMnrs6JKrCy6TQdzYJZkMZJDng7QAsD"
#                     }
#                     }
#                 ]
#                 }
#             }
#
#         self.sock = sock
#
#
#     async def main(self):
#         ws_conn = self.sock.create_connection(self.url)
#
#         frame = ABNF.create_frame(self.data, OPCODE='TEXT', fin=0)
#
#         print("Sending json query frame ...")
#
#         ws_conn.send_frame(frame)
#         await ws_conn.recv_data()
#
# n = n_socket()
# asyncio.get_event_loop().run_until_complete(n.main())
#













# hs = ws_conn.handshake_response

# payload_test: str = "hello"
# data_dict: dict = {
#     "MessageType": "Request",
#     "MessageData":
#         {"jsonrpc": "2.0",
#          "method": "getChainInfo",
#          "params": [],
#          "id": 1234
#          }
# }



# "TimeZone", "MessageID", "Timestamp", "MessageType", "MessageData"
# payload = bytes(jsond, 'utf-8')
# ws_conn.getstatus()
# ws_conn.getheaders()
# # ws_conn.send(payload, websocket.ABNF.OPCODE_TEXT)
# jsond = json.dumps(self.data2)

# ws_conn.send(payload, websocket.ABNF.OPCODE_TEXT)
#
# print("Waiting for json query...")
#
# resultb = ws_conn.recv()
#
# print("Result from json query: ", resultb)

# ws.close()
#
