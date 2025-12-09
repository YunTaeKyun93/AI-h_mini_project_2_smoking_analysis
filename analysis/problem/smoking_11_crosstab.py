from utils.db import load_table
from analysis.common.visualize import plot_corr_heatmap


def run():
    df = load_table()

    output_text = []
    image_files = []

    print("===== [11] 상관관계 분석 =====")
    output_text.append("===== [11] 상관관계 분석 =====")

   
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    df_numeric = df[numeric_cols]

   
    corr = df_numeric.corr()

   
    label_corr = corr["label"].sort_values(ascending=False)
    print("\n▶ label과의 상관계수 (내림차순)")
    print(label_corr)

    output_text.append("\n▶ label과의 상관계수 (내림차순)")
    output_text.append(str(label_corr))

   
    label_corr_top = corr["label"].abs().sort_values(ascending=False).head(6)
    print("\n▶ label과의 상관계수 절대값 기준 상위 6개")
    print(label_corr_top)

    output_text.append("\n▶ label과의 상관계수 절대값 기준 상위 6개")
    output_text.append(str(label_corr_top))

   
    img_path = plot_corr_heatmap(df_numeric, save_path="report_images")
    if img_path:
        image_files.append(img_path)
        output_text.append("\n▶ 상관관계 히트맵 저장 완료")

    print("=============================================")
    output_text.append("=============================================")

    return output_text, image_files


if __name__ == "__main__":
    run()
