#Quotes Inside Quotes
#Puede usar comillas dentro de una cadena, siempre y cuando no coincidan con las comillas que rodean la cadena:
print("He is called 'Johnny'")
print('He is called "Johnny"')
#string multilinea
a = """se puede usar varias lineas
de texto siempre y cuando
se usen 3 comillas al inicio y al final"""
print(a)
"""
Las cadenas son matrices
Al igual que muchos otros lenguajes de programación populares, las cadenas en Python son matrices de bytes que representan caracteres Unicode.

Sin embargo, Python no tiene un tipo de datos de carácter, un solo carácter es simplemente una cadena con una longitud de 1.

Los corchetes se pueden utilizar para acceder a los elementos de la cadena.
"""
a = "HOLA MUNDO!"
print(a[0])

#Bucle a través de un str Dado que las cadenas son matrices, podemos recorrer los caracteres de una cadena, con un bucle.for

for x in "hello":
  print(x)