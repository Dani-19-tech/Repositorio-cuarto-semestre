""" ⁠Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario
indique al inicio del programa."""
n=int(input("Ingresa la cantidad de digitos"))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
    
for i in range(n):
    print(fibonacci(i),end=" ")

