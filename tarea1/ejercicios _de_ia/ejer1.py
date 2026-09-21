# Crea una clase llamada ControlEdades que:
# 1. Tenga un método validar_edad(edad) que devuelva:
#    - True si la edad está entre 0 y 120.
#    - False si está fuera de ese rango.
# 2. Tenga un método cargar_edades(*args) que reciba varias edades, valide cada una y guarde solamente 
# las edades válidas en una lista interna. Al finalizar, debe devolver esa lista.
# 3. Tenga un método promedio() que calcule y devuelva el promedio de las edades almacenadas.

class ControlEdades:
    def __init__(self):
        self.lista = []

    def Validar_edad(self, edad):
        bandera = False

        if (edad >=0) and (edad <=120):
            bandera = True

        return bandera

    def cargar_edades(self, *args):

        for i in args:
            if self.Validar_edad(i):
                self.lista.append(i)

        return self.lista

    def promedio(self):
        return sum(self.lista) / len(self.lista)

a = ControlEdades()
print(a.cargar_edades(18, 25, 150, 20, -3, 30))
print(a.promedio())