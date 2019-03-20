import sqlite3


class Database:

    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE employees (
                     first_name test,
                     last_name text,
                     email text,
                     age integer
                )""")

    def insert(self, row):
        self.c.execute("INSERT INTO employees VALUES(:first_name, :last_name, :email, :age)",
                      {'first_name': row[0], 'last_name': row[1], 'email': row[2], 'age': row[3]})
        self.conn.commit()

    def fetchAll(self):
        self.c.execute("SELECT * FROM employees")
        print(self.c.fetchall())

    def count(self):
        self.c.execute("SELECT COUNT(*) FROM employees")
        return self.c.fetchone()[0]

    def close(self):
        self.conn.close()
