class Carrodecompras:
    def __init__(self):
        self.articulo = {}

    def agregar_articulo(self, nombre, precio):
        #nombre y precio dicionario
        self.articulo[nombre] = precio
    
    def total_carrito(self):
        return sum(self.articulo.values())

    def articulos_rango(self, rango_min, rango_max):
        lista = []
        for nombre, precio in self.articulo.items():
            if rango_min <= precio <= rango_max:
                lista.append(nombre)
        return lista #lista


comp = Carrodecompras()
comp.agregar_articulo("pan", 2.50)
comp.agregar_articulo("leche", 3.00)
print(comp.total_carrito())
print(comp.articulos_rango(2.00, 2.80))