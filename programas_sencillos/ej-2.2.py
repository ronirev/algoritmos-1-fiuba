"""
Ejercicio 2.2. Utilizando la función del ejercicio anterior, escribir un programa que le pregunte
al usuario la cantidad de pesos inicial, la tasa de interés y el número de años y muestre el monto
final a obtener.

"""
def calculate_compound_interest(capital, rate, time):
    capital = int(capital)
    rate = int(rate)
    time = int(time)
    compound_interest= capital * ( 1 + rate/100 ) ** time

    return  round(compound_interest, 2)


capital = input("Ingrese su capital inicial: ")
rate = input("Ingrese la tasa de interes: ")
time = input("Ingrese los años que desea calcular: ")

print(f"Su monto a obtener despues de {time} año/s es ", calculate_compound_interest(capital, rate, time))