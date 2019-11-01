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
        import re
        one_str: str = 'POST HTTP/1.1'
        one_json = json.dumps(one_str, separators=('\n', ': '))
        two_d: dict = {'Content-Type' : 'application/json;charset=UTF-8'}
        three_d: dict = { "Host" : "127.0.0.1" , "Upgrade": "websocket", "Connection" : "Upgrade"}
        four_d: dict = {'Accept' : '*/*', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive'}
        two_three_four_dict: dict = {**two_d, **three_d, **four_d}

        two_three_four_json = json.dumps(two_three_four_dict, separators=('\n', ': ')  )[1:][:-1]
                                                # above [1:][:-1] removes the brackets
        all_json = one_json + "\n" + two_three_four_json
        clean_json_header: str =  re.sub(r'"', "", all_json)

        #print(clean_json_header)
        print()


        query_dict: dict = {'jsonrpc': '2.0',  'method': 'getChainInfo' , "params" : [], "id" : 1234 }
        query_json: str = json.dumps(query_dict, indent=3, separators=(',', ': ') )
        self.post_str = clean_json_header + "\n\n" + query_json
        #print("post_str: ", self.post_str)

        # send_this = '\{ \'POST  HTTP/1.1', 'Host: 127.0.0.1:18003', 'Content-Type: application/json;charset=UTF-8', 'Accept: */*', 'Cache-Control: no-cache' ,'Host: 127.0.0.1:18003', 'Accept-Encoding: gzip deflate' ,'Content-Length: 80' ,'Connection: keep-alive', 'cache-control: no-cache', 'jsonrpc: 2.0' , 'method : getChainInfo',  'params:[]', 'id: 1234' \}'

    async def json_runner_post(self, uri, json_query):
        async with websockets.connect(uri) as websocket_js:

            print(f'Sending post {json_query}. Waiting for post answer')
            await websocket_js.send(json_query)
            json_resp = await websocket_js.recv()
            print(f'Received post response: {json_resp}')



    # async def runner_handshake(self, uri, query):
    #     async with websockets.connect(uri) as websocket_hs:
    #         await websocket_hs.send(self.handshake_str)
    #         print(f'Sending handshake {self.handshake_str}. Waiting for handshake answer')
    #         my_answer_hs = await websocket_hs.recv()
    #         print(f'JUST got response: {my_answer_hs}')

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