# Ejercicio: Control de Inventario
# Crea una clase llamada ControlInventario que permita gestionar el stock de una tienda 
# utilizando un diccionario interno.
# Requerimientos:
# Atributo interno: En el método __init__, crea un diccionario vacío para guardar 
# los productos como claves y su cantidad en stock como valores.
# Método agregar_producto(nombre, cantidad):
# Si el producto ya existe en el diccionario, suma la nueva cantidad al valor actual.
# Si no existe, agrégalo con la cantidad indicada.
# Método producto_mas_stock(): Retorna el nombre del producto que tiene la mayor 
# cantidad de unidades disponibles.
# Método consultar_stock(nombre): Retorna cuántas unidades hay de un producto específico. 
# Si el producto no existe, debe retornar 0.

class ControlInventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, nombre, cantidad):

        if nombre in self.inventario:
            self.inventario[nombre] += (cantidad)
        else:
            self.inventario[nombre] = (cantidad)

    def producto_stock(self):
        return max(self.inventario, key = self.inventario.get)

    def consultar_stock(self, nombre):
        if not self.inventario:
            return 0
        else:
            return self.inventario.get(nombre, 0)

tienda = ControlInventario()
tienda.agregar_producto("manzana", 10)
tienda.agregar_producto("pera", 5)
tienda.agregar_producto("manzana", 8)  # Se reabastece el producto

print(tienda.producto_stock())
print(tienda.consultar_stock("manzana"))