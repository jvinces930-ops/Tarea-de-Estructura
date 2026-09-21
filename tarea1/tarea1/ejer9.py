class Equipos:
    def __init__(self):
        self.diccionario = {}
        self.lista = []

    #primero crear equipos que inicie como una lista vacia en un diccionario
    def crear_equipos(self, nombre_equipo): 
        self.diccionario[nombre_equipo] = []

    #segundo agregar jugador que añada al jugador al equipo
    def agregar_jugador(self, equipo, jugador):
        self.diccionario[equipo].append(jugador)
        return self.diccionario

    def equipo_mayor_integrantes(self):
        mayor = 0
        mayor_jugadores = None

        for equipo, jugadores in self.diccionario.items():
            if len(jugadores) > mayor:
                mayor = len(jugadores)
                mayor_jugadores = equipo

        return mayor_jugadores

jug = Equipos()
jug.crear_equipos("a")
jug.crear_equipos("b")
print(jug.agregar_jugador("a", "josue"))
print(jug.agregar_jugador("b", "mateo"))
print(jug.agregar_jugador("b", "miguelito"))

print(jug.equipo_mayor_integrantes())