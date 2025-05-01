import pandas as pd
import plotly.express as px
import streamlit as st

try:
    df_car_data = pd.read_csv('datasets/vehicles_us.csv')

    st.header('Graficas de datos sobre vehículos en Estados Unidos')
    hist_button = st.button('Crear histograma')
    disp_button = st.button('Crear gráfico de dispersión')
    
except Exception as e:
    st.write('Error al cargar el archivo CSV:', e)

if hist_button: # al hacer clic en el botón, se ejecuta el siguiente bloque de código
    
    try:
        # Escribir el mensaje
        st.write('El histograma para el conjunto de vehículos en el conjunto de datos.')
        
        # Crear el histograma
        fig1 = px.histogram(df_car_data, x='odometer', title='Histograma "odometer"')
        
        # Mostrar el ploty interactive
        st.plotly_chart(fig1, use_container_width=True)
        
    except Exception as e:
        st.write('Error al crear el histograma:', e)

if disp_button: # al hacer clic en el botón, se ejecuta el siguiente bloque de código
    
    try:
        # Escribir el mensaje
        st.write('El gráfico de dispersión para el conjunto de vehículos en el conjunto de datos.')
        
        # Crear el gráfico de dispersión
        fig2 = px.scatter(df_car_data, x='odometer', y='price', title='Gráfico de dispersión "odometer" vs "price"')
        
        # Mostrar el ploty interactive
        st.plotly_chart(fig2, use_container_width=True)
        
    except Exception as e:
        st.write('Error al crear el gráfico de dispersión:', e)

