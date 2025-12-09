from utils.db import load_table


def run():
  df = load_table()
  label_map={0:"비흡연자", 1:"흡연자"}

  print("===== [1] 흡연 여부(label) 기본 분포 =====")
  print("\n▶ 흡연자/비흡연자 수")
  label_count = df["label"].map(label_map).value_counts()
  print(label_count)

    # 📌 2) 비율(%) 출력
  print("\n▶ 흡연자/비흡연자 비율(%)")
  # print((df["label"].map(label_map).value_counts(normalize=True) * 100).round(2))
  
  label_counts = df["label"].value_counts(normalize=True) * 100
  label_counts.index = label_counts.index.map(label_map)
  print(label_counts.round(2))

  print("\n▶ label별 describe 비교 (주요 수치 요약)")
  print(df.groupby("label").describe().T)
if __name__ == "__main__":
    run()
