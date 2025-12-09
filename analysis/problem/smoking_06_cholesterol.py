from utils.db import load_table
import matplotlib.pyplot as plt
import seaborn as sns
import os
from analysis.common.visualize  import plot_compare


def run():
    df = load_table()

    print("===== [6] 콜레스테롤/지질대사 분석 =====")

    lipid_cols = ["cholesterol", "HDL", "LDL", "TG"]

    mean_table = df.groupby("label")[lipid_cols].mean().T
    print(mean_table)
    mean_table["diff"] = mean_table[1] - mean_table[0]
    print("=============================================")
    diff_sort = mean_table["diff"].abs().sort_values(ascending=False)
    print("\n▶ 차이 큰 순서")
    print(diff_sort.head)
    print("\n▶ 가장 차이 큰 지표")
    print(diff_sort.head(1))
    top_col = diff_sort.index[0]
    save_dir = "report_images"
    os.makedirs(save_dir, exist_ok=True)

    plot_compare(df, top_col, save_path=save_dir)
    plt.show()

    print("=============================================")


if __name__ == "__main__":
    run()
