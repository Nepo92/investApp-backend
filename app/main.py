import psycopg2
from http.server import HTTPServer, BaseHTTPRequestHandler
from config import host, user, password, db_name

def connect_to_db():
    try:
        connection = psycopg2.connect(host=host, user=user, password=password, dbname=db_name)
        print('connected')
    except:
        print("I am unable to connect to the database")
    finally:
        if connection:
            connection.close()
            print("Database connection closed")

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            print('connected')
        

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('localhost', 4000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


connect_to_db()
run()