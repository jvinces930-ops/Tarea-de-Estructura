class Analizar_texto:
    def __init__(self):
        self.palabra_unicas = set()
        self.lista_palabra = []

    def agregar_palabra(self, palabra):

        self.palabra_unicas.add(palabra)
        self.lista_palabra.append(palabra)
        #conjuntos y lista

    def contar_palabra(self):
        return len(self.palabra_unicas)

    def agregar_mutiples(self,*args):
        for texto in args:
            self.agregar_palabra(texto)
        return len(self.palabra_unicas)



text = Analizar_texto()
print(text.agregar_mutiples("hola", "mundo", "hola", "adios"))