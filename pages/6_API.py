import streamlit as st
import pandas as pd
import requests

st.title("Conexiones Avanzadas: API REST")

st.markdown("""
### Ejercicio
A veces los datos están "vivos" y debes consultarlos a través de una API en internet.

1. Vamos a usar la PokéAPI para obtener algunos datos de Pokémon de forma sencilla. 
2. Realiza una petición `GET` a la siguiente URL: `https://pokeapi.co/api/v2/pokemon?limit=10`
3. Verifica que la petición fue exitosa (`status_code == 200`).
4. Convierte la respuesta a formato JSON.
5. Extrae la lista que viene dentro de la llave `"results"`.
6. Convierte esa lista extraída en un DataFrame llamado `df_pokemon` y muéstralo con Streamlit mediante `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación
# Recuerda usar la librería requests que ya está importada arriba
try:
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10")
    if response.status_code == 200:
        data = response.json()
        df_pokemon = pd.DataFrame(data["results"])

    else:
        st.error(f"Error al obtener los datos: {response.status_code}")
except Exception as e:
    st.error(f"Ocurrió un error al obtener los datos: {e}")

st.dataframe(df_pokemon)
