from utils.db import load_table
import pandas as pd
def classify_fpg(x):
    if x < 100:
        return "정상"
    elif x < 126:
        return "전당뇨"
    else:
        return "당뇨"

def run():
    df = load_table()

    print("===== [8] 혈당(FPG) 분석 =====")
    mean_table = df.groupby("label")["FPG"].mean().round(2).rename(index={0: "비흡연자", 1: "흡연자"}).to_frame(name="FPG 평균").T
    print("\n▶ 흡연 여부별 평균 FPG(공복 혈당)")
    print(mean_table)
    df["FPG_stage"] = df["FPG"].apply(classify_fpg)
    print("\n▶ FPG 단계별 분포 (정상 / 전당뇨 / 당뇨)")
    print(df["FPG_stage"].value_counts())

    ctb_ratio = pd.crosstab(df["FPG_stage"], df["label"], normalize="index")*100
    print("\n▶ 단계별 흡연자 / 비흡연자 비율 (%)")
    print(ctb_ratio.round(2))
    print("=============================================")


if __name__ == "__main__":
    run()
