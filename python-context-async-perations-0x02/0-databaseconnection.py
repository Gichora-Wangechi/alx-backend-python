import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


# Usage
with DatabaseConnection("users.db") as cursor:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
