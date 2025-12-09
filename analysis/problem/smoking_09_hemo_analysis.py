from utils.db import load_table
import pandas as pd
from analysis.common.visualize import plot_distribution


def classify_hb(x):
    if x < 12:
        return "빈혈"
    elif x < 16:
        return "정상"
    else:
        return "높음"


def run():
    df = load_table()

    print("===== [9] Hemoglobin(Hb) 분석 =====")

    mean_table = (
        df.groupby("label")["Hb"].mean().round(2)
        .rename(index={0: "비흡연자", 1: "흡연자"})
        .to_frame(name="Hb 평균").T
    )
    mean_table.columns = ["비흡연자(0)", "흡연자(1)"]

    print("\n▶ 비흡연자 , 흡연자 평균 ")
    print(mean_table)

    df["Hb_stage"] = df["Hb"].apply(classify_hb)
    print("=============================================")

    ctb = pd.crosstab(df["Hb_stage"], df["label"], normalize="index") * 100
    print(ctb.round(2))

    plot_distribution(df, "Hb", save_path="report_images")

    print("=============================================")



if __name__ == "__main__":
    run()

