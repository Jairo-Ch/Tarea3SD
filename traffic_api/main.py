from fastapi import FastAPI, Query
import redis
import json
import psycopg2

# Crear la aplicación
app = FastAPI()

# Conexión a Redis
r = redis.Redis(host="redis", port=6379, decode_responses=True)

# Función para conectar a PostgreSQL
def conectar_postgres():
    return psycopg2.connect(
        dbname="trafico",
        user="jairo",
        password="1234",
        host="postgres",
        port="5432"
    )

# Endpoint para obtener eventos recientes
@app.get("/eventos/recientes")
def obtener_eventos_recientes():
    claves = r.keys("evento:*")
    claves = sorted(claves)[:10]  # Se toman solo los primeros 10 eventos
    eventos = []
    for clave in claves:
        dato = r.get(clave)
        if dato:
            eventos.append(json.loads(dato))
    return {"total": len(eventos), "eventos": eventos}

# Endpoint para buscar eventos por ciudad
@app.get("/eventos/zona")
def buscar_eventos_por_ciudad(ciudad: str = Query(...)):
    conn = conectar_postgres()
    cur = conn.cursor()
    cur.execute("""
        SELECT uuid, tipo, subtipo, ciudad, calle, lat, lon, usuario, fecha
        FROM eventos
        WHERE ciudad ILIKE %s
    """, (f"%{ciudad}%",))
    columnas = [desc[0] for desc in cur.description]
    eventos = [dict(zip(columnas, fila)) for fila in cur.fetchall()]
    cur.close()
    conn.close()
    return {"ciudad": ciudad, "total": len(eventos), "eventos": eventos}

# Endpoint para buscar eventos por tipo
@app.get("/eventos/tipo")
def buscar_eventos_por_tipo(tipo: str = Query(..., description="Tipo de evento: ACCIDENT, JAM, POLICE, HAZARD, ROAD_CLOSED, etc.")):
    conn = conectar_postgres()
    cur = conn.cursor()
    cur.execute("""
        SELECT uuid, tipo, subtipo, ciudad, calle, lat, lon, usuario, fecha
        FROM eventos
        WHERE tipo ILIKE %s
    """, (f"%{tipo}%",))
    columnas = [desc[0] for desc in cur.description]
    eventos = [dict(zip(columnas, fila)) for fila in cur.fetchall()]
    cur.close()
    conn.close()
    return {"tipo": tipo, "total": len(eventos), "eventos": eventos}
