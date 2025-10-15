import sqlite3

def init_db():
    conn = sqlite3.connect('sessions.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sessions
                      (session_id TEXT PRIMARY KEY, history TEXT)''')
    conn.commit()
    conn.close()

def get_history(session_id):
    conn = sqlite3.connect('sessions.db')
    cursor = conn.cursor()
    cursor.execute("SELECT history FROM sessions WHERE session_id=?", (session_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else ""

def update_history(session_id, history):
    conn = sqlite3.connect('sessions.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO sessions (session_id, history) VALUES (?, ?)", (session_id, history))
    conn.commit()
    conn.close()