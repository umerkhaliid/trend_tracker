# backend/db.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    timestamp = Column(DateTime)
    likes = Column(Integer)
    comments = Column(Integer)

engine = create_engine('sqlite:///trends.db')  # Works on Windows
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
