# models/database.py - Database Handling
import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Create users table with a phone number column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Run DB setup
init_db()

# routes/submit.py - Handling Form Submission
from flask import request
import sqlite3

def submit_user():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO users (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    conn.close()

    return "User added successfully!"

# app.py - Main Flask App
from flask import Flask, render_template
from routes.submit import submit_user

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    return submit_user()

if __name__ == '__main__':
    app.run(debug=True)
