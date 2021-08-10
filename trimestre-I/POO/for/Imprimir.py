#Imprimir los números del 10 al -3

class Imprimir:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
    
    def Imprimir(self):
        for i in range(self.inicio, self.final+1):
            print(f"Imprimiendo... {i}")

numeros = Imprimir(-3, 10)
numeros.Imprimir()