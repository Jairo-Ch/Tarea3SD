import requests
import time
import random

# Configuraciones iniciales
TOTAL_CONSULTAS = 100
LAMBDA = 0.5  # Promedio de llegada de eventos por segundo

ENDPOINTS = [
    "http://localhost:8000/eventos/recientes",
    "http://localhost:8000/eventos/zona?ciudad=Pudahuel",
    "http://localhost:8000/eventos/tipo?tipo=HAZARD",
]

print("Inicio del generador de tráfico (modelo Poisson)")

for i in range(1, TOTAL_CONSULTAS + 1):
    url = random.choice(ENDPOINTS)
    try:
        inicio = time.time()
        respuesta = requests.get(url, timeout=5)
        fin = time.time()
        print(f"[{i}/{TOTAL_CONSULTAS}] {url} | Código: {respuesta.status_code} | Tiempo: {fin - inicio:.4f} segundos")
    except Exception as error:
        print(f"Error al consultar {url}: {error}")

    tiempo_espera = random.expovariate(LAMBDA)
    time.sleep(tiempo_espera)

print("Generador de tráfico Poisson finalizado.")
