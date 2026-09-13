import pandas as pd 
def industry_analysis(df):
    industry_name=df["industry"].iloc[0]
    stock_num=df["code"].nunique()
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
    industry_info={"行业名称":industry_name,"股票数量":stock_num,"股票列表":stock_list}
    result_df=pd.DataFrame({'股票':stock_list,'区间收益率':returns_list,'最大涨幅':max_increase_list,'最大跌幅':max_decline_list,'波动率':volatility_list,'最大回撤':max_drawdown_list})
    result_df=result_df.sort_values('区间收益率',ascending=False)
    best_returns_stock=result_df["股票"].iloc[0]
    result_df['区间收益率排名']=range(1,len(result_df)+1)
    result_df=result_df.sort_values('波动率',ascending=False)
    result_df['波动率排名']=range(1,len(result_df)+1)
    result_df=result_df[['股票','区间收益率','最大涨幅','最大跌幅','波动率','最大回撤','区间收益率排名','波动率排名']]
    avg_returns=float(result_df["区间收益率"].mean())
    avg_volatility=float(result_df["波动率"].mean())
    industry_summary={"平均收益率":avg_returns,"平均波动率":avg_volatility,"收益率最佳股票":best_returns_stock}
    results={"行业基础信息":industry_info,"行业整体表现":industry_summary}
    print(result_df.to_string(formatters={"区间收益率":"{:}%".format,"最大涨幅":"{:}%".format,"最大跌幅":"{:}%".format,"波动率":"{:}%".format,"最大回撤":"{:}%".format}))
    return result_df,results