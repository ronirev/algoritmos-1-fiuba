"""
Ejercicio 2.4. Escribir un programa que utilice la función anterior para generar una tabla de
conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.

"""
def conver_fah_to_cel(grades):
    # C = (°F - 32) / 1.8
    grades_celcius = round(((grades - 32) / 1.8),2)
    return grades_celcius


def print_table_fahrenheit_to_celcius():
    print("******* TABLE FAHRENHEIT TO CELCIUS ******")
    for i in range(0,130,10):
        conversion= conver_fah_to_cel(i)
        print(f" {i}ºF ==> {conversion}ºC")


print_table_fahrenheit_to_celcius()