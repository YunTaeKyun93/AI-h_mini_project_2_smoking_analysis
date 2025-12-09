from utils.db import load_table
import os
from analysis.common.visualize import plot_compare

def run():
    df = load_table()

    output_text = []
    image_files = []

    output_text.append("===== [6] 콜레스테롤/지질대사 분석 =====")
    print("===== [6] 콜레스테롤/지질대사 분석 =====")

    lipid_cols = ["cholesterol", "HDL", "LDL", "TG"]
    mean_table = df.groupby("label")[lipid_cols].mean().round(2).T

    output_text.append("▶ 흡연자/비흡연자 평균 비교")
    output_text.append(str(mean_table))
    print(mean_table)

    mean_table["diff"] = mean_table[1] - mean_table[0]
    diff_sort = mean_table["diff"].abs().sort_values(ascending=False)

    output_text.append("\n▶ 평균 차이 큰 순서")
    output_text.append(str(diff_sort))
    print("\n▶ 차이 큰 순서")
    print(diff_sort)

    top_col = diff_sort.index[0]

    save_dir = "report_images"
    os.makedirs(save_dir, exist_ok=True)

    img_paths = plot_compare(df, top_col, save_path=save_dir)
    image_files.extend(img_paths)

    output_text.append(f"\n▶ 시각화 저장 변수: {top_col}")

    print("=============================================")
    output_text.append("=============================================")

    return output_text, image_files


if __name__ == "__main__":
    run()
