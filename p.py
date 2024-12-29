import streamlit as st
import requests
from bs4 import BeautifulSoup

# Título de la aplicación
st.title("Buscador de referencias en una página web")

# Instrucciones
st.write("Ingresa una palabra y buscaré todas las referencias a esa palabra en la página [mi.tv](https://mi.tv)")

# Entrada del usuario
palabra = st.text_input("Palabra para buscar:")

# Botón de búsqueda
if st.button("Buscar"):
    if palabra:
        try:
            # URL de la página
            url = "https://mi.tv"
            st.write(f"Buscando en {url}...")

            # Realizar la solicitud GET
            response = requests.get(url)
            response.raise_for_status()  # Verifica si hubo errores en la solicitud

            # Analizar el contenido con BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            texto = soup.get_text()

            # Buscar la palabra en el texto
            resultados = [line for line in texto.split("\n") if palabra.lower() in line.lower()]

            # Mostrar resultados
            if resultados:
                st.write(f"Se encontraron {len(resultados)} referencias a la palabra '{palabra}':")
                for resultado in resultados:
                    st.write(f"- {resultado.strip()}")
            else:
                st.write(f"No se encontraron referencias a la palabra '{palabra}' en la página.")
        except Exception as e:
            st.error(f"Error al buscar en la página: {e}")
    else:
        st.warning("Por favor, ingresa una palabra para buscar.")