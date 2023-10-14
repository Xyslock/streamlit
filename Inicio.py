import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Pagina",
    page_icon="🚀",
    layout="wide",  # Usa el ancho completo de la página
    initial_sidebar_state="expanded",  # La barra lateral está expandida por defecto
)

# Cabecera
st.title("Bienvenido a mi aplicación")

# Subcabecera
st.subheader("Esta es una aplicación interactiva creada con Streamlit")