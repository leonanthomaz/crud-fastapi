from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Session, create_engine
from crud import Medico, get_medicos, create_medico, update_medico, delete_medico

# URL de conexão com banco Postgres local
# Formato padrão:
# postgresql+psycopg2://USUARIO:SENHA@HOST:PORTA/NOME_DO_BANCO
#
# Vamos quebrar em partes pra ficar claro:
# - "postgresql+psycopg2" → indica que vamos usar PostgreSQL com o driver psycopg2
# - "USUARIO" → seu usuário do Postgres (ex: postgres, leonan, etc.)
# - "SENHA" → a senha definida para esse usuário
# - "HOST" → onde está rodando o banco (normalmente "localhost" quando é na sua máquina)
# - "PORTA" → porta do Postgres (padrão é 5432)
# - "NOME_DO_BANCO" → o banco de dados que você criou (ex: hospital)
#
# Exemplo real:
# postgresql+psycopg2://leonan:senha123@localhost:5432/hospital
#
# Obs: Os dois pontos ":" separam USUARIO e SENHA.
#      A arroba "@" separa as credenciais (usuario:senha) do endereço do servidor.
#      A barra "/" separa o endereço do banco do nome do banco.
#
DATABASE_URL = "postgresql+psycopg2://SEU_USUARIO:SUA_SENHA@localhost:5432/hospital"


# Cria um "engine" que será responsável por conectar e interagir com o banco
# echo=True faz logar no terminal todas as queries executadas (útil pra debug)
engine = create_engine(DATABASE_URL, echo=True)

# Função que cria as tabelas no banco de acordo com os modelos definidos
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Instância da aplicação FastAPI
app = FastAPI()

# Evento disparado quando a API sobe
# Aqui chamamos a criação das tabelas (caso ainda não existam)
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Rota GET: retorna lista de médicos cadastrados
@app.get("/medicos")
def listar_medicos():
    with Session(engine) as session:
        return get_medicos(session)

# Rota POST: adiciona um médico novo no banco
@app.post("/medicos")
def adicionar_medico(medico: Medico):
    with Session(engine) as session:
        return create_medico(session, medico)

# Rota PUT: atualiza dados de um médico existente pelo ID
@app.put("/medicos/{medico_id}")
def atualizar_medico(medico_id: int, medico: Medico):
    with Session(engine) as session:
        updated = update_medico(session, medico_id, medico)
        if not updated:
            # Caso não exista médico com o ID informado, devolve erro 404
            raise HTTPException(status_code=404, detail="Médico não encontrado")
        return updated

# Rota DELETE: remove um médico existente pelo ID
@app.delete("/medicos/{medico_id}")
def remover_medico(medico_id: int):
    with Session(engine) as session:
        deleted = delete_medico(session, medico_id)
        if not deleted:
            # Caso não exista médico com o ID informado, devolve erro 404
            raise HTTPException(status_code=404, detail="Médico não encontrado")
        return {"ok": True}

# Permite rodar a API com "python main.py"
# uvicorn é o servidor ASGI que roda a aplicação
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
