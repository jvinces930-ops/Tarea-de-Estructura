# Clase SeparadorNumeros que:

# Tenga un método separar_pares(lista) que reciba una 
# lista de números y retorne una nueva lista que contenga 
# únicamente los números pares, sin usar filtros automáticos; debes hacerlo mediante un bucle.
# Tenga un método separar_multiples(*listas) que reutilice
# el método anterior para procesar varias listas y retorne un diccionario con la estructura:

# {lista_original: lista_de_pares}
class SeparadorNumeros:
    def __init__(self):
        pass

    def separar_pares(self, lista):
        lista_pares = []
        for i in lista:
            if i % 2 == 0:
               lista_pares.append(i)
        return lista_pares

    def separar_multiples(self, *listas):
        diccionario = {}
        for i in listas:
            diccionario[tuple(i)] = (self.separar_pares(i))
        return diccionario

sep = SeparadorNumeros()

print(sep.separar_pares([1, 2, 3, 4, 5, 6]))
print(sep.separar_multiples(
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [10, 11, 12]
))