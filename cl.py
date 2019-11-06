import websocket
import json
import asyncio

class n_socket(object):

    def __init__(self):

        self.url: str = "ws://127.0.0.1:7771"
        self.websock_obj = websocket
        self.data = {
            "MessageID": "45sdj8jcf8899ekffEFefee",
            "Timestamp": "1542102459",
            "TimeZone": "-8",
            "MessageType": "Request",
            "MessageData": {
                "SubscriptionEventCounter": "3",
                "SubscriptionPeriod": "0",
                "SubscriptionRange": "0",
                "ResponseMaxSize": "0",
                "RequestMethods": [
                    {
                    "GetBalance": {
                        "Address": "tNULSeBaMnrs6JKrCy6TQdzYJZkMZJDng7QAsD"
                    }
                    }
                ]
                }
            }

    async def main(self):
        ws_conn = self.websock_obj.create_connection(self.url)
        payload = self.data

        print("Sending json query ...")
        ws_conn.send_frame(payload)
        #ws_conn.send(payload, websocket.ABNF.OPCODE_TEXT)
        await ws_conn.recv_data()

n = n_socket()
asyncio.get_event_loop().run_until_complete(n.main())














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
