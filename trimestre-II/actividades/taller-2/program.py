from pet import Pet

class Program:
    def __init__(this):
        this.vacOptions = ("Vacunas: ", "1.Antirrabica", "2.Antipulgas", "3.Purgatoria")
        this.response = ""
        this.__afirmativeResponses = ["s", "si", "sii", "yes", "claro", "por supuesto", "obviamente", "siza", "siza pai"]
        this.option = "1"
        this.menu = ["\nMenú: \n", "1. Registrar datos de la mascota", "2. Mostrar información de la mascota"]
        this.__menuOptions = {
            "1": ["primera", "la primera", "1"],
            "2": ["segunda", "la segunda", "2"],
        }
    
    def Menu(this):
        pet = Pet()
        sequence = ""
        for option in this.vacOptions:
            sequence = f"{sequence} {option}"
        
        for menu in this.menu:
            print(f"{menu}")
        print(f"{sequence}")
        
        while(this.response != this.__afirmativeResponses):
            
            if(this.option in this.__menuOptions["1"]):
                print(f"\n{this.menu[1]}\n")
                pet.SetData(name=input("Nombre de la mascota: "), age=input("Edad de la mascota: "), sort=input("¿Perro o Gato?: "), raza=input("Raza de la mascota: "))
                this.option = input("\n¿Qué opción del menú desea ejecutar? ").lower()
            
            elif(this.option in this.__menuOptions["2"]):
                print(f"\n{this.menu[2]}\n")
                print(pet.GetData())
                this.option = input("\n¿Qué opción del menú desea ejecutar? ").lower()
            
            else:
                print(f"{this.option} no es una opción correcta.")
                this.response = input("¿Quieres terminar con la ejecución del programa?").lower()
                this.option = input("\n¿Qué opción del menú desea ejecutar? ").lower()