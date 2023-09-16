"""
Ejercicio 1.6. Escribir funciones que resuelvan los siguientes problemas:
a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.
b) Dado un número natural n, imprimir su tabla de multiplicar.

"""

# a 

def calculete_basics(a, b):
    sum = a + b
    rest = a - b 
    div = a / b
    mult= a * b

    print(sum, rest, div, mult)

def times_table (n):
    print(f'**** TABLE of {n} ****')
    for i in range(11):
        print (i,'*', n, '=', i*n)




times_table(2)