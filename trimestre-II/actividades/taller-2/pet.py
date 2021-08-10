class Pet:
    def __init__(this):
        this.name = ""
        this.age = ""
        this.sort = ""
        this.raza = ""
        this.vacunas = {
            "Vacuna-1": "",
            "Vacuna-2": "",
            "Vacuna-3": ""
        }
        this.isSick = False
        this.response = ""
    
    def SetData(this, **data):
        this.name = data["name"]
        this.age = data["age"]
        this.sort = data["sort"]
        this.raza = data["raza"]
        this.vacunas["Vacuna-1"] = input("1. Vacuna antirrabica (SI/NO): ")
        this.vacunas["Vacuna-2"] = input("2. Vacuna antipulgas (SI/NO): ")
        this.vacunas["Vacuna-3"] = input("3. Vacuna purgatoria (SI/NO): ")
        this.response = input("¿Su mascota está enferma? ").lower()
        if(this.response == "si"):
            this.isSick = True
        #print(data)
    
    def GetData(this):
        return f" Nombre de la mascota: {this.name}\n Edad de la mascota: {this.age}\n Especie de la mascota: {this.sort}\n Raza de la mascota: {this.raza}\n Vacunas: {this.vacunas}\n Mascota enferma: {this.isSick}"