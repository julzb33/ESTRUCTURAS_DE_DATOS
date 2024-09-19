"""
Las variables pueden almacenar datos de diferentes tipos, y diferentes tipos pueden hacer cosas diferentes.

Python tiene los siguientes tipos de datos incorporados de forma predeterminada, en estas categorías:

Tipo de texto:	str 
Tipos numéricos:	int, float, complex
Tipos de secuencia:	list, tuple, range
Tipo de mapeo:	dict

de este tipo son una estructura de datos que permite almacenar un conjunto de datos como pares clave-valor,
donde cada valor es accesible a través de una clave única. En otras palabras,
los diccionarios permiten asociar valores con claves.


Tipos de conjuntos:	set, frozenset
Tipo booleano:	bool
Tipos binarios:	bytes, bytearray, memoryview
Ninguno Tipo:	NoneType
"""
x="PALABRA" #str
print(x)
x=30 #int
print(x)
x=3.5#float
print(x)
x=2j #complex
print(x)
colores=["rojo","azul","amarillo"] #list
print(colores)
colores=("rojo","azul","amarillo") #tuple
print(colores)
x=range(1,6);#range
print(x)
x={"name" : "John", "age" : 36} #dict
print(x)
x={"amarillo","azul","rojo"}#set
print(x)
x=frozenset({"amarillo","azul","rojo"})#frozenset este es inmutable
print(x)
x=False
print(x)
x = b"Hello" #bytes	son inmutables
print(x)
x = bytearray(5) #bytearray	son mutables es decir una vez creados se pueden modificar. Los datos tipo bytearray se utilizan para representar secuencias de bytes modificables
print(x)
x = memoryview(bytes(5)) #	memoryview	
print(x)
x = None #NoneType
print(x)
