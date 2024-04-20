import psycopg2
import os

def connectToDB():
    connect = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_LOGIN'),
        password=os.environ.get('DB_PASSWORD'),
    )
    
    return connect
