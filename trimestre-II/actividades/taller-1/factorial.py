""" 
Para calcular el factorial de un número se deben multiplicar todos los números previos a él y el
mismo número, por ejemplo, el factorial de 6 es 1*2*3*4*5*6. Dado un número N calcular su
factorial.
"""

class Factorial:
    def __init__(this):
        this.factorialNum = 0
        this.sequence = ""
        this.counter = 0
        this.multiply = 1
    
    def Calculate(this, N):
        this.factorialNum = N
        for this.counter in range(1, this.factorialNum+1, 1):
            this.sequence = f"{this.sequence} * {this.counter}"
            this.multiply *= this.counter
        print(f"{this.factorialNum}! = {this.sequence} = {this.multiply}")