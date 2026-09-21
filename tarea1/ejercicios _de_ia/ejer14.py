# Crea una clase llamada RegistroProductos que:
# Tenga un método registrar(producto, precio) que guarde el producto y su precio en un diccionario.
# Tenga un método productos_caros(precio_minimo) que retorne una lista con los nombres 
# de los productos cuyo precio sea mayor o igual al precio mínimo.
# Tenga un método producto_mas_caro() que encuentre y retorne el nombre del producto y
#  su precio más alto.

class RegistroProductos:
    def __init__(self):
        self.diccionario = {}

    def registrar(self, productos, precio):
        self.diccionario[productos] = precio

        return self.diccionario

    def productos_caros(self, precio_minimo):
        lista = []

        for i, x in self.diccionario.items():
            if x >= precio_minimo:
                lista.append(i)

        return lista

    def producto_mas_caro(self):
        mayor = 0
        producto = ""

        for a, i in self.diccionario.items():
            if i > mayor:
                mayor = i
                producto = a

        return producto, mayor

r = RegistroProductos()

r.registrar("Laptop", 800)
r.registrar("Mouse", 25)
r.registrar("Teclado", 50)
r.registrar("Monitor", 300)

print(r.productos_caros(100))
print(r.producto_mas_caro())