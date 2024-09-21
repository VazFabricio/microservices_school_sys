from sqlalchemy import Column, String
from database import Base

class Disciplina(Base):
    __tablename__ = 'disciplinas'

    codigo = Column(String(10), primary_key=True)
    nome = Column(String(100))

    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def __repr__(self):
        return f"Disciplina(código={self.codigo}, nome={self.nome})"
