import psycopg2

def connect_database():
    conn = psycopg2.connect(database="wms", user='postgres', password='postgres', host='127.0.0.1', port= '5432')
    return conn