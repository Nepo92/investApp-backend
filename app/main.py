import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from schema import user

import json

from dotenv import load_dotenv

load_dotenv()

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
    def do_POST(self):        
        if self.path == '/graphql':
            try: 
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                result = user.user_schema.execute(data['query'])

                json_string = json.dumps(result.data)
                print(json_string)

                data = bytes(json_string, encoding='utf-8')

                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(json_string))
                self.end_headers()

                self.wfile.write(data)
            except Exception as error:
                print(error)
                self.send_response(400)

def run(server_class=HTTPServer, handler_class=HTTPRequestHandler):
    server_address = (os.environ.get('APP_HOST'), 80)
    httpd = server_class(server_address, handler_class)
    print('stated server')
    httpd.serve_forever()

run()