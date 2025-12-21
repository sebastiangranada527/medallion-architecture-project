# medallion-architecture-project
Roadmap práctico para implementar Arquitectura Medallion, de principiante a proficiente en Data Engineering y Data Science.

# Medallion Architecture Roadmap Project

Proyecto práctico para implementar la **Arquitectura Medallion** (Bronze → Silver → Gold) desde cero, siguiendo el principio de Pareto y enfoque "aprender haciendo".

Basado en el artículo: [Medallion Architecture Case Study](https://thedatatrait.medium.com/medallion-architecture-case-study-how-real-companies-use-it-4b8dcf65f95c)

## Objetivos
- Avanzar de nivel principiante a proficiente en Data Engineering y Data Science.
- Construir un pipeline ETL reproducible y escalable.
- Documentar cada etapa para portafolio profesional.

## Tecnologías
- Python 3.10+
- Pandas, Faker, NumPy
- PySpark (modo local)
- Scikit-learn
- Apache Airflow (en etapas avanzadas)
- Jupyter Notebooks / Scripts modulares

## Estructura del Proyecto

medallion-architecture-project/
├── etapa1-fundamentos/         # Configuración inicial y datos simulados
├── etapa2-bronze/              # Capa Bronze
├── etapa3-silver-gold/         # Capas Silver y Gold
├── etapa4-optimizaciones/      # Optimizaciones y ML
├── etapa5-deployment/          # Orquestación y deployment
├── data/                       # Datos simulados (generados, no commiteados)
├── docs/                       # Diagramas, notas
├── src/                        # Scripts reutilizables
├── requirements.txt
└── README.md


## Instalación
```bash
git clone https://github.com/sebastiangranada527/medallion-architecture-project.git
cd medallion-architecture-project
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
