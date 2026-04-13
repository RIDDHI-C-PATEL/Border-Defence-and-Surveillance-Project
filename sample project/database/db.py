import sqlite3

conn = sqlite3.connect("database/border.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts(
id INTEGER PRIMARY KEY AUTOINCREMENT,
type TEXT,
location TEXT,
confidence REAL
)
""")

conn.commit()
conn.close()

print("Database Created")