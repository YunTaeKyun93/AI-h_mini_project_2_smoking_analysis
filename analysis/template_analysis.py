from utils.db import load_table
from utils.process import clean_data
from analysis.common.visualize import plot_distribution
from analysis.common.stats import summary


def run():
    

    print ("test")
    # 1️⃣ 데이터 로드
    # df = load_table()

    # # 2️⃣3 전처리
    # df = clean_data(df, apply_basic_clean=False)

    # # 3️⃣ 분석 요약 출력
    # summary(df)

    # # 4️⃣시각화 예시

    # numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    # if len(numeric_cols) > 0:
    #     plot_distribution(df, numeric_cols[0])