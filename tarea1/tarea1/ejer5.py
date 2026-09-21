class InversorSecuencia:
    def __init__(self):
        pass

    def invertir_lista(self, lista):
        #retornar una lista invertida
        lista_invertida = []

        for i in range(len(lista)-1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida


    def invertir_multiples(self, *lista):
        #reutalizar la funcion invertir lista y retornar un diccionario (lista_original: lista_invertida)
        diccio = {}
        for list in lista:
            diccio[tuple(list)] = self.invertir_lista(list)
        return diccio




lis = InversorSecuencia()
print(lis.invertir_multiples([1, 2, 3]))
