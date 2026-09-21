# Método crear_tupla(*frutas):
# Recibe varios nombres de frutas como argumentos individuales 
# (por ejemplo: "manzana", "pera") y los retorna dentro de una tupla.
# Método combinar_frutas(*listas_tuplas):
# Recibe múltiples tuplas de frutas usando *listas_tuplas.
# Utiliza un conjunto (set()) para unir todas las frutas enviadas y eliminar automáticamente 
# las que estén repetidas.
# Retorna una lista ordenada alfabéticamente con las frutas únicas.

class GestorDeFrutas:

    def crear_tupla(self, *frutas):
       return frutas

    def combinar_frutas(self, *lista_tuplas):
        conjunto = set()

        for x in lista_tuplas:
            conjunto.update(x)

        return sorted(list(conjunto))

a = GestorDeFrutas()
print(a.combinar_frutas(("manzana", "pera"),("pera", "uva"), ("banano", "manzana")))