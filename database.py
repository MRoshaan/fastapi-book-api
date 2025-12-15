from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = "mysql+mysqlconnector://bookuser:Roshaan_DB2024!@localhost:3306/book_manager"



engine=create_engine(database_url)

sessionlocal=sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base=declarative_base()