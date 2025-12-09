from utils.db import load_table
from analysis.common.visualize import plot_distribution
import pandas as pd
def run():
    df = load_table()

    print("===== [7] 혈압 분석 =====")

    mean_table = (
        df.groupby("label")["blood_pressure"]
        .mean()
        .round(2)
        .rename(index={0: "비흡연자", 1: "흡연자"})
        .to_frame(name="혈압 평균")
        .T
    )

    print("\n▶ 혈압 평균 비교")
    print(mean_table)


    diff = mean_table["흡연자"] - mean_table["비흡연자"]
    diff_value = diff.item() 
    print(f"\n▶ 평균 차이 (흡연자 - 비흡연자): {diff_value:.2f}")

    
    threshold = df["blood_pressure"].quantile(0.80)
    df["BP_risk"] = (df["blood_pressure"] >= threshold).astype(int)

    risk_table = (
        pd.crosstab(df["BP_risk"], df["label"], normalize="index") * 100
    ).round(2)

    print("\n▶ 고혈압 위험군 비율(%):")
    print(risk_table)
    print("\n▶ 혈압 분포 시각화")
    plot_distribution(df, "blood_pressure")


    print("=============================================")


if __name__ == "__main__":
    run()
