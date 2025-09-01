from typing import List, Optional
from sqlmodel import SQLModel, Field, Session, select

# Definição da tabela "Medico" usando SQLModel
# - table=True indica que a classe será mapeada como tabela no banco
class Medico(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Coluna ID, chave primária
    nome: str                                                 # Coluna nome
    especialidade: str                                        # Coluna especialidade

# -------------------------
# Funções CRUD (Create, Read, Update, Delete)
# -------------------------

# READ: Retorna todos os médicos cadastrados no banco
def get_medicos(session: Session) -> List[Medico]:
    return session.exec(select(Medico)).all()

# CREATE: Insere um novo médico na tabela
def create_medico(session: Session, medico: Medico) -> Medico:
    session.add(medico)       # Adiciona o objeto à sessão
    session.commit()          # Confirma a transação no banco
    session.refresh(medico)   # Atualiza o objeto com dados persistidos (ex: id gerado)
    return medico

# UPDATE: Atualiza os dados de um médico existente
def update_medico(session: Session, medico_id: int, medico_data: Medico) -> Optional[Medico]:
    medico = session.get(Medico, medico_id)   # Busca médico pelo ID
    if not medico:
        return None  # Se não existir, retorna None

    # Atualiza os campos
    medico.nome = medico_data.nome
    medico.especialidade = medico_data.especialidade

    session.add(medico)     # Marca objeto como atualizado
    session.commit()        # Salva as alterações
    session.refresh(medico) # Atualiza o objeto com os novos valores
    return medico

# DELETE: Remove um médico do banco pelo ID
def delete_medico(session: Session, medico_id: int) -> bool:
    medico = session.get(Medico, medico_id)   # Busca médico pelo ID
    if not medico:
        return False  # Se não existir, não faz nada

    session.delete(medico)  # Marca objeto para exclusão
    session.commit()        # Aplica a exclusão no banco
    return True
