class Agrupador_edades:
    def __init__(self):
        self.diccionario = {}

    def clasificar_edad(self, edad):
        tupla = ""

        if edad >= 65:
            tupla = "mayor"
        elif edad >= 18:
            tupla = "adulto"
        elif edad >= 12:
            tupla = "adolescente"
        else:
            tupla = "niño"

        return tupla

    def agrupar_por_categoria(self, *edades):
        estado = ""
        for i in edades:
            estado = self.clasificar_edad(i)
            self.diccionario[estado] = (i)

        return self.diccionario

    def edad_promedio(self, categoria):
        if categoria in self.diccionario and len(self.diccionario[categoria]) > 0:
              edades = self.diccionario[categoria]
              return sum(edades) / len(edades)
        return 0.0

a = Agrupador_edades()
a.clasificar_edad(80)
print(a.agrupar_por_categoria(5, 15, 30, 70))
print(a.edad_promedio("adulto"))