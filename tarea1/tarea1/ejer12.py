class ContadorFrecuencia:
    def __init__(self):
        self.diccio = {}

    def agregar_elemento(self, elemento):

        if elemento in self.diccio:
            self.diccio[elemento] += 1
        else:
            self.diccio[elemento] = 1

    def elemento_frecuente(self):
        return max(self.diccio, key = self.diccio.get)

    def conteo_elemento(self, elemento):
        return self.diccio.get(elemento, 0)


a = ContadorFrecuencia()
a.agregar_elemento("a")
a.agregar_elemento("b")
a.agregar_elemento("a")

print(a.elemento_frecuente())
print(a.conteo_elemento("a"))