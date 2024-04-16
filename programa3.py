# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:45:41 2024
@author: Usuario
"""
#Librerias
import datetime  as dt
import streamlit as st
import pandas    as pd
import pip
#import openpyxl
#import numpy     as np
pip.main(['install','openpyxl==1.4.7'])
#pip install  openpyxl
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
#st.header('Catálogo Sísmico')
#st.subheader('Grupo Nº5')
st.divider()
#****************************************************
#    SIDEBAR
#****************************************************
with st.sidebar:
    add_slider = st.slider(label     = 'Latitud',
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
#st.write('Fecha seleccionada: ( ', fecha.strftime('%d/%m/%Y'),')',)
#****************************************************
#    MAPA
#****************************************************
#Extracción de datos
@st.cache_data
def leer_archivo(xarchivo: str,xhoja: str): #-> pd.DataFrame:
    return pd.read_excel(xarchivo , sheet_name=xhoja)
#Leer los datos
A="https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2023.xlsx"
#A='Catalogo1960_2023.xlsx' 
H='Catalogo1960_2023'
df  = leer_archivo(A, H)
#Cambiando de nombre a las columnas de ubicación
df.rename(columns={'LATITUD' :'latitude'  ,
                   'LONGITUD':'longitude'},
          inplace = True)
#Reemplzar por NaN lños valores vacíos
#f = df.fillna(np.nan)
#Eliminar las filas con valores faltantes
#df = df.dropna()
#Mostar el mapa
B = 2
if B == 1:
    st.write(df.head(5))
else:
    st.map(df,
          latitude  = 'latitude'    ,
          longitude = 'longtitude' )#,
          #size     = '',
          #color     = 'Blue')
#**************************************************
# BORRAR
#**************************************************
#@st.cache_data
#def leer_data():
#  archivo = 'TB_UBIGEOS.csv'
#  df      = pd.read_csv(archivo,
#                        sep = ';')
#  return df
#df1 = df.drop(columns = ['id_ubigeo',
#        'ubigeo_reniec'    ,'ubigeo_inei' ,
#        'departamento_inei','departamento',
#        'provincia_inei'   ,'provincia'   ,
#        'distrito'         ,'region'      ,
#        'macroregion_inei' ,'macroregion_minsa',
#        'iso_3166_2'       ,'fips'        ,
#        'superficie'       ,'altitud'     ,
#        'Frontera'     ])
#add_selectbox = st.sidebar.selectbox(
#    "How would you like to be contacted?",
#    ("Email", "Home phone", "Mobile phone")
#)
#tab3, tab2, tab1, tab4 = st.tabs(["Data",
#                                  "Widgets",
#                                  "Texto"
#                                  ,"Tab4"])
#with tab1:
#    st.write ('INTEGRANTES:')
#    st.markdown('- _Carlos Casaño Arzapalo_')
#    st.markdown('- _Juan Heinicke Vercauteren_')
#    st.markdown('- _Carlos Mestanza Novoa_')
#    st.markdown('- _Aricely Sánchez Gómez_')
#    st.markdown('- _Deyvis Victori Abad_')
#    st.code('for i in range(8): foo()')
#with tab2:
#     st.radio('Select one:', [1, 2])
#     st.selectbox('Select', [1,2,3])
#     st.button('Hit me')
#     st.checkbox('Check me out')
#     #st.data_editor('Edit data', data)
#     st.multiselect('Multiselect', [1,2,3])
#     st.slider('Slide me', min_value=0, max_value=20)
#     st.select_slider('Slide to select', options=[1,'2',3,4,5])
#     st.text_input('Enter some text')
#     st.number_input('Enter a number')
#     st.text_area('Area for textual entry')
#     st.date_input('Date input')
#     st.time_input('Time entry')
#     st.file_uploader('File uploader')
#     #st.download_button('On the dl', data)
#     #st.camera_input("Cámara detectada")
#     st.color_picker('Pick a color')
#with tab3:
