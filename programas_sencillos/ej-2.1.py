"""
Ejercicio 2.1. Escribir una función que reciba una cantidad de pesos, una tasa de interés y un
número de años y devuelva el monto final a obtener. La fórmula a utilizar es:

Cn = C × (1 + x100)**n

Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.

"""

def calculate_compound_interest(capital, rate, time):
    capital = int(capital)
    rate = int(rate)
    time = int(time)
    compound_interest= capital * ( 1 + rate/100 ) ** time

    return  compound_interest