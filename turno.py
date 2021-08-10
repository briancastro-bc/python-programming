class Turno:
    def __init__(self):
        self.cliente = ""
        self.tipoCliente = ""
        self.tipoClientes = {
            "ES": "estandar",
            "PR": "preferencial",
            "VP": "vip",
            "PL": "platino"
        }
        self.turno = 0
        self.bd = []
        self.cadena = ""

    def getUsuario(self):
        for usuario in self.bd:
            return f"{usuario}"

    def asignarTurno(self):
        for i in range(1, 12+1, 1):
            self.cliente = input("Su nombre es?: ").lower()
            self.tipoCliente = input("Que tipo de cliente es? ").lower()
            self.turno += 1
            if self.tipoCliente in self.tipoClientes["ES"]:
                print(f"su turno es: ES{self.turno} {self.cliente}")
            elif self.tipoCliente in self.tipoClientes["PR"]:
                print(f"su turno es: PR{self.turno} {self.cliente}")
            elif self.tipoCliente in self.tipoClientes["VP"]:
                print(f"su turno es: VP{self.turno} {self.cliente}")
            elif self.tipoCliente in self.tipoClientes["PL"]:
                print(f"su turno es: PL{self.turno} {self.cliente}")
            else:
                print("El tipo de cliente no es válido.")
            self.bd.append(self.cliente)
        print(self.bd)


x = Turno()
x.asignarTurno()
print(x.getUsuario())