from http.server import HTTPServer, BaseHTTPRequestHandler
from config import host, user, password, db_name

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            print('connected')
        

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('localhost', 4000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()