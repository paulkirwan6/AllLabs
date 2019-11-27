from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer as S
import datetime ##for current dynamic current time 

import cgi
import socket
import subprocess

dev_name= socket.gethostname()
class S(BaseHTTPRequestHandler):
	def set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		self.set_headers()
		self.wfile.write(
		"<html>"\
                "<body>"\
                "<h1>Hello from " + dev_name  + " </h1>"\
		"<form method = \"POST\">"\
			"<label>Device name: </label>"\
			"<input type=\"text\" name=\"dev_name\">"\
			"<input type=\"submit\">"\
			"<input type=\"submit\" name=\"reboot\" value=\"Reboot\">"
                "</body>"\
                "</html>")

	def do_POST(self):
		length = int(self.headers.getheader('content-length'))
		postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
		dev_name=postvars['dev_name'][0]
	##	subprocess.call([socket.gethostname, "Rename-Computer - lakfjdlkjaf"])
		
		self.set_headers()

		if 'reboot' in postvars.keys():
			print("Rebooting...")
			subprocess.call("reboot", shell=True)
		else:
			self.wfile.write("<html><body>Thanks! My new device name is "\
			"<b>" + dev_name + "</b>"\
			"</body></html>")

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

