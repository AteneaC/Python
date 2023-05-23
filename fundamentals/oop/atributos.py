# declarar una clase y darle el nombre Usuario
class Usuario:		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0
#El primer parámetro de un método de instancia dentro de una clase será self
#Los atributos de instancia se definen en un "método mágico" llamado __init__ se llama cuando se crea una instancia de un nuevo objeto

Usuario()
guido = Usuario()
monty = Usuario()
# Accediendo a los atributos de la instancia
print(guido.name)	# salida: Michael
print(monty.name)	# salida: Michael
#instancias de Usuario

guido.name = "Guido"
print(guido.name) # salida: Guido
monty.name = "Monty"
print(monty.name) # salida: Monty


#ATRIBUTOS DE CLASE
class User:
    # declarando un atributo de clase
    nombre_banco = "Primer Dojo Nacional"		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0
#se definen fuera de cualquier método de instancia y se comparten entre todas las instancias de la clase. 

guido = Usuario()
monty = Usuario()
guido.nombre_banco = "Dojo Credit Union"
print(guido.bank_name) # salida: Dojo Credit Union 
print(monty.bank_name) # salida: Primer Dojo Nacional
#cambiar atributos en una instancia


User.bank_name = "Banco del Dojo"
print(guido.nombre_banco) # salida: Banco del Dojo
print(monty.nombre_banco) # salida: Banco del Dojo
#cambiar atributos en toda la clase



class Usuario:
    # los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
    # ¡ahora nuestro método tiene 2 parámetros!
    def __init__(self , name, email_address):
    	# los asignamos en consecuencia
        self.name = name
        self.email = email_address
    	# el balance de la cuenta se establece en $0
        self.balance_cuenta = 0
guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python




