from utils.db import load_table
from analysis.common.visualize import plot_scatter, plot_scatter_hue


def run():
    df = load_table()

    text_blocks = []
    img_files = []

    # 1) 키 vs 몸무게
    desc_hw = df[["height", "weight"]].describe()
    text_blocks.append("===== 키 vs 몸무게 이변량 분석 =====")
    text_blocks.append(str(desc_hw))

    img_files.append(plot_scatter(df, "height", "weight", save_path="report_images"))
    img_files.append(plot_scatter_hue(df, "height", "weight", save_path="report_images"))


    # 2) 콜레스테롤 vs LDL
    desc_cl = df[["cholesterol", "LDL"]].describe()
    text_blocks.append("\n===== 콜레스테롤 vs LDL 분석 =====")
    text_blocks.append(str(desc_cl))

    img_files.append(plot_scatter(df, "cholesterol", "LDL", save_path="report_images"))
    img_files.append(plot_scatter_hue(df, "cholesterol", "LDL", save_path="report_images"))


    # 3) 나이 vs BMI
    desc_ab = df[["age", "BMI"]].describe()
    text_blocks.append("\n===== 나이 vs BMI 분석 =====")
    text_blocks.append(str(desc_ab))

    img_files.append(plot_scatter(df, "age", "BMI", save_path="report_images"))
    img_files.append(plot_scatter_hue(df, "age", "BMI", save_path="report_images"))


    return text_blocks, img_files


if __name__ == "__main__":
    run()
