from matplotlib import pyplot as plt
import pandas as pd
from novel_spider import main
import os
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["font.sans-serif"] = ['SimHei']
# run spider
if os.path.exists('qidian.csv') != True:
    main()

def Main():
    df = pd.read_csv("qidian.csv",
    dtype={
                        "name": str,
                        "author": str,
                        "type": str,
                        "status": str,
                        "month_ticket": int,
                        "week_ticket": int,
                        "reward_num": int,
                        "description": str,
                        "update_time": str,
                        "count_words": float,
                        "recommend_num": float
                        },encoding='utf_8'
                    )
    print(df.head())
    print(df.describe().T)
    df.info()

    # 画出各个类型的小说数量占比的饼图
    type_count = df["type"].value_counts()
    plt.figure(figsize=(5, 5))
    plt.pie(type_count, labels=type_count.index, autopct='%1.1f%%')
    plt.title("各類型的小說數量佔比")
    plt.show()

    # 画出各个类型的小说月票和周票总数
    df.groupby("type")[["month_ticket", "week_ticket"]].sum().sort_values("month_ticket", ascending=False).plot(kind="bar")
    plt.yscale("log")
    plt.title("各類型的小說月票和周票總數")
    plt.show()

    # 画出月票和周票散点图，不同的颜色代表不同的类型
    plt.figure(figsize=(10, 6))
    for name, group in df.groupby("type"):
        plt.scatter(group["month_ticket"], group["week_ticket"], label=name)
    plt.xlabel("月票")
    plt.ylabel("周票")
    plt.legend()
    plt.yscale("log")
    plt.xscale("log")
    plt.title("月票和周票散點圖")

    plt.show()

    # 画出推荐人数和字数的散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(df["recommend_num"], df["count_words"])
    plt.xlabel("推薦人數")
    plt.ylabel("字數（萬）")
    plt.title("推薦人數和字數的散佈圖")
    plt.show()

    # 画出推荐人数和周票的散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(df["recommend_num"], df["week_ticket"])
    plt.xlabel("推荐人数（万）")
    plt.ylabel("周票")
    # plt.yscale("log")
    plt.title("推荐人数和周票的散点图")
    plt.show()

if __name__ == "__main__":
    Main()