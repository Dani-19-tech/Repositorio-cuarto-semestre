"""⁠Llenar dos arreglos de n elementos con números generados con la función random.
Compararlos y decir:
a. Cuál de los dos tiene la suma más alta
b. Cuál de los dos tiene el número mayor
c. Cuál de los dos tiene el número menor
d. Cuál es el promedio conjunto (uniendo los dos arreglos)
e. Sacar el promedio de cada uno y decir si está por encima o por debajo del
promedio de las listas juntas
f. Cuál de los dos tiene mayor cantidad de pares"""

import random

def generar_arreglo(n):
    arreglo = []
    for i in range(n):
        arreglo.append(random.randint(1,100))
    return arreglo

def suma(lista):
    return sum(lista)
def mayor(lista):
    return max(lista)
def menor(lista):
    return min(lista)
def promedio(lista):
    return sum(lista) / len(lista)
def pares(lista):
    return sum(1 for num in lista if num % 2 ==0)
def impares(lista):
    return sum(1 for num in lista if num % 2 !=0)
n= int(input("Ingrese el tamaño de los arreglos"))
arreglo1=generar_arreglo(n)
arreglo2=generar_arreglo(n)

print("\nArreglo 1:",arreglo1)
print("Arreglo 2:",arreglo2)

# a. Cuál tiene la suma más alta
suma1 = suma(arreglo1)
suma2 = suma(arreglo2)
if suma1 > suma2:
    print("\na) El arreglo 1 tiene la suma más alta:", suma1)
elif suma2 > suma1:
    print("\na) El arreglo 2 tiene la suma más alta:", suma2)
else:
    print("\na) Ambos tienen la misma suma:", suma1)

# b. Cuál tiene el número mayor
mayor1 = mayor(arreglo1)
mayor2 = mayor(arreglo2)
if mayor1 > mayor2:
    print("b) El número mayor está en el arreglo 1:", mayor1)
elif mayor2 > mayor1:
    print("b) El número mayor está en el arreglo 2:", mayor2)
else:
    print("b) Ambos arreglos tienen el mismo número mayor:", mayor1)

# c. Cuál tiene el número menor
menor1 = menor(arreglo1)
menor2 = menor(arreglo2)
if menor1 < menor2:
    print("c) El número menor está en el arreglo 1:", menor1)
elif menor2 < menor1:
    print("c) El número menor está en el arreglo 2:", menor2)
else:
    print("c) Ambos arreglos tienen el mismo número menor:", menor1)

# d. Promedio conjunto
promedio_total = promedio(arreglo1 + arreglo2)
print("d) El promedio conjunto de los dos arreglos es:", promedio_total)

# e. Promedio de cada uno comparado con el conjunto
prom1 = promedio(arreglo1)
prom2 = promedio(arreglo2)

print("e) Promedio arreglo 1:", prom1, "->", "Encima" if prom1 > promedio_total else "Debajo")
print("   Promedio arreglo 2:", prom2, "->", "Encima" if prom2 > promedio_total else "Debajo")

# f. Cuál tiene mayor cantidad de pares
pares1 = pares(arreglo1)
pares2 = pares(arreglo2)
if pares1 > pares2:
    print("f) El arreglo 1 tiene más pares:", pares1)
elif pares2 > pares1:
    print("f) El arreglo 2 tiene más pares:", pares2)
else:
    print("f) Ambos tienen la misma cantidad de pares:", pares1)

# g. Cuál tiene mayor cantidad de impares
impares1 = impares(arreglo1)
impares2 = impares(arreglo2)
if impares1 > impares2:
    print("g) El arreglo 1 tiene más impares:", impares1)
elif impares2 > impares1:
    print("g) El arreglo 2 tiene más impares:", impares2)
else:
    print("g) Ambos tienen la misma cantidad de impares:", impares1)
