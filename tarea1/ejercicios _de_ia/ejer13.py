# Clase MezcladorListas
# Crea una clase llamada MezcladorListas que:
# Tenga un método combinar(lista1, lista2) que retorne una lista alternando 
# los elementos de ambas listas.
# Tenga un método combinar_multiples(*listas) que reutilice el método combinar() p
# ara combinar varias listas de dos en dos.
# 📥 ENTRADA
# Dos o más listas
# ⚙️ PROCESO
# Alternar elementos utilizando índices y bucles.
# 📤 SALIDA
# Lista combinada/intercalada

class MezcladorListas: 
    def __init__(self):
        pass

    def combinar(self, lista1, lista2):
        intercalar = []

        for i in range (len(lista1)):
            intercalar.append(lista1[i])
            intercalar.append(lista2[i])

        return intercalar

    def combinar_multiples(self, *listas):
        resultado = []

        for i in range (0, len(listas), 2):
            resultado.append(self.combinar(listas[i], listas[i + 1]))
        return resultado
             
a = MezcladorListas()
a.combinar((10,20), (30,40))
print(a.combinar_multiples([1, 2], [3, 4], [5, 6], [7, 8]))