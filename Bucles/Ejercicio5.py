#Cociente y residuo sin usar división ni módulo
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

mayor = max(a, b)
menor = min(a, b)
cociente = 0

resto = mayor
while resto >= menor:
    resto -= menor
    cociente += 1

print(f"Cociente: {cociente}, Residuo: {resto}")
