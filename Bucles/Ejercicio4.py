
#Determinar si un número es perfecto
numero=int(input('Ingresa Un numero'))
suma=0

for i in range(1, numero):
    if numero % i == 0:
        suma += i

if suma == numero:
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero } no es un número perfecto.")