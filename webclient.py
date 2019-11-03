##########!/usr/bin/env python

import websocket
import json

from websocket import create_connection
# ws2 = create_connection("ws://echo.websocket.org/")
#ws = create_connection("ws://Delia:9003", http_proxy_port=8888)


ws = create_connection("ws://127.0.0.1:9004")
print("websocket status: ", ws.status)
print("is websock connected? ", ws.connected)
print("websock headers: ", ws.getheaders)
print("ws.handshake_response: ", ws.handshake_response)
print("ws.fileno: ", ws.fileno())


print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Receiving...")
result = ws.recv()
print("Received '%s'" % result)
ws.close()






#
#
# class webclient:
#     def __init__(self):
#         self.uri: str = "ws://127.0.0.1:8888"
#         self.json_q = None
#         self.post_str = None
#         self.query_jd = None
#
#     def init_strings(self) -> str:
#         method_str: str = 'POST HTTP/1.1' # method
#         headers_grp: dict = {'cache-control': 'no-cache', 'Content-Type': 'application/json'};
#
#         method_jd: str = json.dumps(method_str, separators=('\n', ': '))
#         header_str_jd: str = json.dumps(headers_grp, separators=('\n', ': '))
#         all_top= method_jd + "\n" + header_str_jd
#         all_top2: str =  re.sub(r'"', "", all_top)
#         all_top3: str =  re.sub(r'{', "", all_top2)
#         all_top4: str =  re.sub(r'}', "", all_top3)
#
#         query_dict: dict = {'jsonrpc': '2.0', 'method': 'getChainInfo', "params": [], "id": 1234}
#         self.query_jd: str = json.dumps(query_dict, indent=3, separators=(',', ': '))
#         query_str = all_top4 + "\n\n" + self.query_jd
#         return query_str
#
#
#     async def run_me(self):
#         async with websockets.connect(self.uri) as wshs:
#             print(f'Sending post. Waiting for post answer...\n')
#             # the_str: str = "hi"
#             # await wshs.send(self.json_q)
#             await wshs.request_headers()
#             ggd = await wshs.recv()
#             await wshs.send(self.query_jd)
#             json_resp = await wshs.recv()
#             print(f'Received post response:\n{json_resp}')
#
#     def main(self):
#         self.json_q = self.init_strings()
#         print("Starting app.")
#         asyncio.get_event_loop().run_until_complete(self.run_me())
#         print('Program done')
#
#
# w = webclient()
# w.main()
#
#
#
#








# two_d: dict = {'Content-Type': 'application/json;charset=UTF-8'}
# three_d: dict = {"Host": "127.0.0.1", "Upgrade": "websocket", "Connection": "Upgrade"}
# four_d: dict = {'Accept': '*/*', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive'}
# two_three_four_dict: dict = {**two_d, **three_d, **four_d}


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