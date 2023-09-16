"""
Ejercicio 2.5. 
a) Escribir una función que dado un número entero devuelva 1 si el mism es impar y 0 si fuera par.
b) Escribir una función que dado un número entero devuelva 0 si el mismo es impar y 1 si
fuera par.
c) Escribir una función que dado un número entero devuelva el dígito de las unidades. Por
ejemplo, para 153 debe devolver 3.
d) Escribir una función que dado un número devuelva el primer número múltiplo de 10
inferior a él. Por ejemplo, para 153 debe devolver 150.

"""
# a
def is_odd(n):
    if(n % 2 == 0 ):
        return 0
    return 1

print(is_odd(1))


# b
def is_even(n):
    if(n % 2 != 0):
        return 0
    return 1

print(is_even(1))


#c
def count_dig(n):
    return len(str(n))

print(count_dig(153))

# d
def first_multiple_ten(n):
    for i in range(n, 0, -1):
        if(i % 10 == 0 and i < n):
            return i

print(first_multiple_ten(153))