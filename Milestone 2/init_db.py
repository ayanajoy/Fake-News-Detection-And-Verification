import sqlite3

conn = sqlite3.connect("nlp.db")
cur = conn.cursor()


cur.execute("""
        CREATE TABLE processed_text(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_text TEXT,
            cleaned_text TEXT
        )
""")

cur.execute("""
        CREATE TABLE entities(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_id INTEGER,
            entity TEXT,
            entity_type TEXT
        )
""")

conn.commit()
conn.close()

print("Database Created Successfully")