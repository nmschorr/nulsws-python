#The Nulsws-Python-Connect Libraries
##### by Nancy M Schorr, for Nuls-io
##### February, 2020
 
* Style Note: 
The coding style
 recommendation can be found here:  
 https://www.python.org/dev/peps/pep-0008/#package-and-module-names

### Introduction
The nulsws-python-connect library is built to provide communication between Nulstar ports and 
client applications and ports. It is based on the python library and framework 
__Tornado__.

Berzeck in Bolivia has been my mentor and lead on this project. The project goal is to 
implement the goals set forth mainly in these two Nulstar messaging documents: 

- Nulstar - Documentation - Module Specification.pdf
- Nulstar - Documentation - Message Protocol


These outline 8 types of JSON message structures to be supported initially. 4 are for 
the sending client, and 4 for the receiving/responding server. These libraries are the base
 upon which NULS customers can base their own Python-based modules messaging modules.

The eight types of messages in development are:
- 1  Negotiate Connection
- 2  Negotiate Connection Response
- 3  Request
- 4  Unsubscribe
- 5  Response
- 6  Ack
- 7  Register Compound Method
- 8  Unregister Compound Method.

 Messages have a common structure composed of six fields which comprise what I later 
 refer to as the "top" portion of the message:
-  ProtocolVersion: version the service to understand,2 numbers, major/minor
-  MessageID: identifies a request.
-  Timestamp:  Number  of  seconds  since  epoch January 1,1970
-  TimeZone: The time zone where the request was originated
-  MessageType: The message type, these are specified on section 3
-  MessageData: A Json object with the message payload

The first message sent from a client to the server is the request for a connection. 
Tornado takes care of all the necessary header details, including the request to 
"upgrade" the socket communication to http. 

 The next object sent only goes if the negotiation is ok. If it isn't, a
  NegotiateConnectionResponse object should be received with
 Status set to 0 (Failure) and disconnect immediately. Python programmers please note that
  Nulstar is written in C++ and the standard for 0 and True is reversed.

Example Negotiate request:

 "MessageType": "NegotiateConnection",
 "MessageData": {
     "CompressionAlgorithm": "zlib",
     "CompressionRate": "3"



## Tornado
 
Tornado is a Python a framework and asynchronous networking library, originally developed at FriendFeed - 
later acquired by Facebook. By using non-blocking network I/O, Tornado can scale to tens of 
thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a  
long-lived connection to each user.

WebSockets http://dev.w3.org/html5/websockets/,  The module implements the final version of the WebSocket protocol as
defined in `RFC 6455 <http://tools.ietf.org/html/rfc6455>`. 

 Tornado is a scalable, non-blocking web server and web application framework written in Python.
 It provides a means for bidirectional communication between client and server.  It was
  developed by FriendFeed (acquired by Facebook in 2009), and was open-sourced soon 
  after. 
  
  I chose this library after trying a few other that either weren't sufficiently
   supported and up-to-date, or were too complex for our needs.  Tornado does a 
   very satifactory job of setting up the ports for websocket bidirectional communication.
   The first communication between the ports is a little tricky. 
    The  header and preliminary message protocol have two parts:  a 
    handshake and a data transfer.

   The handshake from the client looks roughly like this:

        GET /chat HTTP/1.1
        Host: server.example.com
        Upgrade: websocket
        Connection: Upgrade
        Origin: http://example.com
        Sec-WebSocket-Protocol: chat, superchat
        Sec-WebSocket-Version: 13

   And the handshake from the server looks like:

        HTTP/1.1 101 Switching Protocols
        Upgrade: websocket
        Connection: Upgrade
        Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
        Sec-WebSocket-Protocol: chat
        
Once the client and server have done their handshakes - if successful -  data transfer 
 begins. This is a two-way communication where each side can, independently from the  
 other, send data.

### The nulsws-python-connect library contains the following files:

The client (client.py) - Class 'Client'
uses the libraries to build JSON messages, then send them out, and receive the responses to those messages.
It uses Python's newer asyncio communication model. 

There is just one method in the main class Client - main(). This method calls 
 run_queries.RunQueries.run_queries_m.  This method runs everything else. 
 
 The JSON structures are created in 3 main steps - make_top.py, make_middle.py, and make_very_top
 .  make_middle takes care of the bottom. Luckily for us - Python dictionaries are almost exactly
  like JSON messages - so converting back and forth is simple and easy.
 

- Inside client.py is main(self, runlist, msg_type=3):  This method takes input from the scripting
 area below the
 class in the
 class file - ie, the runlist and the message type. Currently the message default is set to 3. The 
 development phase is focussed mainly on type 3. main() sets things in motion by executing  asyncio_run 
 which is the parent of all further asyncio activity in the client application.
 
 The runlist is a list of requests desired by the client - and to be answered by the Nulstar modules.
  
 sending it the top-to-middle portion, an indexing parameter to ensure no two requests have the same id, 
 the requesting "runlist" of api requests, and the message type which in this case is '3' for request.
  
run_queries_m() calls "negotiate list". This method set's up the connection with the target port
, then sends 
 message type 2 which is a Negotiate request. This negotiation must be done every time a port is opened.
 
 After the building of JSON requests, opening and negotiating, the JSON request is sent via the
  same open connection via regular_request.RegularRequest.regular_request_m.
  
The runlist is put at the bottom of the main client file like this:

'''
if __name__ == '__main__':
    RUNLIST = [b.AC_GET_ACCOUNT_BYADDRESS, b.AC_GET_ALL_ADDRESS_PREFIX, b.AC_GET_ACCOUNT_LIST,
                b.AC_GET_ADDRESS_LIST, b.AC_GET_ADDRESS_PREFIX_BY_CHAINID, b.AC_GET_ALL_ADDRESS_PREFIX,
                b.AC_GET_ALL_PRIKEY, b.AC_GET_ALIASBY_ADDRESS]
    message_type = 3 
    nws = Client()    
    nws.main(RUN_LIST, message_type)
'''

The framework includes a set of Constants libraries contained in the file "call_d" which is a
 dictionary used to lookup settings and call names for each call.
. This is a somewhat complex 
behind-the-scenes mechanism that make setting preferences for each of the 228 or so 
types of message easy for the developer.  Within those 228 types of requests are 124 
different parameters. Many of the requests only require one or parameters, but some as 
many as eight or so. With the average being maybe 3-4 - that gives us a total of around
1,000 possible specific parameters for this nuls-python-connect library.

The user/developer initially only needs to set parameter for those functions he/she is 
interested in. The settings go into two user parameter files in the NulsWsRequest 
directory. 

The first file, calls_d.py, contains every one of the possible parameters. 
Once set in this file, it is fed into the library, and no further setup is needed to 
access the as-is nuls blockchain via the Nulstar Connector module. 

__Here's a sample:__

     'AC_CREATE_MULTI_SIGN_TRANSFER': {"ac_createMultiSignTransfer": {
            par_d.get("CHAINID"): u.get("z4_AC_CREATE_MULTI_SIGN_TRANSFER_chainId"),
            par_d.get("INPUTS"): u.get("z4_AC_CREATE_MULTI_SIGN_TRANSFER_inputs"),
            par_d.get("OUTPUTS"): u.get("z4_AC_CREATE_MULTI_SIGN_TRANSFER_outputs"),
            par_d.get("REMARK"): u.get("z4_AC_CREATE_MULTI_SIGN_TRANSFER_remark"),
            par_d.get("INPUTS"): u.get("z4_AC_CREATE_MULTI_SIGN_TRANSFER_signAddress"),
            par_d.get("SIGNPASSWORD"):
                u.get("z4_AC_CREATE_MULTI_SIGN_TRANSFER_signPassword"),
            par_d.get("SIGNPASSWORD"): u.get("z25_AC_SET_MULTISIGN_ALIAS_signPassword")}},


As you can see the parameters are numbered so we have some basis for distinguishing them
 from each other besides their names. Currently 
every one of the 1000+ parameters is set to something, although in most cases it ends 
up being 1 or 0.

This file never changes unless you are developing.  In that case - it is in dictionary format, so
 care needs to be taken if it is edited.

#### usersettings.py
Most user editing will be done in the user_settings/usersettings.py file. Here's a sample:

connect_method = "ws://"   # could be wss
host_req = "127.0.0.1"
port_req = "7772"    
compress_type_VALUE = "zlib"
compress_rate_VALUE = 0                      # 0-9
my_pubkeys: 1
my_chainid: int = 1               # int
my_account: str = "NULSd6Hggvrij3MPW9QTHJGBv7uiyMKw41i7t"             # java-type-String
my_password = 'nuls123456'   # str
my_addresstype: int = 0               # int
my_assetchainid: int = 1               # int
my_assetid: int = 1               # int
my_blocktype: int = 0               # int
my_circulatechainid: int = 0               # int
my_commissionrate: int = 0               # int
my_height: int = 0               # int
my_address: str = "NULSd6Hggvrij3MPW9QTHJGBv7uiyMKw41i7t"             # java-type-String
my_addressprefix: str = 'NULS'           # java-type-String


### Further project goals
- Complete implementation of the python library as described in Berzeck's documents
- Further document this framework
- Properly package it according to Python standards so it can be easily installed, 
accessed, and built-upon. See https://packaging.python.org/overview/ for details.

