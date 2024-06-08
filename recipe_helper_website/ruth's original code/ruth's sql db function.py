import mysql.connector


def connect_db():
    conn = mysql.connector.connect(
        host='localhost',  # Need to update the DB details
        user='your_username',
        password='your_password',
        database='your_database'
    )
    return conn
