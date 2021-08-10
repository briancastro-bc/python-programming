def sum(a:int, b: int):
    sum: int = 0
    for i in range(a, b):
        print(i)
        if(i%2):
            sum += i
    print(f"Suma = {sum}")
sum(2, 10)