import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="inventory@212427",
        database="inventory_db"
    )

    print("MySQL Connection Successful!")

    conn.close()

except Exception as e:
    print("MySQL Connection Failed!")
    print(e)