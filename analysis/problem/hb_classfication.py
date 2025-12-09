from utils.db import load_table
import pandas as pd
from analysis.common.visualize import plot_distribution_mk2

def classify_hb(x):
    if x < 12:
        return "빈혈"
    elif x < 16:
        return "정상"
    else:
        return "높음"

def run():
    df = load_table()

    print("===== Hb 단변량 분석 =====")
   
    text_list = []
    img_list = []
    text_list.append(str("===== Hb 단변량 분석 ====="))
    desc = df["Hb"].describe()
    print(desc)
    text_list.append(str(desc))

    img_paths = plot_distribution_mk2(df, "Hb", save_path="report_images")
    if img_paths:
      img_list.extend(img_paths)

    df["Hb_stage"] = df["Hb"].apply(classify_hb)
    stage_ratio = pd.crosstab(df["Hb_stage"], df["label"], normalize="index") * 100
    df["Hb_int"] = df["Hb"].round().astype(int)
    ctd = pd.crosstab(df["Hb_int"], df["label"])
    print('----------------')
    print(ctd)
    print('----------------')
    print(stage_ratio)
    
    text_list.append(str(stage_ratio))

    return text_list, img_list
