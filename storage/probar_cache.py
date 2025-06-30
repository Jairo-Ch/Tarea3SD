from cache_manager import guardar_evento, obtener_evento, listar_claves, vaciar_cache

evento_de_prueba = {
    "uuid": "abc123",
    "tipo": "ACCIDENT",
    "ciudad": "Santiago",
    "calle": "Av. Apoquindo",
    "lat": -33.42,
    "lon": -70.61,
    "usuario": "test",
    "fecha": 123456789
}

# Guardar en cache
guardar_evento(evento_de_prueba)

# Leer desde cache
recuperado = obtener_evento("abc123")
print("Evento recuperado:", recuperado)

# Ver claves actuales
print("Claves en cache:", listar_claves())
