from sqlalchemy import create_engine


def get_singlestore_engine(user: str, password: str, host: str, port: str, database: str):
    """
    Cria e retorna um SQLAlchemy Engine para o SingleStore DB.

    Args:
    - user (str): Nome do usuário para autenticação no SingleStore DB.
    - password (str): Senha do usuário para autenticação no SingleStore DB.
    - host (str): Hostname ou endereço IP do servidor SingleStore DB.
    - port (str): Porta do servidor SingleStore DB.
    - database (str): Nome do banco de dados SingleStore a ser usado.

    Returns:
    - engine (SQLAlchemy Engine): Objeto Engine para conexão com o SingleStore DB.
    """
    # Constrói a URL de conexão para o SingleStore DB
    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

    # Cria e retorna o Engine do SQLAlchemy
    engine = create_engine(connection_string)
    return engine
