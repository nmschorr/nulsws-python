from simple_websocket_server import WebSocketServer, WebSocket
import socket


class SimpleEcho(WebSocket):
    # print(str(WebSocket.client))
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

delia = '0.0.0.0'
port = 9005
print("serving on port: ", port)
server = WebSocketServer(delia, port, SimpleEcho)
server.serve_forever()


# HANDSHAKE_STR = (
#     'HTTP/1.1 101 Switching Protocols\r\n'
#     'Upgrade: WebSocket\r\n'
#     'Connection: Upgrade\r\n'
#     'Sec-WebSocket-Accept: %(acceptstr)s\r\n\r\n'
# )
# from WebSocketServer init