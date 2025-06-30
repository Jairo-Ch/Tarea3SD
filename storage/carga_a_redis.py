import json
from cache_manager import guardar_evento

# Cargar eventos desde eventos.json
with open("../event_collector/eventos.json", "r", encoding="utf-8") as f:
    eventos = json.load(f)

# Guardar los primeros 100 en Redis
for evento in eventos[:100]:
    guardar_evento(evento, ttl=600)  # TTL de 600 segundos (10 min)

print(f"✅ Se cargaron {min(len(eventos), 100)} eventos a Redis.")
