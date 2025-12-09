from utils.db import load_table

# - 'health_data' 데이터의 정보를 확인해보세요.
# - 'describe', 'info', 'head', 'tail' 등 전부 활용해봅시다.

def run():
  df = load_table()
  print('=====================DESCRIBE===========================')
  print(df.describe())
  print('=====================HEAD===========================')
  print(df.head())
  print('=====================TAIL===========================')
  print(df.tail())
  print(f"총 행수 : {len(df)}")
  print('=====================INFO===========================')
  print(df.info())


  if __name__ == "__main__":
    run()