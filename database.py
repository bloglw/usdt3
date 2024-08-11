import sqlite3
from config import database_path

def init_db():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            address TEXT NOT NULL,
            private_key TEXT NOT NULL,
            balance REAL DEFAULT 0,
            available_balance REAL DEFAULT 0,
            frozen_balance REAL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_user(user_id, address, private_key):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (user_id, address, private_key) VALUES (?, ?, ?)', (user_id, address, private_key))
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_balance(user_id, balance):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET balance=? WHERE user_id=?', (balance, user_id))
    conn.commit()
    conn.close()

def update_available_balance(user_id, amount):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET available_balance = available_balance + ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

if __name__ == '__main__':
    init_db()
