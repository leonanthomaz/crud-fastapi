# 🩺 CRUD FastAPI - Médicos

## Descrição
Um projeto simples de **CRUD (Create, Read, Update, Delete)** feito com **FastAPI** e **SQLModel**, usando PostgreSQL como banco de dados.  
Esse projeto é ótimo para iniciantes que querem aprender como integrar uma API Python com um banco relacional. 🚀  

## 📂 Estrutura do Projeto

```
crud-fastapi/
├── main.py # Arquivo principal: inicia a API e define as rotas
├── crud.py # Lógica de CRUD e definição da tabela "medicos"
├── Dicas.txt # Algumas dicas para iniciantes
└── README.md # Este arquivo
```

## ⚙️ Tecnologias Utilizadas
- **Python 3.9+**
- [FastAPI](https://fastapi.tiangolo.com/) → Framework web moderno
- [SQLModel](https://sqlmodel.tiangolo.com/) → ORM simplificado (mistura de Pydantic + SQLAlchemy)
- **PostgreSQL** (ou **SQLite** para testes rápidos)
- [Uvicorn](https://www.uvicorn.org/) → Servidor ASGI para rodar a aplicação
---

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/leonanthomaz/crud-fastapi.git
cd crud-fastapi
```

## 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

## 3. Instale as dependências
pip install -r requirements.txt

## 4. Configure o banco de dados
Edite no arquivo main.py a variável DATABASE_URL:
```bash
DATABASE_URL = "postgresql+psycopg2://USUARIO:SENHA@localhost:5432/hospital"
```
- USUARIO → seu usuário do Postgres (ex: postgres)
- SENHA → a senha configurada
- localhost → onde está rodando o banco
- 5432 → porta padrão do Postgres
- hospital → nome do banco que você criou

Se não quiser usar Postgres, pode usar SQLite trocando por:
DATABASE_URL = "sqlite:///database.db"

### 5. Rode a aplicação
```bash
python main.py
```
A API ficará disponível em:
👉 http://127.0.0.1:8000

### Endpoints

- GET /medicos → Lista todos os médicos
- POST /medicos → Cria um novo médico
- PUT /medicos/{id} → Atualiza um médico existente
- DELETE /medicos/{id} → Remove um médico

Você pode testar tudo via Swagger UI:
👉 http://127.0.0.1:8000/docs


## Contato

Desenvolvedor: Leonan Thomaz
Email: leonan.thomaz@gmail.com

#### Redes Sociais

- LinkedIn: https://www.linkedin.com/in/leonanthomaz
- GitHub: https://github.com/leonanthomaz







