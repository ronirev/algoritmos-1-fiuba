""" Ejercicio 1.2. Utilizando la función del ejercicio anterior, escribir un programa (un archivo .py)
que pida al usuario dos números, y luego muestre el producto. """

first_n = int(input('Ingrese un numero: '))
second_n = int(input('Ingrese un segundo numero: '))

def f(a,b):
    return a *b

print(f(first_n,second_n))
