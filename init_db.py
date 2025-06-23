import sqlite3

conn = sqlite3.connect('livros.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL
)
''')

conn.commit()
conn.close()