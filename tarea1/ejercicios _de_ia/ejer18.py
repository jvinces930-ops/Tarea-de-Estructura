# Ejercicio práctico: Calculador de distancias entre lugares
# Vamos a crear un programa en Python utilizando clases, métodos, tuplas, listas y *args.
# 📌 Situación
# Una aplicación necesita calcular qué lugar está más cerca de una ubicación de referencia.
# Cada lugar se representa mediante una coordenada (x, y).
# Por ejemplo:
# (2, 3)
# (5, 7)
# (1, 1)
# 1️⃣ Crear la clase
# Crea una clase llamada:
# CalculadorDistancia
# La clase debe tener un atributo:
# distancias
# Este atributo será una lista vacía donde se almacenarán todas las distancias calculadas.
# 2️⃣ Método distancia_euclidiana
# Dentro de la clase crea:
# distancia_euclidiana(p1, p2)
# Debe recibir dos tuplas.
# Por ejemplo:
# p1 = (2, 3)
# p2 = (5, 7)
# Debe calcular la distancia utilizando:
# \[
# d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
# \]💡 Recuerda que para calcular una raíz cuadrada puedes utilizar:
# import math
# y después:
# math.sqrt()
# El método debe:
# 1. Obtener x e y del primer punto.
# 2. Obtener x e y del segundo punto.
# 3. Aplicar la fórmula.
# 4. Guardar el resultado en distancias.
# 5. Retornar la distancia.
# 3️⃣ Método punto_mas_cercano
# Ahora crea:
# punto_mas_cercano(referencia, *puntos)
# Este método recibirá:
# - Un punto de referencia.
# - Una cantidad variable de puntos.
# Por ejemplo:
# referencia = (0, 0)
# puntos = (3, 4), (2, 2), (6, 1), (1, 3)
# El método debe calcular la distancia desde:
# (0, 0)
# hasta cada uno de los puntos.
# Después debe determinar cuál es el punto más cercano y retornarlo.
# 🎯 Prueba final
# Cuando termines la clase, utiliza:
# cd = CalculadorDistancia()
# Después prueba:
# print(cd.distancia_euclidiana((0, 0), (3, 4)))
# Deberías obtener:
# 5.0
# Luego prueba:
# referencia = (0, 0)
# print(cd.punto_mas_cercano(
#     referencia,
#     (3, 4),
#     (2, 2),
#     (6, 1),
#     (1, 3)
# ))
# Tu programa debe determinar cuál de esos puntos está más cerca de (0, 0).
# Finalmente muestra:
# print(cd.distancias)
# para comprobar que las distancias calculadas quedaron almacenadas en la lista.

import math


class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        distancia_menor = float("inf")

        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = punto

        return punto_cercano


cd = CalculadorDistancia()

print(cd.distancia_euclidiana((0, 0), (3, 4)))

referencia = (0, 0)

print(cd.punto_mas_cercano(
    referencia,
    (3, 4),
    (2, 2),
    (6, 1),
    (1, 3)
))

print(cd.distancias)