
class Pay:
    
    def __init__(self):
        self.rango = ""
        self.horas = 0
    
    trabajador = {
		"horas": 0,
		"rangos": ['bajo', 'medio', 'alto']
	}
    
    def main(self):
        while True:
            try:
                horas = int(input("¿Cuántas horas trabajó?: "))
                self.horas = horas
                if(horas < 10):
                    print("No trabajó las horas suficientes.")
                    break
                rango = input("¿Cuál es su rango? (bajo, medio, alto): ").lower()
                self.establecerRango(rango)
                break
            except ValueError as e:
                print("El valor escrito es incorrecto. Reintente.")
            except TypeError as e:
                print(e)
    
    def establecerRango(self, rango):
        if(rango in self.trabajador['rangos']):
            self.rango = rango
            self.calcularHoras(self.horas)
        else:
            print("El rango escrito no es correcto")
    
    def calcularHoras(self, horas:int):
        if(self.rango == "bajo"):
            costoHora = 20000
            auxilio = self.horas * costoHora / 100
            print(f"\n Su sueldo es de: {self.horas * costoHora} \n Auxilio: {auxilio} \n Total: {self.horas * costoHora + auxilio}")
            horasAdicionales = self.horasAdicionales()
            if(horasAdicionales > 0):
                print(f"Horas adicionales: {horasAdicionales}. Total: {self.horas * costoHora + auxilio + (horasAdicionales*25000)}")
            
        elif(self.rango == "medio"):
            costoHora = 40000
            descuento = 1.5 * self.horas / 100
            print(f"\n Su sueldo es de: {self.horas * costoHora} \n Descuento: {descuento} \n Total: {self.horas * costoHora + descuento}")
            horasAdicionales = self.horasAdicionales()
            if(horasAdicionales > 0):
                print(f"Horas adicionales: {horasAdicionales}. Total: {self.horas * costoHora + descuento + (horasAdicionales*25000)}")
            
        elif(self.rango == "alto"):
            print(f"Su rango es {self.rango}")
            costoHora = 60000
            descuento = 1.5 * self.horas / 100
            print(f"\n Su sueldo es de: {self.horas * costoHora} \n Descuento: {descuento} \n Total: {self.horas * costoHora + descuento}")
            horasAdicionales = self.horasAdicionales()
            if(horasAdicionales > 0):
                print(f"Horas adicionales: {horasAdicionales}. Total: {self.horas * costoHora + descuento + (horasAdicionales*25000)}")
            
        else:
            print("El rango es inválido")
    
    def horasAdicionales(self):
        horaAdicional = 0
        if(self.horas > 50):
            for i in range(50, self.horas):
                horaAdicional += 1
            return horaAdicional
        return horaAdicional

empleador = Pay()
empleador.main()