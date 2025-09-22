"""""
⁠Llenar un arreglo de n elementos con números generados con la función random. N es
ingresado por el usuario. Diseñe un menú con las siguientes operaciones.
a. Imprimir arreglo original (El primero que se generó)
b. Suma
c. Promedio
d. Mayor
e. Menor
f. Ordenar ascendente (No perder el arreglo original; el del punto a)
g. Ordenar descendente (No perder el arreglo original; el del punto a)
h. Moda
i. Mediana
j. Buscar. Decir si encuentra el número, en qué posición(es) está, cuantas veces está
"""""

import random
import statistics  #libreria para la moda

#arreglo con n numeros aleatorios
def generar_arreglo(n):
    arreglo = []
    for i in range(n):
        arreglo.append(random.randint(1,100))
    return arreglo
    
    #imprimir el arreglo original 
def imprimir (arreglo):
    print("Arreglo original:",arreglo)
        #suma de los numeros del arrgle
def suma(arreglo):
            return sum(arreglo)
        #promedio
def promedio(arreglo):
            return sum(arreglo)/ len(arreglo)
        #mayor
def mayor(arreglo):
            return max(arreglo)
        #menor
def menor(arreglo):
            return min(arreglo)
        # Devuelve el arreglo ordenado de menor a mayor
def ordenar_ascendente(arreglo):
            return sorted(arreglo)
    # Devuelve el arreglo ordenado de menor a mayor
def ordenar_descendente(arreglo):
        return sorted(arreglo,reverse=True)
    
    #moda
def moda(arreglo):
        return statistics.multimode(arreglo)
#mediana
def mediana(arreglo):
    return statistics.median(arreglo)
#buscar
def buscar(arreglo,num):
    posiciones=[]
    for i in range(len(arreglo)):
        if arreglo[i]==num:
            posiciones.append(i)
            return posiciones
        
    #menu
def menu():
        print("\n---MENU---")
        print("A.Imprimir Arreglo Original")
        print("B.suma")
        print("C.promedio")
        print("D.mayor")
        print("E.menor")
        print("F.ordernar ascendente")
        print("G.ordernar descendente")
        print("H.moda")
        print("I.mediana")
        print("J.Buscar Numero")
        print("K.salir")

n=int(input("Cuantos numeros quieres en el arreglo"))
#arreglo original
arreglo_original = generar_arreglo(n)

#Ciclo principal para mostrar el menú y hacer operaciones
while True:
    menu()  # Mostramos el menú
    opcion = input("Elige una opción: ")

    if opcion == "A":
        imprimir(arreglo_original)

    elif opcion == "B":
        print("Suma:", suma(arreglo_original))

    elif opcion == "C":
        print("Promedio:",promedio(arreglo_original))

    elif opcion == "D":
        print("Mayor:", mayor(arreglo_original))

    elif opcion == "E":
        print("Menor:", menor(arreglo_original))

    elif opcion == "F":
        print("Ascendente:", ordenar_ascendente(arreglo_original))

    elif opcion == "G":
        print("Descendente:", ordenar_descendente(arreglo_original))

    elif opcion == "H":
        print("Moda:", moda(arreglo_original))

    elif opcion == "I":
        print("Mediana:", mediana(arreglo_original))

    elif opcion == "J":
        num = int(input("Número a buscar: "))
        posiciones = buscar(arreglo_original, num)
        if posiciones:
            print(f"El número {num} está en las posiciones {posiciones} y aparece {len(posiciones)} veces.")
        else:
            print("El número no está en el arreglo.")

    elif opcion == "K":
        print("Fin del programa.")
        break

    else:
        print("Opción inválida, prueba de nuevo.")