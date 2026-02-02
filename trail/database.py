from sqlalchemy import create_engine
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base

# declarative_base() creates a base class that tells SQLAlchemy which Python classes should be treated as database tables.

DATABASE_URL = "sqlite://./tes.db"


engine = create_engine(
    url= DATABASE_URL,
    connect_args= {'check_same_thread': False}
)

SessionLocal = create_session(
    bind= engine,
    auto_flush = False,
    auto_commit = False
)

Base = declarative_base()
