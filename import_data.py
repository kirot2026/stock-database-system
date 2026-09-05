import sqlite3
import database
import pandas as pd 
import tushare as ts
from config import TOKEN
ts.set_token(TOKEN) 
pro = ts.pro_api()
codes = ['600519.SH','000858.SZ','300750.SZ','600036.SH','000001.SZ']
def import_stock_data(codes,start_date,end_date):
    conn=database.get_connection()
    data_list = []
    for code in codes:
        df = pro.daily(ts_code=code,start_date=start_date,end_date=end_date)
        data_list.append(df)
    df = pd.concat(data_list, ignore_index=True)
    df=df.rename(columns={"ts_code":"code","trade_date":"date","pct_chg":"pct_change","vol":"volume"})
    df=df.sort_values(['code','date'],ascending=[True,True])
    df.to_sql("stock_daily",conn,if_exists="append",index=False)
    conn.close()

stockIfomation_data = [("600519.SH","贵州茅台","白酒"),
               ("000858.SZ", "五粮液","白酒"),
               ("300750.SZ","宁德时代","新能源"),
               ("600036.SH","招商银行","银行"),
               ("000001.SZ","平安银行","银行")]
def import_stock_info(stockIfomation_data):
    conn=database.get_connection()
    cursor = conn.cursor()
    cursor.executemany('''INSERT OR IGNORE INTO stock_info (code,stock,industry) VALUES (?, ?, ?)''',stockIfomation_data)
    conn.commit()
    conn.close()
