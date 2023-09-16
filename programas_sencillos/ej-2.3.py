"""
Ejercicio 2.3. Escribir una función que convierta un valor dado en grados Fahrenheit a grados
Celsius. Recordar que la fórmula para la conversión es: F = (9/5)C + 32


"""
def conver_fah_to_cel(grades):
    # C = (°F - 32) / 1.8
    grades_celcius = (grades - 32) / 1.8
    return grades_celcius


grade_fahrenheit = int(input("Ingrese los grados a convertir: "))

conversion = round(conver_fah_to_cel(grade_fahrenheit),2)

print(f"{grade_fahrenheit}º Fahrenheit a Grados Celcius son {conversion}ºC")
