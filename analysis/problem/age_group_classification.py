from utils.db import load_table
import pandas as pd
# '나이' 구간을 기준으로 나이대를 분류해볼까요 ?
# 30대 이하
# 30~50대
# 50~70대
# 70대 이상


def run ():
  df = load_table()
  bins = [0 ,30, 50, 70, float("inf")]
  labels =["30대 이하", "30~50대", "50~70대", "70대 이상"]
  df["Age_Group"] = pd.cut(df["age"], bins=bins, labels=labels, right=True)
  print(df[["age", "Age_Group"]].head(10))






if __name__ == "__main__":
    run()
