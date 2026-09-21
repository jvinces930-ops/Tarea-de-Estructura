# Crea una clase llamada Inventario que:
# 1. Tenga un método agregar_producto(nombre, precio) que guarde cada producto en un diccionario, 
# utilizando el nombre como clave y el precio como valor.
# 2. Tenga un método calcular_total() que retorne la suma de los precios de todos 
# los productos almacenados.
# 3. Tenga un método productos_por_rango(precio_min, precio_max) que retorne una lista 
# con los nombres de los productos cuyo precio esté dentro del rango indicado.

class Inventario:
    def __init__(self):
        self.dicciionario = {}
        
    def agregar_producto(self, nombre, precio):
        
        self.dicciionario[nombre] = precio


    def calcular_total(self):
        suma = 0
        for i, x in self.dicciionario.items():
            suma += x
        return suma

    def productos_por_rango(self, precio_min, precio_max):
        lista_nombre = []

        for i, x in self.dicciionario.items():
            if (x >= precio_min) and (x <= precio_max):
                lista_nombre.append(i)

        return lista_nombre

a = Inventario()
a.agregar_producto("cuaderno", 3.50)
a.agregar_producto("mochila", 25.00)
a.agregar_producto("lapiz", 1.00)
a.agregar_producto("carpeta", 5.50)
a.agregar_producto("calculadora", 18.00)

print(a.calcular_total())
print(a.productos_por_rango(3.00, 10.00))