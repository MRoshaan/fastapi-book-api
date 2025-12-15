from sqlalchemy import Column , Integer , String 
from database import Base

class book(Base):
    __tablename__="books"
    id = Column(Integer,primary_key=True,index=True)
    name= Column(String(255),nullable=False)
    author=Column(String(255),nullable=False)
    rating=Column(String(255),nullable=False)
