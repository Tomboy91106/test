import mysql.connector #type: ignore

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='remind_me'
    )
