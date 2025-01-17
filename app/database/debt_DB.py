from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.constants import DB_DebtConfig as DB

URL_Database = f'{DB.db_type}://{DB.db_user}:{DB.db_password}@localhost:5432/{DB.db_name}'

engine = create_engine(URL_Database)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

