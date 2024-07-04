print("hello, world!")

print("ex 1:")

x=5
y=46
print(x+y)


print("ex 2:")

x, y, z = "Orange", "Banana", "Cherry"
print(y)


print("ex 3:")

x = y = z = "Orange"
print(x, y, z)


print("ex 4:")

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("ex 5:")

x = "love "
y = "apple "
print(x + y) # operador + coloca espaços entre as strings

print("ex 6:")
x = 5
y = "John"
print(x, y) #se usar o operador + dara erro


print("ex 7:")

x = "awesome" #variável global: podem ser usadas por qualquer pessoa, tanto dentro quanto fora das funções.

def myfunc(): # declaração de função
  print("Python is " + x)

myfunc()


print("ex 8:")

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


"""
Tipo de texto:	str
Tipos numéricos:	int, float, complex
Tipos de sequência:	list, tuple, range
Tipo de mapeamento:	dict
Tipos de conjuntos:	set,frozenset
Tipo Booleano:	bool
Tipos binários:	bytes, bytearray, memoryview
Nenhum Tipo:	NoneType
"""

#tipos de dados python

x = 5
print(type(x)) # função para saber o tipo da variavél

"""
x = str("Hello World")	
x = int(20)	           
x = float(20.5)	
x = complex(1j)	
x = list(("apple", "banana", "cherry"))		
x = tuple(("apple", "banana", "cherry"))		
x = range(6)		
x = dict(name="John", age=36)		
x = set(("apple", "banana", "cherry"))		
x = frozenset(("apple", "banana", "cherry"))		
x = bool(5)		
x = bytes(5)		
x = bytearray(5)		
x = memoryview(bytes(5))	

"""
#Float também pode ser um número científico com um "e" para indicar a potência de 10.
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

#Números complexos são escritos com um "j" como parte imaginária:
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

#Converter de um tipo para outro:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Importe o módulo aleatório e exiba um número aleatório entre 1 e 9:

import random

print(random.randrange(1, 10))

#Você pode atribuir uma string multilinha a uma variável usando três aspas:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)