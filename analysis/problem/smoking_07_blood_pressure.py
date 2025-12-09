from utils.db import load_table
from analysis.common.visualize import plot_distribution
import pandas as pd
import os

def run():
    df = load_table()

    output_text = []
    image_files = []

    print("===== [7] 혈압 분석 =====")
    output_text.append("===== [7] 혈압 분석 =====")


    mean_table = (
    df.groupby("label")["blood_pressure"]
    .mean()
    .round(2)
    .to_frame(name="혈압 평균")
    .T
    )   
    mean_table.columns = ["비흡연자", "흡연자"]
    mean_table = mean_table.astype(float)

    print("\n▶ 혈압 평균 비교")
    print(mean_table)

    output_text.append("\n▶ 혈압 평균 비교")
    output_text.append(str(mean_table))


    


    threshold = df["blood_pressure"].quantile(0.80)
    df["BP_risk"] = (df["blood_pressure"] >= threshold).astype(int)

    risk_table = (
        pd.crosstab(df["BP_risk"], df["label"], normalize="index") * 100
    ).round(2)

    print("\n▶ 고혈압 위험군 비율(%):")
    print(risk_table)

    output_text.append("\n▶ 고혈압 위험군 비율(%)")
    output_text.append(str(risk_table))


    save_dir = "report_images"
    os.makedirs(save_dir, exist_ok=True)

    img_path = plot_distribution(df, "blood_pressure", save_path=save_dir)
    if img_path:  
        image_files.append(img_path)

    print("\n▶ 혈압 분포 그래프 저장 완료")
    output_text.append("\n▶ 혈압 분포 그래프 저장 완료")

    print("=============================================")
    output_text.append("=============================================")

    return output_text, image_files


if __name__ == "__main__":
    run()
