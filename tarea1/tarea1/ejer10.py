class AnalizadorString:
    
    def __init__(self):
        self.palabra_larga = ""
        self.vocales = ["a","e","i","o","u","A","E","I","O","U"]

    def solo_vocales(self, letra):

        vocal = False

        for i in self.vocales:
            if i == letra:
                vocal = True
                break

        return vocal

    def contar_por_tipo(self, texto):

        if len(texto) > len(self.palabra_larga):
            self.palabra_larga = texto

        contador_vocales = 0
        contador_digitos = 0 
        contador_consonantes = 0
        
        for i in texto:
        
            if self.solo_vocales(i):
                contador_vocales = contador_vocales + 1
            elif i.isdigit():
                contador_digitos = contador_digitos + 1
            elif i.isalpha():
                contador_consonantes = contador_consonantes + 1 

        return {
            "vocales":[contador_vocales],
            "consonantes":[contador_consonantes],
            "digitos":[contador_digitos]
        }
                     

pala = AnalizadorString()
print(pala.contar_por_tipo("Josue2"))
