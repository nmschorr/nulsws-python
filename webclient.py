

import json
import json.encoder
import requests

url = "http://127.0.0.1:18003"
url2 = "ws://127.0.0.1:9006"
url = "http://127.0.0.1:7771"


def main():
    dataj = {
        "jsonrpc": "2.0",
        "method": "getChainInfo",
        "params": [],
        "id": 1234
    }
    data_body = json.dumps(dataj)
    r = requests.post(url=url, data=data_body)
    print(r)
    print(r.text)

main()

