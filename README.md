# nuls-python-connect


This is the repository for the (as yet unfinished) Python 3.7 libs - enabling connections to the
 Nuls
 blockchain modules and platform via Nulstar and Websockets.


###JSON and WebSockets
Every Nuls
microservice is both a client and a server. Therefore a full-duplex, bi-directional
communication protocol is needed. It needs to implement a special type
of publish-subscription pattern. In this library, methods can be invoked just
once -- and the caller can receive constant updates afterwards in two different ways:

• **Event based:** When the method sends notifications after a predefined number
of events

• **Period based:** When the method sends notifications after a predefined
number of seconds

WebSockets is a mature option offering full-duplex connectivity natively. Other
alternatives such as standard JSON-RPC do not offer bidirectional channels. This library uses
 JSON as it is the most widely used for message interchange, and is easy to debug.

The Nuls platform is language agnostic - so modules can be developed using different 
 languages. The only requirements are that modules use the same transport mechanism (WebSockets
 /JSON) and that they send their calls to the Manager module.

Eight types of Messages are currently defined that must be implemented as classes or structures
(depending on implementation language):

- **NegotiateConnection**

- **NegotiateConnectionResponse**

- **Request**
- **Unsubscribe**
- **Response**
- **Ack**
- **RegisterCompoundMethod**
- **UnregisterCompoundMethod**

Please refer to Nulstar - Documentation - Message Protocol document for specific field details.

Packets received should be decoded and processed depending on the Message type:

• NegotiateConnection: The module should send back a Message of type
NegotiateConnectionResponse, the filed NegotiationStatus should be set to “1” if the protocol is
compatible and if it is able to send compressed packets with the specified compression level using
zlib algorithm, “0” otherwise. This message type could be extended in the future with user
authentication mechanism.

• NegotiateConnectionResponse: When the module receives a Message of this type, it should check
the NegotiateConnection field, and send a Log Request to Storage module (See section 3.1.12 for
further details). If negotiation is successful then the connection must be tagged as such so further
requests/responses could be processed, otherwise 2 more tries with 10 second interval must be
performed, if these tries fail then it must report to the Manager that the module can’t operate
normally.

• Request: This message should be decoded and the module must process the methods specified in
the RequestMethods array field with their respective parameters. A Response Message should be
crafted with the required specific information. If one method fails then the Response should be
considered unsuccessful as a whole even if some methods processed successfully. If Event or
Period intervals are declared, methods should be processed again resulting in a new Response
Message at each Event/Period.

• Response: How to process this message is defined by each module, if no more Responses are
expected then PendingMessages queue should eliminate the respective entry (See section 3.1.6
for further details)

• Notification: How to process this message is defined by each module.

• RegisterCompoundMethod: The module should be able to create a new virtual method with the
specified name and parameter aliases, then an API Registration Request should be sent to the
Manager module to add the virtual function (Check 3.1.10 for information about crafting such
request)

• UnregisterRegisterCompoundMethod: The module should be able to remove the specified virtual
method, then an API Registration Request should be sent to the Manager module to add the virtual
function (Check 3.1.10 for information about crafting such request).