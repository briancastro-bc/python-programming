class Recarga:
    def __init__(self, cantidadMins: int):
        self.cantidadMins = cantidadMins
        self.valorMins = 100
        self.__adicion = self.cantidadMins * 2
    
    def Main(self):
        print(self.__str__())
    
    def __HacerRecarga(self):
        recarga = self.cantidadMins * self.valorMins
        return recarga
    
    def __str__(self):
        if self.cantidadMins > 50:
            return f"La recarga de {self.cantidadMins} minutos, se ha realizado. Costo: {self.__HacerRecarga()} + Adición: {self.__adicion} minutos"
        elif self.cantidadMins <= 0:
            return "No introdujo una cantidad válida"
        else:
            return f"La recarga de {self.cantidadMins} minutos, se ha realizado. Costo: {self.__HacerRecarga()}"

#Instanciando objeto: celular
celular = Recarga(int(input("Escriba la cantidad de minutos: ")))
celular.Main()