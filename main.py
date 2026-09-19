import database
import import_data
import query_data
import compare
import single_analysis
import industry_analysis
import draw
import save_data
def initialize_database():
    database.create_tables()
    import_data.import_stock_info(import_data.stockIfomation_data)
    import_data.import_stock_data(import_data.codes,"20250101","20251231")
   
def input_date(prompt):
    while True:
        date = input(prompt).strip()
        if len(date) == 8 and date.isdigit():
            return date
        print("日期格式错误,请输入YYYYMMDD")

def main():
    print("="*20)
    print("股票数据分析数据库")
    print("="*20)
    while True:
          print("1.初始化数据库\n2.查询股票基本信息\n3.分析单只股票\n4.比较多只股票\n5.行业股票分析\n6.退出")
          num=input("请输入操作：")
          if num=="1":
            initialize_database()
          elif num=="2":
               df=query_data.get_stock_info()
               print(df)
          elif num=="3":
              code=input("请输入股票代码：")
              start_date=input_date("请输入起始日期：")
              end_date=input_date("请输入终止日期：")
              df=query_data.get_stock_data_by_date(code,start_date,end_date)
              if df.empty:
                 print("没有找到符合条件的数据")
                 continue
              single_analysis_results=single_analysis.analyze_stock(df)
              draw.draw_candle(df)
              filename="single_analysis_result.json"
              save_data.save_or_print(filename,single_analysis_results)
          elif num=="4":
              codes=input("请输入要比较的股票代码：")
              codes = [code.strip() for code in codes.split(",")]
              df=query_data.get_more_stock_data(codes)
              if df.empty:
                 print("没有找到符合条件的数据")
                 continue
              df,compare_results=compare.compare_stocks(df)
              draw.draw(df)
              filename="compare_result.json"
              save_data.save_or_print(filename,compare_results)
          elif num=="5":
              industry=input("请输入行业名称：")
              df=query_data.get_industry_stocks(industry)
              if df.empty:
                 print("没有找到符合条件的数据")
                 continue
              df,industry_results=industry_analysis.industry_analysis(df)
              draw.draw(df)
              filename="industry_result.json"
              save_data.save_or_print(filename,industry_results)
          elif num=="6":
              break
          else:
              print("请输入正确的操作序号")
    
if __name__ == "__main__":
    main()
