from simple_websocket_server import WebSocketServer, WebSocket


class SimpleEcho:
    def __init__(self):
        None


    def handle(self):
        # echo message back to client
        self.send_message(self.data)

    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')


server = WebSocketServer('', 9003, SimpleEcho)
server.serve_forever()

