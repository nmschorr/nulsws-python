// https://medium.com/@martin.sikora/node-js-websocket-simple-chat-tutorial-2def3a841b61
//"use strict";

//process.title = 'node-chat';
var http = require('http');
var websockport2 = 9002;
var websockport = 80;

var webSocketServer = require('websocket').server;

var history = [ ];
var clients = [ ];

function htmlEntities(str) {
  return String(str)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

var colors = [ 'red', 'green', 'blue', 'magenta', 'purple', 'plum', 'orange' ];

colors.sort(function(a,b) { return Math.random() > 0.5; } );

var server = http.createServer(function(request, response) {
});

server.listen(websockport, function() {
  console.log((new Date()) + " Server is listening on port "  + websockport);
});


var wsServer = new webSocketServer({  httpServer: server  });

wsServer.on('request', function(request) {
      console.log((new Date()) + ' Connection from origin '  + request.origin + '.');

      var connection = request.accept(null, request.origin);
      var index = clients.push(connection) - 1;
      var userName = false;
      var userColor = false;
      console.log((new Date()) + ' Connection accepted.');



wsServer.on('upgrade', (req, socket) => {
    // Make sure that we only handle WebSocket upgrade requests
    if (req.headers['upgrade'] !== 'websocket') {
      console.log((new Date()) + ' got upgrade request.');

      socket.end('HTTP/1.1 400 Bad Request');
      return;
    }
    });



  if (history.length > 0) {
    connection.sendUTF(
        JSON.stringify({ type: 'history', data: history} ));
  }
  connection.on('message', function(message) {
    if (message.type === 'utf8') {

    if (userName === false) {
        userName = htmlEntities(message.utf8Data);
        userColor = colors.shift();
        connection.sendUTF(
            JSON.stringify({ type:'color', data: userColor }));
        console.log((new Date()) + ' User is known as: ' + userName
                    + ' with ' + userColor + ' color.');      } else {
        console.log((new Date()) + ' Received Message from '
                    + userName + ': ' + message.utf8Data);

        var obj = {
          time: (new Date()).getTime(),
          text: message.utf8Data,
          //text: htmlEntities(message.utf8Data),
          author: userName,
          color: userColor
        };

        history.push(obj);
        history = history.slice(-100);
        var json = JSON.stringify({ type:'message', data: obj });
        for (var i=0; i < clients.length; i++) {
          clients[i].sendUTF(json);
        }
      }
    }
  });

  connection.on('close', function(connection) {
    if (userName !== false && userColor !== false) {
      console.log((new Date()) + " Peer "
          + connection.remoteAddress + " disconnected.");
      clients.splice(index, 1);
      colors.push(userColor);
    }
  });
});











//
//
//
//
//
//const http = require('http');
//const static = require('node-static');
//const file = new static.Server('./');
//const server = http.createServer((req, res) => {
//  req.addListener('end', () => file.serve(req, res)).resume();
//});
//const port = 9001;
//server.listen(port, () => console.log(`Server running at http://localhost:${port}`));
//
//server.on('upgrade', (req, socket) => {
//// Make sure that we only handle WebSocket upgrade requests
//if (req.headers['upgrade'] !== 'websocket') {
//  socket.end('HTTP/1.1 400 Bad Request');
//  return;
//}
//});
//
//
//
//
//
//
//

//
//const http = require('http');
//const crypto = require('crypto');
//const port = 9001;
//
//
//const static = require('node-static');
//const file = new static.Server('./');
//const server = http.createServer((req, res) => {
//  req.addListener('end', () => file.serve(req, res)).resume();
//});
//
//server.listen(port, () => console.log('Server running at localhost'));
//
//server.on('upgrade', function (req, socket) {
//// const protocol = req.headers['sec-websocket-protocol'];
// if (req.headers['upgrade'] !== 'websocket') {
//    socket.end('HTTP/1.1 400 Bad Request');
//    return;
//    }
//
// // const acceptKey = req.headers['sec-websocket-key']; // Generate the response value to use in the response:
//
////  const hash = generateAcceptValue(acceptKey); // Write the HTTP response into an array of response lines:
//
// // const responseHeaders = [ 'HTTP/1.1 101 Web Socket Protocol Handshake', 'Upgrade: WebSocket', 'Connection: Upgrade', `Sec-WebSocket-Accept: ${hash}` ];
//   socket.write(responseHeaders.join('\r\n') + '\r\n\r\n');
//     });
//
////const protocols = !protocol ? [] : protocol.split(',').map(s => s.trim());
////
////
//// if (protocols.includes('json')) {
////     responseHeaders.push(`Sec-WebSocket-Protocol: json`);   }
//
//function generateAcceptValue (acceptKey) {
//  return crypto
//  .createHash('sha1')
//  .update(acceptKey + '258EAFA5-E914–47DA-95CA-C5AB0DC85B11', 'binary')
//  .digest('base64');
//}
//
