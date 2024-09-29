from sqlalchemy.orm import Session
from aluno import Aluno
from disciplina import Disciplina
from turma import Turma

# ALUNO CRUD
def create_aluno(db: Session, nome: str, matricula: int, email: str):
    db_aluno = Aluno(nome=nome, matricula=matricula, email=email)
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def read_aluno(db: Session, matricula: int):
    return db.query(Aluno).filter(Aluno.matricula == matricula).first()

def update_aluno(db: Session, matricula: int, nome: str = None, email: str = None):
    aluno = db.query(Aluno).filter(Aluno.matricula == matricula).first()
    if not aluno:
        return None
    if nome:
        aluno.nome = nome
    if email:
        aluno.email = email
    db.commit()
    return aluno

def delete_aluno(db: Session, matricula: int):
    aluno = db.query(Aluno).filter(Aluno.matricula == matricula).first()
    if aluno:
        db.delete(aluno)
        db.commit()
        return True
    return False

# DISCIPLINA CRUD
def create_disciplina(db: Session, nome: str, codigo: str):
    db_disciplina = Disciplina(nome=nome, codigo=codigo)
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina

def read_disciplina(db: Session, codigo: str):
    return db.query(Disciplina).filter(Disciplina.codigo == codigo).first()

def update_disciplina(db: Session, codigo: str, nome: str = None):
    disciplina = db.query(Disciplina).filter(Disciplina.codigo == codigo).first()
    if not disciplina:
        return None
    if nome:
        disciplina.nome = nome
    db.commit()
    return disciplina

def delete_disciplina(db: Session, codigo: str):
    disciplina = db.query(Disciplina).filter(Disciplina.codigo == codigo).first()
    if disciplina:
        db.delete(disciplina)
        db.commit()
        return True
    return False

# TURMA CRUD
def create_turma(db: Session, codigo: str, disciplina_id: str):
    db_turma = Turma(codigo=codigo, disciplina_id=disciplina_id)
    db.add(db_turma)
    db.commit()
    db.refresh(db_turma)
    return db_turma

def read_turma(db: Session, codigo: str):
    return db.query(Turma).filter(Turma.codigo == codigo).first()

def update_turma(db: Session, codigo: str, disciplina_id: str = None):
    turma = db.query(Turma).filter(Turma.codigo == codigo).first()
    if not turma:
        return None
    if disciplina_id:
        turma.disciplina_id = disciplina_id
    db.commit()
    return turma

def delete_turma(db: Session, codigo: str):
    turma = db.query(Turma).filter(Turma.codigo == codigo).first()
    if turma:
        db.delete(turma)
        db.commit()
        return True
    return False

# Adicionar aluno a turma
def add_aluno_to_turma(db: Session, codigo: str, aluno_matricula: int):
    turma = db.query(Turma).filter(Turma.codigo == codigo).first()
    aluno = db.query(Aluno).filter(Aluno.matricula == aluno_matricula).first()

    if not turma or not aluno:
        return None

    turma.alunos.append(aluno)  # Adiciona o aluno à lista de alunos da turma (Many-to-Many)
    db.commit()
    return turma
