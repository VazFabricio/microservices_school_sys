from database import SessionLocal, engine, Base
from disciplina import Disciplina
from aluno import Aluno
from turma import Turma
from crud import CRUD

# Criar uma nova sessão
session = SessionLocal()

# Criar as tabelas no banco de dados (se ainda não existirem)
Base.metadata.create_all(bind=engine)

# Lógica do seu sistema
if __name__ == "__main__":
    session = SessionLocal()
    
    # Criar um novo aluno
    aluno = CRUD.create_aluno(session, "Alice", 1, "alice@email.com")
    print(aluno)

    # Buscar um aluno
    aluno_encontrado = CRUD.read_aluno(session, 1)
    print(aluno_encontrado)

    # Atualizar aluno
    aluno_atualizado = CRUD.update_aluno(session, 1, nome="Alice Atualizada")
    print(aluno_atualizado)

    # Deletar aluno
    sucesso = CRUD.delete_aluno(session, 1)
    print("Aluno excluído:", sucesso)

    session.close()
