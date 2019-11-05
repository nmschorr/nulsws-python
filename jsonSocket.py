import json
import socket
import struct
import logging
import time

# https://github.com/Near32/JSONPythonClientServer/blob/master/jsonSocket.py


logger = logging.getLogger("jsonSocket")
logger.setLevel(logging.DEBUG)
FORMAT = '[%(asctime)-15s][%(levelname)s][%(funcName)s] %(message)s'

logging.basicConfig(format=FORMAT)


class jsonSocket(object):
    def __init__(self, address='127.0.0.1', port=18003):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = self.socket
        self._timeout = None
        self._address = address
        self._port = port

    def sendObj(self, obj):
        msg = json.dumps(obj)
        if self.socket:
            frmt = "=%ds" % len(msg)
            packedMsg = struct.pack(frmt, msg)
            packedHdr = struct.pack('!I', len(packedMsg))

            self._send(packedHdr)
            self._send(packedMsg)

    def _send(self, msg):
        sent = 0
        while sent < len(msg):
            sent += self.conn.send(msg[sent:])

    def _read(self, size):
        data = ''
        while len(data) < size:
            dataTmp = self.conn.recv(size - len(data))
            data += dataTmp
            if dataTmp == '':
                raise RuntimeError("socket connection broken")
        return data

    def _msgLength(self):
        d = self._read(4)
        s = struct.unpack('!I', d)
        return s[0]

    def readObj(self):
        size = self._msgLength()
        data = self._read(size)
        frmt = "=%ds" % size
        msg = struct.unpack(frmt, data)
        return json.loads(msg[0])

    def close(self):
        self._closeSocket()
        if self.socket is not self.conn:
            self._closeConnection()

    def _closeSocket(self):
        logger.debug("closing main socket")
        self.socket.close()

    def _closeConnection(self):
        logger.debug("closing the connection socket")
        self.conn.close()

    def _get_timeout(self):
        return self._timeout

    def _set_timeout(self, timeout):
        self._timeout = timeout
        self.socket.settimeout(timeout)

    def _get_address(self):
        return self._address

    def _set_address(self, address):
        pass

    def _get_port(self):
        return self._port

    def _set_port(self, port):
        pass

    timeout = property(_get_timeout, _set_timeout, doc='Get/set the socket timeout')
    address = property(_get_address, _set_address, doc='read only property socket address')
    port = property(_get_port, _set_port, doc='read only property socket port')


class JSONClient(jsonSocket):
    def __init__(self, address='127.0.0.1', port=18003):
        super(JSONClient, self).__init__(address, port)

    def connect(self):
        for i in range(10):
            try:
                self.socket.connect((self._address, self._port))
            except socket.error as msg:
                logger.error("SockThread Error: %s" % msg)
                time.sleep(3)
                continue
            logger.info("...Socket Connected")
            return True
        return False
