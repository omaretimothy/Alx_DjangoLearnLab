import mysql.connector

connection = None
cursor = None

try:
    # Connect to MySQL Server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''  # Leave blank if no password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if connection and connection.is_connected():
        if cursor:
            cursor.close()
        connection.close()
        print("MySQL connection is closed.")
