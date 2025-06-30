import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo desde el entorno local
df = pd.read_csv('eventos_por_tipo.csv', header=None, names=['Tipo', 'Cantidad'])

# Ordenar descendente
df = df.sort_values(by='Cantidad', ascending=False)

# Crear gráfico
plt.figure(figsize=(12,6))
plt.bar(df['Tipo'], df['Cantidad'])
plt.xticks(rotation=90)
plt.title('Cantidad de eventos por tipo')
plt.xlabel('Tipo de evento')
plt.ylabel('Cantidad')
plt.tight_layout()

# Guardar en el entorno local
plt.savefig('eventos_por_tipo.png')
plt.show()
