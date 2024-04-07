import streamlit as st
import pandas as pd
import plotly.express as px

# lendo os dados do arquivo csv
car_data = pd.read_csv('../files/vehicles.csv')

st.header('Análise de dados de veículos')  # título

hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
