from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from .config import Settings

#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:5Point_0@localhost:5432/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{Settings.database_username}:{Settings.database_password}@{Settings.database_hostname}:{Settings.database_port}/{Settings.database_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='5Point_0',cursor_factory=RealDictCursor)
#         cursor  = conn.cursor()
#         print("Database connection was succesfull, Yaaaaaay!")
#         break
#     except Exception as error:
#         print("Connecting to DB failed")
#         print("Error: ", error)
#         time.sleep(2)