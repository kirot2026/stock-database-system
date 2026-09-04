import sqlite3
import pandas as pd 
import tushare as ts
from config import TOKEN
ts.set_token(TOKEN) 
pro = ts.pro_api()
codes = ['600519.SH','000858.SZ','300750.SZ','600036.SH','000001.SZ']
data_list = []
for code in codes:
    df = pro.daily(ts_code=code,start_date='20250101',end_date='20251231')
    data_list.append(df)
df = pd.concat(data_list, ignore_index=True)
df=df.rename(columns={"ts_code":"code","trade_date":"date","pct_chg":"pct_change","vol":"volume"})
df=df.sort_values(['code','date'],ascending=[True,True])
conn = sqlite3.connect('stock_database.db')
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
    volume INTEGER,                               
    amount INTEGER,
    PRIMARY KEY (code,date))''')
conn.commit()
df.to_sql("stock_daily",conn,if_exists="append",index=False)
conn.close()
