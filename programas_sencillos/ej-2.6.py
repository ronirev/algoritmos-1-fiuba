"""
Ejercicio 2.6. Escribir un programa que imprima todos los números pares entre dos números
que se le pidan al usuario.
"""

def is_even(n):
    if(n % 2 != 0):
        return False
    return True

def print_even(a, b):
    print(f"Entre los numeros {a} y {b} existen los siguientes pares: ")
    for i in range(a,b+1):
        if(is_even(i)):
            print(f"Numero Par: {i}")

print_even(2,4)