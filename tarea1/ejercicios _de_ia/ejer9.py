# Diseña la clase AnalizadorNumerico que cumpla con los siguientes requerimientos:
# Estado interno (__init__):
# Debe tener un atributo suma_total que inicie en 0. Guardará la suma acumulada de todos 
# los números procesados en la historia de la instancia.
# Método helper es_numero_par(self, digito):
# Recibe un carácter o entero digito.
# Retorna True si es un número par (0, 2, 4, 6, 8) y False en caso contrario.
# Método principal clasificar_y_sumar(self, texto):
# Recibe una cadena de texto (ejemplo: "a1b2c3d4").
# Reutiliza el método es_numero_par para verificar cada número encontrado.
# Cuenta cuántos dígitos son pares y cuántos son impares (ignora letras o símbolos).
# Suma el valor de todos los dígitos encontrados en la cadena y actualiza el atributo suma_total.11
# Retorna un diccionario con la estructura: {'pares': cant, 'impares': cant, 'suma_texto': suma}.

class AnalizadorNumerico: 
    def __init__(self):
        self.suma_total = 0

    def es_numero_par(self, digito):
        numero_par = False

        if digito.isdigit():
            self.suma_total += int(digito)
            if int(digito)%2==0:
                numero_par = True

        return numero_par

    def Clasificar_y_sumar(self, texto):
        
        clasificacion = {
            "pares" : 0,
            "impares" : 0,
            "cadena" : 0
        }

        for i in texto:
            if self.es_numero_par(i):
                clasificacion["pares"] += 1
            elif i.isalpha():
                clasificacion["cadena"] += 1
            else:
                clasificacion["impares"] += 1

        return clasificacion
    
    def suma_total_numeros(self):
        return (self.suma_total)


a = AnalizadorNumerico()
print(a.Clasificar_y_sumar("a1b2c4"))
print(a.Clasificar_y_sumar("x8y9"))

print(a.suma_total_numeros())
