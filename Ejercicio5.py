"""Llenar un arreglo de n elementos con números generados con la 
función random. Cada número siguiente debe ser mayor que el anterior, pero no puede exceder el valor de la siguiente decena."""""

import random

def generar_arreglo(n):
    arreglo = []
    # Primer número aleatorio entre 1 y 9
    arreglo.append(random.randint(1, 9))

    for _ in range(1, n):
        anterior = arreglo[-1]   # último número generado
        limite_superior = ((anterior // 10) + 1) * 10  # siguiente decena

        # generar un número mayor que el anterior pero <= limite_superior
        if anterior < limite_superior:
            num = random.randint(anterior + 1, limite_superior)
        else:
            # si ya llegamos a una decena exacta, saltamos a la siguiente
            num = random.randint(anterior + 1, limite_superior + 10)

        arreglo.append(num)

    return arreglo


# Programa principal
n = int(input("Ingrese el tamaño del arreglo: "))
arreglo = generar_arreglo(n)

print("\nArreglo generado:", arreglo)
