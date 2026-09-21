class Inventario:
    def __init__(self):
        self.diccionario = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.diccionario():
            self.diccionario[producto] += (cantidad)
        else: 
            self.diccionario[producto] = (cantidad)
        return self.diccionario

    def restar_stock(self, producto, cantidad):
        bandera = False
        total = 0
        for i, x in self.diccionario.items():
            if i == producto:
                total = x - cantidad
            if total > 0:
                self.diccionario[i] = (total)
                bandera = True

        return bandera

    def productos_bajo_stock(self, minimo):

        lista = []

        for x, i in self.diccionario.items():
            if i < minimo:
                lista.append(x)

        return lista



a = Inventario()
print(a.agregar_stock("manzana", 10))
print(a.restar_stock("manzana", 5))

print(a.productos_bajo_stock(15))
