from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings.envs import env

SQLALCHEMY_DATABASE_URL = f"postgresql://{env.DB_HOST_NAME}:{env.DB_PASSWORD}@{env.DB_HOST}/{env.DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()