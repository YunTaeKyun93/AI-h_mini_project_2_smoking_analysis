from utils.db import load_table
import pandas as pd 
# BMI 구간을 기준으로 건강상태를 분류해볼까요 ?
# 저체중 (<18.5)
# 정상 (<25)
# 과체중 (<30)
# 비만 (>=30


def classify_BMI(bmi):
    if bmi < 18.5:
        return "저체중"
    elif bmi < 25:
        return "정상"
    elif bmi < 30:
        return '과체중'
    else :
        return "비만"


def run():
    df = load_table()
    df["BMI_status"] = df["BMI"].apply(classify_BMI)
    # 2 입맛대로 사용
    # bins = [0, 18.5, 25,30, float("inf")]
    # labels =["저체중", "정상","과체중","비만"]
    # df["BMI_status"] = pd.cut(df["BMI"], bins=bins, labels=labels, right=False)
    print(df[["BMI", "BMI_status"]].head())





if __name__ == "__main__":
    run()
