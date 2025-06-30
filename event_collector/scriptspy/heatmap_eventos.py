import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('eventos_por_tipo_y_comuna.csv', header=None, names=['Tipo', 'Calle', 'Cantidad'])

# Crear tabla dinámica
df_pivot = df.pivot_table(index='Calle', columns='Tipo', values='Cantidad', aggfunc='sum', fill_value=0)

# Ordenar calles por total de eventos
df_pivot['Total'] = df_pivot.sum(axis=1)
df_pivot = df_pivot.sort_values(by='Total', ascending=False).drop(columns='Total').head(30)  # Top 30 calles

# Dibujar heatmap
plt.figure(figsize=(12,10))
sns.heatmap(df_pivot, cmap='YlGnBu', linewidths=.5, annot=True, fmt='d')  # Con valores visibles
plt.title('Mapa de calor: Eventos por tipo y calle')
plt.xlabel('Tipo de evento')
plt.ylabel('Calle')
plt.tight_layout()
plt.savefig('mapa_eventos_tipo_calle.png')
plt.show()
