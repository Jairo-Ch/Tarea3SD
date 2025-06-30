import json
import csv

# campos que exportaremos 
CAMPOS = ["uuid", "tipo", "subtipo", "ciudad", "calle", "lat", "lon", "fecha"]

with open("eventos.json", "r", encoding="utf-8") as f_json:
    eventos = json.load(f_json)

with open("eventos_crudo.csv", "w", newline="", encoding="utf-8") as f_csv:
    writer = csv.DictWriter(f_csv, fieldnames=CAMPOS)
    writer.writeheader()
    for evento in eventos:
        fila = {campo: evento.get(campo, "") for campo in CAMPOS}
        writer.writerow(fila)

print(f"Archivo eventos.csv generado con {len(eventos)} filas.")
