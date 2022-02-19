import requests
import pandas as pd
import logging
import os
import re
import config
import time
import sqlalchemy
from sqlalchemy import create_engine

logging.basicConfig(
    filename='myapp.log',
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

logging.debug('Inicio del programa')

current_directory = os.getcwd()  # Directorio de trabajo actual
pathSep = '\\' if os.name == 'nt' else '/'  # Separador de directorios segun sistema operativo


for categoria in config.CATEGORIAS:  # Por categoría nos fijamos si ya existen sus carpetas o si hay que crearlas

    categoria =categoria.rstrip('\r\n')
    foldersPath = f'{current_directory}{pathSep}{categoria}{pathSep}{time.strftime("%Y-%B")}'  # Directorio a crear (con carpetas)

    logging.debug(f'Las carpetas necesarias para {categoria} ya estan presentes') if os.path.exists(foldersPath) else logging.debug(f'Creando directorios: {foldersPath}')

    os.makedirs(foldersPath, exist_ok=True)  # Se crean las carpetas si es que no existian

    try:
        logging.debug(f'Haciendo request para conseguir csv de {categoria}')
        matchPattern = re.compile(r'(?<=class="btn btn-green btn-block" href=").*?(?=">DESCARGAR<\/a>)')  # Patron RegEx para extraer el link de descarga del HTML
        r = requests.get([config.URL_MUSEOS, config.URL_CINES, config.URL_BIBLIOTECAS][config.CATEGORIAS.index(categoria)])  # Hacemos la request
        linkDescarga = matchPattern.findall(r.text)[0]
        print(linkDescarga)
        rDescarga = requests.get(f"{linkDescarga}")  # Request al link de descarga para luego conseguir el csv

    except Exception as e:
        logging.exception(f'Hubo una excepción: {e}')

    with open(f'{foldersPath}{pathSep}{categoria}{time.strftime("-%d-%m-%Y")}.csv', 'wb') as f:
        logging.debug(f'Guardando archivo csv de {categoria}')
        f.write(rDescarga.content)  # Escribimos el contenido de la request (el csv) en las carpetas donde tienen que estar como "categoria-dia-mes-año.csv"


# Proceso los Datos

# Armo los dataframes de cada categoría para normalizar la información luego
logging.debug(f'Creando dataframe a partir de csv de museos')
df_museos = (pd.read_csv(f'{current_directory}{pathSep}museos{pathSep}{time.strftime("%Y-%B")}{pathSep}museos{time.strftime("-%d-%m-%Y")}.csv')).rename(columns= {"fuente": "Fuente"})

logging.debug(f'Creando dataframe a partir de csv de cines')
df_cines = pd.read_csv(f'{current_directory}{pathSep}cines{pathSep}{time.strftime("%Y-%B")}{pathSep}cines{time.strftime("-%d-%m-%Y")}.csv')

logging.debug(f'Creando dataframe a partir de csv de bibliotecas')
df_bibliotecas = pd.read_csv(f'{current_directory}{pathSep}bibliotecas{pathSep}{time.strftime("%Y-%B")}{pathSep}bibliotecas{time.strftime("-%d-%m-%Y")}.csv')

logging.debug(f'Filtrando dataframe de museos y renombrando columnas')
df_museosFiltrado = df_museos.drop(config.museoFilter, 1).rename(columns= config.museosRenames_dict)

logging.debug(f'Filtrando dataframe de cines y renombrando columnas')
df_cinesFiltrado = df_cines.drop(config.cineFilter, 1).rename(columns= config.cinesRenames_dict)

logging.debug(f'Filtrando dataframe de bibliotecas y renombrando columnas')
df_bibliotecasFiltrado = df_bibliotecas.drop(config.bibliotecaFilter, 1).rename(columns= config.bibliotecasRenames_dict)


logging.debug(f'Creando dataframe de Tabla Unica')
df_unicaTabla = pd.concat([df_museosFiltrado, df_cinesFiltrado, df_bibliotecasFiltrado], ignore_index=True)

# Dataframe para segunda tabla con criterio: Cantidad de registros totales por categoría, Cantidad de registros totales por fuente, Cantidad de registros por provincia y categoría
logging.debug(f'Creando dataframe de Tabla 2')

df_PreTabla2 = pd.concat([df_museos.rename(columns= config.museosRenames_dict), df_cines.rename(columns= config.cinesRenames_dict), df_bibliotecas.rename(columns= config.bibliotecasRenames_dict)], ignore_index=True)

df_PreTabla2Fuente = df_PreTabla2.groupby(["provincia", "categoria"])[["Fuente"]].size().to_frame("Cant. Total Fuentes")
df_PreTabla2categoria = df_PreTabla2.groupby(["provincia", "categoria"])[["categoria"]].size().to_frame("Cant. Total categoria")
df_Tabla2 = pd.concat([df_PreTabla2Fuente, df_PreTabla2categoria], axis=0)

df_Tabla2.insert(0, 'Fecha de Carga', f'{time.strftime("%d/%m/%Y")}')  # Insertamos columna Fecha de Carga

# Dataframe para tercer tabla con criterio: Provincia, Cantidad de pantallas, Cantidad de butacas y Cantidad de espacios INCAA
logging.debug(f'Creando dataframe de Tabla 3')

df_PreTabla3 = df_cines.rename(columns= config.cinesRenames_dict)
df_PreTabla3['espacio_INCAA'] = df_PreTabla3['espacio_INCAA'].map({"SI": 1, "si":1, "Si":1})  # Cambio los SI de la columna espacio INCAA por 1
df_PreTabla3_Prov = df_PreTabla3.groupby(["provincia"])[["Pantallas", "Butacas", "espacio_INCAA"]].sum()
df_Tabla3 = df_PreTabla3_Prov.rename(columns={'Pantallas':'Cantidad de Pantallas',
                                              'Butacas': 'Cantidad de Butacas',
                                              'espacio_INCAA':'Cantidad de espacios INCAA'})

df_Tabla3.insert(0, 'Fecha de Carga', f'{time.strftime("%d/%m/%Y")}')  # Insertamos columna Fecha de Carga

logging.debug(f'Creando engine para Base de Datos')
engine = create_engine("postgresql://santi:admin@localhost:5432/alkemy_db")  # Creamos el engine

# Actualizamos las tablas o las creamos si no estan creadas
logging.debug(f'Actualizando Base de Datos...')
df_unicaTabla.to_sql("Tabla Unica", con=engine, if_exists="replace")  # Tabla Unica
df_Tabla2.to_sql("Tabla_Prov_Cat", con=engine, if_exists="replace")  # Tabla con Cantidad de registros totales por categoría, Cantidad de registros totales por fuente, Cantidad de registros por provincia y categoría
df_Tabla3.to_sql("Tabla_Cines", con=engine, if_exists="replace")  # Tabla con Provincia, Cantidad de pantallas, Cantidad de butacas y Cantidad de espacios INCAA
logging.debug(f'Fin del Programa')
