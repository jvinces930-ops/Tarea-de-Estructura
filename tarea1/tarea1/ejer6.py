class AnalizadorNumeros:
    def __init__(self):
        pass

    #"primero es par?"
    def es_par (self, numero):
        par = False

        if numero % 2 == 0:
            par = True

        return par

    # Segundo separar numero que retorne un diccionario ("pares": [...], impares: [...] reutilizando par)
    def separar_numeros (self, *numeros):
        diccio = {
            "pares":[],
            "impares":[]
        }

        for num in numeros:
            if self.es_par(num):
                diccio["pares"].append(num)
            else:
                diccio["impares"].append(num)

        return diccio

nu = AnalizadorNumeros()
print(nu.separar_numeros(1, 2, 3, 4, 5))