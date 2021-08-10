import random


class Apuesta:
    def __init__(self, apostado):
        self.apostado = apostado
        self.aleatorio = random.randrange(7)
        
    def comparar(self):
        if self.apostado == self.aleatorio:
            print(f"Gano.... con el número {self.apostado}")
        elif self.apostado > 6 and self.apostado < 1:
            print("Inserte un valor válido")
        else:
            print(f"perdio.. con el numero {self.aleatorio}")


for i in range(5):
    apuesta = Apuesta(int(input("Escribe un número del 1 al 6:")))
    apuesta.comparar()