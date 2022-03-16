from model import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib
from  dotenv  import  dotenv_values

def retornaSession():
    config = dotenv_values(".env")

    USUARIO = config['USUARIO']
    SENHA = config['SENHA']
    HOST = config['HOST']
    BANCO = config['BANCO']
    PORT = config['PORT']
    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"
    engine = create_engine(CONN, echo=False)
    Session = sessionmaker(bind=engine)
    return Session()
class ControllerCadastro:
    @classmethod
    def verificaDados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        return 1
    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retornaSession()
        usuario = session.query(User).filter(User.email == email).all()
        if len(usuario) > 0:
            return 5
        dadosVerificados = cls.verificaDados(nome, email, senha)
        if dadosVerificados != 1:
            return dadosVerificados
        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            newUser = User(nome = nome, email = email, senha = senha)
            session.add(newUser)
            session.commit()
            return 1
        except:
            return 6
class ControllerLogin:
    @classmethod
    def login(cls, email, senha):
        session = retornaSession()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        logado = session.query(User).filter(User.email == email).filter(User.senha == senha).all()
        
        if len(logado) == 1:
            return {"logado": True, "id": logado[0].id}
        else:
            return False