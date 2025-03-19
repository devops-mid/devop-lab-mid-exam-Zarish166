from flask import request, redirect
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
