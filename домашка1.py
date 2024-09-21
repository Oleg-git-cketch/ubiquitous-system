import sqlite3


def create_database():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT, full_name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE, balance REAL DEFAULT 0);")
    conn.commit()
    conn.close()


def register_client(full_name, phone):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    try:
        cursor.execute(f"INSERT INTO clients (full_name, phone) VALUES ('{full_name}', '{phone}')")
        conn.commit()
    except sqlite3.IntegrityError:
        print("Ошибка: Клиент с таким номером телефона уже зарегистрирован.")
    finally:
        conn.close()


def find_client(full_name=None, phone=None):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    query = "SELECT * FROM clients WHERE 1=1"

    if full_name:
        query += f" AND full_name LIKE '%{full_name}%'"
    if phone:
        query += f" AND phone = '{phone}'"

    cursor.execute(query)
    clients = cursor.fetchall()
    conn.close()

    return clients


def deposit_balance(phone, amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE clients SET balance = balance + {amount} WHERE phone = '{phone}'")
    conn.commit()
    conn.close()


def withdraw_balance(phone, amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE clients SET balance = balance - {amount} WHERE phone = '{phone}' AND balance >= {amount}")
    conn.commit()
    conn.close()


def view_balance(phone):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT balance FROM clients WHERE phone = '{phone}'")
    balance = cursor.fetchone()
    conn.close()

    return balance[0] if balance else None


def calculate_deposit(phone, months):
    interest_rate = 0.05