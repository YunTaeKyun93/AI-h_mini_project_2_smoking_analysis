from utils.db import get_engine
from sqlalchemy import text

def run():
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SHOW TABLES;")).fetchall()
        print(result)


if __name__ == "__main__":
    run()
