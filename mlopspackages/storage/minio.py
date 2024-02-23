from io import BytesIO

import boto3
import pandas as pd
from botocore.exceptions import ClientError


def get_minio_client(endpoint_url: str, aws_access_key_id: str, aws_secret_access_key: str) -> boto3.client:
    """
    Obtém um cliente MinIO configurado.

    Args:
    - endpoint_url (str): URL do endpoint MinIO.
    - aws_access_key_id (str): Chave de acesso da AWS.
    - aws_secret_access_key (str): Chave secreta de acesso da AWS.

    Returns:
    - s3_client (boto3.client): Cliente MinIO configurado.
    """
    s3_client = boto3.client(
        's3',
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        config=boto3.session.Config(signature_version='s3v4')
    )
    return s3_client


def load_dataframe_from_minio(minio_client: boto3.client, bucket_name: str, key: str) -> pd.DataFrame:
    """
    Carrega um DataFrame a partir de um arquivo no MinIO.

    Args:
    - minio_client (boto3.client): Cliente MinIO configurado.
    - bucket_name (str): Nome do bucket no MinIO.
    - key (str): Chave do arquivo no MinIO.

    Returns:
    - df (pd.DataFrame): DataFrame carregado a partir do arquivo no MinIO.
    """
    try:
        file_obj = minio_client.get_object(Bucket=bucket_name, Key=key)
        file_content = file_obj['Body'].read()
        df = pd.read_csv(BytesIO(file_content))
        return df
    except ClientError as e:
        raise Exception(
            f"Erro ao carregar DataFrame do MinIO ({key}): {str(e)}")


def save_dataframe_to_minio(minio_client: boto3.client, bucket_name: str, key: str, dataframe: pd.DataFrame) -> str:
    """
    Salva um DataFrame no MinIO.

    Args:
    - minio_client (boto3.client): Cliente MinIO configurado.
    - bucket_name (str): Nome do bucket no MinIO.
    - key (str): Chave do arquivo no MinIO.
    - dataframe (pd.DataFrame): DataFrame a ser salvo.

    Returns:
    - key (str): Chave do arquivo salvo no MinIO.
    """
    try:
        # Transforma o DataFrame em bytes
        dataframe_bytes = dataframe.to_csv(index=False).encode('utf-8')
        # Faz o upload do DataFrame para o MinIO
        minio_client.put_object(
            Bucket=bucket_name, Key=key, Body=dataframe_bytes)
        return key
    except ClientError as e:
        raise Exception(f"Erro ao salvar DataFrame no MinIO ({key}): {str(e)}")
