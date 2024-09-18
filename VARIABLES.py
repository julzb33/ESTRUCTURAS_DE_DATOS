#creacion de variables
x=5 
y="palabra" #Las variables str se pueden declarar mediante comillas simples o dobles
#Las variables en phyton no tienen que ser declaradas con ningun tipo de variable en especifico
print(x)
print(y)
#fundición de valriables
x=int(3)
y=str(3)
print(type(x))#usando el metodo type nos dice que tipo de variables son
"""
los nombres de una variable tienen ciertas reglas:
El nombre de una variable debe comenzar con una letra o el carácter de subrayado
El nombre de una variable no puede comenzar con un número
El nombre de una variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _ )
Los nombres de las variables distinguen entre mayúsculas y minúsculas (age, Age y AGE son tres variables diferentes)
Un nombre de variable no puede ser ninguna de las palabras clave de Python.
"""
#NOMBRAR VARIAS VARIAVLES AL MISMO TIEMPO
X, Y, Z=20,16,1
#Unpack a Collection
perifericos = ["mouse", "teclado", "monitor"]
x, y, z = perifericos
print(x)
print(y)
print(z)
#salida de variables
x = "salida de datos"
print(x)
#tambien se pueden mostrar varias variables al mismo tiempo
x = "salida"
y = "de datos"
print(x,y)
#El uso del operador "+" tambien funciona para mostrar multiples variales pero tambien funciona para sumar cuando son variables numericas
x = 5
y = 10
print(x + y)
#si intentas usar variables numericas y de letras no va a funcionar para mostrar debes usar la coma

#VARIABLES GLOBALES
"""
Las variables globales secrean fuera de una función (como en todos los ejemplos en las páginas anteriores) se 
conocen como variables globales.

"""
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

"""
Las variables que se llaman de la misma manera dentro de una función, esta variable será local y 
solo se puede usar dentro de la función. La variable global con el mismo nombre se mantendrá como estaba, 
global y con el valor original.
"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)