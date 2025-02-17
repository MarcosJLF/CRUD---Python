from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os



load_dotenv()
database_url = os.getenv('URL_DB')

DATABASE_URI = database_url
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

class Carro(Base):
    __tablename__ = 'carro'

    id = Column(Integer, primary_key=True)
    modelo = Column(String)
    marca = Column(String)
    ano = Column(Integer)
    cor = Column(String)
    km = Column(Integer)
    preco = Column(Integer)



Base.metadata.create_all(engine)
