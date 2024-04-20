# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:45:41 2024
@author: Carls Casaño
"""
#Librerias
import datetime  as dt
import streamlit as st
import pandas    as pd
import numpy     as np
import pip
pip.main(['install','openpyxl==1.4.7'])
#****************************************************
#Configuracndo la página
#****************************************************
st.set_page_config(page_title = 'Proyecto IA',
                  page_icon  = 'bar_chart:',
                  layout     = 'wide'
                  )
#****************************************************
#    TITULO
#****************************************************
st.title(':satellite_antenna: :blue[Catálogo Sísmico]')
st.divider()
#****************************************************
#    SIDEBAR
#****************************************************
with st.sidebar:
    add_selectbox = st.selectbox('Departamento: ',
                                 ['Lima','Piura','Tacna', '...'],
                                 1)
    add_selectbox = st.selectbox('Magnitud: ',
                                 ['1','2','3','4','5','6','7','8'],
                                 1)
    add_selectbox = st.selectbox('Profundidad (km)): ',
                                 ['1','5','10','15','20'],
                                 1)
    add_slider    = st.slider(label     = 'Latitud',
        min_value = -23.3000,
        max_value =  -1.5000,
        value     = -12.0453,
        step      =   0.5000)
    add_slider = st.slider(label     = "Longitud",
                           min_value = -82.8000,
                           max_value = -67.0000,
                           value     = -77.0308,
                           step      =   0.1)
    add_slider = st.slider(label = 'Fecha del sismo',
                           min_value = dt.datetime(1960,  1,  1, 0, 0),
                           max_value = dt.datetime(2023, 12, 31, 0, 0),
                           value     = dt.datetime(2000,  1,  1, 0, 0),
                           format    = 'DD/MM/YYYY')
#****************************************************
#    MAPA
#****************************************************
#Extracción de datos
@st.cache_data
def leer_archivo(xarchivo: str,xhoja: str): #-> pd.DataFrame:
    return pd.read_excel(xarchivo , sheet_name=xhoja)
#Leer los datos
A="https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2023.xlsx"
H='Catalogo1960_2023'
df  = leer_archivo(A, H)
#Cambiando de nombre a las columnas de ubicación
df.rename(columns={'LATITUD' :'latitude'  ,
                   'LONGITUD':'longitude'},
          inplace = True)
#Reemplzar por NaN lños valores vacíos
df = df.fillna(np.nan)
#Eliminar las filas con valores faltantes
df = df.dropna()
#Mostar el mapa
st.map(df,
       latitude  = 'latitude'  ,
       longitude = 'longtitude' )
