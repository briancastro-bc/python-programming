from src.Carrito import Carrito

class Program:
    
    def __init__(self):
        self.mensaje = "no"
        self.respuestas = ["s", "si", "sii", "yes", "claro", "por supuesto", "asi es", "siza pai"]
        self.opcionesRespuesta = {
            "primera": ["primera", "la uno", "la primera", "1"],
            "segunda": ["segunda", "la dos", "la segunda", "2"],
            "tercera": ["tercera", "la tres", "la tercera", "3"],
            "cuarta": ["cuarta", "la cuatro", "la cuarta", "4"],
            "quinta": ["quinta", "la quinta", "la cinco", "5"]
        }
        self.carrito = Carrito()
    
    def Main(self):
        opciones = ("Menú:\n", "1. Insertar producto", "2. Mostrar productos", "3. Eliminar producto", "4. Editar producto", "5. Salir del programa \n")
        for i in opciones:
            print(f"{i}")
        
        while(self.mensaje != self.respuestas):
                opcion = input("¿Qué opción desea ver? ").lower()
                
                if(opcion in self.opcionesRespuesta["primera"]):
                    print(f"\n{opciones[1]}\n")
                    try:
                        self.carrito.agregar(input("Nombre del producto: "), float(input("Valor del producto: ")), int(input("Cantidad del producto: ")))
                    except:
                        print("El valor que escribió es incorrecto.")
                
                elif(opcion in self.opcionesRespuesta["segunda"]):
                    print(f"\n{opciones[2]}\n")
                    self.carrito.mostrar()
                
                elif(opcion in self.opcionesRespuesta["tercera"]):
                    print(f"\n{opciones[3]}\n")
                    try:
                        self.carrito.eliminar(input("Nombre del producto a eliminar: "))
                    except:
                        print("Valor incorrecto")
                
                elif(opcion in self.opcionesRespuesta["cuarta"]):
                    print(f"\n{opciones[4]}\n")
                    self.carrito.editar(input("Nombre del producto a editar: "))
                
                elif(opcion in self.opcionesRespuesta["quinta"]):
                    print(f"\n{opciones[5]}\n")
                    print("El programa se cerrará")
                    break
                
                else:
                    print("Opción incorrecta")