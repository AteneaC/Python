class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    # agregando el método de depósito
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
    	self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido

guido.hacer_depósito(100)
guido.hacer_depósito(200)
monty.hacer_depósito(50)
print(guido.balance_cuenta)	# salida: 300
print(monty.balance_cuenta)	# salida: 50

# El parámetro self incluye toda la información sobre el objeto individual que ha llamado al método. 

