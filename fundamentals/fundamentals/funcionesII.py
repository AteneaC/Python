#1.cuenta regresiva
def countdown(num):
    lista = list(range(num, -1, -1))
    return lista
num = 5
resultado = countdown(num)
print(resultado)

#2.imprimir y devolver
def imprimir_y_devolver(lista):
    primer_valor = lista[0]
    segundo_valor = lista[1]
    print(primer_valor)
    return segundo_valor
lista = [1, 2]
resultado = imprimir_y_devolver(lista)
print(resultado)

#3.primero mas logitud
def primero_mas_longitud(lista):
    primer_valor = lista[0]
    resultado = primer_valor + len(lista)
    return resultado

lista = [1, 2, 3, 4, 5]
resultado = primero_mas_longitud(lista)
print(resultado)

#4.valores mayores que el segundo
def valores_mayores_que_el_segundo(lista):
    if len(lista) < 2:
        return False

    segundo_valor = lista[1]
    valores_mayores = [valor for valor in lista if valor > segundo_valor]

    print(len(valores_mayores))
    return valores_mayores
lista1 = [5, 2, 3, 2, 1, 4]
resultado1 = valores_mayores_que_el_segundo(lista1)
print(resultado1)

lista2 = [3]
resultado2 = valores_mayores_que_el_segundo(lista2)
print(resultado2)

#5.esta longitud, ese valor
def length_and_value(tamaño, valor):
    lista = [valor] * tamaño
    return lista
resultado1 = length_and_value(6, 3)
print(resultado1)

resultado2 = length_and_value(3, 9)
print(resultado2)


