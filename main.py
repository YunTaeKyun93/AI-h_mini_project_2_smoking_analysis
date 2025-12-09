import argparse
import sys
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


from analysis.template_analysis import run as run_template
from analysis.problem.test_load import run as run_test_load
from analysis.problem.show_tables_test import run as run_show_tables
from analysis.problem.bmi_classification import run as run_bmi
from analysis.problem.age_group_classification import run as run_age
from analysis.problem.smoking_01_overview import run as run_smoking1
from analysis.problem.smoking_02_health_means import run as run_smoking2
from analysis.problem.smoking_03_distribution import run as run_smoking3
from analysis.problem.smoking_04_bmi_relation import run as run_smoking4
from analysis.problem.smoking_05_age_relation import run as run_smoking5
from analysis.problem.smoking_06_cholesterol import run as run_smoking6
from analysis.problem.smoking_07_blood_pressure import run as run_smoking7
from analysis.problem.smoking_08_fpg_analysis import run as run_smoking8
from analysis.problem.smoking_09_hemo_analysis import run as run_smoking9
from analysis.problem.smoking_10_liver_function import run as run_smoking10
from analysis.problem.smoking_11_crosstab import run as run_smoking11
from analysis.problem.smoking_12_stats_test import run as run_smoking12

from analysis.problem.total_report import run as total
# 예시와 같이 나중에 추가하면 됩니다 
# from analysis.problems.activity_analysis import run as run_activity
# from analysis.problems.risk_analysis import run as run_risk


ANALYSIS_MAP = {
    "template": run_template,
    "test_load" : run_test_load,
    "show_tables": run_show_tables,
    "bmi" :run_bmi,
    "age" :run_age,
    "step1" : run_smoking1,
    "step2" : run_smoking2,
    "step3" : run_smoking3,
    "step4" : run_smoking4,
    "step5" : run_smoking5,
    "step6" : run_smoking6,
    "step7" : run_smoking7,
    "step8" : run_smoking8,
    "step9" : run_smoking9,
    "step10" : run_smoking10,
    "step11" : run_smoking11,
    "total" : total,
    # "step12" : run_smoking12,
    # "activity": run_activity,
    # "risk": run_risk,
}
#  python main.py --analysis template 해당 명령어로 분리해서 문제 분석가능합니다.

def main():
    parser = argparse.ArgumentParser(description="AI Health Data Analysis CLI")
    parser.add_argument(
        "--analysis",
        type=str,
        required=True,
        help="실행할 분석 이름 (예: template, activity, risk)"
    )
    args = parser.parse_args()

    analysis_name = args.analysis
    print(analysis_name)
    if analysis_name not in ANALYSIS_MAP:
        print(f"❌ Error: '{analysis_name}' 분석은 존재하지 않습니다.")
        print(f"➡️ 사용 가능 분석: {list(ANALYSIS_MAP.keys())}")
        sys.exit(1)

    print(f"🚀 실행 중: {analysis_name} 분석")
    ANALYSIS_MAP[analysis_name]()  


if __name__ == "__main__":
    main()
