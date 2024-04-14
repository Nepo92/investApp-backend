import psycopg2
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from schema import schema
from dotenv import load_dotenv

load_dotenv()


print(os.environ.get('DB_HOST'))

def connect_to_db():
    connection = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_LOGIN'),
        password=os.environ.get('DB_PASSWORD'),
    )
    print("connect to the database")
    connection.close()


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/graphql':
            print('graphql')

    def do_POST(self):
        if self.path == '/graphql':
            query = """{
                hello
            }"""

            print(schema.execute(query).data)

def run(server_class=HTTPServer, handler_class=HTTPRequestHandler):
    server_address = (os.environ.get('APP_HOST'), 80)
    httpd = server_class(server_address, handler_class)
    print('stated server')
    httpd.serve_forever()

run()