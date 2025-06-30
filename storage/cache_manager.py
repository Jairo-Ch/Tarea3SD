import redis
import json

# Conexión a Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def guardar_evento(evento, ttl=300):
    # Guarda un evento en Redis con tiempo de expiración (por defecto 5 minutos)
    clave = f"evento:{evento['uuid']}"
    r.set(clave, json.dumps(evento), ex=ttl)

def obtener_evento(uuid):
    # Recupera un evento usando su uuid
    clave = f"evento:{uuid}"
    dato = r.get(clave)
    if dato:
        return json.loads(dato)
    return None

def listar_eventos():
    # Lista todas las claves de eventos guardadas en Redis
    return r.keys("evento:*")

def limpiar_cache():
    # Elimina todos los eventos guardados en Redis
    claves = listar_eventos()
    if claves:
        r.delete(*claves)
