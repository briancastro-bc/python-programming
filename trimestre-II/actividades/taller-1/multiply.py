#Generar e imprimir las primeras N tablas de multiplicar, desde el 1 hasta el 9.

class Multiply:
    def __init__(this):
        this.num = 0
        this.final = 10
    
    def CreateTable(this, numTable):
        this.num = numTable
        for i in range(1, this.final):
            print(f"{this.num} * {i} = {this.num*i}")