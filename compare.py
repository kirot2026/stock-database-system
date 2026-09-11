import pandas as pd 
def compare_stocks(df):
    stock_list=[]
    returns_list=[]
    volatility_list=[]
    max_increase_list=[]
    max_decline_list=[]
    max_drawdown_list=[]
    for stock,group in df.groupby('stock'):
        stock_list.append(stock)
        returns=float(((group.iloc[-1]['close']-group.iloc[0]['close'])/group.iloc[0]['close'])*100)
        volatility=float(group['pct_change'].std())
        max_increase=float(group['pct_change'].max())
        max_decline=float(group['pct_change'].min())
        group['highest_point']=group['close'].cummax()
        max_drawdown=float((((group['close']-group['highest_point'])/group['highest_point']).min())*100)
        returns_list.append(returns)
        volatility_list.append(volatility)
        max_increase_list.append(max_increase)
        max_decline_list.append(max_decline)
        max_drawdown_list.append(max_drawdown)
    df=pd.DataFrame({'股票':stock_list,'区间收益率':returns_list,'最大涨幅':max_increase_list,'最大跌幅':max_decline_list,'波动率':volatility_list,'最大回撤':max_drawdown_list})
    df=df.sort_values('区间收益率',ascending=False)
    df['区间收益率排名']=range(1,len(df)+1)
    df=df.sort_values('波动率',ascending=False)
    df['区间波动率排名']=range(1,len(df)+1)
    df=df[['股票','区间收益率','最大涨幅','最大跌幅','波动率','最大回撤','区间收益率排名','区间波动率排名']]
    results=df.to_dict('records')
    print(df.to_string(formatters={"区间收益率":"{:}%".format,"最大涨幅":"{:}%".format,"最大跌幅":"{:}%".format,"波动率":"{:}%".format,"最大回撤":"{:}%".format}))
    return df,results