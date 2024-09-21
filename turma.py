from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from associativas import turma_alunos  # Importar a tabela associativa

class Turma(Base):
    __tablename__ = 'turmas'

    codigo = Column(String(10), primary_key=True)
    disciplina_id = Column(String(10), ForeignKey('disciplinas.codigo'))

    disciplina = relationship("Disciplina")
    alunos = relationship("Aluno", secondary=turma_alunos, back_populates="turmas")  # Relacionamento com Aluno

    def __init__(self, codigo, disciplina):
        self.codigo = codigo
        self.disciplina = disciplina

    def __repr__(self):
        return f"Turma(código={self.codigo}, disciplina={self.disciplina})"
