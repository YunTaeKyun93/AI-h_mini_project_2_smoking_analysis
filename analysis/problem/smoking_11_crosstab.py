from utils.db import load_table
import matplotlib.pyplot as plt
import seaborn as sns
from analysis.common.visualize import plot_corr_heatmap


def run():
    df = load_table()

    print("===== [11] 상관관계 분석 =====")

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    df_numeric = df[numeric_cols]
    corr = df_numeric.corr()
    print(corr["label"].sort_values(ascending=False))

    plot_corr_heatmap(df_numeric, save_path="report_images")


    label_corr = corr["label"].abs().sort_values(ascending=False)
    print(label_corr.head(6))

    print("=============================================")


if __name__ == "__main__":
    run()
