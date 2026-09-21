# 🟦 Ejercicio: Gestor de calificaciones
# Crea una clase llamada GestorCalificaciones que permita administrar las calificaciones de varios estudiantes.
# El programa debe tener:
# 1. Un atributo calificaciones
# Debe ser un diccionario vacío:
# self.calificaciones = {}

# La estructura será:
# {
#     "Ana": 8.5,
#     "Luis": 7.0,
#     "Carlos": 9.2
# }

# 2. Método agregar_calificacion(self, estudiante, nota)
# Debe agregar la calificación de un estudiante.
# Ejemplo:
# g = GestorCalificaciones()

# g.agregar_calificacion("Ana", 8.5)
# g.agregar_calificacion("Luis", 7.0)

# Resultado:
# {
#     "Ana": 8.5,
#     "Luis": 7.0
# }

# Si el estudiante ya existe, debe actualizar su nota.
# 3. Método promedio(self)
# Debe recorrer todas las calificaciones y calcular el promedio.
# Por ejemplo:
# Ana     → 8.5
# Luis    → 7.0
# Carlos  → 9.5
# Entonces:
# (8.5 + 7.0 + 9.5) / 3 = 8.33
# Debe devolver:
# 8.33...
# 4. Método estudiantes_aprobados(self, minimo)
# Debe devolver una lista con los estudiantes cuya nota sea mayor o igual al mínimo.
# Por ejemplo:
# g.estudiantes_aprobados(7)

# Si tenemos:
# {
#     "Ana": 8.5,
#     "Luis": 6.5,
#     "Carlos": 9.0,
#     "Pedro": 5.8
# }

# Debe devolver:
# ["Ana", "Carlos"]

# 5. Método mejor_estudiante(self)
# Debe encontrar al estudiante que tenga la nota más alta.
# Con:
# {
#     "Ana": 8.5,
#     "Luis": 6.5,
#     "Carlos": 9.0,
#     "Pedro": 5.8
# }
class GestorCalificaciones:

    def __init__(self):
        self.calificaciones = {}

    def agregar_calificacion(self, estudiante, nota):
        self.calificaciones[estudiante] = nota
        return self.calificaciones

    def promedio(self):
        total = 0

        for estudiante, nota in self.calificaciones.items():
            total += nota

        if len(self.calificaciones) > 0:
            return total / len(self.calificaciones)

        return 0

    def estudiantes_aprobados(self, minimo):
        aprobados = []

        for estudiante, nota in self.calificaciones.items():
            if nota >= minimo:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        mejor = None
        mejor_nota = None

        for estudiante, nota in self.calificaciones.items():

            if mejor_nota is None or nota > mejor_nota:
                mejor = estudiante
                mejor_nota = nota

        return mejor


# Crear el objeto
g = GestorCalificaciones()

# Agregar calificaciones
print(g.agregar_calificacion("Ana", 8.5))
print(g.agregar_calificacion("Luis", 6.5))
print(g.agregar_calificacion("Carlos", 9.0))
print(g.agregar_calificacion("Pedro", 5.8))

# Mostrar resultados
print("Promedio:", g.promedio())

print("Aprobados:", g.estudiantes_aprobados(7))

print("Mejor estudiante:", g.mejor_estudiante())