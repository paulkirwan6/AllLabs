from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import codecs
from sense_hat import SenseHat


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'HTML')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        # Write your response message here:
        sense = SenseHat()
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        # temperature = 100
        # humidity = 12     
        f=codecs.open("test7.2.2.html", 'r').read().format(temp=temperature, hum=humidity)
        self.wfile.write(f)



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
