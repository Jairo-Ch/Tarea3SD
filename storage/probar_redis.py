import redis


r= redis.Redis(host='localhost', port=6379, decode_responses=True)

r.set("evento:prueba", "Choque en Kennedy", ex=60)

valor = r.get("evento:prueba")

print("Valor desde Redis: ", valor)