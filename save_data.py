import json
def save_json(dict,filename):
    with open(filename,'w')as f:
        json.dump(dict,f,ensure_ascii=False,indent=4)

def save_or_print(filename,dict):
    chioce=input("请选择是否保存数据(是:y,否:n):")
    if chioce=="y":
        save_json(dict,filename)
    else:
        print("\n========== 分析结果 ==========")
        for category, values in dict.items():
            print(f"\n【{category}】")
            for key, value in values.items():
                print(f"{key}：{value}")
        print("=" * 30)


