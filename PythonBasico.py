#Esto es un comentario
print("Hello, World!\n")

"""
Esto es un comentario
escrito en más de una
sola linea
"""

v = 5
w = "John"
print(v)
print(w)

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

a = 5
b = "John"
print(type(a))
print(type(b))

#Declaración de variables permitida
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

"""
Declaración de variables no permitida
2myvar = "John"
my-var = "John"
my var = "John"
"""

#Camel Case 
myVariableName = "John"

#Pascal Case 
MyVariableName = "John"

#Snake Case
my_variable_name = "John"

#Variables Multiples
naranja, banana, fresa = "Orange", "Banana", "Cherry"
print('\n' +naranja)
print(banana)
print(fresa +'\n')

#Coleción de datos
frutas = ["apple", "banana", "cherry"]
manzana, banano, cherry = frutas
print(manzana)
print(banano)
print(cherry)

#Variables Globales
x = "awesome"

def miFuncion():
    global x
    x = "fantastico"

miFuncion()

print("\nPython is "+ x)

"""
Tipo Texto: (str)
Tipo Numerico: (int, float, complex)
Tipo Secuencia: (list, tuple, range)
Tipo Mapeo: (dict)
Tipo Set: (set, frozenset)
Tipo Boolean: (bool)
Tipo Binario: (bytes, bytearray, memoryview)
"""

#String
variable = "Hello World"
print('\n' + variable)

#Entero
variable = 20
print(variable)

#flotante
variable = 20.5
print(variable)

#Números Complejos
variable = 1j
print(variable)

#Lista
variable = ["manzana", "banana", "fresa"]
print(variable)

#Tupla
variable = ("manzana", "banana", "fresa")
print(variable)

#Range
variable = range(6)
print(variable)

#Diccionario
variable = {"nombre" : "John", "edad" : 36}
print(variable)

#Conjunto de datos Set
variable = {"manzana", "banana", "fresa"}
print(variable)

#Son valores inmutables en un conjunto Set
variable = frozenset({"manzana", "banana", "fresa"})
print(variable)

#Booleano
variable = True
print(variable)

#Bytes
variable = b"Hello"
print(variable)

#BytesArray
variable = bytearray(5)
print(variable)

#Memoryview
variable = memoryview(bytes(5))
print(variable)

