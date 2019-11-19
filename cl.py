
##### python 3.7

# class WebSocketClientConnection(simple_httpclient._HTTPConnection):
"""WebSocket client connection.

This class should not be instantiated directly; use the
`websocket_connect` function instead.
"""
# Override `on_message` to handle incoming messages, and use
# `write_message` to send messages to the client.


from tornado.websocket import websocket_connect, WebSocketClosedError
from tornado.websocket import WebSocketHandler
import json
import asyncio
import tornado


class WsClient(WebSocketHandler):

    def __init__(self):
        method: str = "ws://"
        host = "localhost"
        port = "9006"
        # port = "18003"
        self.my_url: str = ''.join([method, host, ":", port])
        self.msg = self.get_msg_body()
        self.answer = None
        self.answer1 = None
        self.going = True

    async def handle_stuff(self):
        while self.going:
            try:
                connection = await websocket_connect(self.my_url)
                await asyncio.sleep(1)

                self.answer1 = await connection.write_message(u"helloThere!!!!!!")

                print("first answer: " , self.answer1)
                await asyncio.sleep(1)
                self.answer = await connection.write_message(self.msg)
                print("received answer!!!!  :  ", self.answer)
            except WebSocketClosedError as e:
                print(e)

    def get_msg_body(self) -> str:
        dataj = {
            "jsonrpc": "2.0",
            "method": "getChainInfo",
            "params": [],
            "id": 1234
        }
        data_body = json.dumps(dataj)
        return data_body


    async def main(self):
        await self.handle_stuff()


if __name__ == "__main__":
    w = WsClient()
    asyncio.run(w.main(), debug=True)





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
