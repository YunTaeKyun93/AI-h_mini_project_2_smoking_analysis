import os
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")



def _ensure_dir(path):
    if path:
        os.makedirs(path, exist_ok=True)


# 단일 분포 그래프 (Histogram + KDE)

def plot_distribution(df, column, save_path=None):
    paths = []
    plt.figure(figsize=(8, 4))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")

    _ensure_dir(save_path)
    if save_path:
        plt.savefig(os.path.join(save_path, f"{column}_distribution.png"))

    plt.close()  
    return paths


def plot_distribution_mk2(df, column, save_path=None):
    paths = []
    _ensure_dir(save_path)


    plt.figure(figsize=(8, 4))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")

    hist_path = None
    if save_path:
        hist_path = os.path.join(save_path, f"{column}_distribution.png")
        plt.savefig(hist_path)
        paths.append(hist_path)

    plt.close()


    plt.figure(figsize=(8, 4))
    plt.scatter(df.index, df[column], alpha=0.6)
    plt.title(f"Scatter Plot of {column}")
    plt.xlabel("Index")
    plt.ylabel(column)

    scatter_path = None
    if save_path:
        scatter_path = os.path.join(save_path, f"{column}_scatter.png")
        plt.savefig(scatter_path)
        paths.append(scatter_path)

    plt.close()

    return paths

# def plot_scatter(df, x, y, save_path=None):
#     plt.figure(figsize=(6, 5))
#     sns.scatterplot(data=df, x=x, y=y)
#     sns.regplot(data=df, x=x, y=y, scatter=False, color='red')  
#     plt.title(f"Scatter Plot: {x} vs {y}")

#     _ensure_dir(save_path)
#     if save_path:
#         out_path = os.path.join(save_path, f"{x}_{y}_scatter.png")
#         plt.savefig(out_path)
#     plt.close()
    
#     return out_path if save_path else None



def plot_scatter(df, x, y, save_path=None):
    plt.figure(figsize=(7, 6))

    sns.scatterplot(data=df, x=x, y=y, alpha=0.6)

    sns.regplot(data=df, x=x, y=y, scatter=False, color='yellow', line_kws={"linewidth":2})

    plt.title(f"Scatter Plot: {x} vs {y}")
    plt.xlabel(x)
    plt.ylabel(y)

    _ensure_dir(save_path)
    out_path = None
    if save_path:
        out_path = os.path.join(save_path, f"{x}_{y}_scatter.png")
        plt.savefig(out_path)

    plt.close()
    return out_path

def plot_scatter_hue(df, x, y, save_path=None, hue="label"):
    g = sns.lmplot(
        data=df,
        x=x,
        y=y,
        hue=hue,
        height=6,
        aspect=1.1,
        scatter_kws={'alpha': 0.6}
    )

    g.figure.suptitle(f"Scatter Plot with Hue: {x} vs {y}", y=1.02)

    _ensure_dir(save_path)
    out_path = None
    if save_path:
        out_path = os.path.join(save_path, f"{x}_{y}_scatter_hue.png")
        g.savefig(out_path)

    plt.close()
    return out_path



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
    paths = []

    kde_path = None
    plt.figure(figsize=(8, 4))
    sns.kdeplot(data=df, x=column, hue=label_col, fill=True)
    plt.title(f"KDE Plot - {column} (흡연자 vs 비흡연자)")
    if save_path:
        kde_path = os.path.join(save_path, f"{column}_kde.png")
        plt.savefig(kde_path)
        paths.append(kde_path)
    plt.close()

    box_path = None
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x=label_col, y=column)
    plt.title(f"Boxplot - {column} (흡연자 vs 비흡연자)")
    if save_path:
        box_path = os.path.join(save_path, f"{column}_box.png")
        plt.savefig(box_path)
        paths.append(box_path)
    plt.close()

    return paths



# Pairplot
def plot_pair(df, cols, save_path=None):

    _ensure_dir(save_path)

    g = sns.pairplot(df[cols], diag_kind="kde")

    if save_path:
        g.savefig(os.path.join(save_path, "pairplot.png"))

    plt.close()


# 상관관계 히트맵
def plot_corr_heatmap(df, save_path=None):
    _ensure_dir(save_path)

    img_path = None
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")

    if save_path:
        img_path = os.path.join(save_path, "corr_heatmap.png")
        plt.savefig(img_path)

    plt.close()
    return img_path

