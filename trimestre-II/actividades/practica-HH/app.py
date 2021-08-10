# 30 minutos.

def Main(num: int):
    try:
        divisible, divisible2 = 3, 5
        for i in range(1, num+1, 1):
            if(i is divisible and i is divisible2):
                print(f"{i} es divisible por 3 y 5")
                divisible += 3
                divisible2 += 5
            elif(i is divisible):
                print(f"{i} es divisible por 3")
                divisible += 3
            elif(i is divisible2):
                print(f"{i} es divisible por 5")
                divisible2 += 5
            else:
                print(i)
    except:
        print(f"Ha ocurrido un error. Reintente")

Main(10)
