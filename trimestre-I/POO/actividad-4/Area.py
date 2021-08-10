from math import pi

class Area:
    def __init__(self, opcion):
        self.opcion = opcion
    
    def Program(self):
        if self.opcion == 1:
            circulo = self.__AreaCirculo(float(input("Radio: ")), float(input("Diametro: ")))
            print(f"El área del circulo es: {circulo}")
        elif self.opcion == 2:
            cuadrado = self.__AreaCuadrado(float(input("Valor del lado: ")))
            print(f"El área del cuadrado es: {cuadrado}")
        else:
            print("Opción incorrecta")
    
    def __AreaCirculo(self, radio, diametro):
        area = pi * radio**2
        #resultadoArea = area (pi * diametro**2) / 4
        return area
    
    def __AreaCuadrado(self, a):
        area = a**2
        return area
    
figura = Area(int(input("Escribe una opción (1. Área del circulo, 2 Área del cuadrado): ")))
figura.Program()