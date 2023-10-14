import streamlit as st
import pandas as pd

# Cargar los datos
df = pd.read_csv('archivos/programas_educacion_superior.csv',sep=";")

# Crear los filtros
st.sidebar.header('Filtros')

# Filtro 1
filtro1 = st.sidebar.selectbox('Filtro 1', df['nombreinstitucion'].unique())
df = df[df['nombreinstitucion'] == filtro1]

# Filtro 2
filtro2 = st.sidebar.selectbox('Filtro 2', df['nombredepartinstitucion'].unique())
df = df[df['nombredepartinstitucion'] == filtro2]

# Filtro 3
filtro3 = st.sidebar.selectbox('Filtro 3', df['nombrenivelformacion'].unique())
df = df[df['nombrenivelformacion'] == filtro3]

# Filtro 4
filtro4 = st.sidebar.selectbox('Filtro 4', df['numeroresolucionacreditacion'].unique())
df = df[df['numeroresolucionacreditacion'] == filtro4]

# Filtro 5
filtro5 = st.sidebar.selectbox('Filtro 5', df['nombrenivelacademico'].unique())
df = df[df['nombrenivelacademico'] == filtro5]

# Filtro 6
filtro6 = st.sidebar.selectbox('Filtro 6', df['numeroresolucionacreditacion'].unique())
df = df[df['numeroresolucionacreditacion'] == filtro6]

# Filtro 7
filtro7 = st.sidebar.selectbox('Filtro 7', df['nombrenbc'].unique())
df = df[df['nombrenbc'] == filtro7]

# Filtro 8
filtro8 = st.sidebar.selectbox('Filtro 8', df['nombredepartprograma'].unique())
df = df[df['nombredepartprograma'] == filtro8]

# Filtro 9
filtro9 = st.sidebar.selectbox('Filtro 9', df['nombreorigeninstitucional'].unique())
df = df[df['nombreorigeninstitucional'] == filtro9]

# Filtro 10
filtro10 = st.sidebar.selectbox('Filtro 10', df['codigomunicipioprograma'].unique())
df = df[df['codigomunicipioprograma'] == filtro10]

# Mostrar los datos filtrados
st.dataframe(df)