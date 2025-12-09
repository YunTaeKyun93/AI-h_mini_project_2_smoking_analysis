from utils.db import load_table
import pandas as pd
def run():
    df = load_table()

    print("===== [5] 나이대 vs 흡연율 =====")

    bins = [0 ,30, 50, 70, float("inf")]
    labels =["30대 이하", "30~50대", "50~70대", "70대 이상"]
    df["Age_Group"] = pd.cut(df["age"], bins=bins, labels=labels, right=True)
    ctab = pd.crosstab(df["Age_Group"], df["label"])
    print(ctab)
    print("==================== 나이별 흡연자/비흡연자 비율=========================")
    ctab_ratio = pd.crosstab(df["Age_Group"], df["label"], normalize="index") *100
    print(ctab_ratio.round(2))
    print("=============================================")

if __name__ == "__main__":
    run()
