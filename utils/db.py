from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv
from typing  import Optional



load_dotenv()

def get_engine():
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_DB = os.getenv("MYSQL_DB")

    engine = create_engine(
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}",
        connect_args={
            "ssl": {
                "ssl": True
            }
        }
    )
    return engine


def load_table(table_name: Optional[str] = None):
    engine = get_engine()

    if table_name is None:
        table_name = os.getenv("DEFAULT_TABLE")

    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql(query, engine)
    return df
