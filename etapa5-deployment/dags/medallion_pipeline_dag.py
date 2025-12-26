from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys

# Aseguramos que la carpeta raíz del despliegue esté en el PATH
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# Definimos la base del proyecto para rutas absolutas
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Funciones "Proxy" para evitar cargar Spark al inicio (Soluciona el SIGSEGV en Mac)
def run_ingest(input_csv, output_parquet):
    from scripts.bronze_ingest import ingest_to_bronze
    ingest_to_bronze(input_csv, output_parquet)

def run_silver(input_parquet, output_parquet):
    from scripts.silver_transform import transform_to_silver
    transform_to_silver(input_parquet, output_parquet)

def run_gold(input_parquet, daily_output, product_store_output):
    from scripts.gold_aggregate import aggregate_to_gold
    aggregate_to_gold(input_parquet, daily_output, product_store_output)

default_args = {
    'owner': 'sebastiangranada',
    'start_date': datetime(2025, 12, 1),
    'retries': 1,
}

with DAG('medallion_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    bronze_task = PythonOperator(
        task_id='ingest_bronze',
        python_callable=run_ingest,
        op_kwargs={
            'input_csv': os.path.join(BASE_DIR, 'etapa1-fundamentos/data/raw_sales.csv'),
            'output_parquet': os.path.join(BASE_DIR, 'etapa2-bronze/data/bronze/sales_raw.parquet')
        }
    )

    silver_task = PythonOperator(
        task_id='transform_silver',
        python_callable=run_silver,
        op_kwargs={
            'input_parquet': os.path.join(BASE_DIR, 'etapa2-bronze/data/bronze/sales_raw.parquet'),
            'output_parquet': os.path.join(BASE_DIR, 'etapa3-silver-gold/data/silver/sales_clean.parquet')
        }
    )

    gold_task = PythonOperator(
        task_id='aggregate_gold',
        python_callable=run_gold,
        op_kwargs={
            'input_parquet': os.path.join(BASE_DIR, 'etapa3-silver-gold/data/silver/sales_clean.parquet'),
            'daily_output': os.path.join(BASE_DIR, 'etapa3-silver-gold/data/gold/sales_fact_daily.parquet'),
            'product_store_output': os.path.join(BASE_DIR, 'etapa3-silver-gold/data/gold/sales_fact_product_store.parquet')
        }
    )

    bronze_task >> silver_task >> gold_task