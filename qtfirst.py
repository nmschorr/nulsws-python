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
import sys


mode1 = PySide2.QtCore.QUrl.ParsingMode.TolerantMode
host1 = "127.0.0.1"
port1 = 18003
scheme1 = "http"

sockUrl = PySide2.QtCore.QUrl()
sockUrl.setHost(host1, mode1)
sockUrl.setScheme(scheme1)
sockUrl.setPort(port1)

myNetworkReq = PySide2.QtNetwork.QNetworkRequest()
my_header_type = PySide2.QtNetwork.QNetworkRequest.ContentTypeHeader
myNetworkReq.setHeader(my_header_type, 'POST')


print("starting...")


myWebSocket = PySide2.QtWebSockets.QWebSocket()
myWebSocket.setProperty("id", "socket")


myWebSocket.open(myNetworkReq)


c = PySide2.QtWebSockets.QWebSocket.connect

myWebSocket.sendTextMessage("hello")





x = PySide2.QtWebSockets.QWebSocket.open(myWebSocket, sockUrl)
print("Sending 'Hello, World'...")
myint = myWebSocket.sendTextMessage("Hello, World")
print("send result: ", myint)




data1 = '{"jsonrpc":"2.0","method":"getChainInfo","params”:[], “id":1234}'
#myint2 = pqsock.sendTextMessage(my_header_type)

myint3 = myWebSocket.sendTextMessage(data1)
print("send result: ", myint3)


x = myWebSocket.request()

new_val = PySide2.QtWebSockets.QWebSocket.textMessageReceived

print("Sent")
myWebSocket.close()




# #curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"getChainInfo","params”:[], “id":1234}' http://127.0.0.1:18003
# 'Content-Type: application/json'
#
#
# --data '{"jsonrpc":"2.0","method":"getChainInfo","params”:[], “id":1234}' http://127.0.0.1:18003





print('done')
