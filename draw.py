import matplotlib.pyplot as plt 
import pandas as pd
import mplfinance as mpf

def draw(df):
    plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.scatter(df['波动率'],df['区间收益率'])
    for i, row in df.iterrows():
        plt.text(row['波动率'],row['区间收益率'],row['股票'])
    plt.title('股票区间收益率比较图')
    plt.xlabel('波动率(%)')
    plt.ylabel('区间收益率(%)')
    plt.show()

def calculate_RSI(df,period=14):
    delta = df['close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    average_gain=gain.ewm(alpha=1/period,adjust=False,min_periods=period).mean()
    average_loss=loss.ewm(alpha=1/period,adjust=False,min_periods=period).mean()
    RS=average_gain/average_loss.replace(0, float('inf'))
    RSI=100-(100/(1+RS))
    return RSI

def draw_candle(df):
    df=df[["date","open","high","low","close","volume"]]
    df['date']=pd.to_datetime(df['date'])
    df=df.set_index('date')
    df['RSI']=calculate_RSI(df)
    ap=mpf.make_addplot(df['RSI'],panel=2,color='purple',ylabel='RSI')
    mpf.plot(df,type='candle',volume=True,mav=(5,20),figsize=(14,6),addplot=[ap],style='yahoo')
    
 