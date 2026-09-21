# Crea una clase llamada AnalizadorNumeros que tenga los siguientes métodos:
# 1. encontrar_multiplos(numero, limite)
# Debe retornar una tupla con todos los múltiplos de numero desde 1 hasta limite
# 2. es_par(numero)
# Debe determinar si un número es par
# encontrar_multiples_numeros(*numeros)
# Debe recibir varios números y utilizar el método encontrar_multiplos() 
# para guardar los resultados en un diccionario.
# Para hacerlo más interesante, utiliza como límite 20.
# Por ejemplo:

class AnalizadorNumeros:
    def __init__(self):
        pass

    def encontrar_multiplos(self, numero, limite):
        multiplos = []

        for i in range (numero, limite+1, numero):

            multiplos.append(i)

        return tuple(multiplos)

    def es_par(self, numero):
        par = False

        if numero % 2 == 0:
            par = True

        return par

    def encontrar_multiples_numeros(self, *numeros):
        diccionario = {}

        for i in numeros:
            diccionario[i] = self.encontrar_multiplos(i, 20)

        return diccionario

a = AnalizadorNumeros()
print(a.encontrar_multiplos(3, 15))
print(a.es_par(8))
print(a.encontrar_multiples_numeros(2, 3, 5))