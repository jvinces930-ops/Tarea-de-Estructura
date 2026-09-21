class GestorTemperatura:
    def __init__(self):
        self.lis = []

    # primero registar temperatura y lo guarde en una lista 
    def registar_temperatura(self, temp):
        self.lis.append(temp)

    #realizar calculos max, min, promedio que calculen estadistica
    def min(self):
        return min(self.lis)

    def max(self):
        return max(self.lis)

    def prom(self):
        return sum(self.lis)/len(self.lis)

    #registar multiples temperaturas y reutilizar la funcion registar temperatura
    def registar_multiples(self, *tem):
        for i in tem:
            self.registar_temperatura(i)


temp = GestorTemperatura()
temp.registar_multiples(20, 25, 18, 30)

print(temp.max())
print(temp.min())
print(temp.prom())