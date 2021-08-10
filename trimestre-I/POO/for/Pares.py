class Par:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
    
    def NumerarPares(self):
        for i in range(self.inicio, self.final+1, 2):
            print(f"Número {i}")

numero = Par(10, 20)
numero.NumerarPares()