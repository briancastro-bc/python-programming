class Pares():
    def __init__(self):
        self.inicio = 0
        self.final = 10
    
    def SacarPares(self):
        while self.inicio < self.final:
            self.inicio += 2
            print(self.inicio)

numeros = Pares()
numeros.SacarPares()