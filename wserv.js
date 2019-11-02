

const WebSocket = require('ws');
const ws = new WebSocket.Server({ port: 9003 });
console.log("serving on port 9003.")
 
ws.on('connection', function connection(ws) {
	  ws.on('message', function incoming(message) {
		console.log('received: %s', message);
		ws.send(message);
		    });
	 
});




