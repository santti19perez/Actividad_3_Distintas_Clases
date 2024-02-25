import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.esquina1 = punto1
        self.esquina2 = punto2

    def calcular_perimetro(self):
        lado1 = abs(self.esquina1.x - self.esquina2.x)
        lado2 = abs(self.esquina1.y - self.esquina2.y)
        return 2 * (lado1 + lado2)

    def calcular_area(self):
        lado1 = abs(self.esquina1.x - self.esquina2.x)
        lado2 = abs(self.esquina1.y - self.esquina2.y)
        return lado1 * lado2

    def es_cuadrado(self):
        lado1 = abs(self.esquina1.x - self.esquina2.x)
        lado2 = abs(self.esquina1.y - self.esquina2.y)
        return lado1 == lado2

esquina_sup_izq = Punto(2, 4)
esquina_inf_der = Punto(5, 1)

mi_rectangulo = Rectangulo(esquina_sup_izq, esquina_inf_der)

print("El perímetro del rectángulo es:", mi_rectangulo.calcular_perimetro())

print("El área del rectángulo es:", mi_rectangulo.calcular_area())

if mi_rectangulo.es_cuadrado():
    print("El rectángulo es un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")

#Aca decidi implementar numeros al azar en ambos puntos tanto de Perimetro como de Area, cambie los valores
#y dependiendo su resultado dictara gracias a los prints si es o no un cuadrado.
