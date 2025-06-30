import requests
import random
import time

# Configuración
ENDPOINTS = [
    "http://localhost:8000/eventos/recientes",
    "http://localhost:8000/eventos/zona?ciudad=Pudahuel",
    "http://localhost:8000/eventos/tipo?tipo=HAZARD"
]

# Intervalo de espera entre consultas (en segundos)
INTERVALO_MIN = 0.5
INTERVALO_MAX = 2.0

# Número de consultas a realizar
TOTAL_CONSULTAS = 100

print("Iniciando generador de tráfico uniforme...")

for i in range(TOTAL_CONSULTAS):
    endpoint = random.choice(ENDPOINTS)
    try:
        inicio = time.time()
        respuesta = requests.get(endpoint, timeout=5)
        duracion = time.time() - inicio
        print(f"{i+1}/{TOTAL_CONSULTAS} - {endpoint} - Código: {respuesta.status_code} - Tiempo: {duracion:.4f}s")
    except Exception as error:
        print(f"Error al consultar: {error}")

    espera = random.uniform(INTERVALO_MIN, INTERVALO_MAX)
    time.sleep(espera)

print("Generador de tráfico uniforme finalizado.")
