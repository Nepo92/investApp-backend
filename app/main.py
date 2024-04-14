import psycopg2
from http.server import HTTPServer, BaseHTTPRequestHandler
from config import host, user, password, db_name

def connect_to_db():
    psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    print("connect to the database")


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            connect_to_db()

def run(server_class=HTTPServer, handler_class=HTTPRequestHandler):
    server_address = ('0.0.0.0', 80)
    httpd = server_class(server_address, handler_class)
    print('stated server')
    httpd.serve_forever()

run()