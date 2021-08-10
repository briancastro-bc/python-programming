#Importar el módulo de pandas.
import pandas as pd

#Declarar la ruta del archivo excel en una variable.
rutaArchivo = ".\\archivo\\ejemplo.xlsx"

#Instanciar variable y llamar al método de lectura
abrirArchivo = pd.read_excel(".\\archivo\\ejemplo.xlsx", sheet_name="Hoja1", engine="openpyxl")

"""
Se llama a la propiedad values (la cual contiene los datos del archivo excel) de la instancia 
abrirArchivo y se guarda en una variable.
"""
datos = abrirArchivo.values

#Se recorre la variable datos la cual devuelve una matriz de datos.
for valor in datos:
    print(valor)