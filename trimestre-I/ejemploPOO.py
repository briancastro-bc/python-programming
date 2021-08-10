class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def __add__(self, este):
        return f"{self.__nombre} {este.__nombre}"
    
p1 = Persona(5)
p2 = Persona(5)
p3 = Persona(5)
print(p1 + p2)