import sqlite3
from config import DB_NAME
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_tables():
    conn=get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS stock_daily (
    code TEXT,
    date TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    pre_close REAL,
    change REAL,
    pct_change REAL,
    volume REAL,                               
    amount REAL,
    PRIMARY KEY (code,date))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS stock_info (
    code TEXT PRIMARY KEY ,
    stock TEXT,
    industry TEXT)''')
    conn.commit()
    conn.close()