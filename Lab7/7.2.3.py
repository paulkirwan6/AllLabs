from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import codecs
import json
# from sense_hat import SenseHat

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_GET(self):
        self._set_headers()
        # Write your response message here:
        # sense = SenseHat()
        # temperature = round(sense.get_temperature(), 4)
        # humidity = round(sense.get_humidity(), 4)
        temperature = 100
        humidity = 12   
        f=codecs.open("test7.2.2.html", 'r').read().format(temp=temperature, hum=humidity)
        
        
	f = { "temperature": temperature,"humidity":  humidity };
	d =json.dumps(f)
	self.wfile.write(d)

def run(server_class=HTTPServer, handler_class=S, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()