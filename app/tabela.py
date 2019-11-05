import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE contatos (
        id INTEGER NOT NULL PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    );
""")



print('Tabela criada')
conn.close()