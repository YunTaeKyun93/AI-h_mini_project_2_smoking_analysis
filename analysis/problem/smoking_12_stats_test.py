# from utils.db import load_table
# import pandas as pd
# from scipy.stats import ttest_ind, chi2_contingency

# def run():
#     df = load_table()

#     print("===== [12] 통계적 유의성 검정 =====")


#     smoker = df[df["label"] == 1]["Hb"].dropna()
#     non_smoker = df[df["label"] == 0]["Hb"].dropna()

#     t_result = ttest_ind(smoker, non_smoker, equal_var=False, nan_policy='omit')

#     # ↓↓↓ 이 한 줄이면 끝! (scipy 1.11 이상/이하 모두 완벽 대응)
#     t_stat = float(t_result.statistic if hasattr(t_result, 'statistic') else t_result[0])
#     p_value = float(t_result.pvalue if hasattr(t_result, 'pvalue') else t_result[1])

#     print("\n▶ [T-test] 흡연자 vs 비흡연자 Hb 평균 비교")
#     print("t-stat:", round(t_stat, 3))
#     print("p-value:", f"{p_value:.6f}")
#     print("➡ 결론:", "유의미한 차이가 있다!" if p_value < 0.05 else "통계적으로 유의미하지 않다(우연)")


#     def classify_fpg(x):
#         if pd.isna(x): 
#             return "결측"
#         if x < 100: 
#             return "정상"
#         elif x < 126: 
#             return "전당뇨"
#         else: 
#             return "당뇨"

#     df["FPG_stage"] = df["FPG"].apply(classify_fpg)
#     temp_df = df[df["FPG_stage"] != "결측"]

#     ctb = pd.crosstab(temp_df["FPG_stage"], temp_df["label"])

#     chi2_result = chi2_contingency(ctb)

#     chi2 = float(chi2_result.statistic if hasattr(chi2_result, 'statistic') else chi2_result[0])
#     p_chi = float(chi2_result.pvalue if hasattr(chi2_result, 'pvalue') else chi2_result[1])

#     print("\n▶ [Chi-square] FPG 단계 ↔ 흡연 여부 관련성 검사")
#     print("chi2:", round(chi2, 3))
#     print("p-value:", f"{p_chi:.6f}")
#     print("➡ 결론:", "통계적으로 관련이 있다!" if p_chi < 0.05 else "관련성이 없다(우연일 가능성)")

#     print("=============================================")

# if __name__ == "__main__":
#     run()