class CuentaBancaria:
    def __init__(self, tasa_interes, monto=0):
        self.balance = monto
        self.tasa_interes = tasa_interes   
    def deposito(self, monto):
        self.balance += monto    
    def retiro(self, monto):
        if self.balance >= monto:
            self.balance -= monto
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5   
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")   
    def generar_interes(self):
        if self.balance > 0:
            interes = self.balance * self.tasa_interes
            self.balance += interes


# Crear la primera cuenta y realizar operaciones encadenadas
cuenta1 = CuentaBancaria(0.02).deposito(100).deposito(200).deposito(300).retiro(150).generar_interes().mostrar_info_cuenta()
# Crear la segunda cuenta y realizar operaciones encadenadas
cuenta2 = CuentaBancaria(0.01, 500).deposito(5000).deposito(100).retiro(1500).retiro(1500).retiro(1500).retiro(1500).generar_interes().mostrar_info_cuenta()