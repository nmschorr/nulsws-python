#!/usr/bin/env python

import asyncio
import websockets

aa = 'GET /chat HTTP/1.1\n '
bb = 'Host: server.example\n '
cc = 'Upgrade: websocket\n '
dd = 'Connection: Upgrade\n '
ee = 'Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\n '
ff = 'Sec-WebSocket-Origin: http://schorrmedia.com\n '
gg = 'Sec-WebSocket-Protocol: chat\n '
hh = 'Sec-WebSocket-Version: 6\n '

newlist = 'GET /chat HTTP/1.1 \n '
my_list = aa + bb + cc + dd + ee + ff + gg + hh
msg = str(my_list)


jsonstr: str = '{"jsonrpc": "2.0", "method": "getChainInfo", "params": [], "id": 1234}'
sendthis: str = ''

uri7 = 'ws://demos.kaazing.com/'
uri9 = 'ws://localhost:9001'
echo_uri = 'wss://echo.websocket.org/'
uri = uri7

hello = "Hello world!"

async def send_msg(uri):
    print("sending this: ", msg)
    async with websockets.connect(uri) as websocket:
        await websocket.send(msg)
        my_answer = await websocket.recv()
        print(f"response: {my_answer}")

asyncio.get_event_loop().run_until_complete(send_msg(uri))

print("Program done")




# @handshake << <<EOF
# HTTP/1.1 101 Switching Protocols\r
# Upgrade: websocket\r
# Connection: Upgrade\r
# Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=\r
# \r
# EOF

# In the parameter section click on "raw" and select format as "JSON" and add the json request in the testarea provided.
#  In the headers section add "Content-Type" as header and "application/json;charset=UTF-8" as the value.