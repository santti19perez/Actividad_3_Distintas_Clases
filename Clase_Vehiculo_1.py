class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

vehiculo1 = Vehiculo(255, 70000)
print("Velocidad máxima del vehículo 1:", vehiculo1.velocidad_maxima)
print("Kilometraje del vehículo 1:", vehiculo1.kilometraje)

vehiculo2 = Vehiculo(130, 100000)
print("Velocidad máxima del vehículo 2:", vehiculo2.velocidad_maxima)
print("Kilometraje del vehículo 2:", vehiculo2.kilometraje)

#Aca utilice lo basico, selfs, para definir las dos instancias que se me pedian, finalmente quise añadirle
#valores randoms de una velocidad maxima y un km para dar ejm de detalles de autos
