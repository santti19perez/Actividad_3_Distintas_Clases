import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
        print(f"El punto se ha movido a las coordenadas: ({self.x}, {self.y})")

    def calcular_distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia

punto1 = Punto(3, 4)
punto2 = Punto(6, 8)

punto1.mostrar()
punto2.mostrar()

distancia_entre_puntos = punto1.calcular_distancia(punto2)
print("Distancia entre los puntos 1 y 2:", distancia_entre_puntos)

punto1.mover(5, 7)
punto1.mostrar()

#En la parte de calcular_distancia utilice una formula de la Geometria que es la formula Euclidiana
#la cual con el Teorema de Pitagoras permite que se calcule la distancia entre puntos, la idea de usar
#esta operacion la saque de un video de youtube
