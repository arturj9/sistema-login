from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import User

def retornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "sistema-login"
    PORT = 3306

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = retornaSession()

class DaoUser:
    @classmethod
    def cadastrarUsuario(cls, nome, email, senha):
        try:
            newUser = User(nome = nome, email = email, senha = senha)
            session.add(newUser)
            session.commit()
            return True
        except:
            return False

    @classmethod
    def ler(cls):
        return session.query(User).all()

    @classmethod
    def removerUsuario(cls, id):
        try:
            session.query(User).filter(User.id==id).delete()
            return True
        except:
            return False

    @classmethod
    def alterarUsuarioNome(cls, id, novoNome):
        try:
            user = session.query(User).filter(User.id==id).all()
            user[0].nome = novoNome
            session.commit()
            return True
        except:
            return False

    @classmethod
    def alterarUsuarioEmail(cls, id, novoEmail):
        try:
            user = session.query(User).filter(User.id==id).all()
            user[0].email = novoEmail
            session.commit()
            return True
        except:
            return False

    @classmethod
    def alterarUsuarioSenha(cls, id, novaSenha):
        try:
            user = session.query(User).filter(User.id==id).all()
            user[0].senha = novaSenha
            session.commit()
            return True
        except:
            return False


x=DaoUser()
print(x.removerUsuario(2))