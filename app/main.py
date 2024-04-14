import os
from http.server import HTTPServer, BaseHTTPRequestHandler

from dotenv import load_dotenv

load_dotenv()

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/graphql':
            print('graphql')

    def do_POST(self):
        if self.path == '/graphql':
            print('graphql')

def run(server_class=HTTPServer, handler_class=HTTPRequestHandler):
    server_address = (os.environ.get('APP_HOST'), 80)
    httpd = server_class(server_address, handler_class)
    print('stated server')
    httpd.serve_forever()

run()