from math import pi, sqrt

class Triangulo:
    def __init__(self, opcion: str):
        self.opcion = opcion.lower() #Convierte a mminusculas.
    
    def Program(self):
        try:
            if self.opcion == "perimetro":
                perimetro = self.__HallarPerimetro(float(input("Lado 1: ")), float(input("Lado 2: ")), float(input("Lado 3: ")))
                print(f"El resultado del {self.opcion} es: {perimetro}")
            elif self.opcion == "area":
                area = self.__HallarArea(float(input("Escribe la base: ")), float(input("Escribe la altura: ")))
                print(f"El resultado del {self.opcion} es: {area}")
            elif self.opcion == "hipotenusa":
                hipotenusa = self.__HallarHipotenusa(int(input("Cateto (b): ")), int(input("Cateto (c): ")))
                print(f"El resultado de la {self.opcion} es: {hipotenusa}")
            elif self.opcion == "salir":
                print(f"El programa se cerrará.")
            else:
                print(f"No escribió una opción correcta.")
        except SyntaxError:
            print(SyntaxError)
    
    def __HallarPerimetro(self, lado1, lado2, lado3):
        resultadoPerimetro = lado1 + lado2 + lado3
        return resultadoPerimetro
    
    def __HallarArea(self, base, altura):
        resultadoArea = (base * altura) / 2
        return resultadoArea
    
    def __HallarHipotenusa(self, cat1, cat2):
        hipotenusa = cat1**2 + cat2**2
        resultadoHipotenusa = sqrt(hipotenusa)
        return resultadoHipotenusa

triangulo = Triangulo(input("Escribe una opción (1. Perimetro, 2. Area, 3. Hipotenusa, 4. Salir): "))
triangulo.Program()