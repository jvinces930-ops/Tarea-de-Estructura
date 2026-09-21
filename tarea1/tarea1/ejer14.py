class ConrdinadorLista:

    def __init__(self):
        pass

    def intercalar(self, lista1, lista2):
        lista_unida = []
        for i in range (len(lista1)):
            lista_unida.append(lista1[i])
            lista_unida.append(lista2[i])
        return lista_unida

    def intercalar_multiples(self, *lista):
        resultado = []

        for i in range (0, len(lista), 2):
            resultado.append(self.intercalar(lista[i], lista[i + 1]))

        return resultado

c = ConrdinadorLista()
print(c.intercalar([1,2],[3,4]))
print(c.intercalar_multiples([1, 2], [3, 4], [5, 6]))