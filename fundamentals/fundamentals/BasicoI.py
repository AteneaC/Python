#Basico
for x in range(0,151):
    print (x)

#Multiplos de 5
for i in range(5,1001,5):
    print(i)

#Contando al estilo dojo
for a in range(1,101): 
    if a % 5 == 0:
        print("Coding")
    elif a % 10 == 0:
        print("Coding Dojo")
    else:
        print(a)

#Whoa. Es un gran idiota
sum = 0
for x in range(1,500001,2):
    sum += x
print(f"La suma final es: {sum}")

#Cuenta Regresiva de 4
count = 2018
while count > 0:
    print(count)
    count -= 4

#Contador flexible
LowNum = 2
highNum = 9
mult = 3
for num in range(LowNum, highNum + 1):
    if num % mult == 0:
        print(num)