
#Clase del carrito de compras
class Carrito:
    
    #Constructor de la clase
    def __init__(self):
        #Estructura de datos utilizada para desarrollar el programa, corresponde a un diccionario.
        self.carData = {
            "nombre": [],
            "valor": [],
            "cantidad": []
        }
    
    def agregar(self, nombre: str, valor: float, cantidad: int):
        self.carData["nombre"].append(nombre)
        self.carData["valor"].append(valor)
        self.carData["cantidad"].append(cantidad)
        print("Mensaje: los productos se han agregado: Nombre: {0}. Valor: {1}. Cantidad: {2}".format(nombre, valor, cantidad))
    
    def mostrar(self):
        for clave, valor in self.carData.items():
            print("{0}: {1}".format(clave, valor))
    
    def eliminar(self, nombre):
        if(nombre in self.carData["nombre"]):
            index = self.carData["nombre"].index(nombre)
            self.carData["nombre"].remove(nombre)
            valor = self.carData["valor"][index]
            self.carData["valor"].remove(valor)
            cantidad = self.carData["cantidad"][index]
            self.carData["cantidad"].remove(cantidad)
            print("Los datos relacionados y el producto se han borrado")
        else:
            print("No se encontró el producto: {}".format(nombre))
    
    def editar(self, nombre):
        if(nombre in self.carData["nombre"]):
            index = self.carData["nombre"].index(nombre)
            nuevoNombre = input("Nuevo nombre del producto: ")
            nuevoValor = float(input("Nuevo valor del producto: "))
            nuevaCantidad = int(input("Nueva cantidad del producto: "))
            self.carData["nombre"][index] = nuevoNombre
            self.carData["valor"][index] = nuevoValor
            self.carData["cantidad"][index] = nuevaCantidad
            print("Los datos del producto se actualizaron. Nombre: {0}. Valor: {1}. Cantidad: {2}. \n".format(nuevoNombre, nuevoValor, nuevaCantidad))
        else:
            print("No se encontró el nombre: {0}".format(nombre))