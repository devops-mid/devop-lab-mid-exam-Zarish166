import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    ALTER TABLE users ADD COLUMN phone TEXT;
''')

conn.commit()
conn.close()

