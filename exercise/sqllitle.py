import sqlite3
from employee import Employee

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('employee.db')

c = conn.cursor()

#c.execute("""CREATE TABLE employees (
#             fist test,
#             last text,
#             pay integer
#            )""")

#c.execute("INSERT INTO employees VALUES('Corey', 'Smith', 1000)")
#conn.commit()

emp_1 = Employee('John1', 'Doe1', 11)

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES(:first, :last, :pay)", {'first':emp.first, 'last':emp.last, 'pay':emp.pay})


insert_emp(emp_1)

#print(emp_1.first)

#c.execute("INSERT INTO employees VALUES('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))

#c.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

c.execute("INSERT INTO employees VALUES(:first, :last, :pay)", {'first':emp_1.first, 'last':emp_1.last, 'pay':emp_1.pay})


c.execute("SELECT * FROM employees")


print(c.fetchall())

conn.commit()

conn.close()


