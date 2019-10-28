#!/usr/bin/python3
# import PySide2
#
#
# import PySide2.Qt3DCore
# import PySide2.Qt
# import PySide2.QtNetwork
# import PySide2.QtHelp
import PySide2.QtWebSockets
import PySide2.QtCore

mode = "TolerantMode"
host = "127.0.0.1"
port = "18003"
scheme = "http"

print("starting...")
pqsock = PySide2.QtWebSockets.QWebSocket()

pq = PySide2.QtCore.QUrl()
pq.setHost(host, mode)
pq.setScheme(scheme)



x = PySide2.QtWebSockets.QWebSocket.open(pqsock, pq)
print(x)
print('done')
