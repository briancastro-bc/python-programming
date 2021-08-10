class Contrato:
    def __init__(self, contrato):
        self.comision = 0.10
        self.costoContrato = contrato
    
    def main(self):
        if self.costoContrato == 1000000:
            print(f"Su comisión es del: {self.__HacerCalculo()}")
        else:
            print(f"El costo del contrato es de: {self.__HacerCalculo()}")
    
    def __HacerCalculo(self):
        if self.costoContrato == 1000000:
            return (self.costoContrato * self.comision) / 100
        else:
            return self.costoContrato

empleado = Contrato(float(input("¿De cuánto es el contrato?: ")))
empleado.main()