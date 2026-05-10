import sqlite3

DB_NAME = "news.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE,
            source TEXT,
            date TEXT,
            url TEXT
        )
    ''')

    conn.commit()
    conn.close()



def insert_news(news_list):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for news in news_list:
        try:
            cursor.execute('''
                INSERT INTO news (title, source, date, url)
                VALUES (?, ?, ?, ?)
            ''', (
                news['title'],
                news['source'],
                news['date'],
                news['url']
            ))
        except:
            pass

    conn.commit()
    conn.close()



def get_news(keyword=None, source=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = "SELECT title, source, date, url FROM news WHERE 1=1"

    params = []

    if keyword:
        query += " AND title LIKE ?"
        params.append(f"%{keyword}%")

    if source:
        query += " AND source LIKE ?"
        params.append(f"%{source}%")

    cursor.execute(query, params)

    data = cursor.fetchall()

    conn.close()

    return data