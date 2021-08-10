#Importando el objeto app desde src/app.py
from src.app import app

#Constantes de configuración del servidor.
HOST="localhost"
PORT=4000
DEBUG=True

#Llamada al método run y paso de parámetros para el arranque del servidor.
if __name__ == '__main__':
    app.run(HOST, PORT, DEBUG)