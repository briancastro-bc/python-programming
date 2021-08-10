""" 
    Función de entrada, recibe los valores por consola.
    @Input = permite digitar X cantidad de números enteros.
    @Return = un arreglo con los números digitados.
"""

def Input(numsLenght: int):
    numList = []
    print("\nA continuación, podrá digitar los {0} números para realizar el cáculo\n".format(numsLenght))
    for i in range(numsLenght):
        try:
            num = float(input("Número {0}: ".format(i+1)))
        except ValueError:
            print("\nValor incorrecto. Por favor, introduce un número válido: \n")
            num = float(input("Número {0}: ".format(i+1)))
        numList.append(num)
    return numList