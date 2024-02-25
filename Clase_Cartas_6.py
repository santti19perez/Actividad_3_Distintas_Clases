class Carta:

    CORAZON = "Corazón"
    DIAMANTE = "Diamante"
    TREBOL = "Trébol"
    ESPADA = "Espada"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

carta1 = Carta(10, Carta.CORAZON)
print("Valor de la carta:", carta1.valor)
print("Pinta de la carta:", carta1.pinta)

carta2 = Carta("As", Carta.TREBOL)
print("Valor de la carta:", carta2.valor)
print("Pinta de la carta:", carta2.pinta)

#Aca defini los campos para hablar de 2 cartas, cada una de ellas tendra tanto valor como nombre y pues su pinta
#di valores ya asignados pero desde la parte del codigo se puede modificar en caso de que quiera otro valor-pinta
