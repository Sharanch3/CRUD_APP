from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



DATABASE_URL = "sqlite:///./test.db"

#establish a connection to database
engine = create_engine(
    url= DATABASE_URL,
    connect_args= {'check_same_thread': False}
)

#to create new database session
SessionLocal = sessionmaker(bind= engine, autoflush= False, autocommit = False)

Base = declarative_base()