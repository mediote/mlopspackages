import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException


def get_data_from_solr(url: str, solr_username: str, solr_password: str, query_params: dict) -> pd.DataFrame:
    """
    Obtém dados do Solr e converte para um DataFrame pandas.

    Args:
    - url (str): URL do servidor Solr.
    - solr_username (str): Nome de usuário para autenticação no Solr.
    - solr_password (str): Senha para autenticação no Solr.
    - query_params (dict): Parâmetros de consulta para a solicitação ao Solr.

    Returns:
    - df (pd.DataFrame): DataFrame pandas contendo os dados do Solr.
    """
    try:
        # Configuração da autenticação básica no Solr
        auth = HTTPBasicAuth(solr_username, solr_password)

        # Faça a solicitação ao Solr usando a biblioteca requests
        response = requests.get(url, params=query_params,
                                auth=auth, verify=False)

        # Verifique se a solicitação foi bem-sucedida
        response.raise_for_status()

        # Converta a resposta JSON para um DataFrame pandas
        metadados = response.json().get('response', {}).get('docs', [])
        df = pd.DataFrame(metadados)

        return df

    except RequestException as e:
        # Trate exceções relacionadas a problemas de solicitação
        print(f"Houve um erro ao consultar o Solr: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro
