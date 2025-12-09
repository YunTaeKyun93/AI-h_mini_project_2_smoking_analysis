import os
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")



def _ensure_dir(path):
    if path:
        os.makedirs(path, exist_ok=True)


# 단일 분포 그래프 (Histogram + KDE)

def plot_distribution(df, column, save_path=None):

    plt.figure(figsize=(8, 4))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")

    _ensure_dir(save_path)
    if save_path:
        plt.savefig(os.path.join(save_path, f"{column}_distribution.png"))

    plt.close()  # 🔥 핵심: 그래프 닫기 (멈춤 방지)


# KDE 비교 
def plot_kde_compare(df, column, label_col="label", save_path=None):

    plt.figure(figsize=(8, 4))
    sns.kdeplot(data=df, x=column, hue=label_col, fill=True)
    plt.title(f"KDE Compare - {column}")

    _ensure_dir(save_path)
    if save_path:
        plt.savefig(os.path.join(save_path, f"{column}_kde_compare.png"))

    plt.close()


# Boxplot 비교 
def plot_box_compare(df, column, label_col="label", save_path=None):

    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x=label_col, y=column)
    plt.title(f"Boxplot - {column} by {label_col}")

    _ensure_dir(save_path)
    if save_path:
        plt.savefig(os.path.join(save_path, f"{column}_box_compare.png"))

    plt.close()


# KDE + Boxplot 통합 
def plot_compare(df, column, label_col="label", save_path=None):

    _ensure_dir(save_path)

    # 📌 KDE Plot
    plt.figure(figsize=(8, 4))
    sns.kdeplot(data=df, x=column, hue=label_col, fill=True)
    plt.title(f"KDE Plot - {column} (흡연자 vs 비흡연자)")

    if save_path:
        plt.savefig(os.path.join(save_path, f"{column}_kde.png"))

    plt.close()

    # 📌 Boxplot
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x=label_col, y=column)
    plt.title(f"Boxplot - {column} (흡연자 vs 비흡연자)")

    if save_path:
        plt.savefig(os.path.join(save_path, f"{column}_box.png"))

    plt.close()


# Pairplot
def plot_pair(df, cols, save_path=None):

    _ensure_dir(save_path)

    g = sns.pairplot(df[cols], diag_kind="kde")

    if save_path:
        g.savefig(os.path.join(save_path, "pairplot.png"))

    plt.close()


# 상관관계 히트맵
def plot_corr_heatmap(df, save_path=None):

    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")

    _ensure_dir(save_path)
    if save_path:
        plt.savefig(os.path.join(save_path, "corr_heatmap.png"))

    plt.close()
