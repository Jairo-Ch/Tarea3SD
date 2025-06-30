import requests
import json
import time
import os
import random

# Límites de la Región Metropolitana
LAT_MIN = -33.75
LAT_MAX = -33.30
LON_MIN = -70.85
LON_MAX = -70.45

# Configuraciones iniciales
RADIO = 0.02
MAX_EVENTOS = 20000
eventos = {}
nuevos_eventos = 0
consultas_realizadas = 0

URL = "https://www.waze.com/live-map/api/georss?top={top}&bottom={bottom}&left={left}&right={right}&env=row&types=alerts,traffic"

# Si existe un archivo anterior, cargar los eventos
if os.path.exists("eventos.json"):
    with open("eventos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        eventos = {e["uuid"]: e for e in datos}
    print(f"Eventos cargados desde eventos.json: {len(eventos)}")

# Bucle para recolectar eventos hasta llegar al máximo
while len(eventos) < MAX_EVENTOS:
    lat_centro = random.uniform(LAT_MIN, LAT_MAX)
    lon_centro = random.uniform(LON_MIN, LON_MAX)

    top = lat_centro
    bottom = lat_centro - RADIO
    left = lon_centro
    right = lon_centro + RADIO

    url_consulta = URL.format(top=top, bottom=bottom, left=left, right=right)
    print(f"Consultando área: {top:.3f}, {left:.3f} -> {bottom:.3f}, {right:.3f}")

    try:
        respuesta = requests.get(url_consulta, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()

        for alerta in datos.get("alerts", []):
            uuid = alerta.get("uuid")
            if uuid and uuid not in eventos:
                eventos[uuid] = {
                    "tipo": alerta.get("type"),
                    "subtipo": alerta.get("subtype"),
                    "ciudad": alerta.get("city"),
                    "calle": alerta.get("street"),
                    "lat": alerta.get("location", {}).get("y"),
                    "lon": alerta.get("location", {}).get("x"),
                    "usuario": alerta.get("reportBy"),
                    "fecha": alerta.get("pubMillis"),
                    "uuid": uuid
                }
                nuevos_eventos += 1
                print(f"Nuevo evento: {alerta.get('type')} en {alerta.get('city')} - {alerta.get('street')}")
                print(f"Eventos registrados: {len(eventos)}")

    except requests.exceptions.Timeout:
        print(f"Se agotó el tiempo de espera al consultar: {url_consulta}")
    except requests.exceptions.RequestException as error:
        print(f"Error al consultar la API: {error}")
    except Exception as error:
        print(f"Error inesperado: {error}")

    consultas_realizadas += 1
    time.sleep(0.2)  # Pausa para no saturar al servidor

# Guardar los eventos obtenidos
with open("eventos.json", "w", encoding="utf-8") as archivo:
    json.dump(list(eventos.values()), archivo, indent=2, ensure_ascii=False)

print("\n--- Resultados finales ---")
print(f"Consultas realizadas: {consultas_realizadas}")
print(f"Nuevos eventos encontrados: {nuevos_eventos}")
print(f"Total de eventos guardados: {len(eventos)}")
print("Archivo eventos.json actualizado.")

