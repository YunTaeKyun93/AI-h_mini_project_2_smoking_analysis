from utils.db import load_table
import seaborn as sns
import matplotlib.pyplot as plt
from analysis.common.visualize import plot_compare




def run():
    df = load_table()

    for col in ["blood_pressure", "BMI"]:
        print(f"\n 현재 시각화 중: {col}")
        plot_compare(df, col)

    plt.show()
  
    print("=============================================")

if __name__ == "__main__":
    run()
