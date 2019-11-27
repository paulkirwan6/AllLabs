from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer as S


class S(BaseHTTPRequestHandler):
	def set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		self.set_headers()
		self.wfile.write("<html><body><h1>hello</h1><p>Smaller</p></body></html>")

def run(server_class=HTTPServer, handler_class=S, port=8000):
	server_address = ('',port)
	print 'Starting server'
	httpd = server_class(server_address, handler_class)
	print 'Server up'
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()
