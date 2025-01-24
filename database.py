from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# db_user = 'Eshar'
# db_password = '#4787'
# db_host = 'localhost'
# db_port = '3307'
# db_name = 'project_management'
db_user = 'Eshar'
db_password = '#4787'
db_host = 'localhost'
db_port = '3307'
db_name = 'project_management'
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://mysql:{db_user}{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()