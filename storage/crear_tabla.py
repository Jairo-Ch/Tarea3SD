import psycopg2

conn = psycopg2.connect(
    dbname="trafico",
    user="jairo",
    password="1234",
    host="localhost"
)

cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS eventos (
    uuid TEXT PRIMARY KEY,
    tipo TEXT,
    subtipo TEXT,
    ciudad TEXT,
    calle TEXT,
    lat DOUBLE PRECISION,
    lon DOUBLE PRECISION,
    usuario TEXT,
    fecha BIGINT
);
""")
conn.commit()
cur.close()
conn.close()

print("✅ Tabla 'eventos' creada con éxito.")
