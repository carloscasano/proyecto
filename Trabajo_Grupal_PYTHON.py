

############## Desarrolle su codigo a continuacion ###################

#Librerias
import datetime       as dt
import streamlit      as st
import pandas         as pd
import numpy          as np
import pip
pip.main(['install','plotly.express'])
import plotly.express as px
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
st.title(':satellite_antenna: :blue[Catálogo Sísmico del Perú (1960 - 2023)]')
#st.divider()
#****************************************************
#    SIDEBAR
#****************************************************
# with st.sidebar:
#     add_selectbox = st.selectbox('Departamento: ',
#                                  ['Amazonas','Ancash','Apurimac', 'Arequipa', 'Ayacucho', 'Cajamarca', 'Cusco', 'Huancavelica', 'Huánuco',
#                                   'Ica', 'Junin', 'La Libertad', 'Lambayeque', 'Lima', 'Loreto', 'Madre de Dios', 'Moquegua', 'Pasco',
#                                   'Piura', 'Puno', 'San Martin', 'Tacna', 'Tumbes', 'Ucayali'],
#                                  1)
#     add_selectbox = st.selectbox('Magnitud (Mw): ',
#                                  ['3.0','4.0','5.0','6.0','7.0','8.0'],
#                                  1)
#     add_selectbox = st.selectbox('Profundidad (km)): ',
#                                  ['60','300','750'],
#                                  1)
#     add_slider    = st.slider(label     = 'Latitud',
#                            min_value = -23.4000,
#                            max_value =  -1.5000,
#                            value     = -12.0453,
#                            step      =   0.5000)
#     add_slider = st.slider(label     = "Longitud",
#                            min_value = -82.8937,
#                            max_value = -66.9807,
#                            value     = -77.0308,
#                            step      =   0.1)
#****************************************************
#    SLIDER DE FECHAS
#****************************************************
add_slider = st.slider(label='Fecha del evento:',
                       min_value=dt.datetime(1960, 1, 1, 0, 0),
                       max_value=dt.datetime(2023, 12, 31, 0, 0),
                       value=(dt.datetime(1960, 1, 1, 0, 0),
                              dt.datetime(2023, 12, 31, 0, 0)), format='DD/MM/YYYY')
#****************************************************
#    PROCESANDO LOS DATOS
#********************************** ******************
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

# Convertir las fechas en el DataFrame a tipo datetime
df['FECHA_UTC'] = pd.to_datetime(df['FECHA_UTC'], format='%Y%m%d')

#Asignar los colores segùn la columna PROFUNDIDAD
def colores(x):
  if   x <   60             : return '#ff0000' #Rojo
  elif x >=  60  and x < 300: return '#00ff00' #Verde
  elif x >= 300             : return '#0000ff' #Azul
df['color'] = df['PROFUNDIDAD'].apply(colores)

#Asignar los tamaños de los puntos según la columna MAGNITUD
def tamaños(x):
  if   x <  4           : return (x * 10)
  elif x >= 4  and x < 7: return (x * 2000)
  elif x >=  0          : return (x * 5000)
df['tamaño'] = df['MAGNITUD'].apply(tamaños)

# Filtrar el DataFrame según el rango de fechas seleccionado en el slider
filtered_df = df[(pd.to_datetime(df['FECHA_UTC'],
                                 format='%Y%m%d') >= add_slider[0])
              & (pd.to_datetime(df['FECHA_UTC'],
                                 format='%Y%m%d') <= add_slider[1])]

# Filtro de acuerdo a magnitudes
# Superficial = filtered_df[filtered_df['PROFUNDIDAD'] < 60]
# Intermedio = filtered_df[(filtered_df['PROFUNDIDAD'] >= 60) & (filtered_df['PROFUNDIDAD'] < 300)]
# Profundo = filtered_df[filtered_df['PROFUNDIDAD'] >= 300]
# M_baja = filtered_df[filtered_df['MAGNITUD'] < 4]
# M_media = filtered_df[(filtered_df['MAGNITUD'] >= 4) & (filtered_df['MAGNITUD'] < 7)]
# M_alta = filtered_df[filtered_df['MAGNITUD'] >= 7]

#Agregar un botón para mostrar todos los sismos en el rango de fechas
todos = st.sidebar.button ('Todos')

# Agregar checkbox para seleccionar la profundidad
profundidad = st.sidebar.radio('Seleccionar Profundidad:',
                              ['Superficial (profundidad < 60 km)',
                               'Intermedia (60 km <= profundidad < 300 km)',
                               'Profunda (profundidad >= 300 km)'])
magnitud    = st.sidebar.radio('Seleccionar Magnitud:',
                              ['Magnitud_baja ( < 4)',
                               'Magnitud_media ( >=  4 y < 7)',
                               'Magnitud_alta ( >= 7)'])
# Filtrar el DataFrame según la profundidad seleccionada y magnitud seleccionada
# if st.button('Actualizar mapa'):
#   if 'Superficial' in profundidad and 'Magnitud_baja' in magnitud:
#     st.map(Superficial[(Superficial['PROFUNDIDAD'] < 60) & (Superficial['MAGNITUD'] < 4)], latitude='latitude', longitude='longitude', color='#F20505', size=20)
#   elif 'Superficial' in profundidad and 'Magnitud_media' in magnitud:
#     st.map(Superficial[(Superficial['PROFUNDIDAD'] < 60) & (Superficial['MAGNITUD'] >= 4) & (Superficial['MAGNITUD'] < 7)], latitude='latitude', longitude='longitude', color='#F20505', size=50)
#   elif 'Superficial' in profundidad and 'Magnitud_alta' in magnitud:
#     st.map(Superficial[(Superficial['PROFUNDIDAD'] < 60) & (Superficial['MAGNITUD'] >= 7)], latitude='latitude', longitude='longitude', color='#F20505', size=100)
#   elif 'Intermedia' in profundidad and 'Magnitud_baja' in magnitud:
#     st.map(Intermedio[(Intermedio['PROFUNDIDAD'] >= 60) & (Intermedio['PROFUNDIDAD'] < 300) & (Intermedio['MAGNITUD'] < 4)], latitude='latitude', longitude='longitude', color='#05F140', size=20)
#   elif 'Intermedia' in profundidad and 'Magnitud_media' in magnitud:
#     st.map(Intermedio[(Intermedio['PROFUNDIDAD'] >= 60) & (Intermedio['PROFUNDIDAD'] < 300) & (Intermedio['MAGNITUD'] >= 4) & (Intermedio['MAGNITUD'] < 7)], latitude='latitude', longitude='longitude', color='#05F140', size=50)
#   elif 'Intermedia' in profundidad and 'Magnitud_alta' in magnitud:
#     st.map(Intermedio[(Intermedio['PROFUNDIDAD'] >= 60) & (Intermedio['PROFUNDIDAD'] < 300) & (Intermedio['MAGNITUD'] >= 7)], latitude='latitude', longitude='longitude', color='#05F140', size=100)
#   elif 'Profunda' in profundidad and 'Magnitud_baja' in magnitud:
#     st.map(Profundo[(Profundo['PROFUNDIDAD'] >= 300) & (Profundo['MAGNITUD'] < 4)], latitude='latitude', longitude='longitude', color='#1D05F2', size=20)
#   elif 'Profunda' in profundidad and 'Magnitud_media' in magnitud:
#     st.map(Profundo[(Profundo['PROFUNDIDAD'] >= 300) & (Profundo['MAGNITUD'] >= 4) & (Profundo['MAGNITUD'] < 7)], latitude='latitude', longitude='longitude', color='#1D05F2', size=50)
#   elif 'Profunda' in profundidad and 'Magnitud_alta' in magnitud:
#     st.map(Profundo[(Profundo['PROFUNDIDAD'] >= 300) & (Profundo['MAGNITUD'] >= 7)], latitude='latitude', longitude='longitude', color='#1D05F2', size=100)

#
if 'Magnitud_baja'    in magnitud   : filtered_df = filtered_df[(filtered_df['MAGNITUD']    <  4)]
elif 'Magnitud_media' in magnitud   : filtered_df = filtered_df[(filtered_df['MAGNITUD']    >= 4) & (filtered_df['MAGNITUD']     <   7)]
elif 'Magnitud_alta'  in magnitud   : filtered_df = filtered_df[(filtered_df['MAGNITUD']    >  7)]

if   'Superficial'    in profundidad: filtered_df = filtered_df[(filtered_df['PROFUNDIDAD'] < 60)]
elif 'Intermedia'     in profundidad: filtered_df = filtered_df[(filtered_df['PROFUNDIDAD'] >= 60) & (filtered_df['PROFUNDIDAD'] < 300)]
elif 'Profunda'       in profundidad: filtered_df = filtered_df[(filtered_df['PROFUNDIDAD'] >= 300)]

if todos:
    filtered_df = df[(pd.to_datetime(df['FECHA_UTC'],
                                     format='%Y%m%d') >= add_slider[0])
                   & (pd.to_datetime(df['FECHA_UTC'],
                                     format='%Y%m%d') <= add_slider[1])]
extracto_df  = filtered_df.copy()
resumido1_df = extracto_df.groupby(by=['MAGNITUD']   ).count().sort_values(by='MAGNITUD')
resumido2_df = extracto_df.groupby(by=['PROFUNDIDAD']).count().sort_values(by='PROFUNDIDAD')
resumido1_df = resumido1_df.rename(columns={'ID': 'Eventos'})
resumido2_df = resumido2_df.rename(columns={'ID': 'Eventos'})
resumen1 = px.bar(resumido1_df, x = resumido1_df.index, y = 'Eventos'  , orientation = "v", width = 20, height = 200) #title = "<b>Gráfico resumen</b>" )
resumen2 = px.bar(resumido2_df, x = resumido2_df.index, y = 'Eventos'  , orientation = "v", width = 20, height = 200) #title = "<b>Gráfico resumen</b>" )
resumen1.update_layout(plot_bgcolor = "rgba(0,0,0,0)", xaxis=(dict(showgrid = False)))
resumen2.update_layout(plot_bgcolor = "rgba(0,0,0,0)", xaxis=(dict(showgrid = False)))

#if st.button('Actualizar mapa'):
caja1_1, caja1_2 = st.columns(2)
with caja1_1:   #Gráfico del mapa
     #st.header('Cabecer caja 1 1')
     st.map(filtered_df,latitude='latitude',longitude='longtitude',zoom=4.0,size='tamaño',color='color')
with caja1_2:
     #Grafico de barra para MAGNITUD
     st.plotly_chart(resumen1, use_container_width =True, )
     #Grafico de barra para PROFUNDIDAD
     st.plotly_chart(resumen2, use_container_width =True, )

if filtered_df.shape[0] == 0:st.write('Datos no encontrados.')

########################################################################
