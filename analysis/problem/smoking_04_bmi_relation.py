from utils.db import load_table
import pandas as pd

def run():
    df = load_table()

    output_text = []
    image_files = []   

    # ------------------------------
    # 1) 제목
    # ------------------------------
    title = "===== [4] BMI 상태 vs 흡연 여부 ====="
    print(title)
    output_text.append(title)

    # ------------------------------
    # 2) BMI 상태 구간화
    # ------------------------------
    bins = [0, 18.5, 25, 30, float("inf")]
    labels = ["저체중", "정상", "과체중", "비만"]
    df["BMI_status"] = pd.cut(df["BMI"], bins=bins, labels=labels, right=False)

    # ------------------------------
    # 3) CrossTab (빈도)
    # ------------------------------
    ctab = pd.crosstab(df["BMI_status"], df["label"])
    
    print(ctab)
    output_text.append("\n▶ BMI 상태별 흡연자/비흡연자 수")
    output_text.append(str(ctab))

    # ------------------------------
    # 4) CrossTab 비율(%)
    # ------------------------------
    print("\n==================== BMI 상태에서 흡연자/비흡연자 비율 =========================")
    
    ctab_ratio = pd.crosstab(df["BMI_status"], df["label"], normalize="index") * 100
    
    print(ctab_ratio.round(2))

    output_text.append("\n▶ BMI 상태별 흡연자 비율(%)")
    output_text.append(str(ctab_ratio.round(2)))

    print("=============================================")
    output_text.append("=============================================")

    return output_text, image_files


if __name__ == "__main__":
    run()
