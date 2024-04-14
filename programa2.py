# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:14:59 2024

@author: Usuario
"""
#Librerias
import streamlit as st
import pandas    as pd
import numpy     as np
import datetime  as dt
#********************************************
# CONFIGURANDO LA PÁGINA
#********************************************
st.set_page_config(page_title = 'Proyecto IA',
                  page_icon  = 'moneybag:',
                  layout     = 'wide'
                  )
#********************************************
# TITULO DEL DASHBOARDS
#********************************************
#Título del aplicativo
st.title('DASHBOARD DEL CURSO')
st.write('==========================================================')
#********************************************
# GRAFICO 1: SLIDER POR VALORES ENTEROS
#********************************************
txt10 = '1. Slicer de valores enteros'
txt11 = 'Número seleccionado: {}'
#Mostrar slider
st.title(txt10)
n = st.slider("n",
              5,
              100,
              value=(20,30),
              step =1             
             )
#Mostrar texto del slider
st.write(txt11.format(n))
#********************************************
# GRAFICO 2: SLIDER DE HORAS
#********************************************
txt20 = '2. Slicer en horas'
txt21 = 'Fecha de agenda: '
#Mostrar slider
st.title(txt20)
calen = st.slider(txt20,
                  min_value = dt.time(8,0),
                  max_value = dt.time(18,0), 
                  value     = (dt.time(11,30),
                               dt.time(12,45)
                              )
                  #step      = dt.timedelta(hour=1)
              )
st.write(txt21, '(', calen[0], calen[1], ')')
#********************************************
# GRAFICO 3: SLIDER DE DIAS
#********************************************
txt30 = '3. Slicer en días'
txt31 = 'Fecha de agenda: '
#Mostrar slider
st.title(txt30)
fecha = st.slider(txt30,
                   value = dt.datetime(2000, 1, 1, 9, 30),
                   format = 'DD/MM/YYYY - hh:mm'
                   )
st.write('Fecha seleccionada: ( ', fecha.strftime('%d/%m/%Y'),')',)
#********************************************
# GRAFICO 4: GRÁFICO CON DATOS ALEATORIOS
#********************************************
txt40 = '4. Ejemplo de gràfico'
txt41 = 'Eje X'
st.title(txt40)
var = st.slider('n', 5, 100, step = 1)
grf = pd.DataFrame(np.random.randn(var), columns=['data'])
st.line_chart(grf)
#********************************************
# GRAFICO 5: EJEMPLO DE MAPA
#********************************************
txt50 = '5. Mapa del gráfico'
txt51 = 'Estado de Washington'
st.title(txt50)
df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.36, -122.4],
                  columns=['lat','lon']
                 )
st.map(df)
#********************************************
# GRAFICO 4: SLIDER DE DIAS POR RANGO
#********************************************
#txt30 = '4. Slicer en días pòr rangos'
#txt31 = 'Fecha de agenda: '
#Mostrar slider
#st.title(txt30)
#fecha = st.slider(txt30,
#                   value = dt.datetime(2000, 1, 1, 9, 30),
#                   format = 'DD/MM/YYYY - hh:mm'
#                   )
#st.write('Fecha seleccionada: ( ', fecha.strftime('%d/%m/%Y'),')',)

#

#slider_placeholder = st.empty()
##time_range = st.slider("Select a time range", 0, 23, (0, 23))
 
# Update the datetime slider based on the selected time range
##start_date = datetime(2020, 1, 1, time_range[0])
##end_date = start_date + timedelta(hours=time_range[1] - time_range[0])
 
##selected_date = slider_placeholder.slider(
##    "Select a date range",
##    min_value=start_date,
##    max_value=end_date,
##    value=(start_date, end_date),
##    step=timedelta(hours=1),
##)






#grf = pd.DataFrame(np.random.randn(n)
#                  ,columns=['data']
#                  )
#st.line_chart(grf)















