# 공통 통계함수(차후ㅡ 업데이트 요망)

import pandas as pd

def summary(df: pd.DataFrame):
    print("🖨️ 데이터 요약")
    print(df.describe(include="all"))
