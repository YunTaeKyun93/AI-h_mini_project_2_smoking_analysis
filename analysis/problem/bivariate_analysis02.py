from utils.db import load_table
from analysis.common.visualize import plot_scatter

def run():
    df = load_table()

    print("===== 키 vs 몸무게 이변량 분석 =====")

    text_list = []
    img_list = []

    text_list.append("===== 키 vs 몸무게 이변량 분석 =====")
    text_list.append(str(df[["height", "weight"]].describe()))

    img_path = plot_scatter(df, "height", "weight", save_path="report_images")
    if img_path:
        img_list.append(img_path)

    return text_list, img_list
