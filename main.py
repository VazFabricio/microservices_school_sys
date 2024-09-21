from database import SessionLocal, engine, Base
from disciplina import Disciplina
from aluno import Aluno
from turma import Turma

# Criar uma nova sessão
session = SessionLocal()

# Criar as tabelas no banco de dados (se ainda não existirem)
Base.metadata.create_all(bind=engine)

# Lógica do seu sistema
if __name__ == "__main__":
    disciplina1 = Disciplina("Matemática", "MAT101")
    session.add(disciplina1)
    session.commit()

    aluno1 = Aluno("Alice", 1, "alice@email.com")
    session.add(aluno1)
    session.commit()

    turma1 = Turma("T1", disciplina1)
    session.add(turma1)
    session.commit()

    # Adicionando alunos à turma
    turma1.alunos.append(aluno1)  # Adiciona o aluno à turma
    session.commit()

    print("Tabelas criadas e dados inseridos.")
