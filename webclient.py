##########!/usr/bin/env python

import asyncio
import websockets
import json
import requests

class webclient:
    def __init__(self):
        self.json_q = None

        self.uri: str = "ws://127.0.0.1:80"
        self.post_str = None

    def init_strings(self) -> str:
        # one_str: str = 'POST HTTP/1.1'
        # one_json = json.dumps(one_str, separators=('\n', ': '))
        # two_d: dict = {'Content-Type': 'application/json;charset=UTF-8'}
        # three_d: dict = {"Host": "127.0.0.1", "Upgrade": "websocket", "Connection": "Upgrade"}
        # four_d: dict = {'Accept': '*/*', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive'}
        # two_three_four_dict: dict = {**two_d, **three_d, **four_d}
        # two_three_four_json = json.dumps(two_three_four_dict, separators=(',', ':'))
                                                # above [1:][:-1] removes the brackets
        # all_json = one_json + "\n" + two_three_four_json
        # clean_json_header: str =  re.sub(r'"', "", all_json)

        query_dict: dict = {'jsonrpc': '2.0', 'method': 'getChainInfo', "params": [], "id": 1234}
        query_j: str = json.dumps(query_dict, indent=3, separators=(',', ': '))
        # self.post_str = clean_json_header + "\n\n" + query_json
        return query_j


    async def run_me(self):
        async with websockets.connect(self.uri) as wshs:
            print(f'Sending post. Waiting for post answer')
            # the_str: str = "hi"
            await wshs.send(self.json_q)
            json_resp = await wshs.recv()
            print(f'Received post response: {json_resp}')

    def main(self):
        self.json_q = self.init_strings()
        print("sending data...")
        asyncio.get_event_loop().run_until_complete(self.run_me())
        print('Program done')


w = webclient()
w.main()





# send_this = '\{ \'POST  HTTP/1.1', 'Host: 127.0.0.1:18003', 'Content-Type: application/json;charset=UTF-8', 'Accept: */*', 'Cache-Control: no-cache' ,'Host: 127.0.0.1:18003', 'Accept-Encoding: gzip deflate' ,'Content-Length: 80' ,'Connection: keep-alive', 'cache-control: no-cache', 'jsonrpc: 2.0' , 'method : getChainInfo',  'params:[]', 'id: 1234' \}'

# self.ws_uri: websockets.uri = websockets.parse_uri(self.uri)

# websocket_hs.handshake()
# hs_str = self.handshake_str
# await websocket_hs.send(hs_str)
# print(f'Sending handshake {hs_str}. Waiting for handshake answer')
# my_answer_hs = await websocket_hs.recv()
# print(f'JUST got response: {my_answer_hs}')


# asyncio.get_event_loop().run_until_complete(self.json_runner_post( self.uri, self.post_str ))
# asyncio.get_event_loop().run_forever(self.json_runner_post( self.uri, self.post_str ))











# aa = 'GET /chat HTTP/1.1\n'
# bb = 'Host: server.example\n'
# cc = 'Upgrade: websocket\n'
# dd = 'Connection: Upgrade\n'
# self.handshake_str = str(aa + bb + cc + dd)


# r = requests.request()
#
# r = requests.get(uri5,
#     headers={"Authorization": "Bearer " + sts_token},
#     params={"transport": "websocket"},
#     verify="FiddlerRoot.crt",
#     proxies={
#      'http': 'http://127.0.0.1:8888',
#      'https': 'http://127.0.0.1:8888'
#     })

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