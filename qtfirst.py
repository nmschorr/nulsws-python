#!/usr/bin/python3
# import PySide2
#
#
# import PySide2.Qt3DCore
# import PySide2.Qt
import PySide2.QtNetwork
# import PySide2.QtHelp
import PySide2.QtWebSockets
import PySide2.QtCore
import PySide2.examples

mode1 = PySide2.QtCore.QUrl.ParsingMode.TolerantMode
host1 = "127.0.0.1"
port1 = 18003
scheme1 = "http"

print("starting...")
pqsock = PySide2.QtWebSockets.QWebSocket()

pq = PySide2.QtCore.QUrl()
pq.setHost(host1, mode1)
pq.setScheme(scheme1)
pq.setPort(port1)


x = PySide2.QtWebSockets.QWebSocket.open(pqsock, pq)
print("Sending 'Hello, World'...")
myint = pqsock.sendTextMessage("Hello, World")
print("send result: ", myint)

nr = PySide2.QtNetwork.QNetworkRequest()
my_header_type = PySide2.QtNetwork.QNetworkRequest.ContentTypeHeader

nr.setHeader(my_header_type, 'POST')


data1 = '{"jsonrpc":"2.0","method":"getChainInfo","params”:[], “id":1234}'
#myint2 = pqsock.sendTextMessage(my_header_type)

myint3 = pqsock.sendTextMessage(data1)
print("send result: ", myint3)


x = pqsock.request()

new_val = PySide2.QtWebSockets.QWebSocket.textMessageReceived

print("Sent")
pqsock.close()




# #curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"getChainInfo","params”:[], “id":1234}' http://127.0.0.1:18003
# 'Content-Type: application/json'
#
#
# --data '{"jsonrpc":"2.0","method":"getChainInfo","params”:[], “id":1234}' http://127.0.0.1:18003





print('done')
