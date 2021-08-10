#importando la clase Program la cual se encarga de construir el programa.
from src.main import Program

#Función de arranque del proyecto.
def Main():
    start = Program()
    start.Main()

print("¡Hola! A continuación se mostrará un menú por pantalla: \n")
#Llamada a la función Main.
Main()