import sqlite3
import pandas as pd 
import database
def get_all_stocks():
    conn=database.get_connection()
    df=pd.read_sql('''SELECT stock_daily.code,
                   stock_info.stock,stock_info.industry,
                   stock_daily.date,stock_daily.open,
                   stock_daily.high,stock_daily.low,
                   stock_daily.close,stock_daily.pre_close,
                   stock_daily.change,stock_daily.pct_change,
                   stock_daily.volume,stock_daily.amount
               FROM stock_daily 
               JOIN stock_info 
               ON stock_daily.code=stock_info.code''',conn)
    conn.close()
    return df

def get_stock_data(stock_code):
    conn=database.get_connection()
    placeholders = ','.join(['?'] * len(stock_code))
    sql=f'''SELECT stock_daily.code,
                   stock_info.stock,stock_info.industry,
                   stock_daily.date,stock_daily.open,
                   stock_daily.high,stock_daily.low,
                   stock_daily.close,stock_daily.pre_close,
                   stock_daily.change,stock_daily.pct_change,
                   stock_daily.volume,stock_daily.amount
                   FROM stock_daily 
                   JOIN stock_info 
               ON stock_daily.code=stock_info.code 
               WHERE stock_daily.code IN ({placeholders})'''
    df=pd.read_sql(sql,conn,params=tuple(stock_code))
    conn.close()
    return df

def get_industry_stocks(industry):
    conn=database.get_connection()
    df=pd.read_sql('''SELECT stock_daily.code,
                   stock_info.stock,stock_info.industry,
                   stock_daily.date,stock_daily.open,
                   stock_daily.high,stock_daily.low,
                   stock_daily.close,stock_daily.pre_close,
                   stock_daily.change,stock_daily.pct_change,
                   stock_daily.volume,stock_daily.amount
                   FROM stock_daily 
                   JOIN stock_info 
               ON stock_daily.code=stock_info.code 
               WHERE stock_info.industry=?''',conn,params=(industry,))
    conn.close()
    return df

def get_stock_data_by_date(code,start_date,end_date):
    conn=database.get_connection()
    df=pd.read_sql('''SELECT stock_daily.code,
                   stock_info.stock,stock_info.industry,
                   stock_daily.date,stock_daily.open,
                   stock_daily.high,stock_daily.low,
                   stock_daily.close,stock_daily.pre_close,
                   stock_daily.change,stock_daily.pct_change,
                   stock_daily.volume,stock_daily.amount
                   FROM stock_daily 
                   JOIN stock_info 
               ON stock_daily.code=stock_info.code 
               WHERE stock_daily.code=? AND stock_daily.date BETWEEN ? AND ?''',conn,params=(code,start_date,end_date))
    conn.close()
    return df