
const http = require('http');
const static = require('node-static');
const file = new static.Server('./');
const server = http.createServer((req, res) => {
  req.addListener('end', () => file.serve(req, res)).resume();
});
const port = 9001;
server.listen(port, () => console.log(`Server running at http://localhost:${port}`));

server.on('upgrade', (req, socket) => {
// Make sure that we only handle WebSocket upgrade requests
if (req.headers['upgrade'] !== 'websocket') {
  socket.end('HTTP/1.1 400 Bad Request');
  return;
}
});








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
