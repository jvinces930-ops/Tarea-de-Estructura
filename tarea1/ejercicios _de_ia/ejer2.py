# Crea una clase llamada RegistroProductos que:
# 1. Tenga un método agregar_producto(producto) que agregue el producto a un conjunto para evitar duplicados 
# y también a una lista para conservar el orden en que fueron registrados.
# 2. Tenga un método contar_productos() que devuelva la cantidad de productos únicos registrados.
# 3. Tenga un método agregar_varios(*args) que reciba varios productos y reutilice el método agregar_producto() para agregarlos.

class RegistroProductos:
    def __init__(self):
        self.lista = []
        self.conjuntos = set()

    def agregar_productos(self,producto):
        self.lista.append(producto)
        self.conjuntos.add(producto)

    def contar_producto(self):
        return len(self.conjuntos)

    def agregar_varios(self, *args):
        
        for i in args:
            self.agregar_productos(i)
        return self.conjuntos

a = RegistroProductos()
print(a.agregar_varios("laptop","mouse", "teclado","laptop","mouse","monitor"))
print(a.contar_producto())   