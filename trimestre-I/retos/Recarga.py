class Recarga():
    def __init__(self, valorRecarga: int, operador: str):
        self.valorRecarga: int = valorRecarga
        self.operador: str = operador.lower()
        self.valorMinutos = 100
    
    def Program(self):
        print("El sistema está procesando la información...\n")
        if self.operador == "claro":
            print(f"Operador: {self.operador}")
            print(self.__Notificar())
        elif self.operador == "movistar":
            print(f"Operador: {self.operador}")
            print(self.__Notificar())
        elif self.operador == "tigo":
            print(f"Operador: {self.operador}")
            print(self.__Notificar())
        else:
            print(f"No insertó un operador válido, su recarga no se hará")
    
    def __ProcesarRecarga(self):
        recargar = self.valorRecarga // self.valorMinutos
        return recargar
    
    def __Notificar(self):
        if self.valorRecarga < 1000:
            return f"Error: No permitimos recargas de menos de $1000"
        elif self.valorRecarga >= 10000:
            adicion = self.valorRecarga // self.valorMinutos * 2
            #totalAdicion = self.valorRecarga // self.valorMinutos + adicion
            return f"Hecho: su recarga de ${self.valorRecarga} se ha realizado. Minutos: {adicion}. Le hemos adicionado: {self.__ProcesarRecarga()} minutos"
        else:
            return f"Hecho: su recarga de ${self.valorRecarga} se ha realizado. Minutos: {self.__ProcesarRecarga()}"
        
celular = Recarga(int(input("¿Valor de la recarga?: ")), input("¿Cuál es su operador?: "))
celular.Program()