import sqlite3
import os

def create_users_table():
    os.makedirs("app_db", exist_ok=True)

    conn = sqlite3.connect("app_db/users.db")
    c = conn.cursor()

    # Users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)

    # Video info table
    c.execute("""
        CREATE TABLE IF NOT EXISTS video_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            upload_path TEXT,
            download_path TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    """)

    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect("app_db/users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect("app_db/users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    conn.close()
    return result

def save_video_log(username, upload_path, download_path):
    conn = sqlite3.connect("app_db/users.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO video_logs (username, upload_path, download_path)
        VALUES (?, ?, ?)
    """, (username, upload_path, download_path))
    conn.commit()
    conn.close()

def get_video_logs(username):
    conn = sqlite3.connect("app_db/users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM video_logs WHERE username = ?", (username,))
    logs = c.fetchall()
    conn.close()
    return logs