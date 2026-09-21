# Crea una clase llamada ClasificadorNotas que permita categorizar notas de estudiantes, 
# agruparlas en listas según la escala y calcular estadísticas por categoría.
# Requisitos:
# Método 1: clasificar_nota(nota)
# Recibe una nota numérica (de 0 a 100).
# Retorna la categoría según el rango:
# Menor a 60: "reprobado"
# De 60 a 79: "regular"
# De 80 a 89: "bueno"
# De 90 a 100: "excelente"
# Método 2: agrupar_por_categoria(*notas)
# Recibe un número variable de notas (*notas).
# Inicializa/reinicia un diccionario como atributo (self.grupos) con las claves: 
# "reprobado", "regular", "bueno", "excelente", conteniendo listas vacías.
# Recorre las notas recibidas, clasifica cada una reutilizando 
# clasificar_nota y las añade a la lista correspondiente.
# Retorna el diccionario self.grupos.
# Método 3: promedio_por_categoria(categoria)
# Recibe el nombre de una categoría (str).
# Retorna el promedio de las notas almacenadas en esa categoría dentro de self.grupos.
# (Importante: Si la lista está vacía, debe retornar 0.0 para evitar errores de 
# división entre cero).

class ClasificadorNotas:
    def __init__(self):
        self.diciconario = {}

    def clasificar_nota(self, nota):

        categoria = ""

        if nota < 60:
            categoria = "reprobado" 
        elif nota < 80:
            categoria = "regular"
        elif nota < 90:
            categoria = "bueno"
        else:
            categoria = "excelente"

        return categoria

    def agrupar_por_categorias(self, *categoria):

        self.diciconario = {
            "reprobado" : [],
            "regular" : [],
            "bueno" : [],
            "excelente" : []
        }

        for i in categoria:
            cate = self.clasificar_nota(i)
            self.diciconario[cate].append(i)

        return self.diciconario

    def promedio_por_categorias(self, categoria):
        if categoria in self.diciconario and len(self.diciconario[categoria]) > 0:
            a = self.diciconario[categoria]
            return sum(a) / len(a)
        return 0.0

cn = ClasificadorNotas()

resultado = cn.agrupar_por_categorias(45, 75, 88, 95, 62, 90)
print(resultado)

promedio_excelente = cn.promedio_por_categorias("excelente")
print(f"Promedio excelente: {promedio_excelente}")
