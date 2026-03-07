import sqlite3

def init_db():
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news_text TEXT,
            prediction TEXT,
            confidence REAL
        )
    """)

    conn.commit()
    conn.close()

def save_result(news, prediction, confidence):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO news_results (news_text, prediction, confidence)
        VALUES (?, ?, ?)
    """, (news, prediction, confidence))

    conn.commit()
    conn.close()