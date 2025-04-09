import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Add multiple users
users = [
    ('ansu', 'ansu1234'),
    ('sai', 'sai1234'),
    ('vasu', 'vasu1234'),
    ('myt', 'myt1234'),
]

for username, password in users:
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        print(f"User '{username}' added.")
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")

conn.commit()
conn.close()
