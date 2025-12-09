from sqlalchemy import text
from utils.db import get_engine, load_table


def test_mysql_connection():
    print("=== MySQL 연결 테스트 ===")

    engine = get_engine()
    print("Engine 객체 생성됨:", engine)

    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1")).fetchone()
            print("✅ MySQL 연결 성공:", result)

            print("=========================")

            print("📋 DB Load 성공:", result)
    except Exception as e:
        print("❌ MySQL 연결 실패:", e)
    
    print("=========================")


if __name__ == "__main__":
    test_mysql_connection()
