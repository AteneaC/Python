class Usuario:
    nombre_banco = "hola"
    def __init__(self , balance_cuenta):
        self.balance_cuenta = 10000
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
    def hacer_depósito(self, amount):
        self.balance_cuenta += amount

Nicolas = Usuario("balance_cuenta")
Leonel = Usuario("balance_cuenta")
Atenea = Usuario("balance_cuenta")

Nicolas.hacer_depósito(50000)
Nicolas.hacer_depósito(10000)
Nicolas.hacer_depósito(20000)
Nicolas.hacer_retiro(5000)

Leonel.hacer_depósito(30000)
Leonel.hacer_depósito(60000)
Leonel.hacer_retiro(2500)
Leonel.hacer_retiro(9000)

Atenea.hacer_depósito(150000)
Atenea.hacer_retiro(3060)
Atenea.hacer_retiro(2060)
Atenea.hacer_retiro(7080)

print(f"Nicolas, Balance: {Nicolas.balance_cuenta}")
print(f"Leonel, Balance: {Leonel.balance_cuenta}")
print(f"Atenea, Balance: {Atenea.balance_cuenta}")
