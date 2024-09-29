# api_turma.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_turma, read_turma, update_turma, delete_turma, add_aluno_to_turma
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TurmaCreate(BaseModel):
    codigo: str
    disciplina_id: str

class AddAlunoToTurma(BaseModel):
    aluno_matricula: int

@router.post("/")
def create_turma_endpoint(turma: TurmaCreate, db: Session = Depends(get_db)):
    return create_turma(db, codigo=turma.codigo, disciplina_id=turma.disciplina_id)

@router.get("/{codigo}")
def read_turma_endpoint(codigo: str, db: Session = Depends(get_db)):
    turma = read_turma(db, codigo=codigo)
    if not turma:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return turma

@router.put("/{codigo}")
def update_turma_endpoint(codigo: str, turma: TurmaCreate, db: Session = Depends(get_db)):
    turma_atualizada = update_turma(db, codigo=codigo, disciplina_id=turma.disciplina_id)
    if not turma_atualizada:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return turma_atualizada

@router.delete("/{codigo}")
def delete_turma_endpoint(codigo: str, db: Session = Depends(get_db)):
    sucesso = delete_turma(db, codigo=codigo)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return {"message": "Turma deletada com sucesso"}

@router.post("/{codigo}/alunos")
def add_aluno_to_turma_endpoint(codigo: str, aluno: AddAlunoToTurma, db: Session = Depends(get_db)):
    turma_atualizada = add_aluno_to_turma(db, codigo=codigo, aluno_matricula=aluno.aluno_matricula)
    if not turma_atualizada:
        raise HTTPException(status_code=404, detail="Erro ao adicionar aluno à turma")
    return turma_atualizada
