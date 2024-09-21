import sqlite3


conn = sqlite3.connect('mydatabase.db')

sql = conn.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER,name TEXT, age INTEGER, grade TEXT);')
sql.execute('INSERT INTO students VALUES (1, "Pavel", 18, "A");')
sql.execute('INSERT INTO students VALUES (2, "Sasha", 17, "A");')
sql.execute('INSERT INTO students VALUES (3, "Mihail", 19, "C");')
sql.execute('INSERT INTO students VALUES (4, "Vladimir", 20, "B");')
conn.commit()


def get_student_by_name(name):
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()

    cursor.execute('SELECT name, age, grade FROM students WHERE name = ?', (name,))

    student = cursor.fetchone()
    connection.close()

    return student if student else None


def get_student_name(name):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM students WHERE name = '{name}'")
    student = cursor.fetchone()
    conn.close()
    return student


def update_student_grade(name, new_grade):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE students SET grade = '{new_grade}' WHERE name = '{name}'")
    conn.commit()
    conn.close()


def delete_student(name):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM students WHERE name = '{name}'")
    conn.commit()
    conn.close()