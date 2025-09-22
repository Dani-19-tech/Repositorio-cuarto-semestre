
import random

def generar_arreglo(n):
    arreglo = []
    while len (arreglo) < n:
        num=random.randint(1,100)
        if num in arreglo:
            print(f"El numero{num} ya ha sido digitado ateriormente")
        else:
            arreglo.append(num)
    return arreglo
n=int(input("Ingrese el tamaño del arreglo"))
arreglo= generar_arreglo(n)
print("/n Arreglo sin repeticiones",arreglo)
    


