class GestorPersonas:
    def __init__(self):
        self.persona = {}

    #primero agregar persona que guarde en un diccionario
    def agregar_personas(self, nombre, edad):
        self.persona[nombre] = edad

    #segundo tenga metodo personas mayores que retorne cuya edad sea >= 18
    def personas_mayores(self, edad_minima):
        edades = []
        for nombre, edad in self.persona.items():
            if edad >= edad_minima:
                edades.append(nombre)
        return edades

    #edad_promedio que retorne el promedio de las edades
    def edad_promedio(self):
        return sum(self.persona.values())/len(self.persona)
                
person = GestorPersonas()
person.agregar_personas("Ana", 22)
person.agregar_personas("Bob", 17)
#person.agregar_personas("Josue", 30)
print(person.personas_mayores(18))
print(person.edad_promedio())