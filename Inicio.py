import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Mi Aplicación",
    page_icon="🚀",
    layout="wide",  # Usa el ancho completo de la página
    initial_sidebar_state="expanded",  # La barra lateral está expandida por defecto
)

# Cabecera
st.title("Bienvenido a mi aplicación")

# Subcabecera
st.subheader("Esta es una aplicación interactiva creada con Streamlit")

# Imagen
st.image("img\leon.jpg", use_column_width=True)

# Botón interactivo
if st.button("Haz clic en mí"):
    st.balloons()

# Deslizador interactivo
value = st.slider("Desliza el control deslizante", 0, 100, 50)
st.write(f"Has seleccionado {value}")

# Gráfico interactivo
import pandas as pd
import numpy as np

# Genera algunos datos aleatorios
data = pd.DataFrame(
    np.random.randn(50, 2)/[50, 50] + [6.2442, -75.5812],
    columns=['lat', 'lon']
)

st.map(data)