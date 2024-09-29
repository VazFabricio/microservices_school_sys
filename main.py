# main.py
from fastapi import FastAPI
from apis.api_aluno import router as aluno_router
from apis.api_disciplina import router as disciplina_router
from apis.api_turma import router as turma_router
from database import Base, engine

# Inicializar o banco de dados
Base.metadata.create_all(bind=engine)

# Inicializar o app FastAPI
app = FastAPI()

# Incluir as rotas
app.include_router(aluno_router, prefix="/alunos")
app.include_router(disciplina_router, prefix="/disciplinas")
app.include_router(turma_router, prefix="/turmas")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9050)