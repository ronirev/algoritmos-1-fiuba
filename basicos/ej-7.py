"""
Ejercicio 1.7. Escribir un programa que le pida una palabra al usuario, para luego imprimirla
1000 veces, en una única línea, con espacios intermedios.
Ayuda: Investigar acerca del parámetro end de la función print.

"""

word = input("Ingrese una palabra: ")

for i in range(1001):
    print(word, end=" ")