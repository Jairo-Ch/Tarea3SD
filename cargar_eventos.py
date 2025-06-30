import csv
from elasticsearch import Elasticsearch, helpers

# Conexión a Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Nombre del índice
indice = "eventos_limpios"

# Si ya existe el índice, lo borro para empezar limpio
if es.indices.exists(index=indice):
    es.indices.delete(index=indice)

# Configuración del índice con mapeo de campos
mapeo = {
    "mappings": {
        "properties": {
            "id": {"type": "keyword"},
            "categoria": {"type": "keyword"},
            "tipo": {"type": "keyword"},
            "comuna": {"type": "keyword"},
            "calle": {"type": "text"},
            "lat": {"type": "float"},
            "lon": {"type": "float"},
            "location": {"type": "geo_point"},
            "timestamp": {"type": "date", "format": "epoch_millis"}
        }
    }
}

# Crear el índice
es.indices.create(index=indice, body=mapeo)

# Ruta al archivo con los eventos limpios
archivo_csv = "event_collector/eventos_limpios/part-m-00000"

# Lista de documentos para insertar
eventos = []

# Leer y preparar los eventos
with open(archivo_csv, "r", encoding="utf-8") as f:
    lector = csv.reader(f)
    for fila in lector:
        if len(fila) != 8:
            continue
        evento = {
            "_index": indice,
            "_source": {
                "id": fila[0],
                "categoria": fila[1],
                "tipo": fila[2],
                "comuna": fila[3],
                "calle": fila[4],
                "lat": float(fila[5]),
                "lon": float(fila[6]),
                "location": {
                    "lat": float(fila[5]),
                    "lon": float(fila[6])
                },
                "timestamp": int(fila[7])
            }
        }
        eventos.append(evento)

# Cargar en Elasticsearch
helpers.bulk(es, eventos)
print(f"✅ Se cargaron {len(eventos)} eventos en el índice '{indice}'.")
