class MathDojo:
    def __init__(self):
        self.resultado = 0

    def sumar(self, *args):
        for numero in args:
            self.resultado += numero
        return self

    def restar(self, *args):
        for numero in args:
            self.resultado -= numero
        return self

    def obtener_resultado(self):
        return self.resultado

# Crear una instancia de MathDojo
calculadora = MathDojo()

# Ejemplos de sumar
resultado = calculadora.sumar(5).sumar(10, 15).sumar(20, 25, 30).obtener_resultado()
print("Resultado de la suma:", resultado)  # Output: 105

# Restablecer el resultado a 0
calculadora.resultado = 0

# Ejemplos de restar
resultado = calculadora.restar(5).restar(10, 15).restar(20, 25, 30).obtener_resultado()
print("Resultado de la resta:", resultado)  # Output: -105
