from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from  dotenv  import  dotenv_values

config = dotenv_values(".env")

USUARIO = config['USUARIO']
SENHA = config['SENHA']
HOST = config['HOST']
BANCO = config['BANCO']
PORT = config['PORT']

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(200))
    senha = Column(String(100))

Base.metadata.create_all(engine)