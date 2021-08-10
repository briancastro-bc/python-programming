from input import Input
from median import Median
from output import Output


""" 
    Método principal de la aplicación.
    @Main = Entrada de la aplicación.
    @Param
    @Type: void = llama al resto de funciones.
"""

def Main():
    try:
        x = int(input("¿Cuántos números va a digitar para calcular su mediana?: "))
    except ValueError:
        print("No insertó un número válido. Por favor intentelo de nuevo.")
        x = int(input("¿Cuántos números va a digitar para calcular su mediana?: "))
    numList = Input(x)
    median = Median(numList)
    print(Output(median))

Main()