class Parqueo:
    def __init__(self, horas):
        self.costoHora = 500
        self.cantidadHoras = horas
    
    def Main(self):
        print(f"El costo de parqueo por {self.cantidadHoras} horas es: {self.__CalcularParqueo()}")
    
    def __CalcularParqueo(self):
        if self.cantidadHoras > 3:
            self.costoHora = 300
            return self.costoHora * self.cantidadHoras
        else:
            return self.costoHora * self.cantidadHoras

moto = Parqueo(int(input("¿Cuántas horas va a parquear?: ")))
moto.Main()