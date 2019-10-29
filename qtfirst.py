#!/usr/bin/python3
# import PySide2
#
import sys

# from PySide2 import QtQml
# from PySide2 import QtQuick
from PySide2 import QtNetwork
from PySide2 import QtWebSockets
# from PySide2 import QtWebChannel
from PySide2 import QtCore
import PySide2

import typing
from typing import Any

myCall = typing.Callable
import shiboken2 as Shiboken


print("starting...")

tolerant = QtCore.QUrl.ParsingMode.TolerantMode

host1 = "127.0.0.1"
port1 = 3001
scheme1 = "http"

sockUrl = QtCore.QUrl()
sockUrl.setHost(host1, tolerant)
sockUrl.setScheme(scheme1)
sockUrl.setPort(port1)

myNetworkReq = QtNetwork.QNetworkRequest()
my_header_type = QtNetwork.QNetworkRequest.ContentTypeHeader
myNetworkReq.setHeader(my_header_type, 'GET')

myWebSocket = PySide2.QtWebSockets.QWebSocket()

myStr = "Hello"
a: Any = None

QtWebSockets.QWebSocket.connect(myStr, a, QtWebSockets.QWebSocket.open(myWebSocket, myNetworkReq))

exit()






# PySide2.QtCore.QObject.connect(str, typing.Callable,
#    PySide2.QtCore.Qt.ConnectionType=PySide2.QtCore.Qt.ConnectionType.AutoConnection)

# myWebSocket.connect(myStr, PySide2.QtCore.SIGNAL("0"), QtCore.Qt.ConnectionType.AutoConnection)
# my_signal = PySide2.QtWebSockets.QWebSocket.connected()
# connect(hostLineEdit, & QLineEdit::textChanged,  this, & Client::enableGetFortuneButton);
#
# myWebSocket.open(myNetworkReq)
#
# myWebSocket.sendTextMessage("hello")
#
#
# print("Done...")
#QtWebSockets.QWebSocket.ConnnectionType()
# autoConnection = QtCore.Qt.ConnectionType.AutoConnection()


# myWebSocket.setProperty("id", "socket")







#
#
# x = PySide2.QtWebSockets.QWebSocket.open(myWebSocket, sockUrl)
# print("Sending 'Hello, World'...")
# myint = myWebSocket.sendTextMessage("Hello, World")
# print("send result: ", myint)
#
# PySide2.QtWebSockets.QWebSocket.textMessageReceived()
#
# data1 = '{"jsonrpc":"2.0","method":"getChainInfo","params”:[], “id":1234}'
# #myint2 = pqsock.sendTextMessage(my_header_type)
#
# myint3 = myWebSocket.sendTextMessage(data1)
# print("send result: ", myint3)
#
#
# x = myWebSocket.request()
#
# new_val = PySide2.QtWebSockets.QWebSocket.textMessageReceived
#
# print("Sent")
# myWebSocket.close()
#



# #curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"getChainInfo","params”:[], “id":1234}' http://127.0.0.1:18003
# 'Content-Type: application/json'
#
#
# --data '{"jsonrpc":"2.0","method":"getChainInfo","params”:[], “id":1234}' http://127.0.0.1:18003





print('done')
