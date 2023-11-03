import psycopg2
#from decouple import config

DB_HOST='localhost'
DB_USER='root'
DB_PASSWORD='root'
DB_PORT="5432"

def DBConnection(database):
    source_host = DB_HOST
    source_port = DB_PORT
    source_database = database
    source_user = DB_USER
    source_password = DB_PASSWORD
    source_connection = psycopg2.connect(
        host=source_host,
        port=source_port,
        database=source_database,
        user=source_user,
        password=source_password
        )
    return source_connection