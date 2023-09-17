"""
Ejercicio 2.7. Escribir un programa que le pregunte al usuario un número n e imprima los
primeros n números triangulares, junto con su índice. Los números triangulares se obtienen
mediante la suma de los números naturales desde 1 hasta n. Es decir, si se piden los primeros 5
números triangulares, el programa debe imprimir:

"""

def print_triangular_formula(n):
    for i in range(1, n+1):
        i_triangular = round(i*(i +1)/2)
        print(f"{i} - {i_triangular}")

def print_triangular(n):
    for i in range(1, n+1):
        if(i == 1 ):
            i_triangular = i
        else:
            i_triangular += i
        print(f"{i} - {i_triangular}")


print_triangular(5)