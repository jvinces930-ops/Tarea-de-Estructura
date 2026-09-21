# Crea una clase llamada AnalizadorNombres que:
# 1. Tenga un método buscar_nombres(texto, inicial) que busque los nombres que empiecen con la inicial indicada y devuelva una lista.
# 2. Tenga un método agrupar_por_longitud(texto) que devuelva un diccionario donde:
#    - La clave sea la longitud del nombre.
#    - El valor sea una lista con los nombres de esa longitud.
# 3. Tenga un método nombres_unicos(texto) que utilice un conjunto (set) para eliminar nombres repetidos.

class AnalizadorNombres:

    def buscar_nombres(self, texto, inicial):
        nombres = texto.split()
        encontrados = []

        for nombre in nombres:
            if nombre.startswith(inicial):
                encontrados.append(nombre)

        return encontrados

    def agrupar_por_longitud(self, texto):
        nombres = texto.split()
        grupos = {}

        for nombre in nombres:
            longitud = len(nombre)

            if longitud not in grupos:
                grupos[longitud] = []

            grupos[longitud].append(nombre)

        return grupos

    def nombres_unicos(self, texto):
        nombres = texto.split()
        return set(nombres)


# Crear objeto
an = AnalizadorNombres()

texto = "Ana Luis Carlos Ana Pedro Luis Miguel"

# Buscar nombres que comienzan con A
print("Nombres con A:")
print(an.buscar_nombres(texto, "A"))

# Agrupar por longitud
print("\nNombres agrupados por longitud:")
print(an.agrupar_por_longitud(texto))

# Obtener nombres únicos
print("\nNombres únicos:")
print(an.nombres_unicos(texto))