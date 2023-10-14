import streamlit as st
import pandas as pd


ventas_vehiculos = st.file_uploader("Cargar archivo", type=["csv"])
if ventas_vehiculos is not None:
    df = pd.read_csv(ventas_vehiculos)

    st.write("Valores faltantes:")
    st.write(df.isnull().sum())

    @st.experimental_memo
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(df)
    st.download_button(
        "Descargar datos limpios",
        csv,
        "datos_limpios.csv",
        "text/csv",
        key='download-csv'
    )
