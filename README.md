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
├── etapa3-silver-gold/             # (En progreso)
├── etapa4-optimizaciones/          # (Pendiente)
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
| 3     | En progreso  | Capas Silver y Gold: limpieza, estandarización y creación de tablas curadas          |
| 4     | Pendiente    | Optimizaciones, feature engineering y modelado ML básico                             |
| 5     | Pendiente    | Orquestación con Airflow y preparación para deployment                               |

## Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/sebastiangranada527/medallion-architecture-project.git
cd medallion-architecture-project


