from utils.db import load_table
import pandas as pd
from analysis.common.visualize import plot_distribution_mk2

def classify_tg(x):
    if x < 150:
        return "정상"
    elif x < 200:
        return "경계"
    elif x < 500:
        return "높음"
    else:
        return "매우 높음"

def run():
    df = load_table()

    print("===== TG 단변량 분석 =====")

    text_list = []
    img_list = []

    text_list.append(str("===== TG 단변량 분석 ====="))
    desc = df["TG"].describe()
    print(desc)
    text_list.append(str(desc))

   
    img_paths = plot_distribution_mk2(df, "TG", save_path="report_images")
    if img_paths:
        img_list.extend(img_paths)

   
    df["TG_stage"] = df["TG"].apply(classify_tg)


    tg_ratio = pd.crosstab(df["TG_stage"], df["label"], normalize="index") * 100
    print(tg_ratio.round(2))

    text_list.append(str(tg_ratio.round(2)))

    return text_list, img_list
