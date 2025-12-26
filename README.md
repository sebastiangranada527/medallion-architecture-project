# Medallion Architecture Roadmap Project

Proyecto práctico para implementar la **Arquitectura Medallion** (Bronze → Silver → Gold) desde cero, siguiendo el principio de Pareto (80/20) y enfoque "aprender haciendo".  
Basado en el artículo: [Medallion Architecture Case Study](https://thedatatrait.medium.com/medallion-architecture-case-study-how-real-companies-use-it-4b8dcf65f95c)

## Objetivos
- Avanzar de nivel principiante a proficiente en roles de **Data Engineer** y **Data Scientist**.
- Construir un pipeline ETL reproducible, escalable y bien documentado.
- Crear un portafolio profesional que demuestre habilidades prácticas en data engineering y ciencia de datos.

## Tecnologías utilizadas (hasta ahora)
- Python 3.10+
- Pandas, Faker, NumPy
- PySpark (modo local)
- Jupyter Notebooks
- Próximamente: Scikit-learn, Apache Airflow, TensorFlow (opcional)

## Estructura del Proyecto
medallion-architecture-project/
├── etapa1-fundamentos/             # Configuración inicial y generación de datos simulados
│   ├── notebooks/
│   │   └── 01_generacion_y_exploracion_datos.ipynb
│   └── data/
│       └── raw_sales.csv (generado, no commiteado)
├── etapa2-bronze/                  # Capa Bronze: ingesta cruda sin transformaciones
│   ├── notebooks/
│   │   └── 02_capa_bronze.ipynb
│   └── data/
│       └── bronze/
│           └── sales_raw.parquet (generado)
├── etapa3-silver-gold/             # Capas Silver y Gold: limpieza y tablas curadas
│   ├── notebooks/
│   │   └── 03_capas_silver_gold.ipynb
│   └── data/
│       ├── silver/
│       │   └── sales_clean.parquet
│       └── gold/
│           ├── sales_fact_daily.parquet
│           └── sales_fact_product_store.parquet
├── etapa4-optimizaciones/          # Optimizaciones, EDA y Machine Learning
│   ├── notebooks/
│   │   └── 04_optimizaciones_y_ml.ipynb
│   └── data/                       # (opcional: particiones o datos adicionales)
├── etapa5-deployment/              # (Pendiente)
├── data/                           # Datos generados (no commiteados por .gitignore)
├── docs/                           # Documentación adicional (diagramas, notas)
├── src/                            # Scripts reutilizables (futuro)
├── requirements.txt
└── README.md

## Progreso actual
| Etapa | Estado       | Descripción principal                                                                 |
|-------|--------------|---------------------------------------------------------------------------------------|
| 1     | ✅ Completada | Generación de datos simulados (ventas minoristas) y exploración inicial (Pandas)     |
| 2     | ✅ Completada | Capa Bronze: ingesta cruda con PySpark, almacenamiento en Parquet, simulación de late-arriving data |
| 3     | ✅ Completada | Capas Silver y Gold: limpieza, estandarización y creación de tablas curadas (revenue diario, por producto/tienda) |
| 4     | ✅ Completada | Optimizaciones de rendimiento, EDA, feature engineering y modelo de churn básico con Random Forest |
| 5     | Pendiente    | Orquestación con Airflow y preparación para deployment

## Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/sebastiangranada527/medallion-architecture-project.git
cd medallion-architecture-project

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
source venv/bin/activate          # Linux/Mac
# o
venv\Scripts\activate             # Windows


## Instalar dependencias

pip install -r requirements.txt

## Ejecutar las etapas existentes
### Etapa 1 – Generación y exploración de datos simulados:

jupyter notebook etapa1-fundamentos/notebooks/01_generacion_y_exploracion_datos.ipynb

Genera 5,000 filas de ventas minoristas simuladas (con Faker).
Explora inconsistencias reales (e.g., store_id con formatos variados).
Crea visualizaciones básicas con Matplotlib.

### Etapa 2 – Capa Bronze:

jupyter notebook etapa2-bronze/notebooks/02_capa_bronze.ipynb

Lee el CSV crudo generado en Etapa 1.
Almacena los datos sin ninguna transformación en formato Parquet.
Simula "late-arriving data" (datos que llegan tarde) y los agrega en modo append.
Verifica integridad y trazabilidad.

### Etapa 3 – Capas Silver y Gold:

jupyter notebook etapa3-silver-gold/notebooks/03_capas_silver_gold.ipynb

Silver: Limpieza y estandarización (normaliza store_id, maneja nulos, filtra corruptos).
Gold: Crea tablas curadas (revenue diario, métricas por producto y tienda).
Visualiza revenue diario para validar el resultado.

Nota: Ejecuta las etapas en orden (1 → 2 → 3

Tareas realizadas hasta ahora

Generación de datos simulados realistas con inconsistencias intencionales.
Capa Bronze: ingesta cruda, almacenamiento eficiente, soporte para datos tardíos.
Capa Silver: limpieza y estandarización de datos.
Capa Gold: creación de tablas curadas y métricas de negocio.
Documentación detallada en notebooks y README.
Uso de Git con commits atómicos y mensajes claros.

Próximos pasos


### 4. Ejecutar las etapas existentes
4. **Etapa 4** – Optimizaciones y Machine Learning:
   ```bash
   jupyter notebook etapa4-optimizaciones/notebooks/04_optimizaciones_y_ml.ipynb

Escala datos agregando filas adicionales a Silver (simulación de crecimiento).
Optimiza rendimiento: cacheo de DataFrames y particionamiento por fecha.
Análisis exploratorio avanzado (EDA) con Pandas/Seaborn.
Feature engineering para clientes: total gastado, número de compras, días desde última compra.
Modelo de clasificación de churn con Random Forest (incluye métricas: classification report y ROC AUC).

Tareas realizadas en Etapa 4

Escalado de datos para simular volúmenes mayores.
Optimización de consultas Spark (cache y particionamiento).
Análisis exploratorio detallado y visualización de patrones.
Feature engineering a nivel cliente.
Entrenamiento y evaluación de modelo de predicción de churn (Random Forest).
Transición clara de rol Data Engineer a Data Scientist dentro del mismo pipeline Medallion.

Próximos pasos

Etapa 5: Orquestación del pipeline completo con scripts modulares y automatización Python (Orquestador Ligero para Mac).

## Automatización y Despliegue (Etapa 5)

En esta etapa hemos refactorizado toda la lógica de los notebooks a scripts de producción modulares y creado un orquestador automático.

### Ejecutar todo el Pipeline con un solo comando:
Simplemente corre el script maestro que se encargará de ejecutar (Bronze -> Silver -> Gold) en orden y reportar el estado:

```bash
python orchestrator.py
```

### Estructura de Deployment:
*   `etapa5-deployment/scripts/bronze_ingest.py`: Ingesta de datos crudos.
*   `etapa5-deployment/scripts/silver_transform.py`: Limpieza profunda y particionamiento.
*   `etapa5-deployment/scripts/gold_aggregate.py`: Agregación de KPIs de negocio.
*   `orchestrator.py`: Script maestro que automatiza el flujo completo.