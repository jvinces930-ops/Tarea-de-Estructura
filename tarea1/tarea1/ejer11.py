class Tareas:
    def __init__(self):
        self.tupla = []

    def agregar_tarea(self, descripcion, prioridad):

        tarea = (descripcion, prioridad)
        self.tupla.append(tarea)

    def tareas_prioritari(self):
        prioridad = []

        for i in self.tupla:
            if i[1] == "alta":
                prioridad.append(i)

        return prioridad

    def eliminar_completada(self, descripcion):
        for i in self.tupla:
            if i[0] == descripcion:
                self.tupla.remove(i)
                break

t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritari())