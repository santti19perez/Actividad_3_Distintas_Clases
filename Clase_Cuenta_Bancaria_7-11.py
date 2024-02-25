class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Se han depositado {cantidad} en la cuenta {self.numero_cuenta}. Nuevo balance: {self.balance}")

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se han retirado {cantidad} de la cuenta {self.numero_cuenta}. Nuevo balance: {self.balance}")
        else:
            print("No hay suficientes fondos en la cuenta.")

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= cuota_manejo
        print(f"Se ha aplicado una cuota de manejo del 2% en la cuenta {self.numero_cuenta}. Nuevo balance: {self.balance}")

    def mostrar_detalles(self):
        print(f"Detalles de la cuenta bancaria:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance}")

cuenta1 = CuentaBancaria("123456", ["Juan", "María"], 1000)

cuenta1.mostrar_detalles()
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.aplicar_cuota_manejo()
cuenta1.mostrar_detalles()

#para hice cada uno de los def con las cosas que se me pedian, en resumidas cuentas defini una cuenta con
#todos los requisitos, detalles de la cuenta, entre estos, numero de la cuenta, propietarios y su balance
