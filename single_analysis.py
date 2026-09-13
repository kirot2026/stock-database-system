import pandas as pd 
def analyze_stock(df):
    code=df["code"][0]
    name=df["stock"][0]
    industry=df["industry"][0]
    start_date=df["date"].iloc[0]
    end_date=df["date"].iloc[-1]
    trate_date=len(df)
    basic_info={"股票代码":code,"股票名称":name,"所属行业":industry,"起始日期":start_date,"终止日期":end_date,"交易天数":trate_date}
    max_close=df["close"].max()
    min_close=df["close"].min()
    avg_close=df["close"].mean()
    latest_close=df["close"].iloc[-1]
    price_info={"最高收盘价":max_close,"最低收盘价":min_close,"平均收盘价":avg_close,"最新收盘价":latest_close}
    returns=df['close'].iloc[-1]/df['close'].iloc[0]-1
    i=0
    j=0
    for change in df['change']:
        if change>0:
           i=i+1
        elif change<0:
           j=j+1
    change_info={}
    change_info["区间收益率"]=float(returns)
    change_info["上涨天数"]=int(i)
    change_info["下跌天数"]=int(j)
    change_info["最大单日上涨"]=float(df['change'].max())
    change_info["最大单日下跌"]=float(df['change'].min())
    volatility=float(df['pct_change'].std())
    df['highest_point']=df['close'].cummax()
    max_drawdown=float((((df['close']-df['highest_point'])/df['highest_point']).min())*100)
    risk_info={"波动率":volatility,"最大回撤":max_drawdown}
    results={"基础信息":basic_info,"价格信息":price_info,"涨跌情况":change_info,"风险指标":risk_info}
    return results