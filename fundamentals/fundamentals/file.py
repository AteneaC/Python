num1 = 42 #es una variable de tipo numero y es entero
num2 = 2.3 #es una variable de tipo numero y es decimal
boolean = True  #es un tipo de dato primitivo y es un valor booleano
string = 'Hello World'  #es un tipo de dato primitivo y es una cadena
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #arreglo tipo lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #variable tipo diccionario
fruit = ('blueberry', 'strawberry', 'banana')   #es un tipo de dato compuesto y es una tupla
print(type(fruit)) #imprimir o mostrar la tupla
print(pizza_toppings[1]) #imprimir o mostrar la posicion 1 de la lista
pizza_toppings.append('Mushrooms') #agregar
print(person['name'])  #imprimir el valor de la clave name
person['name'] = 'George'  #agregar dato
person['eye_color'] = 'blue'  #agregar dato
print(fruit[2]) #imprimir o mostrar la posicion 2 de la lista

if num1 > 45:   #condicional si
    print("It's greater")   #imprimir  o mostrar
else:   #condicional si no
    print("It's lower") #imprimir  o mostrar

if len(string) < 5: #condicional si
    print("It's a short word!") #imprimir  o mostrar
elif len(string) > 15:  
    print("It's a long word!")  #imprimir  o mostrar
else:   #condicional si no
    print("Just right!")    #imprimir  o mostrar

for x in range(5):  #for en un rango de 0 a 5
    print(x)     #imprimir  o mostrar   x
for x in range(2,5):    #for en un rango de 0 a 2
    print(x)     #imprimir  o mostrar   x
for x in range(2,10,3): #for en un rango de 2 a 10 a 3
    print(x)     #imprimir  o mostrar   x
x = 0   #declarar el valor de una variable
while(x < 5): #mientras x sea menor que 5
    print(x)     #imprimir  o mostrar   x
    x += 1  # x mayor o igual a 1

pizza_toppings.pop() #elimina o retorna
pizza_toppings.pop(1) #elimina o retorna posicion 1

print(person) #imprime o muestra
person.pop('eye_color') #elimina o retorna
print(person)  #imprime o muestra

for topping in pizza_toppings: #bucle topping 
    if topping == 'Pepperoni': #condicional si es igual a
        continue 
    print('After 1st if statement') #imprime o muestra
    if topping == 'Olives': #condicional si es igual a
        break

def print_hello_ten_times(): #definir vaiable
    for num in range(10):   #for en un rango de  0 a 10
        print('Hello') #impimir o mostrar

print_hello_ten_times()

def print_hello_x_times(x): #definir vaiable
    for num in range(x):   #for en un rango de x 
        print('Hello')  #impimir o mostrar

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #definir vaiable
    for num in range(x): #for en un rango de 0 a x = 10
        print('Hello')  #impimir o mostrar

print_hello_x_or_ten_times()    
print_hello_x_or_ten_times(4)