#!/usr/bin/env python3
import mysql.connector

def stream_ages():
    """Generator that yields ages of all users in the database."""
    connection = mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="your_mysql_password",
        database="ALX_prodev"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:
        yield float(age)

    cursor.close()
    connection.close()
