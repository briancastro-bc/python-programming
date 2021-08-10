class Notas:
    def __init__(self, opcion):
        self.opcion = opcion.lower()
    
    def Program(self):
        if self.opcion == "aprendiz":
            notas = self.__PromediarNotas(float(input("Nota 1: ")), float(input("Nota 2: ")), float(input("Nota 3: ")))
            print(f"El promedio de sus notas es: {notas}")
        else:
            print(self.__PromediarNotas())
    
    def __PromediarNotas(self, nota1, nota2, nota3):
        if self.opcion == "aprendiz":
            calculoPromedio = (nota1 + nota2 + nota3) / 3
            return calculoPromedio
        else:
            return f"No es un aprendiz, no podemos calcular su promedio"

estudiante = Notas(input("Escribe una opción (1. Aprendiz): "))
estudiante.Program()