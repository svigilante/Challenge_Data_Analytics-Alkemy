# Challenge_Data_Analytics-Alkemy

En este repositorio se encuentra mi resolución a la consigna del Challenge Data Analytics - Python de [Alkemy](https://www.alkemy.org/)

### Componentes necesarios para el proyecto
En el archivo _[requirements.txt](https://github.com/svigilante/Challenge_Data_Analytics-Alkemy/blob/master/requirements.txt)_ se encuentran las bibliotecas necesarias para el proyecto junto a sus versiones recomendadas.

### Como crear el entorno virtual de Python: ⚙️
1. Primero, con una terminal vamos a ir al directorio donde queremos que se encuentre nuestro entorno virtual (usando "__cd__" y orientandonos con "__ls__" si hace falta)
2. Luego corremos el comando 
```
python3 -m venv <Nombre_del_entornoVirtual>
```
- *AVISO: Previo a esto hay que estar seguro de tener Python, si su sistema operativo es macOS o Linux muy probable que lo tenga, sino debe descargarlo en https://www.python.org junto con pip.*
3. Activamos el entorno escribiendo en la terminal:
- para Mac
```
source <Nombre_del_entornoVirtual>/bin/activate
```
- para Windows
```
<Nombre_del_entornoVirtual>\Scripts\activate.bat
```

4. Instalar las bibliotecas necesarias con el comando:
```
pip3 install <Nombre_Paquete>
```
 - Use los nombres que se encuentran en _[requirements.txt](https://github.com/svigilante/Challenge_Data_Analytics-Alkemy/blob/master/requirements.txt)_.

## Guía de Archivo Principal 🗄️📂
__[main.py](https://github.com/svigilante/Challenge_Data_Analytics-Alkemy/blob/master/main.py)__ es el script Principal, dentro de este encontraremos en la linea 97:
```python
engine = create_engine("postgresql://santi:admin@localhost:5432/alkemy_db")  # Creamos el engine
```
Se puede modificar lo que se le pasa a esa función para que apunte a su base de datos.
 - De esta forma:
 ```
 postgresql://<Usuario>:<Contraseña>@localhost:<Puerto>/<Nombre_Base_de_Datos>
 ```
