# Crea una clase llamada Cursos que:

# Tenga un método crear_curso(nombre_curso) que cree un curso como una lista vacía dentro de un diccionario.
# Tenga un método agregar_estudiante(curso, estudiante) que agregue un estudiante al curso.
# Tenga un método curso_mayor_estudiantes() que retorne el nombre del curso que tenga más estudiantes.

class Cursos:
    def __init__(self):
        self.estudiante = {}

    def crear_cursos(self, nombre_curso):
        self.estudiante[nombre_curso] = []

    def agregar_estudiante(self, curso, estudiante):
        self.estudiante[curso].append(estudiante)
        return self.estudiante

    def curso_mayor_estudiante(self):
        mayor = 0
        mayor_estudiantes = None

        for curso, estudiante in self.estudiante.items():
            if len(estudiante) > mayor:
                mayor = len(estudiante)
                mayor_estudiantes = curso

        return mayor_estudiantes

est = Cursos()
#Creacion de curso
est.crear_cursos("A")
est.crear_cursos("B")
#Agregamos estudiantes
est.agregar_estudiante("A", "Josue")
est.agregar_estudiante("A","Michelle")
est.agregar_estudiante("B", "Mateo")
est.agregar_estudiante("B", "Milena")
print(est.agregar_estudiante("A", "Miguel"))

print(est.curso_mayor_estudiante())
