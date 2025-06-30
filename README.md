# Tarea3SD: Manejo de la información del análisis de tráfico en Region Metropolitana

Proyecto de Sistemas Distribuidos - 2025-1

---

## Descripción

En esta tercera entrega se aborda la indexación y visualización de eventos de tránsito mediante herramientas distribuidas como **Elasticsearch** y **Kibana**.

El objetivo fue cargar los eventos limpios obtenidos desde la etapa anterior en un índice de **Elasticsearch**, permitiendo realizar consultas eficientes y generar visualizaciones a partir de los datos. Para ello, se definió un mapeo con campos relevantes, incluyendo coordenadas geográficas (**geo_point**) para habilitar la representación espacial.

Posteriormente, se utilizaron las capacidades de **Kibana** para crear visualizaciones y dashboards interactivos, que permiten explorar los eventos según tipo, comuna, ubicación y fecha. Todo el entorno fue desplegado usando **Docker Compose**

---

## Estructura del Proyecto


```
TAREA3SD/
├── README.md
├── cargar_eventos.py
├── docker-compose.yml
├── requirements.txt
├── get-pip.py
├── event_collector/
│   ├── eventos.json
│   ├── csv/
│   │   ├── eventos.csv
│   │   ├── eventos_por_tipo.csv
│   │   └── eventos_por_tipo_y_comuna.csv
│   ├── eventos_limpios/
│   │   └── part-m-00000
│   ├── eventos_por_fecha/
│   │   └── part-r-00000
│   ├── eventos_por_tipo/
│   │   └── part-r-00000
│   ├── eventos_por_tipo_y_comuna/
│   │   └── part-r-00000
│   ├── accidentes_por_tipo/
│   │   └── part-r-00000
│   ├── eventos_accidente_por_fecha/
│   │   └── part-r-00000
│   ├── top5_ciudades_accidente/
│   │   └── part-r-00000
│   ├── resultados_agrupados/
│   │   └── part-r-00000
│   ├── scriptspig/
│   │   ├── *.pig
│   ├── scriptspy/
│   │   ├── graficar_calles.py
│   │   ├── graficar_eventos.py
│   │   ├── heatmap_eventos.py
│   │   ├── json_a_csv.py
│   │   └── waze_scraper_masivo.py
│   └── img/
│       ├── eventos_por_tipo.png
│       ├── mapa_eventos_tipo_calle.png
│       └── top_calles_eventos.png
├── pig_env/
│   └── Dockerfile
├── storage/
│   ├── cache_manager.py
│   ├── carga_a_redis.py
│   ├── crear_tabla.py
│   ├── insertar_eventos.py
│   ├── probar_cache.py
│   ├── probar_redis.py
│   └── __pycache__/
├── tests/
│   └── pruebas_rendimiento.py
├── traffic_api/
│   ├── Dockerfile
│   ├── main.py
│   ├── total_accidentes/
│   │   └── part-r-00000
│   └── __pycache__/
└── traffic_generator/
    ├── generador_poisson.py
    └── generador_uniforme.py

```





---

## Tecnologías Utilizadas

- **Python 3.11**
- **Apache Pig 0.17**
- **Hadoop 3.3.6**
- **Docker / Docker Compose**
- **Pandas, Matplotlib, Seaborn** (para visualización)
- **Elasticsearch 8.13.2**
- **Kibana 8.13.2**
- **PostgreSQL 15**
- **Redis 7**
---

## Instalación y Ejecución

1. Clona el repositorio:
   ```bash
    git clone https://github.com/Jairo-Ch/Tarea3SD.git
   cd Tarea2SD
   ```

2. Crea y activa un entorno virtual para evitar conflictos de dependencias:

   ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
   ```

3. Levanta el entorno distribuido con Docker (incluye Apache Pig y Hadoop):

  ```bash
    docker compose up --build
  ```

4. Carga los datos en Elasticsearch

  ```bash
      source venv/bin/activate      
      python cargar_eventos.py      
  ```
5. Carga los eventos en PostgresSQL
  ```bash
      cd storage
      python crear_tabla.py         
      python insertar_eventos.py    

  ```


Para visualizar

1. Kibana: abrir http://localhost:5601 en el navegador para explorar visualizaciones.
  
  
## Resultados Generados
Se cargaron los eventos limpios en Elasticsearch, permitiendo su visualización y análisis en Kibana mediante mapas y gráficos

## Notas Finales

Esta entrega integró herramientas distribuidas Elasticsearch y Kibana  en un entorno desplegado con Docker Compose. El sistema permite explorar los datos de forma visual y eficiente.
