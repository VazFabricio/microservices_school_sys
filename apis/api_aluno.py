# api_aluno.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_aluno, read_aluno, update_aluno, delete_aluno
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class AlunoCreate(BaseModel):
    nome: str
    matricula: int
    email: str

@router.post("/")
def create_aluno_endpoint(aluno: AlunoCreate, db: Session = Depends(get_db)):
    return create_aluno(db, nome=aluno.nome, matricula=aluno.matricula, email=aluno.email)

@router.get("/{matricula}")
def read_aluno_endpoint(matricula: int, db: Session = Depends(get_db)):
    aluno = read_aluno(db, matricula=matricula)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.put("/{matricula}")
def update_aluno_endpoint(matricula: int, aluno: AlunoCreate, db: Session = Depends(get_db)):
    aluno_atualizado = update_aluno(db, matricula=matricula, nome=aluno.nome, email=aluno.email)
    if not aluno_atualizado:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno_atualizado

@router.delete("/{matricula}")
def delete_aluno_endpoint(matricula: int, db: Session = Depends(get_db)):
    sucesso = delete_aluno(db, matricula=matricula)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"message": "Aluno deletado com sucesso"}
