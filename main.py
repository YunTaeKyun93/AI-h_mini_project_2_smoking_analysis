import argparse
import sys


from analysis.template_analysis import run as run_template
# 예시와 같이 나중에 추가하면 됩니다 
# from analysis.problems.activity_analysis import run as run_activity
# from analysis.problems.risk_analysis import run as run_risk


ANALYSIS_MAP = {
    "template": run_template,
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

    if analysis_name not in ANALYSIS_MAP:
        print(f"❌ Error: '{analysis_name}' 분석은 존재하지 않습니다.")
        print(f"➡️ 사용 가능 분석: {list(ANALYSIS_MAP.keys())}")
        sys.exit(1)

    print(f"🚀 실행 중: {analysis_name} 분석")
    ANALYSIS_MAP[analysis_name]()  


if __name__ == "__main__":
    main()
