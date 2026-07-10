import os
import urllib.parse

from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

DB_PASSWORD = os.getenv("DB_PASSWORD", "HwLZQkm7ccACPJ91")
DB_USER = os.getenv("DB_USER", "BFn2KhvJ4ztT5V93.root")
DB_HOST = os.getenv("DB_HOST", "gateway01.ap-southeast-1.prod.aws.tidcloud.com")
DB_PORT = os.getenv("DB_PORT", "4000")
DB_NAME = os.getenv("DB_NAME", "test")


def create_database_engine():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        safe_password = urllib.parse.quote_plus(DB_PASSWORD)
        database_url = f"mysql+pymysql://{DB_USER}:{safe_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    if database_url.startswith("mysql"):
        try:
            engine = create_engine(
                database_url,
                pool_pre_ping=True,
                connect_args={
                    "ssl": {"ssl_mode": "PREFERRED"},
                    "connect_timeout": 30,
                },
            )
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("Connected to TiDB successfully.")
            return engine
        except Exception as exc:
            print(f"TiDB connection failed: {exc}")
            print("Falling back to local SQLite database.")

    fallback_url = os.getenv("SQLITE_URL", "sqlite:///./resume_app.db")
    return create_engine(fallback_url, pool_pre_ping=True)


engine = create_database_engine()
sessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()