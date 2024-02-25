import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2)
        return distancia_centro_punto <= self.radio

centro = Punto(0, 0)
circulo = Circulo(centro, 5)

print("Área del círculo:", circulo.calcular_area())
print("Perímetro del círculo:", circulo.calcular_perimetro())

punto1 = Punto(3, 4)
punto2 = Punto(6, 8)

print("¿El punto (3, 4) pertenece al círculo?", circulo.punto_pertenece(punto1))
print("¿El punto (6, 8) pertenece al círculo?", circulo.punto_pertenece(punto2))

#defini un centro y un radio para el circulo, con estos dos datos contruyo el area y perimetro, asi mismo
#al punto se le define su centro y radio con valores randoms puestos por mi para dictaminar si pertenece
#o no al circulo

