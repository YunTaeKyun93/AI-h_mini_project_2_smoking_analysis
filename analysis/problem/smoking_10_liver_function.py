from utils.db import load_table
import pandas as pd

def run():
    df = load_table()

    print("===== [10] 간 기능(LFT) 분석 =====")

    # TODO 1: LFT 평균 비교
    mean_table = df.groupby("label")["LFT"].mean().round(2).rename(index={0: "비흡연자", 1: "흡연자"}).to_frame(name="LFT 평균").T
    print("\n▶ 간 기능(LFT) 평균 비교")
    print(mean_table)


    threshold = df["LFT"].quantile(0.80)
    df["LFT_high"] = (df["LFT"] >= threshold).astype(int)
    ratio = pd.crosstab(df["LFT_high"], df["label"], normalize="index") * 100
    print("\n▶ LFT 높은 사람 기준 (상위 20%):", round(threshold, 3))
    print("\n▶ LFT 높은 그룹에서 흡연자 비율")
    print(ratio.round(2))

    print("=============================================")




if __name__ == "__main__":
    run()
