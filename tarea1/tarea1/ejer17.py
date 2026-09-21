class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        Ascci = ""

        Ascci = (chr((ord(letra) - ord("a") + desplazamiento) % 26 + ord("a")))

        return Ascci

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for i in palabra:
            resultado += self.codificar_letra(i, desplazamiento)

        self.historial[palabra] = (resultado)
        return resultado, self.historial
    
a = CodificadorCesar()
print(a.codificar_palabra("michelle", 3))