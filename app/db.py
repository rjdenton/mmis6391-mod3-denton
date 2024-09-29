import mysql.connector
from mysql.connector import Error

def get_db_connection():
    db_config = {
        'user': 'phk51m847pg19v0w',
        'password': 'wdvedu7x318sbqzo',
        'host': 'arfo8ynm6olw6vpn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
        'database': 'tpobmwnvw9nqjzlz'
    }
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            return conn
        else:
            raise Exception("Failed to connect to the database")
    except Error as e:
        print(f"Error: {e}")
        return None
