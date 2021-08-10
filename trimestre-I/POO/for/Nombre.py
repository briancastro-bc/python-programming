#Imprimir el nombre las veces que yo quiera

class Nombre:
    def __init__(self, nombre, veces):
        self.nombre = nombre
        self.veces = veces
    
    def Imprimir(self):
        for i in range(self.veces):
            print(f"{self.nombre}")

nombre = Nombre(input("Nombre: "), int(input("Veces a repetir: ")))
nombre.Imprimir()