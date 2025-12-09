from utils.db import load_table


def run():
  df = load_table()
  label_map={0:"비흡연자", 1:"흡연자"}
  output_text = []
  image_files = []


  output_text.append("===== [1] 흡연 여부(label) 기본 분포 =====")
  output_text.append("\n▶ 흡연자/비흡연자 수")
  label_count = df["label"].map(label_map).value_counts()
  output_text.append(str(label_count))

    # 2) 비율(%) 출력
  output_text.append("\n▶ 흡연자/비흡연자 비율(%)")
  # print((df["label"].map(label_map).value_counts(normalize=True) * 100).round(2))
  
  label_counts = df["label"].value_counts(normalize=True) * 100
  label_counts.index = label_counts.index.map(label_map)
  output_text.append(str(label_counts.round(2)))

  output_text.append("\n▶ label별 describe 비교 (주요 수치 요약)")
  describe_text = df.groupby("label").describe().T
  output_text.append(str(describe_text))

  print("===== [1] 흡연 기본 분석 완료 =====")

  
  return output_text, image_files



if __name__ == "__main__":
    run()
