sconst http = require('http');
const pcap = require('pcap');

const server = http.createServer((req, res) => {
  console.log('Incoming request');
  // handle incoming request
});

server.listen(8080, () => {
  console.log('Server started on port 3000');
});
