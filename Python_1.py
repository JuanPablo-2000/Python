#Numeros Random
import random

print(random.randrange(1, 10))
print('\n')

#ciclos
for x in "banana":
    print(x)

a = "Hello, World!"
print('\n')
print(len(a))

#Busca la palabra en el txt
txt = "The best things in life are free!"
print("free" in txt)

#Condicional if
if "free" in txt:
    print("Yes, 'free' is present.")


txt = "Hello, World!"
print(txt[2:5])
print(txt[:5])
print(txt[2:])
print(txt[-5:-2])

#Upper Case
print(txt.upper())

#Lowe Case 
print(txt.lower())

#Remove WhiteSpace
#remueve los espacios al principio y al final del texto
print(txt.strip())

#Replace String
print(txt.replace("H", "J"))

#Split String
"""
Separa los Strings 
segun el dato por 
el que quiera que 
se separe
"""
print(txt.split(","))

edad = 20
txt = "Mí nombre es Juan Pablo, y tengo {}"
print(txt.format(edad))

#Caracteres de Escape
txt = "Nosotros somos los llamados \"Vikings\" del norte"
print(txt)

"""
\\ Barra invertida
\n Nueva Linea
\r Acarrea la oración
\t Tabulación
\b Quita el espacio entre texto
\f Alinea un formulario
"""

"""
capitalize() convierte el primer caracter en mayuscula
casefold() convierte la cadena en minuscula completamente
center() retorna el centro de toda la cadena
count("frase") retorna el número el número de veces un valor especificado en una cadena
endcode() retorna el final de la cadena codificada
endswith("") retorna verdadero si termina con el símbolo especificado
expandtabs(2)  Da saltos horizontales en la cadena
find("frase") busca en el string la frase especificada y retorna la posición donde esta 
format(frase) da formato a un string
format_map()

index() busca una cadena un valor especificada y retorna la posición donde se encontró
isalnum() retorna verdadero si todos los caracteres del string son alphanumericos
isalpha() retorna verdadero si todos los caracteres del string son digítos  
isdecimal() retorna verdadero si los caracteres del string son decimales
isdigit() retorna verdadero si todos los caracteres del string son números
isidentifier() retorna verdadero si todos los caracteres del string ha excepción del primero sean diferente a una letra 
islower() retorna verdadero si todos los caracteres estan en minuscula
isnumeric() retorna verdadero si todos los caracteres son númericos
isprintable() retorna verdadero si no esta en saltado en una nueva linea
isspace() retorna verdadero si la cadena tiene espaciados
istitle() retorna verdadero si la cadena tiene las teglas para ser un titulo
isupper() retorna verdadero si la cadena esta completamente en mayuscula
join() une los elementos de una iteración al final de la cadena 
ljust() retorna la cadena justificada al lado izquierdo
lower() convierte la cadena completamente en minuscula
lstrip() retorna una versión recortada a la izquierda de la cadena
maketrans("letra-vieja", "letra-nueva") retorna la cadena con la letra reemplazada 
partition() retorna una tupla donde el string esta partido en dos partes
replace() retorna una cadena donde toma un valor especificado y otro por el cual será reemplazado 
rfind() encuentra las cadenas para especificar un valor y retornarlo en la ultima posición
rindex() busca la cadena para especificar el valor y retornar la ultima posición donde fue encontrada
rjust() retorna la cadena justificado hacia la derecha
rpartition() retorna una tupla donde la cadena donde la cadena es partida dentro de 3 partes
rsplit() separa las cadenas especificando el separador y retorna una lista
rstrip() devuelve una version recortada a la derecha por la cadena
split() separa la cadena especificando el separador  y retorna una lista
splitlines() separa la cadena con lineas y retornandola en una lista 
startswith() retorna verdadero si la cadena inicia con el valor especificado
strip() retorna una version recortada del string 
swapcase() intercambia casos, los casos mínusculos los convierte a mayuscula y vice versa
title() comvierte el primer caracter de cada palabra a mayuscula
translate() retorna una cadena transladada
upper() convierte la cadena en mayuscula
zfill() rellena la cadena con un número especificado de valores 0 al principio

"""

""" Listas en Python """
""" Las listas aceptan valores repetidos """

"""
    append() Agrega elementos al final de la lista
    clear() Remueve todos los elementos de la lista
    copy() Retorna una copia de la lista
    count() Retorna el número de elementos con el valor especificado
    extends() Agrega los elementos de una lista, a el final de la lista pasada como parametro
    index() Retorna el index de el primer elemento con el valor especificado
    insert() Agrega los elementos a una posición especificada 
    pop() Remueve los elementos de una posición especificada 
    remove() Remueve los items con el valor especificado
    reverse() Invierte el orden de la lista
    sort() Clasifica la lista
"""

lista = ["manzana", "banana", "fresa", "naranja", "kiwi", "melon"]
print(len(lista))

"""Tambien aceptan todo tipo de valores en una misma lista """

lista1 = ["abc", 34, True, 40, "male"]
print(lista1)

print(type(lista))
print(lista[1])
print(lista[2:5])
print(lista[:4])
print(lista[2:])

lista[1:2] = ["blackcurrant", "watermelon"]
print(lista)

lista.insert(2, "piña")
print(lista)

lista.append("Lulo")
print(lista)

lista.extend(lista)
print(lista)

t = ("maracuya", "mango")
lista.extend(t)
print(lista)

lista.remove("naranja")
print(lista)

lista.pop()
print(lista)

del lista[0]
print(lista)

lista.clear()
print(lista)

for x in lista:
    print(x)

for i in range(len(lista)):
    print(lista[i])

[print(x) for x in lista]

frutas = ["apple", "banana", "cherry", "kiwi", "mango"]
#nuevaLista = [x for x in frutas if "a" in x]
#nuevaLista2 = [x for x in frutas if x != "apple"]

thislist = ["Banana", "Orange", "Kiwi", "Cherry"]
thislist.reverse()
print(thislist)

frutas.sort()
print(frutas)

frutas.sort(reverse = True)
print(frutas)

frutas.copy()
print(frutas)

lista01 = ["a", "b", "c"]
lista02 = [1, 2, 3]

lista01.extend(lista02)
print(lista01)



""" Tuplas en Python """


thisTuple = ("Manzana", "Banana", "Fresa", "Mango")
print(thisTuple)

tupla1 = ("Manzana", "Banana", "Fresa")
tupla2 = (1, 3 , 4, 5, 6, 8)
tupla3 = (True, False, False)

tupla = ("abc", 34, True, 40, "male")
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
print(fruits)

for i in range(len(fruits)):
    print(fruits[i])

for x in fruits:
    print(x)

print(fruits * 2)


""" Set en Python """

myset = {"Manzana", "Banana", "Fresa"}
print(myset)

print(len(myset))

set1 = {"Apple", "Banana", "Cherry"}
set2 = {1, 3, 4, 6, 8}
set3 = {True, False, False}

setexample = {"abc", 34, True, 40, "male"}

for x in setexample:
    print(x)

print("Banana" in myset)
myset.add("Orange")
print(myset)

thisset = {"Manzana", "Banana", "Fresa"}
tropical = {"Piña", "Mango", "Papaya"}

thisset.remove("Fresa")
print(thisset)

thisset.discard("Banana")
print(thisset)

thisset.update(tropical)
print(thisset)

thisset.clear()
print(thisset)

set4 = set1.union(set2)
print(set4)

x = {"Apple", "Banana", "Fresa"}
y = {"Google", "Microsoft","Apple"}

x.symmetric_difference_update(y)
print(x)

x.intersection_update(y)
print(x)

z = x.intersection(y)
print(z)


""" Dictionario en Python """

thisdict = {
    "Marca": "Ford",
    "Modelo": "Mustang",
    "Year": 1964
}

