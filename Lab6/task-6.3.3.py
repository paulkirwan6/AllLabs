from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer as S
##import picamera
import subprocess

class S(BaseHTTPRequestHandler):
	def set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.send_header('Content-type', 'image/jpg')
	        self.send_header('Refresh', '5')
		self.end_headers()

	def do_GET(self):
		self.set_headers()
		subprocess.call("raspistill -n -t 250 -o task_6_3_3_image.jpg", shell=True)
		content = open("task_6_3_3_image.jpg", 'rb')
		self.wfile.write(content.read())
##		self.wfile.write("<html><body><h1>hello</h1></body></html>")
		content.close();
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

