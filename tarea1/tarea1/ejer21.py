class AnalizadorPatrones:
    def __init__(self):
        self.palabra_unica = set()

    def encontrar_palabras(self, texto, patron):
        palabra = texto.split()
        resultado = []
        for i in palabra:
            if i.startswith(patron):
                resultado.append(i)

        return resultado

    def agrupar_por_longitud(self, texto):
        palabra = texto.split()
        grupos = {}

        for i in palabra:
            longitud = len(i)
            if longitud not in grupos:
                grupos[longitud] = []

            grupos[longitud].append(i)

        return grupos

    def palabras_unicas(self, texto):
        palabras = texto.split()
        unicas = set(palabras)

        return unicas


a = AnalizadorPatrones()
print(a.agrupar_por_longitud("el gato esta aqui"))
print(a.palabras_unicas("hola hola adios"))
print(a.encontrar_palabras("el gato esta aqui", "a"))