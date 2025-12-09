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

    output_text = []
    image_files = []

    print("===== [9] Hemoglobin(Hb) 분석 =====")
    output_text.append("===== [9] Hemoglobin(Hb) 분석 =====")

   
    mean_table = (
        df.groupby("label")["Hb"]
        .mean()
        .round(2)
        .rename(index={0: "비흡연자", 1: "흡연자"})
        .to_frame(name="Hb 평균")
        .T
    )
    mean_table.columns = ["비흡연자(0)", "흡연자(1)"]

    print("\n▶ 비흡연자 , 흡연자 평균 ")
    print(mean_table)

    output_text.append("\n▶ 비흡연자 , 흡연자 평균 ")
    output_text.append(str(mean_table))

   
    df["Hb_stage"] = df["Hb"].apply(classify_hb)
    ctb = (pd.crosstab(df["Hb_stage"], df["label"], normalize="index") * 100).round(2)

    print("\n▶ Hb 단계별 흡연자 비율 (%)")
    print(ctb)

    output_text.append("\n▶ Hb 단계별 흡연자 비율 (%)")
    output_text.append(str(ctb))

   
    img_path = plot_distribution(df, "Hb", save_path="report_images")
    if img_path:  
        image_files.append(img_path)

    output_text.append("\n▶ Hb 분포 그래프 저장 완료")
    print("\n▶ Hb 분포 그래프 저장 완료")

    print("=============================================")
    output_text.append("=============================================")

    return output_text, image_files


if __name__ == "__main__":
    run()
