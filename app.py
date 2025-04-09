from flask import Flask, render_template, request, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecret'

def check_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_user(username, password):
            return f"Welcome, {username}!"
        else:
            flash('Invalid username or password')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
