import streamlit as st
from emoji import emojize
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


documentos_booleano = ['Doc1', 'Doc2', 'Doc3']
documentos_escogido = ['DocA', 'DocB', 'DocC']

df = pd.DataFrame({
    'Modelo booleano': documentos_booleano,
    'Modelo escogido': documentos_escogido
})


# Datos de ejemplo para los modelos
modelo_booleano_metricas = {
    'Precision': 0.85,
    'Recall': 0.75,
    'F': 0.80,
    'F1': 0.79,
    'R-Prec.': 0.82,
    'Prop. de fallo': 0.25
}

modelo_escogido_metricas = {
    'Precision': 0.75,
    'Recall': 0.80,
    'F': 0.78,
    'F1': 0.79,
    'R-Prec.': 0.78,
    'Prop. de fallo': 0.30
}

# Crear un gráfico de barras
fig, ax = plt.subplots()

# Datos para el gráfico
metrics = ['Precision', 'Recall', 'F', 'F1', 'R-Prec.', 'Prop. de fallo']
modelo_1_values = [modelo_booleano_metricas[metric] for metric in metrics]
modelo_2_values = [modelo_escogido_metricas[metric] for metric in metrics]

# Definir el ancho de las barras y el desplazamiento
n = len(metrics)
width = 0.25 # Ancho de las barras
r = np.arange(n) # Rango de posiciones en el eje x

# Crear las barras para el primer modelo con colores pastel
modelo_1_bars = ax.bar(r, modelo_1_values, color='lightblue', width=width, edgecolor='black', label='Modelo booleano')

# Crear las barras para el segundo modelo desplazadas con colores pastel
modelo_2_bars = ax.bar(r + width, modelo_2_values, color='lightgreen', width=width, edgecolor='black', label='Modelo escogido')

# Añadir leyenda y título
ax.legend()
ax.set_title('Comparación de Métricas entre Modelos')

# Añadir etiquetas en el eje x
ax.set_xticks(r + width / 2) # Centrar las etiquetas
ax.set_xticklabels(metrics)

# Añadir etiquetas en el eje y
ax.set_ylabel('Valores')
ax.set_xlabel('Métricas')

# Cambiar el color de las barras según el modelo
for bar in modelo_1_bars:
    bar.set_color('lightblue')
for bar in modelo_2_bars:
    bar.set_color('lightgreen')

# Mostrar el gráfico
plt.show()

st.title('Bienvenido a nuestro SRI')

col1, col2 = st.columns([4, 1])

query = col1.text_input("Introduce tu consulta aquí", key="query_input")

if query:
    st.session_state['saved_query'] = query

if col2.button(emojize(":mag_right: Buscar")):
    st.write('Estos son los resultados de nuestro programa: ')
    st.dataframe(df,100000)
    st.pyplot(fig)
