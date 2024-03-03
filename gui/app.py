import streamlit as st
from emoji import emojize

st.title('Sistema de Recuperación de Información')

col1, col2 = st.columns([4, 1])

query = col1.text_input("Introduce tu consulta aquí", key="query_input")

if query:
    st.session_state['saved_query'] = query

# Crear el botón de búsqueda con un emoji en la segunda columna
if col2.button(emojize(":mag_right: Buscar")):
    # Lógica de búsqueda aquí
    st.write('Has hecho clic en el botón!')
