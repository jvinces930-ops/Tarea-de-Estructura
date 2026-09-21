from math import sqrt

class Calculadordistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1

        distancia = sqrt(dx**2 + dy**2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        mas_cercano = None
        menor_distancia = None

        for i in puntos:
            distancia = self.distancia_euclidiana(referencia, i)

            if menor_distancia is None or distancia < menor_distancia:
                mas_cercano = i
                menor_distancia = distancia

        return mas_cercano

    


a = Calculadordistancia()

print(a.distancia_euclidiana((0, 0), (3, 4)))
punto = a.punto_mas_cercano(
    (0, 0),
    (3, 4),
    (1, 1),
    (10, 2)
)

print("Punto más cercano:", punto)
print("Distancias calculadas:", a.distancias)