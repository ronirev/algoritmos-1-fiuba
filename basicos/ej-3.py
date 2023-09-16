""" Ejercicio 1.3. Escribir funciones que permitan:
a) Calcular el perímetro de un rectángulo dada su base y su altura.
b) Calcular el área de un rectángulo dada su base y su altura.
c) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas
x1, x2, y1, y2.
d) Calcular el perímetro de un círculo dado su radio.
e) Calcular el área de un círculo dado su radio.
f) Calcular el volumen de una esfera dado su radio.
g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. """


# a 
def rectangle_perimeter(base,height):
    return base * 2 + height * 2

#b
def rectangle_area(base,heigth):
    return base * heigth

# d 
def circle_perimeter(radio):
    PI = 3.14
    return 2 * PI * radio


#e
def circle_area(radio):
    PI = 3.14
    return PI * radio**2

#f
def volume_sphere(radio):
    PI = 3.14
    constant = 4/3

    return constant * PI * radio**3



#g
def calculate_hypotenuse(ca, cb):
    hypotenuse = pow(ca**2 + cb **2, 0.5)
    return hypotenuse


