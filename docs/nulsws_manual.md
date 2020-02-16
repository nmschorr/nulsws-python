#The Nulsws-Python-Connect Libraries
##### by Nancy M Schorr, for Nuls-io
##### December, 2019
 
* Style Note: 
Please note: much of "correct" Python style is in lower case. Much of this code - being
 in an early dev stage does not yet follow these conventions, although it is my intent 
 for the finished product to follow them as much as possible. The coding style
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
the sending client, and 4 for the receiving/responding server. These libraries are the
 upon which Nuls customers can base their own Python-based modules messaging modules.

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

 the first object that should be sent - only if the negotiation is ok service may process
 further requests -otherwise a NegotiateConnectionResponse object should be received with
 Status set to 0 (Failure) and disconnect immediately.

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
defined in `RFC 6455 <http://tools.ietf.org/html/rfc6455>`_. 

 Tornado 
is a scalable, non-blocking web server and web application framework written in Python.
 It provides a means for bidirectional communication between client and server.  It was
  developed by FriendFeed (acquired by Facebook in 2009), and was open-sourced soon 
  after. I chose this library after trying a few other that either weren't sufficiently
   supported and up-to-date, or were too complex for our needs.  Tornado does a 
   very satifactory job of setting up the ports for websocket bidirectional communication.
   The first communication between the ports is a little tricky. 
    The  header and preliminary messages look like this: The protocol has two parts:  a 
    handshake and the data transfer.

   The handshake from the client looks roughly like this:

        GET /chat HTTP/1.1
        Host: server.example.com
        Upgrade: websocket
        Connection: Upgrade
        Origin: http://example.com
        Sec-WebSocket-Protocol: chat, superchat
        Sec-WebSocket-Version: 13

   And the handshake from the server looks like::

        HTTP/1.1 101 Switching Protocols
        Upgrade: websocket
        Connection: Upgrade
        Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
        Sec-WebSocket-Protocol: chat
        
Once the client and server have done their handshakes - if successful -  data transfer 
 begins. This is a two-way communication where each side can, independently from the  
 other, send data.

### The nulsws-python-connect library contains the following files:

1) The Client, (ClientApp\nulsws_RUNNER_client.py) later to become both a client and a server.  The client 
uses the libraries to build JSON messages, then send them out, and receive the responses to those messages.

The main class is called Client. It uses Python's newer asyncio communication model. 

The four methods currently in nulsws_RUNNER are:

-  main(self, runlist, msg_type=3):  This method takes input from the scripting area below the class in the
 class file - ie, the runlist and the message type. Currently the message default is set to 3. The 
 development phase is focussed mainly on type 3. main() sets things in motion by executing  asyncio_run 
 which is the parent of all further asyncio activity in the client application.
 
 The runlist is a list of requests desired by the client - and to be answered by the Nulstar modules.
 
 main() first calls prep_NEGOTIATE_request() to prepare the top-to-middle portion of the JSON request.
 
Then main() calls:
  asyncio_run(  self.negotiate_list(   top_pls_middle_dict, myindx, runlist, mtpe))   
  
 sending it the top-to-middle portion, an indexing parameter to ensure no two requests have the same id, 
 the requesting "runlist" of api requests, and the message type which in this case is '3' for request.
  
 main() then calls "negotiate list". This method set's up the connection with the target port, then sends 
 message type 2 which is a Negotiate request. This negotiation must be done every time a port is opened.
 
 After the opening and negotiating, the "Regular" request is sent via:
  REGULAR_req(self, websock_connct: WebSocketClientConnection, j_reg_dict):
 
 The 'connection' is sent to this method with the "Regular" request.
 
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

The framework then include a set of Constants libraries. This is a somewhat complex 
behind-the-scenes mechanism that make setting preferences for each of the 228 or so 
types of message easy for the developer.  Within those 228 types of requests are 124 
different parameters. Many of the requests only require one or parameters, but some as 
many as eight or so. With the average being maybe 3-4 - that gives us a total of around
1,000 possible specific parameters for this nuls-python-connect library.

The user/developer initially only needs to set parameter for those functions he/she is 
interested in. The settings go into two user parameter files in the NulsWsRequest 
directory. 

The first file, nulsws-USER_PARAMS.py, contains every one of the possible parameters. 
Once set in this file, it is fed into the library, and no further setup is needed to 
access the as-is nuls blockchain via the Nulstar Connector module. 

__Here's a sample:__

`1_AC_CREATE_ACCOUNT_chainId = my_chainid`
`1_AC_CREATE_ACCOUNT_count = my_chainid`
`1_AC_CREATE_ACCOUNT_password = my_password`
`2_AC_CREATE_CONTRACT_ACCOUNT_chainId = my_chainid`
`3_AC_CREATE_MULTI_SIGN_ACCOUNT_chainId = my_chainid`
`3_AC_CREATE_MULTI_SIGN_ACCOUNT_pubKeys = my_pubkeys`
`3_AC_CREATE_MULTI_SIGN_ACCOUNT_minSigns = my_minsigns`
`4_AC_CREATE_MULTI_SIGN_TRANSFER_chainId = my_chainid`

As you can see the parameters are numbered so we have some basis for sanity. Currently 
every one of the 1000+ parameters is set to something, although in most cases it ends 
up being 1 or 0.

This file never changes on the left side of the "=" unless the user is developing and 
changes the underlying structure.  And once the parameters on the right side are set up,
then may rarely need to be changed.

#### nulsws_SET.py
Most editing will be done in the nulsws_SET.py file. Here's a sample:

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

### Personal goals
- Get this python framework done
- Polish my Python skills
- Learn more blockchain
- Host a node or three

#### Background
 
 Code-wise - I've been a Java coder for some years. I was on the Swing and
  AWT QA and tools teams at Sun starting in 1997. During those years, I also worked a 
  lot with Oracle databases, and was certified as an Oracle DBA in 2013. I also 
  programmed extensively in Perl, and before that in other languages. At Apple I worked
  in performance cpu testing and developed low-level tracing tools in C. You can see 
   my resume for further details. Born in New York, I graduated from UC Irvine and did 
   some graduate work in Transpersonal Psychology at CIIS in San Francisco.
   
 ### Why Python? ###
  I love the direct and simple philosophy and the wealth of methods 
 that 
 greatly simplify things that have been too complicated for too long. After years of C 
 and Java - it's been a pure joy to immerse myself in the Python world.
 
  ### Nuls and me
My experience with Nuls is that it has a very strong and functioning Java and C basis.
I've been very impressed with the code I've seen. Nuls provides an easy to use and 
understand blockchain model. It's not just one of the many Ethereum knockoffs. I believe
 it has a future. I very much like the open community model that is expressed in it's 
 public documentation. I'm very comfortable with all the tools in use including Git, 
 Telegram, etc.
  
 ### Personal Details
 Berzeck asked me to include something personal like hobbies. My hobbies include light 
 trail hiking (up to maybe 5 miles in a day), camping, gardening, astronomy, friends and 
  family of course, and tending to our friend Cosmo the hummingbird we helped rescued 
  last winter and who lives now in our yard. I also occasionally babysit the 3 chickens 
  next door. I live in the south-part of the San Francisco Bay Area in Santa Clara with
   my fiance Shawn who I've been with now for about 11 years.


#### The following is from my experience with the Nuls Hackathon ####

### My Experience Coding with Nuls
Wow, amazing. It's hard to believe a loosely organized open-source, international group of people have this giant code-base not only working but available for everyone. The transactions, encryption, data flow etc are all functional. Clearly the expertise of the developers was very advanced to begin with. In this project you will find:

- Abstract Classes, Interfaces
- Collections â€“ List, Map, Set etc.
- File IO, Serialization, RPC
- Spring, Annotations and Optionals
- Multithreading and Synchronization
- Generics; Dependency Injection, Lambda's
- Grizzly/Jersey Servers, Servlets, Sockets, 
- Web Technologies - HTML, REST, CSS, Javascript, JQuery and Ajax
- And don't forget Maven, Git, and Bash


###Some Things I Changed from Chainbox

Much of the code was difficult to read at first since it was both unfamiliar, and frankly - I had given up on Java and have been using Python more and more over the past few years. Going back to Java was a little bit painful. But I found I enjoyed the 'sturdy' feeling of something that won't tie itself together unless it's developers really "make it so". Also, much of the technology around Java - like profiling and debugging - are very advanced. 

A lot of the Chainbox code had been condensed so that it was fast, lightweight, efficient - but difficult to step through with a debugger for learning purposes. So I undid a lot of the function calls within function calls, etc. I also moved functionality around a little bit so that the main working parts were more together. 

Since my app doesn't send email - in the future I'd like to remove some of that and other extraneous code if posssible.


##Debugging Nuls 

When I moved onto the meat and potatoes of the app - I discovered that transferring nuls between accounts was easier said than done. In order to better understand the process, I usually use the debugger built into whatever IDE I'm using. However, in the case of Nuls - a giant, complex code base with numerous configuration files - this wasn't going to be possible. Also, you would want debugging run on the entire system because it would slow to a crawl.


The Java JDK ships with it's own built in debugger - often accessed by the command line via the cli tool jdb. However, having little experience using that I did some research and found that Intellij Idea for Java would run with the JDK build in debugger.

I enabled the debugger to run with just my module. Included in this package is a file in the "webextras" directory called "start.debugger.sh" that enables this. Rename the this file to "start.sh" and copy it over the start.sh in <project-directory>/NULS_WALLET/Modules/Nuls/nuls-blockparty/1.0.0/ . Type "start.sh nuls-blockparty" or just restart with "start-dev" and you're on your way. If you run 'tools' again it will be erased.

The debugger runs on port 8000. Go into the Run / Edit Configurations and add a configuration for Remote from the run templates provided. Enter 8000 for the port. It should automatically fill in the settings which are:

       -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=localhost:8000

These are the same settings that go into the java run instruction for the module you want to debug.

Addendum:  Resume


