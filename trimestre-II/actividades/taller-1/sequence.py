# Generar la siguiente secuencia: S = 2 + 4 - 6 + 8 + 10 - 9 + 11 + 13 - 15 + 17 + 19 - 18...+N
#15. Calcular e imprimir la serie y el valor de S definida por:

class Sequence:
    def __init__(this):
        this.sequence = ""
        this.num = 0
        this.counter = 0
        this.sum = 0
        this.operator = ""
        this.increment = 0
        this.multiples = [9, 18, 27, 36, 45, 54]
    
    def Generate(this, N):
        this.num = N
        while(this.counter <= this.num):
            if(this.isPositive):
                this.counter += 2
                this.sequence = "{0} + {1}".format(this.sequence, str(this.counter))
                this.sum += this.counter
                this.isPositive = False
            else:
                this.counter += 2
                this.sequence = "{0} + {1}".format(this.sequence, str(this.counter))
                this.sum -= this.counter
                this.isPositive = True
        print(f"S = {this.sequence} = {this.sum}")
    
    def GenerateSequence(this, N):
        this.num = N
        for this.counter in range(2, this.num, 2):
            this.increment += 1
                
            if(this.operator == ""):
                this.sequence += f"+{str(this.counter)}"
                this.sum += this.counter
                this.operator = "+"
            
            elif(this.operator == "+"):
                this.sequence += f"+{str(this.counter)}"
                this.sum += this.counter
                this.operator = "-"
            
            elif(this.operator == "-"):
                this.sequence += f"-{str(this.counter)}"
                this.sum -= this.counter
                this.operator = ""
            
        print(f"S = {this.sequence}")
        print(this.sum)

num = Sequence()
num.GenerateSequence(50)