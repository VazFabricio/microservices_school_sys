from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Tabela Associativa
turma_alunos = Table(
    'turma_alunos', Base.metadata,
    Column('turma_id', String(10), ForeignKey('turmas.codigo'), primary_key=True),
    Column('aluno_id', Integer, ForeignKey('alunos.matricula'), primary_key=True)
)
