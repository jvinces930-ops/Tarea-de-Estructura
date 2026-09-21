# Crea una clase llamada CodificadorInverso que implemente un cifrado basado en desplazamiento 
# de caracteres en el 
# alfabeto en minúsculas ('a' - 'z') e incluya un historial de operaciones.
# Requisitos:
# Atributo de instancia:
# historial: Un diccionario para almacenar cada palabra original como 
# clave y su versión codificada como valor.
# Método 1: codificar_letra(letra, desplazamiento)
# Recibe una letra en minúscula y un entero de desplazamiento (1-25).
# Aplica la fórmula de desplazamiento dentro del rango 'a'-'z' usando 
# el operador % y las funciones ord() y chr().
# Retorna la nueva letra codificada. (Si se recibe un carácter no alfabético, 
# como un espacio o número, puede retornarlo sin cambios).
# Método 2: codificar_palabra(palabra, desplazamiento)
# Recibe una palabra/texto y un desplazamiento.
# Reutiliza codificar_letra en cada carácter para construir la palabra codificada final.
# Guarda el resultado en el diccionario historial ({palabra_original: palabra_codificada}).
# Retorna la palabra codificada.

class CodificadorInverso:
    def __init__(self):
        self.historial_operaciones = {}

    def codificar_letra(self, letra, desplazamiento):
        codi = ""

        codi = (chr((ord(letra)-ord("a") + desplazamiento) % 26 + ord("a")))

        return codi

    def codificar_palabra(self, palabra, desplazamiento):
        pala = ""

        for i in palabra:
            pala += self.codificar_letra(i, desplazamiento) 

        self.historial_operaciones[palabra] = (pala)

        return self.historial_operaciones

a = CodificadorInverso()
print(a.codificar_palabra("josue", 3))
