import os
import sys

# Añadimos la carpeta de scripts al PATH para poder importar los módulos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
scripts_path = os.path.join(BASE_DIR, "etapa5-deployment")
sys.path.append(scripts_path)

try:
    from scripts.bronze_ingest import ingest_to_bronze
    from scripts.silver_transform import transform_to_silver
    from scripts.gold_aggregate import aggregate_to_gold
except ImportError as e:
    print(f"Error importando scripts: {e}")
    print("Asegúrate de ejecutar este script desde la raíz del proyecto.")
    sys.exit(1)

def run_pipeline():
    print("🚀 Iniciando Orquestación del Pipeline Medallion...")
    
    # Rutas relativas desde la raíz del proyecto
    RAW_CSV = "etapa1-fundamentos/data/raw_sales.csv"
    BRONZE_PATH = "etapa2-bronze/data/bronze/sales_raw.parquet"
    SILVER_PATH = "etapa3-silver-gold/data/silver/sales_clean.parquet"
    GOLD_DAILY = "etapa4-optimizaciones/data/gold/sales_fact_daily.parquet"
    GOLD_PROD_STORE = "etapa4-optimizaciones/data/gold/sales_fact_product_store.parquet"

    # 1. BRONZE
    print("\n📦 [ETAPA 2] Ejecutando Ingesta Bronze...")
    ingest_to_bronze(RAW_CSV, BRONZE_PATH)

    # 2. SILVER
    print("\n🥈 [ETAPA 3] Ejecutando Transformación Silver...")
    transform_to_silver(BRONZE_PATH, SILVER_PATH)

    # 3. GOLD
    print("\n🥇 [ETAPA 4] Ejecutando Agregaciones Gold...")
    aggregate_to_gold(SILVER_PATH, GOLD_DAILY, GOLD_PROD_STORE)

    print("\n✨ ¡Pipeline completado con éxito! Los datos están listos en la capa Gold.")

if __name__ == "__main__":
    run_pipeline()
