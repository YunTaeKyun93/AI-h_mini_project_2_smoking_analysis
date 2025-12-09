from utils.db import load_table

def run():
    df = load_table()

    output_text = []
    image_files = []

    print("===== [2] 주요 건강지표 평균 비교 =====")
    output_text.append("===== [2] 주요 건강지표 평균 비교 =====\n")

    health_cols = ["blood_pressure", "FPG", "cholesterol", "HDL", "LDL", "TG", "BMI"]

    mean_table = df.groupby("label")[health_cols].mean().round(2).T
    mean_table.columns = ["비흡연자(0)", "흡연자(1)"]

    print("\n▶ 비흡연자 , 흡연자 평균 차이")
    print(mean_table)

    output_text.append("▶ 비흡연자 , 흡연자 평균 차이")
    output_text.append(str(mean_table))

    mean_table["차이(흡연자-비흡연자)"] = (
        mean_table["흡연자(1)"] - mean_table["비흡연자(0)"]
    )

    diff_sorted = mean_table["차이(흡연자-비흡연자)"].abs().sort_values(ascending=False)

    print("\n▶ 평균 차이(절대값 기준) 지표")
    print(diff_sorted)

    output_text.append("\n▶ 평균 차이(절대값 기준) 지표")
    output_text.append(str(diff_sorted))

    output_text.append("\n=============================================\n")

    return output_text, image_files


if __name__ == "__main__":
    run()
