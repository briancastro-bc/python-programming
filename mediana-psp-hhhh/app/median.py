import statistics as stats

""" 
    Función de cálculo de la mediana.
    @Median= recibe un parámetro con los números insertados en el @Input.
    @Return = el valor de la mediana.
"""

def Median(numList: list):
    median = 0
    orderNums = sorted(numList)
    print(orderNums)
    for i in orderNums:
        if(len(orderNums)%2 == 0):
            #median = len(orderNums)/2
            median = stats.median(orderNums)
        else:
            #median = len(orderNums)/2
            median = stats.median(orderNums)
    return median