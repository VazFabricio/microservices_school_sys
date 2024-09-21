from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir a URI de conexão com o banco de dados MySQL
DATABASE_URI = 'mysql+pymysql://user:userpassword@localhost:3307/escola_db'

# Criar o engine que se conecta ao banco de dados
engine = create_engine(DATABASE_URI)

# Declarar a base para as tabelas ORM
Base = declarative_base()

# Configurar a criação de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função que retorna uma sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Importar e mapear as classes após a criação do Base
from aluno import Aluno  # Importações absolutas
from disciplina import Disciplina
from turma import Turma

# Criar as tabelas no banco de dados (se ainda não existirem)
Base.metadata.create_all(bind=engine)
