import database
import import_data
import query_data
def main():
    print("1.初始化数据库")
    print("2.查询股票数据")
    choice=input("请选择：")
    if choice=="1":
        database.create_tables()
        import_data.import_stock_info(import_data.stockIfomation_data)
        import_data.import_stock_data(import_data.codes,"20250101","20251231")
    elif choice=="2":
        df=query_data.get_all_stocks()
        stock_code="600519.SH"
        stock_rows=query_data.get_stock_data(stock_code)
        for row in stock_rows:
            print(row)
        industry="白酒"
        industry_rows=query_data.get_industry_stocks(industry)
        for row in industry_rows:
            print(row)
        peiod_stock_rows=query_data.get_stock_data_by_date("600519.SH","20250101","20250131")
        for row in peiod_stock_rows:
            print(row)
if __name__ == "__main__":
    main()
