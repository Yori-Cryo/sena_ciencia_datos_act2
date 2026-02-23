import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

st.title("Bases de Datos en la Nube: Firebase Firestore")

st.markdown("""
### Ejercicio
Firebase es otra opción excelente adoptada por múltiples startups para almacenar datos en tiempo real.

**Instrucciones:**
1. Asume que se te proporcionó un archivo de credenciales de servicio `llave_secreta.json`.
2. Escribe el **código teórico (usando st.code() o conectándote si tienes tu propia bd)** que emplearías con `firebase_admin` para arrancar la aplicación y obtener el cliente de la base de datos.
3. El objetivo sería conectarse a la colección `vehiculos` de tu Firestore y traer todos los documentos.
4. Indica cómo convertirías la respuesta iterando los documentos para extraer su `to_dict()`.
5. Convierte esa lista a un DataFrame `df_firebase` final.
""")

st.subheader("Tu resultado:")
st.markdown("Escribe en la parte de abajo el código que usarías para lograr el objetivo. Si usas código comentado/teórico, compártelo adentro de `st.code()`.")

# ESTUDIANTE: Escribe tu código a continuación
try:
    # 1️⃣ Cargar credenciales
    cred = credentials.Certificate("para-la-clase-firebase-adminsdk-fbsvc-d627e2b998.json")

    # 2️⃣ Inicializar Firebase (evita error si ya está inicializado)
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)

    # 3️⃣ Obtener cliente Firestore
    db = firestore.client()

    # 4️⃣ Conectarse a colección 'vehiculos'
    coleccion = db.collection("vehiculos")

    # 5️⃣ Traer todos los documentos
    docs = coleccion.stream()

    lista_documentos = []

    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id  # Guardamos el ID del documento
        lista_documentos.append(data)

    # 6️⃣ Convertir a DataFrame
    df_firebase = pd.DataFrame(lista_documentos)

    st.success("Conexión exitosa a Firebase Firestore 🔥")
    st.dataframe(df_firebase)

except Exception as e:
    st.error(f"Error al conectar con Firestore: {e}")

