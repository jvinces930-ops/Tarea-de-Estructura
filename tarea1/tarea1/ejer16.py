class DivisorFinder:
    def __init__(self):
        pass
        #retorne una tupla con todos sus divisores
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range (1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)
    
    def es_perfecto(self, numero):
        perfecto = False
        suma = 0
        for i in self.encontrar_divisores(numero):
            if i < numero:
                suma += i

        if suma == numero:
            perfecto = True


        return perfecto
    
    def encontrar_multiples_divisores(self, *numeros):
        diccionario = {}
        for i in numeros:
            diccionario[i] = self.encontrar_divisores(i)
        return diccionario

a = DivisorFinder()
print(a.encontrar_divisores(12))
print(a.es_perfecto(6))
print(a.encontrar_multiples_divisores(6,12))