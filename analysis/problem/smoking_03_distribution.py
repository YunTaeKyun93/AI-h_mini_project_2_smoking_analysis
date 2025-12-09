from utils.db import load_table
import seaborn as sns
import matplotlib.pyplot as plt
from analysis.common.visualize import plot_compare


def run():
    df = load_table()

    output_text = []
    image_files = []

    target_cols = ["blood_pressure", "BMI"]

    for col in target_cols:
        msg = f"[시각화] 현재 변수: {col}"
        print(msg)
        output_text.append(msg)

        img_paths = plot_compare(df, col, save_path="report_images")
        image_files.extend(img_paths)

    print("=============================================")
    output_text.append("=============================================")

    return output_text, image_files


if __name__ == "__main__":
    run()
