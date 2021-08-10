class Sumatoria():
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def __CalcularSuma(self):
        if self.num3 > 10:
            return self.num1 + self.num2
        resultadoCalculo = self.num1 + self.num2 + self.num3
        return resultadoCalculo

    def MostrarCalculo(self):
        print(f"El resultado de la suma de los números es: {self.__CalcularSuma()}")

numero = Sumatoria(2, 3, 11)
numero.MostrarCalculo()