#Imprimir números del 1 al 10 sin contar el 8

class Numeros:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
    
    def Contar(self):
        for i in range(self.inicio, self.final+1):
            if i != 8:
                print(f"Contando: {i}")

numeros = Numeros(1, 10)
numeros.Contar()