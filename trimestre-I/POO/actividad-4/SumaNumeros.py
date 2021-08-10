""" 
Crear un programa básico en python, que sume la cantidad de números que el usuario quiera sumar y su vez,
el usuario inserte los valores de esa cantidad de números.
"""

class Sumar():
    def __init__(self, cantidadNumeros: int):
        self.cantidadNumeros: int = cantidadNumeros
        self.sumaNumeros = 0
    
    def GenerarNumeros(self):
        if self.cantidadNumeros <= 0:
            return f"La cantidad de números no es válida"
        else:
            print(f"Vamos a sumar {self.cantidadNumeros} números")
            for i in range(self.cantidadNumeros):
                self.sumaNumeros = int(input("Valor a sumar: "))
                for j in self.sumaNumeros:
                    print(j+j)
    
    def CalcularSuma(self):
        numerosGenerados = self.GenerarNumeros()
        for i in numerosGenerados:
            self.sumaNumeros += i
            resultadoCalculo = self.sumaNumeros
            print(resultadoCalculo)

numero = Sumar(int(input("Escribe la cantidad de números que quieres sumar: ")))
numero.GenerarNumeros()