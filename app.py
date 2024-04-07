import streamlit as st
import pandas as pd
import plotly.express as px

# lendo os dados do arquivo csv
car_data = pd.read_csv('vehicles.csv')

st.header('Análise de dados de veículos')  # título

# criar um checkbox para histograma
hist_checkbox = st.checkbox('Criar um histograma')
# criar um checkbox para gráfico de dispersão
scatter_checkbox = st.checkbox('Criar gráfico de dispersão')
start_button = st.button('Gerar gráfico')  # criar um botão para gerar gráfico

if hist_checkbox:
    hist_selectbox = st.selectbox('Escolha o histograma a ser criado:', ('Odômetro',
                                                                         'Tipo de veículo', 'Condição do veículo', 'Dias de listado'))
if scatter_checkbox:
    scatter_selectbox = st.selectbox(
        'Escolha o gráfico de dispersão a ser criado:', ('Odômetro x Preço', 'Ano x Preço'))

if start_button:  # se o botão for pressionado
    if hist_checkbox:  # se histograma for selecionado
        if hist_selectbox == 'Odômetro':
            # escrever uma mensagem
            st.write(
                'Criando um histograma para a milhagem exibida no odômetro dos veículos...')
            # criar um histograma
            fig = px.histogram(car_data, x='odometer', labels={
                'odometer': 'Odômetro em Milhas'})
            fig.show()  # exibindo
        # escrever uma mensagem
        if hist_selectbox == 'Tipo de veículo':
            st.write(
                'Criando um histograma para o tipo de veículo dos veículos...')
            # criar um histograma
            fig = px.histogram(car_data, x='type', labels={
                'type': 'Tipo de Veículo'})
            fig.show()  # exibindo
        if hist_selectbox == 'Condição do veículo':
            # escrever uma mensagem
            st.write(
                'Criando um histograma para a condição dos veículos...')
            # criar um histograma
            fig = px.histogram(car_data, x='condition', labels={
                'condition': 'Condição do Veículo'})
            fig.show()  # exibindo
        if hist_selectbox == 'Dias de listado':
            # escrever uma mensagem
            st.write(
                'Criando um histograma para o tempo (em dias) desde que os veículos foram listados...')
            # criar um histograma
            fig = px.histogram(car_data, x='days_listed', labels={
                'days_listed': 'Dias desde Listado'})
            fig.show()  # exibindo

        # exibir um gráfico Plotly interativo
        st.plotly_chart(fig, use_container_width=True)

    if scatter_checkbox:  # se gráfico de dispersão for selecionado
        if scatter_selectbox == 'Odômetro x Preço':
            # escrever uma mensagem
            st.write(
                'Criando um gráfico de dispersão para a milhagem exibida no odômetro e o preço dos veículos...')
            # criar um gráfico de dispersão
            fig2 = px.scatter(car_data, x='odometer', y='price', labels={
                'odometer': 'Odômetro em Milhas', 'price': 'Preço em Dólares'})
            fig2.show()  # exibindo
        if scatter_selectbox == 'Ano x Preço':
            # escrever uma mensagem
            st.write(
                'Criando um gráfico de dispersão para o ano de fabricação e o preço dos veículos...')
            # criar um gráfico de dispersão
            fig2 = px.scatter(car_data, x='model_year', y='price', labels={
                'model_year': 'Ano de fabricação', 'price': 'Preço em Dólares'})
            fig2.show()

        # exibir um gráfico Plotly interativo
        st.plotly_chart(fig2, use_container_width=True)
