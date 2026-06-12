import sqlite3
import os

DB_FOLDER = "database"
DB_NAME = "payroll.db"
DB_PATH = os.path.join(DB_FOLDER, DB_NAME)


def create_database():
    """
    Create database and employee table if not exists.
    """

    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        designation TEXT NOT NULL,
        pay_level INTEGER NOT NULL,
        basic_pay REAL NOT NULL,
        hra REAL NOT NULL,
        ta REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_employee(name, department, designation,
                 pay_level, basic_pay, hra, ta):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees
    (name, department, designation, pay_level,
     basic_pay, hra, ta)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        department,
        designation,
        pay_level,
        basic_pay,
        hra,
        ta
    ))

    conn.commit()
    conn.close()


def get_all_employees():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_employee(emp_id):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE emp_id=?",
        (emp_id,)
    )

    employee = cursor.fetchone()

    conn.close()

    return employee


def update_employee(emp_id,
                    name,
                    department,
                    designation,
                    pay_level,
                    basic_pay,
                    hra,
                    ta):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE employees
    SET name=?,
        department=?,
        designation=?,
        pay_level=?,
        basic_pay=?,
        hra=?,
        ta=?
    WHERE emp_id=?
    """, (
        name,
        department,
        designation,
        pay_level,
        basic_pay,
        hra,
        ta,
        emp_id
    ))

    conn.commit()
    conn.close()


def delete_employee(emp_id):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE emp_id=?",
        (emp_id,)
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully.")