#Solicitar 3 números al usuario. 
# Decir si uno de ellos es igual a la suma 
# de los otros dos. Se usan operadores lógicos.

numero1=int(input('Ingrese el primer numero :'))
numero2=int(input('Ingrese el segundo numero :'))
numero3=int(input('Ingrese el tercer  numero :'))

if (numero1 + numero2)== numero3:
    print('La suma del numero 1 y el numero 2 es igual al numero 3 digitado')
if (numero1+numero3)==numero2: 
    print('La suma del numero 1 y el numero 3 es igual al numero 2 digitado')
if(numero2+numero3)==numero1:
    print('La suma del numero 2 y el numero 3 es igual al numero 1 digitado')
else :
    print('ninguno de los números es igual a la suma de los otros dos')
    