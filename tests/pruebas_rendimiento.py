import time
import requests

BASE_URL = "http://localhost:8000"

def medir_tiempo(endpoint, params=None):
    # Mide cuánto demora una consulta a un endpoint
    inicio = time.time()
    respuesta = requests.get(f"{BASE_URL}{endpoint}", params=params)
    duracion = time.time() - inicio
    return duracion, respuesta.status_code

def probar_eventos_recientes(n=100):
    print("Prueba: eventos recientes (Redis)")
    tiempos = []
    for _ in range(n):
        duracion, status = medir_tiempo("/eventos/recientes")
        if status == 200:
            tiempos.append(duracion)
    promedio = sum(tiempos) / len(tiempos)
    print(f"Tiempo promedio: {promedio:.4f} segundos\n")

def probar_eventos_zona(ciudad="Pudahuel", n=100):
    print(f"Prueba: eventos por ciudad '{ciudad}' (PostgreSQL)")
    tiempos = []
    for _ in range(n):
        duracion, status = medir_tiempo("/eventos/zona", {"ciudad": ciudad})
        if status == 200:
            tiempos.append(duracion)
    promedio = sum(tiempos) / len(tiempos)
    print(f"Tiempo promedio: {promedio:.4f} segundos\n")

def probar_eventos_tipo(tipo="ROAD_CLOSED", n=100):
    print(f"Prueba: eventos por tipo '{tipo}' (PostgreSQL)")
    tiempos = []
    for _ in range(n):
        duracion, status = medir_tiempo("/eventos/tipo", {"tipo": tipo})
        if status == 200:
            tiempos.append(duracion)
    promedio = sum(tiempos) / len(tiempos)
    print(f"Tiempo promedio: {promedio:.4f} segundos\n")

if __name__ == "__main__":
    probar_eventos_recientes()
    probar_eventos_zona("Pudahuel")
    probar_eventos_tipo("HAZARD")

