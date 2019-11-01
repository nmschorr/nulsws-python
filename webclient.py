##########!/usr/bin/env python

import asyncio
import websockets



class webclient:
    def __init__(self):
        uri4 = "ws://localhost:18003"
        uri92 = "ws://localhost:9002"
        self.uri = uri4

    def init_strings(self):
        self.short_header = str("\"Content-Type: application/json\"\n")
        # self.long_header = "Content-Type: application/json;charset=UTF-8\n"
        get_str = str("\"GET /chat HTTP/1.1\"\n")
        conn_upg = str("\"Connection: Upgrade\"\n")
        other_part = str("\"Host: Baby.localdomain\"\n" + "\"Upgrade: websocket\"\n" + conn_upg)
        self.handshake_str = str(get_str + other_part)
        print("handshake_str: ", self.handshake_str)
        post_str = str("\"POST /chat HTTP/1.1\"\n")
        j_str = str('''{"jsonrpc": "2.0","method": "getChainInfo","params:[], id": 1234 }\n''')
        self.json_str  = str(  post_str + self.short_header + j_str)

        print("self.json_str: ", self.json_str)
        send_this = str("\{ \"POST  HTTP/1.1", "Host: 127.0.0.1:18003", "Content-Type: application/json;charset=UTF-8",
"Accept: */*", "Cache-Control: no-cache" ,"Host: 127.0.0.1:18003", "Accept-Encoding: gzip deflate" ,"Content-Length: 80" ,"Connection: keep-alive",
"cache-control: no-cache", "jsonrpc: 2.0" , "method : getChainInfo",  "params:[]", "id:1234" "" ) + str("}")

        print(send_this)
        exit()

    async def json_runner(self, uri):
        async with websockets.connect(uri) as websocket_js:

            print(f"Sending handshake {self.json_str}. Waiting for upgrade answer")
            await websocket_js.send(self.json_str)
            json_resp = await websocket_js.recv()
            print(f"Received handshake response: {json_resp}")



    async def runners(self, uri):
        async with websockets.connect(uri) as websocket_hs:
            await websocket_hs.send(self.handshake_str)
            print(f"Sending handshake {self.handshake_str}. Waiting for handshake answer")
            my_answer_hs = await websocket_hs.recv()
            print(f"JUST got response: {my_answer_hs}")

    def main(self):
        self.init_strings()
        asyncio.get_event_loop().run_until_complete(self.runners(self.uri ))
        asyncio.get_event_loop().run_until_complete(self.json_runner(self.uri ))
        print("Program done")

w = webclient()
w.main()









        # ee = "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\n"
        # ff = "Sec-WebSocket-Origin: http://schorrmedia.com\n"
        # gg = "Sec-WebSocket-Protocol: chat\n"
        # hh = "Sec-WebSocket-Version: 6\n"

        # uri7 = "ws://demos.kaazing.com/"
        # uri9 = "ws://localhost:18003"
        #
        # uri2 = "wss://echo.websocket.org/"
# async with websockets.connect(uri) as websocket:
#     print(f"Sending handshake {handshake}. Waiting for upgrade answer")
#     await websocket.send(handshake)
#     handshake_answer = await websocket.recv()
#     print(f"Received handshake response: {handshake_answer}")

# @handshake << <<EOF
# HTTP/1.1 101 Switching Protocols\r
# Upgrade: websocket\r
# Connection: Upgrade\r
# Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=\r
# \r
# EOF

# In the parameter section click on "raw" and select format as "JSON" and add the json request in the testarea provided.
#  In the headers section add "Content-Type" as header and "application/json;charset=UTF-8" as the value.