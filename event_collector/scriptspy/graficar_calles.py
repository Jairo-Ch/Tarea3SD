import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo CSV
df = pd.read_csv('eventos_por_tipo_y_comuna.csv', header=None, names=['Tipo', 'Calle', 'Cantidad'])

# Agrupar por calle y sumar las cantidades
top_calles = df.groupby('Calle')['Cantidad'].sum().sort_values(ascending=False).head(10)

# Crear gráfico
plt.figure(figsize=(12, 6))
top_calles.plot(kind='bar')
plt.title('Top 10 calles con más eventos')
plt.xlabel('Calle')
plt.ylabel('Cantidad de eventos')
plt.xticks(rotation=45)
plt.tight_layout()

# Guardar como imagen
plt.savefig('top_calles_eventos.png')
plt.show()
