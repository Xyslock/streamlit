import streamlit as st
import numpy as np

st.title('Calculadora de Notas de Estudiantes')

# Entrada de datos
nombre = st.text_input('Nombre del estudiante')
num_notas = st.number_input('Número de notas a ingresar', min_value=1, max_value=10, step=1)

notas = []
for i in range(int(num_notas)):
    nota = st.number_input(f'Ingrese la nota {i+1}', min_value=0.0, max_value=10.0)
    notas.append(nota)

# Cálculo del promedio
if st.button('Calcular Promedio') and notas:
    promedio = np.mean(notas)
    st.write(f'El promedio de {nombre} es {promedio:.2f}')