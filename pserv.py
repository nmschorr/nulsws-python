from simple_websocket_server import WebSocketServer, WebSocket
import socket


class SimpleEcho(WebSocket):
    print("this host: ", str(socket.gethostname()))

    def handle(self):
        # echo message back to client
        h = self.headerbuffer
        h2 = self.headertoread
        print(h)
        print(h2)
        self.send_message(self.data)

    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')


print("starting...")

baby = '0.0.0.0'
port = 9006
print("serving on port: ", port)
server = WebSocketServer(baby, port, SimpleEcho)
server.serve_forever()


# # sends a header that looks like this:
# bytearray(b'GET / HTTP/1.1\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nHost: 127.0.0.1:9005\r\nOrigin: http://127.0.0.1:9005\r\nSec-WebSocket-Key: 7DpVVvtu26/fztcG9Wp93w==\r\nSec-WebSocket-Version: 13\r\n\r\n')

# bytearray(b'GET / HTTP/1.1\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nHost: 127.0.0.1:9005\r\nOrigin: http://127.0.0.1:9005\r\nSec-WebSocket-Key: 7DpVVvtu26/fztcG9Wp93w==\r\nSec-WebSocket-Version: 13\r\n\r\n')


