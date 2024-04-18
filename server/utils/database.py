from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from server.main import CONFIGURATION

engine = create_engine(f"sqlite:///./{CONFIGURATION['database']}", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
