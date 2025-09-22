#Escribe un programa que pida tres números y 
# que escriba si son los tres iguales, si hay 
# dos iguales o si son los tres distintos.
numeroA=int(input('Ingrese el primer numero :'))
numeroB=int(input('Ingrese el segundo numero :'))
numeroC=int(input('Ingrese el tercer  numero :'))

if numeroA==numeroB == numeroC:
    print('Los tres numeros son iguales')
if numeroA==numeroB or numeroB==numeroC or numeroA==numeroC:
    print('Hay dos numeros iguales')
else:
    print('Los numeros so diferentes')


