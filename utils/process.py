import pandas as pd
import numpy as np

# etl 탬플릿도 존재하지만, 분석 단계에서 결측치 후속처리가 필요할 때가 있다고 생각합니다 (아직 사용한적은 없음)

def clean_data(df: pd.DataFrame, apply_basic_clean=True) -> pd.DataFrame:

  if not apply_basic_clean:
    return df 
  
  zero_cols = ["FPG", "blood_pressure", "TG", "cholesterol"]

  for col in zero_cols:
        if col in df.columns:
            df[col] = df[col].replace(0, np.nan)


  num_cols = df.select_dtypes(include=["int64", "float64"])
  df[num_cols.columns] = num_cols.fillna(num_cols.mean())

  return df