#Importing modules.
from printing import Print as readWord
from multiply import Multiply as multiplication
from readNums import Nums
from triangle import Triangle
from factorial import Factorial
from multiples import Multiples

class Program:
    def __init__(this):
        this.message = "no"
        this.option = ""
        this.__aresponses = ["s", "si", "sii", "yes", "claro", "por supuesto", "asi es", "siza pai"]
        this.__optionsResponse = {
            "first": ["primera", "la uno", "la primera", "1"],
            "second": ["segunda", "la dos", "la segunda", "2"],
            "third": ["tercera", "la tres", "la tercera", "3"],
            "fourth": ["cuarta", "la cuatro", "la cuarta", "4"],
            "fifth": ["quinta", "la cinco", "la quinta", "5"],
            "sixth": ["sexta", "la seis", "la sexta", "6"],
            "seventh": ["septima", "la siete", "la septima", "7"],
            "eighth": ["octava", "la ocho", "la octava", "8"],
            "nineth": ["novena", "la nueve", "la novena", "9"]
        }
    
    def Menu(this,):
        options = ("Menú:\n", "1. Primera opción: Imprimir X palabra 5 veces", "2. Segunda opción: Generar e imprimir las primeras N tablas de multiplicar, desde el 1 hasta el 9.", "3. Tercera opción: Leer el valor de N e imprimir los primeros N números naturales.", "4. Cuarta opción: Leer el valor de N, imprimir y sumar los números de 1 a N.", "5. Quinta opción: Calcular la suma de los primeros N números pares. ", "6. Sexta: Imprimir la serie de los N primeros números impares y la suma de ellos", "7. Septima: hayar el valor de la hipotenusa entre 2 catetos (a, b)", "8. Octava: hayar el factorial e imprimir la secuencia de N valor", "9. Generar e imprimir la serie y la suma los primero N números múltiplos de M. ")
        for i in options:
            print(f"{i}")
        
        while(this.message != this.__aresponses):
            
            this.option = input("\n¿Qué opción desea ver? ").lower()
            
            if this.option in this.__optionsResponse["first"]:
                print(f"\n{options[1]}\n")
                readWord().Repeat(input("Palabra a repetir: "))
            
            elif this.option in this.__optionsResponse["second"]:
                print(f"\n{options[2]}\n")
                multiplication().CreateTable(int(input("¿Qué tabla de multiplicar desea generar? ")))
            
            elif this.option in this.__optionsResponse["third"]:
                print(f"\n{options[3]}\n")
                Nums().ReadNaturalNums(int(input("¿Hasta qué número desea ver? ")))
            
            elif this.option in this.__optionsResponse["fourth"]:
                print(f"\n{options[4]}\n")
                Nums().AddNums(int(input("¿Qué serie de números deseas sumar de 1 en 1? ")))
            
            elif this.option in this.__optionsResponse["fifth"]:
                print(f"\n{options[5]}\n")
                Nums().CalculatePairAddition(int(input("Números pares a sumar: ")))
            
            elif this.option in this.__optionsResponse["sixth"]:
                print(f"\n{options[6]}\n")
                Nums().CalculateOddAddition(int(input("Números impares a sumar: ")))
            
            elif this.option in this.__optionsResponse["seventh"]:
                print(f"\n{options[7]}\n")
                Triangle().hypotenuse(int(input("Cateto A: ")), int(input("Cateto B: ")))
            
            elif this.option in this.__optionsResponse["eighth"]:
                print(f"\n{options[8]}\n")
                Factorial().Calculate(int(input("Número a calcular factorial: ")))
            
            elif this.option in this.__optionsResponse["nineth"]:
                print(f"\n{options[9]}\n")
                Multiples().GenerateAdd(int(input("Número: ")))
            
            else:
                print("Wrong option")
            
            this.message = input("\n¿Quiere acabar con el programa? ").lower()
            
            if (this.message in this.__aresponses):
                print("Cerraremos el programa. Por favor vuelve pronto:(")
                break