#7. Leer el valor de N e imprimir los primeros N números naturales.
#8. Leer el valor de N, imprimir y sumar los números de 1 a N.
#9. Calcular la suma de los primeros N números pares.
#10. Imprimir la serie de los N primeros números impares y la suma de ellos

class Nums:
    def __init__(this):
        this.N = 0
        this.sequence = ""
    
    def ReadNaturalNums(this, N):
        this.N = N
        for i in range(1, this.N+1, 1):
            this.sequence = str(i)
            print(this.sequence)
    
    def AddNums(this, N):
        this.N = N
        for i in range(1, this.N+1, 1):
            print(f"{i} + 1 = {i + 1}")
    
    def CalculatePairAddition(this, N):
        this.N = N
        for num in range(0, this.N+1, 2):
            print(f"{num} + {num} = {num+num}")
    
    def CalculateOddAddition(this, N):
        this.N = N
        for num in range(1, this.N, 2):
            print(f"{num} + {num} = {num+num}")