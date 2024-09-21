from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from associativas import turma_alunos  # Importar a tabela associativa

class Aluno(Base):
    __tablename__ = 'alunos'

    matricula = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))

    turmas = relationship("Turma", secondary=turma_alunos, back_populates="alunos")  # Relacionamento com Turma

    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def __repr__(self):
        return f"Aluno(matrícula={self.matricula}, nome={self.nome}, email={self.email})"

    def atualizar_informacoes(self, nome=None, email=None):
        if nome:
            self.nome = nome
        if email:
            self.email = email
