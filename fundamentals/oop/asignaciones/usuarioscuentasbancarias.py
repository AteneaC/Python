
class Usuario:
    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = cuenta   
    def hacer_deposito(self, monto):
        self.cuenta.deposito(monto)    
    def hacer_retiro(self, monto):
        self.cuenta.retiro(monto)   
    def mostrar_info_cuenta(self):
        self.cuenta.mostrar_info_cuenta()    
    def generar_interes(self):
        self.cuenta.generar_interes()
