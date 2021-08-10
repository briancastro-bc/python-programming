import math

class Triangle():
    def __init__(this):
        this.side = {
            "a": 0,
            "b": 0
        }
        this.__hypotenuse = 0

    def hypotenuse(this, a, b):
        this.side["a"] = a
        this.side["b"] = b
        this.__hypotenuse = this.side["a"]**2 + this.side["b"]**2
        this.result = math.sqrt(this.__hypotenuse).__round__()
        print(f"El resultado de la hipotenusa del cateto: {a} y cateto: {b} es igual a = {this.result}")