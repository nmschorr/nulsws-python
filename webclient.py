##########!/usr/bin/env python

import asyncio
import websockets
import json


class webclient:
    def __init__(self):
        uri4: str = 'ws://localhost:18003'
        uri92: str = 'ws://localhost:9002'
        self.uri = uri4

    def rem_brackets(self, myvar):
        return myvar[1:][:-1]

    def init_strings(self):
        one_s: str = 'POST  HTTP/1.1'
        two_d: dict = {'Content-Type' : 'application/json;charset=UTF-8'}
        three_d: dict = { "Host" : "127.0.0.1" , "Upgrade": "websocket", "Connection" : "Upgrade"}
        four_d: dict = {'Accept' : '*/*', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive'}
        BIG_d: dict = {**two_d, **three_d, **four_d}

        big_s = json.dumps(BIG_d)[1:][:-1]
        big_string = json.dumps(one_s) + ", " + big_s
        
        five_d: dict = {'jsonrpc': '2.0',  'method': 'getChainInfo' , "params" : "[]" }
        five_jd: str = json.dumps(five_d)[1:][:-1]
        self.post_str = big_string + ", " + five_jd
        print()

        # send_this = '\{ \'POST  HTTP/1.1', 'Host: 127.0.0.1:18003', 'Content-Type: application/json;charset=UTF-8', 'Accept: */*', 'Cache-Control: no-cache' ,'Host: 127.0.0.1:18003', 'Accept-Encoding: gzip deflate' ,'Content-Length: 80' ,'Connection: keep-alive', 'cache-control: no-cache', 'jsonrpc: 2.0' , 'method : getChainInfo',  'params:[]', 'id: 1234' \}'

    async def json_runner(self, uri):
        async with websockets.connect(uri) as websocket_js:

            print(f'Sending handshake {self.json_str}. Waiting for upgrade answer')
            await websocket_js.send(self.json_str)
            json_resp = await websocket_js.recv()
            print(f'Received handshake response: {json_resp}')



    async def runner_post(self, uri, query):
        async with websockets.connect(uri) as websocket_hs:
            await websocket_hs.send(self.handshake_str)
            print(f'Sending handshake {self.handshake_str}. Waiting for handshake answer')
            my_answer_hs = await websocket_hs.recv()
            print(f'JUST got response: {my_answer_hs}')

    def main(self):
        self.init_strings()
        # asyncio.get_event_loop().run_until_complete(self.runner_post(self.uri, self.post_str))
        asyncio.get_event_loop().run_until_complete(self.json_runner_post( self.uri, self.post_str ))
        print('Program done')

w = webclient()
w.main()









        # ee = 'Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\n'
        # ff = 'Sec-WebSocket-Origin: http://schorrmedia.com\n'
        # gg = 'Sec-WebSocket-Protocol: chat\n'
        # hh = 'Sec-WebSocket-Version: 6\n'

        # uri7 = 'ws://demos.kaazing.com/'
        # uri9 = 'ws://localhost:18003'
        #
        # uri2 = 'wss://echo.websocket.org/'
# async with websockets.connect(uri) as websocket:
#     print(f'Sending handshake {handshake}. Waiting for upgrade answer')
#     await websocket.send(handshake)
#     handshake_answer = await websocket.recv()
#     print(f'Received handshake response: {handshake_answer}')

# @handshake << <<EOF
# HTTP/1.1 101 Switching Protocols\r
# Upgrade: websocket\r
# Connection: Upgrade\r
# Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=\r
# \r
# EOF

# In the parameter section click on 'raw' and select format as 'JSON' and add the json request in the testarea provided.
#  In the headers section add 'Content-Type' as header and 'application/json;charset=UTF-8' as the value.