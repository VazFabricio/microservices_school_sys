# api_disciplina.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_disciplina
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DisciplinaCreate(BaseModel):
    nome: str
    codigo: str

@router.post("/")
def create_disciplina_endpoint(disciplina: DisciplinaCreate, db: Session = Depends(get_db)):
    return create_disciplina(db, nome=disciplina.nome, codigo=disciplina.codigo)
