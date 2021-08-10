def Calcular(n: int):
    #a = 1
    for s in range(1, n):
        print(s + 1 - n)
    return s

n = int(input("Valor de N: "))
imprime = Calcular(n)
print(imprime)