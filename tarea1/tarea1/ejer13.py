class SelectorRango: 
    def __init__(self):
        pass

    def crear_rango(self, inicio, fin):
        tup = [inicio, fin]
        return tup

    def elementos_de_multiples_rangos(self, *rango):
        sin_duplicador = set()
        for i, x in rango:
            sin_duplicador.update(self.crear_rango(i, x))
        return sin_duplicador



a = SelectorRango()
print(a.elementos_de_multiples_rangos((1,3),(2,4),(2,5)))