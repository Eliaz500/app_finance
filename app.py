import streamlit as st
import pandas as pd
import yfinance as yf
import investpy as inv
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

def home():
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.image('logo.png', width=300)
        st.markdown('---')
        st.title('Home')
        st.markdown('---')

def panorama():
    st.title('Panorama do Mercado')

def mapa_mensal():
    st.title('Rentabilidade Mensais')

def fundamentos():
    st.title('Fundamentos')


def main():
    st.sidebar.image('logo.png', width=100)
    st.sidebar.title('Finance App')
    st.sidebar.markdown('---')
    lista_menu = ['Home', 'Panorama do Mercado', 'Rentabilidade Mensais', 'Fundamentos']
    escolha = st.sidebar.radio('Menu', lista_menu)

    if escolha == 'Home':
        home()
    if escolha == 'Panorama do Mercado':
        panorama()
    if escolha == 'Rentabilidade Mensais':
        mapa_mensal()
    if escolha == 'Fundamentos':
        fundamentos()


main()
