import sqlite3
import pandas as pd 
import database
def get_all_stocks():
    conn=database.get_connection()
    cursor = conn.cursor()
    df=pd.read_sql('''SELECT *
               FROM stock_daily 
               JOIN stock_info 
               ON stock_daily.code=stock_info.code''',conn)
    conn.close()
    return df

def get_stock_data(stock_code):
    conn=database.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock_daily WHERE code=?",(stock_code,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_industry_stocks(industry):
    conn=database.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock_info WHERE industry=?",(industry,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_stock_data_by_date(code,start_date,end_date):
    conn=database.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock_daily WHERE code=? AND date BETWEEN ? AND ?",(code,start_date,end_date))
    rows = cursor.fetchall()
    conn.close()
    return rows