# 12. Generar e imprimir la serie y la suma los primero N números múltiplos de M.

class Multiples:
    def __init__(this):
        this.num = 0
        this.suma = 0
        this.counter = 0
        this.sequence = ""
    
    def GenerateAdd(this, M):
        this.num = M
        for this.counter in range(0, this.num, 1):
            this.counter += 1
            this.sequence = f"{this.sequence} {this.num} * {this.counter} = {this.num * this.counter}\n"
            this.suma += this.num * this.counter
        print(this.sequence)
        print(f"Suma de los multiplos de {this.num} = {this.suma}")