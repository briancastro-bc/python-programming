class Tamales:
    def __init__(self, tamales: int, bolsas):
        self.costoTamal = 7000
        self.domicilio = 3000
        self.costoBolsas = 100
        self.cantidadTamales = tamales
        self.cantidadBolsas = bolsas

    def Main(self):
        print(f"El costo total es de: {self.__HacerCalculo()}$")

    def __HacerCalculo(self):
        if self.cantidadBolsas > 5:
            return (self.cantidadTamales * self.costoTamal) + (self.cantidadBolsas * self.costoBolsas) + self.domicilio
        else:
            return (self.cantidadTamales * self.costoTamal) + self.domicilio

pedido = Tamales(int(input("¿Cuántos tamales quiere?: ")), int(input("¿Número de bolsas?: ")))
pedido.Main()