class RegistroNotas:
    def __init__(self):
        self.diccio = {}

    def registar(self, estudiantes, notas):
        self.diccio[estudiantes] = notas


    def estudiantes_aprobados(self, nota_minima):
        aprobados = []

        for i, x in self.diccio.items():
            if x >= nota_minima:
                aprobados.append(i)

        return aprobados

    def mejor_estudiante(self):
        mejor = 0
        nombre = ""
        for i, x in self.diccio.items():
            if x > mejor:
                mejor = x
                nombre = i

        return nombre, mejor
    
a = RegistroNotas()
a.registar("Josue", 95)
a.registar("Michelle", 70)
a.registar("Mateo", 100)

print(a.mejor_estudiante())