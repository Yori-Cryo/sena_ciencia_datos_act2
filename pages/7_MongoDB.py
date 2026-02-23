import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.title("Bases de Datos en la Nube: MongoDB")

st.markdown("""
### Ejercicio
MongoDB es una base de datos NoSQL muy popular que almacena la información de forma muy similar a JSON.

**Instrucciones:**
1. Imagina que tienes acceso a un clúster de MongoDB Atlas. Para este ejercicio no necesitas conectarte realmente a la base de datos a menos que tengas un clúster de prueba.
2. Basándote en el material de clase, escribe el **código necesario (comentado si no tienes conexión)** para conectarte usando `pymongo` y la clase `MongoClient`.
3. Supón que la base de datos se llama `Veterinaria` y la colección se llama `mascotas`.
4. El código debe incluir cómo extraer los documentos y convertirlos en el DataFrame `df_mongo`.
""")

st.subheader("Tu resultado:")
st.markdown("Si no tienes la conexión real, escribe tu código usando `st.code()` para demostrar cómo lo harías teóricamente.")

# ESTUDIANTE: Escribe tu código (o tu st.code teórico) a continuación

cliente = MongoClient("mongodb+srv://santivelgu201109_db_user:1234@cluster0.8wudie4.mongodb.net/")

data = cliente["Veterinaria"]
collection = data["mascotas"]
df_mongo = pd.DataFrame(list(collection.find()))
st.dataframe(df_mongo)
