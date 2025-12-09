from utils.db import load_table
import pandas as pd
def run():
    df = load_table()

    print("===== [4] BMI 상태 vs 흡연 여부 =====")



 
    bins =[0,18.5, 25, 30, float("inf")]
    lables= ["저체중","정상","과체중","비만"]
    df["BMI_status"] = pd.cut(df["BMI"], bins=bins, labels=lables, right=False)

    ctab = pd.crosstab(df["BMI_status"], df["label"])
    print(ctab)
    print("==================== BMI 상태에서 흡연자/비흡연자 비율=========================")


    ctab_ratio = pd.crosstab(df["BMI_status"], df["label"], normalize="index") * 100  
    print(ctab_ratio.round(2))
    print("=============================================")


if __name__ == "__main__":
    run()
