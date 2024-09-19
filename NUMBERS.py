#Hay tres tipos de variables numéricas en Python: int, float, complex
"""
INT
o entero, es un número entero, positivo o negativo, sin decimales, de longitud ilimitada.
"""
x = 5
y = 5242525
z = -7
print(type(x))
print(type(y))
print(type(z))
"""
FLOAT
Es un número, positivo o negativo, que contiene uno o más decimales.
Float también puede ser números científicos con una "e o E" para indicar la potencia de 10.
"""
x = 1.02
y = 10E4
z = -75.5
print(type(x))
print(type(y))
print(type(z))
"""
COMPLEX
Los números complejos se escriben con una "j" como parte imaginaria.
"""
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))


#CONVERSIÓN DE TIPOS
x = 5    # int
y = 67.999  # float
z = 1j   # complex

#convertir int en float se le agrega .0:
a = float(x)

#convertir float en int en este metodo solo toma la parte entera ignorando el decimal:
b = int(y)

#convertir int en float se le agrega + 0j:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#NÚMEROS ALEATORIOS
import random  #se tiene que agregar esta libreria

X=random.randrange(1, 100)#rango desde 1 hasta 99
print(X)