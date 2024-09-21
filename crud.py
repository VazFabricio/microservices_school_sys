from sqlalchemy.orm import Session
from aluno import Aluno
from disciplina import Disciplina
from turma import Turma

class CRUD:

    @staticmethod
    def create_aluno(db: Session, nome: str, matricula: int, email: str):
        novo_aluno = Aluno(nome=nome, matricula=matricula, email=email)
        db.add(novo_aluno)
        db.commit()
        db.refresh(novo_aluno)
        return novo_aluno

    @staticmethod
    def read_aluno(db: Session, matricula: int):
        return db.query(Aluno).filter(Aluno.matricula == matricula).first()

    @staticmethod
    def update_aluno(db: Session, matricula: int, nome: str = None, email: str = None):
        aluno = db.query(Aluno).filter(Aluno.matricula == matricula).first()
        if aluno:
            if nome:
                aluno.nome = nome
            if email:
                aluno.email = email
            db.commit()
            db.refresh(aluno)
        return aluno

    @staticmethod
    def delete_aluno(db: Session, matricula: int):
        aluno = db.query(Aluno).filter(Aluno.matricula == matricula).first()
        if aluno:
            db.delete(aluno)
            db.commit()
            return True
        return False


    @staticmethod
    def create_disciplina(db: Session, nome: str, codigo: str):
        nova_disciplina = Disciplina(nome=nome, codigo=codigo)
        db.add(nova_disciplina)
        db.commit()
        db.refresh(nova_disciplina)
        return nova_disciplina

    @staticmethod
    def read_disciplina(db: Session, codigo: str):
        return db.query(Disciplina).filter(Disciplina.codigo == codigo).first()

    @staticmethod
    def update_disciplina(db: Session, codigo: str, nome: str = None):
        disciplina = db.query(Disciplina).filter(Disciplina.codigo == codigo).first()
        if disciplina:
            if nome:
                disciplina.nome = nome
            db.commit()
            db.refresh(disciplina)
        return disciplina

    @staticmethod
    def delete_disciplina(db: Session, codigo: str):
        disciplina = db.query(Disciplina).filter(Disciplina.codigo == codigo).first()
        if disciplina:
            db.delete(disciplina)
            db.commit()
            return True
        return False


    @staticmethod
    def create_turma(db: Session, codigo: str, disciplina: Disciplina):
        nova_turma = Turma(codigo=codigo, disciplina=disciplina)
        db.add(nova_turma)
        db.commit()
        db.refresh(nova_turma)
        return nova_turma

    @staticmethod
    def read_turma(db: Session, codigo: str):
        return db.query(Turma).filter(Turma.codigo == codigo).first()

    @staticmethod
    def update_turma(db: Session, codigo: str, disciplina: Disciplina = None):
        turma = db.query(Turma).filter(Turma.codigo == codigo).first()
        if turma:
            if disciplina:
                turma.disciplina = disciplina
            db.commit()
            db.refresh(turma)
        return turma

    @staticmethod
    def delete_turma(db: Session, codigo: str):
        turma = db.query(Turma).filter(Turma.codigo == codigo).first()
        if turma:
            db.delete(turma)
            db.commit()
            return True
        return False
