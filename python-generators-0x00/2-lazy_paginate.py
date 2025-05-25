#!/usr/bin/env python3
import mysql.connector

def lazy_paginate(page_size=10):
    """Yields pages of user data from the database."""
    connection = mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="your_mysql_password",
        database="ALX_prodev"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")

    while True:
        rows = cursor.fetchmany(size=page_size)
        if not rows:
            break
        yield rows

    cursor.close()
    connection.close()
