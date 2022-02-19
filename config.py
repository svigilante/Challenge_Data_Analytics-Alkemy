CATEGORIAS = ["museos", "cines", "bibliotecas"]

URL_MUSEOS = "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d"
URL_CINES = "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae"
URL_BIBLIOTECAS = "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7"


museoFilter = ["Observaciones",
               "subcategoria",
               "piso",
               "cod_area",
               "Latitud",
               "Longitud",
               "TipoLatitudLongitud",
               "Info_adicional",
               "Fuente",
               "jurisdiccion",
               "año_inauguracion",
               "IDSInCA"]

cineFilter = ["Observaciones",
              "Piso",
              "cod_area",
              "Latitud",
              "Longitud",
              "TipoLatitudLongitud",
              "Información adicional",
              "Fuente",
              "tipo_gestion",
              "Pantallas",
              "Butacas",
              "espacio_INCAA",
              "año_actualizacion",
              "Departamento"]

bibliotecaFilter = ["Observacion",
                    "Subcategoria",
                    "Piso",
                    "Cod_tel",
                    "Latitud",
                    "Longitud",
                    "TipoLatitudLongitud",
                    "Información adicional",
                    "Fuente",
                    "Tipo_gestion",
                    "año_inicio",
                    "Año_actualizacion",
                    "Departamento"]


museosRenames_dict = {"Cod_Loc": "cod_localidad",
                      "IdProvincia": "id_provincia",
                      "IdDepartamento": "id_departamento",
                      "direccion": "domicilio",
                      "CP": "codigo postal",
                      "Mail": "mail",
                      "Web": "web"}

cinesRenames_dict = {"Cod_Loc": "cod_localidad",
                     "IdProvincia": "id_provincia",
                     "IdDepartamento": "id_departamento",
                     "Nombre": "nombre",
                     "Dirección": "domicilio",
                     "Localidad": "localidad",
                     "Provincia": "provincia",
                     "CP": "codigo postal",
                     "Categoría": "categoria",
                     "Teléfono": "telefono",
                     "Mail": "mail",
                     "Web": "web"}

bibliotecasRenames_dict = {"Cod_Loc": "cod_localidad",
                           "IdProvincia": "id_provincia",
                           "IdDepartamento": "id_departamento",
                           "Nombre": "nombre",
                           "Domicilio": "domicilio",
                           "Localidad": "localidad",
                           "Provincia": "provincia",
                           "CP": "codigo postal",
                           "Categoría": "categoria",
                           "Teléfono": "telefono",
                           "Mail": "mail",
                           "Web": "web"}
