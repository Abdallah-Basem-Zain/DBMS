import mysql.connector

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='courses'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
