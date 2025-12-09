from analysis.problem.smoking_01_overview import run as run_01
from analysis.problem.smoking_02_health_means import run as run_02
from analysis.problem.smoking_03_distribution import run as run_03
from analysis.problem.smoking_04_bmi_relation import run as run_04
from analysis.problem.smoking_05_age_relation import run as run_05
from analysis.problem.smoking_06_cholesterol import run as run_06
from analysis.problem.smoking_07_blood_pressure import run as run_07
from analysis.problem.smoking_08_fpg_analysis import run as run_08
from analysis.problem.smoking_09_hemo_analysis import run as run_09
from analysis.problem.smoking_10_liver_function import run as run_10
from analysis.problem.smoking_11_crosstab import run as run_11
from analysis.problem.tg_classification import run as tg
from analysis.problem.hb_classfication import run as hb
from utils.pdf_utils import create_pdf   

def run():
    print("===== 🔍 전체 통합 리포트 실행 시작 =====\n")

    all_text = []
    all_images = []

    for analysis_func in [
        # run_01, run_02, run_03, run_04, run_05,
        # run_06, run_07, run_08, run_09, run_10, run_11
        tg,hb
    ]:
        text, images = analysis_func()
        all_text.extend(text)
        all_images.extend(images)

    create_pdf(
        output_path="report/Smoking_Health_Report.pdf",
        text_blocks=all_text,
        image_paths=all_images
    )

    print("\n===== 🎉 전체 리포트 완료! PDF 생성됨 =====")
