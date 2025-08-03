#######################################
# Variables y Tipos de datos
#######################################
# Convención para definir nombres
    # Variables: snake_case
    # Funciones: snake_case, camelCase
    # Clases: PascalCase

edad = 25
edad: int = 25 # 'edad: hint = 25', hint = pista o indicación, IMPORTANTE 'hint' NO limita la variable a un tipo de dato

    # id: edad
    # tipo: entero
    # valor: 25

PI = 3.14159 # Constante, IMPORTANTE usar mayusculas

print(edad)         # Mostrar/Imprimir en consola
print(id(edad))     # Dirección de memoria
print(type(edad))   # Tipo de dato (entero, cadena, flotante, booleano...)

# Inmutable: no cambia
#######################################
    # Numericos
    # Cadenas
    # Bytes
    # Tuplas
    # Frozensets

# Mutables: cambia
#######################################
    # Listas
    # Arrays de bytes
    # Sets
    # Diccionarios

#######################################
# Numericos
#######################################

# Enteros
#######################################
    # Sin decimales
    # Positivos, negativos o 0
    # No hay tamaño limite

# Booleans
#######################################
    # Subtipo del entero
    # True (1)
    # False (0)

# Reales
#######################################
    # Punto flotante
    # 64 bits (doble precision)
        # Signo (1 bit - positivo o negativo)
        # Exponente (11 bits - cuánto mover la coma/punto en base 2)
        # Mantisa/Fracción (52 bits - dígitos significativos)

# Decimales
#######################################
    # Punto flotante (mayor precision)
    # Importar: from decimal import Decimal
        # Decimal(valor punto flotante)

# Fracciones
#######################################
    # Numerador/Denominador
    # Minimo termino
    # Importar: from fractions import Fraction
        # Fraction(numerador, denominador)

# Complejos
#######################################
    # a + bj
    # Real
    # Imaginario

#######################################
# Cadenas
#######################################
# https://unicode-table.com/es/

# 'cadena'      # Permite escribir en una sola linea
# "cadena"
# '''cadena'''  # Permite escribir en varias lineas
# """cadena"""

#######################################
# Operadores y Operaciones de cadenas
#######################################
cadena = 'Hola'
cadena2 = 'mundo'

print(cadena + cadena2)
print(cadena * 3)

print(len(cadena)) # Longitud/tamaño de la cadena
print(min(cadena)) # El caracter menor segun el valor Unicode
print(max(cadena)) # El caracter mayor segun el valor Unicode

# Indices
#######################################
    # Acceder a los caracteres de la cadena
    # Solo lectura (inmutable)
    # [indice]

cadena = 'Hola mundo'
print(cadena[0])

# Subcadenas
#######################################
# n = delimitador
# : = separador
# s = saltos hasta llegar a n
    # cadena[:n] # Desde 0 hasta n
    # cadena[n:] # Desde n hasta el final
    # cadena[n:n] # Desde n hasta n
    # cadena[n:n:s] # Desde n hasta n con saltos

cadena = 'Hola mundo'
print(cadena[:4])
print(cadena[1:4])
print(cadena[0:10:2])

cadena2 = 'h' + cadena[1:]
print(cadena2)

#######################################
# Métodos de cadenas
#######################################
cadena = ' hola mundo 1 '           # Cadena alfabetica en minuscula

cadena1 = 'abF463HSFG35Wsfghs4'     # Cadena alfanumerica
cadena2 = '   sdghsdfha   '         # Los espacios son caracteres especiales '\n'
cadena3 = '_*%adghs43536--'         # El _*%- son caracteres especiales

cadena4 = 'fasDJFdivas'             # Cadena alfabetica
cadena5 = '123534645'               # Cadena numerica
cadena6 = 'FSAJN ASDJ'              # Cadena alfabetica en mayuscula
cadena7 = '   '                     # Cadena de espacios

print(cadena.capitalize())          # Primer caracter en mayuscula
print(cadena.title())               # Primer caracter de cada palabra en mayuscula
print(cadena.upper())               # Todo en mayuscula
print(cadena.lower())               # Todo en minuscula
print(cadena.replace('o', 'O', 1))  # Reemplazar replace(old, new, end)
print(cadena.strip())               # Quita los espacios al inicio y al final de la cadena

print(cadena1.isalnum())            # True si es alfanumerico sino False
print(cadena4.isalpha())            # True si es alfabetico sino False
print(cadena5.isdigit())            # True si son numeros sino False
print(cadena.islower())             # True si los caracteres alfabeticos estan en minuscula sino False
print(cadena6.isupper())            # True si los caracteres alfabeticos estan en mayuscula sino False
print(cadena7.isspace())            # True si son espacios o tabs sino False

#######################################
cadena = 'tres tristes tigres comian trigo en un trigal'
cadena1 = 'tomate,lechuga,patata'

print(cadena.count('es'))           # Cuenta el numero de veces que aparece la subcadena, count(sub, start, end)
print(cadena.encode())
print(cadena.endswith('a', 0, 44))  # True si termina con el sufijo que se indique sino False, endswith(suf, start, end)
print(cadena.find('tigres'))        # Nos muestra la primera posicion de la ocurrencia en la subcadena, find(sub, start, end)
print(cadena.index('tigres'))       # Nos muestra la primera posicion de la ocurrencia en la subcadena sino Error
print(cadena1.split(','))           # Divide la cadena con un delimitador que se indique

#######################################
# Formato de cadenas
#######################################

# 'cadena' % (args)
#######################################
    # %s                            # Aplica a una cadena

    # %d - %<n>d - %0<n>d           # Aplica a valores en base 10 (numeros enteros)
        # <n>                       # Numero de caracteres, se representa con espacios a la izquierda
        # 0                         # Completar con 0 el numero de caracteres

    # %f - %.<dec>f - %0<n>.<dec>f  # Aplica a valores en punto flotante (hasta 6 decimales)
        # <dec>                     # Numero de decimales a mostrar
        # <n>                       # Numero de caracteres, se representa con espacios a la izquierda
        # 0                         # Completar con 0 el numero de caracteres

    # %x - %X                       # Aplica a valores hexadecimales

nombre = 'Juan'
edad = 20
precio = 20.900
numero = 255

s = 'El nombre es: %s' % (nombre)
d = 'La edad es: %04d' % (edad)
f = 'El precio es: %010.2f' % (precio)
x = 'El numero es: %x %X' % (numero, numero)
print(x)

# 'cadena'.format(args)
#######################################
    # {}

    # {n} , {n:formato}

    # {k} , {k:formato}

nombre = 'Ana'
edad = 20
precio = 2.5

salida = '{} tiene {} años'.format(nombre, edad)                    # Se reemplaza en orden
salida = '{1} tiene {0} años'.format(edad, nombre)                  # Se reemplaza por orden numerico
salida = '{name} tiene {age} años'.format(name=nombre, age=edad)    # Se reemplaza por nombre
salida = f'{nombre} tiene {edad} años'                              # Otra forma, interpolación = incluir variables en la cadena
salida = 'El precio es {0:.2f} dolares'.format(precio)              # Se reemplaza por orden numerico y se pone con dos decimales en punto flotante

print(salida)

#######################################
# Bytes
#######################################
# Almacenar datos contextuales
# Enviar datos

#                     encode
#                 ------------->
# Texto unicode       utf-8       Bytes
#                 <-------------
#                     decode

saludo = 'Hola áéíóú'
print(type(saludo))
print(saludo)

saludo_cod = saludo.encode('utf-8')         # Codifica en utf-8 los caracteres especiales
print(type(saludo_cod))
print(saludo_cod)

saludo_dec = saludo_cod.decode('utf-8')     # Decodifica en utf-8 los caracteres especiales
print(type(saludo_dec))
print(saludo_dec)

#######################################
# Tuplas
#######################################
# Secuencia de objetos arbitrarios separados por comas

t = (5, 2, 9)
t = 5, 2, 9

# Declaración implicita
#######################################
# - Declarar múltiples variables en una línea
# - Funciones que devuelven múltiples objetos
# - Consola

# Operadores y operaciones
#######################################
# Operadores
    # +
    # *
    # in
    # not in

# Funciones
    # min(tupla)
    # max(tupla)
    # sum(tupla)
    # len(tupla)

# Indices
#######################################
# tupla[i]
# tupla[:end]
# tupla[start:]
# tupla[start:end]
# tupla[start:end:steps]

#######################################
# Frozensets
#######################################
# - Colecciones desordenadas de objetos inmutables
# - Objetos hashable (resumibles)

fset = frozenset([1, 3, 5, 7, 9])

# Operadores y operaciones
#######################################
# Operadores
    # | = or (unión)
    # & = and (intercesión)
    # ^ = or exclusivo (que solo esten en uno)
    # - = diferencia (solo al que este adelante del operador)
    # in
    # not in

# Funciones
    # max(frozenset)
    # min(frozenset)
    # sum(frozenset)
    # len(frozenset)

#######################################
# Listas
#######################################
# Colecciones de datos homogéneos o heterogéneos

# Vacía         Valores iniciales
# []            [d1, d2, ..., dn]
# list()        list(iterable)

# Indices
#######################################
# Lectura
    # lista[i]
    # lista[:end]
    # lista[start:]
    # lista[start:end]
    # lista[start:end:steps]

# Escritura
    # lista[i] = dato

# Operadores y operaciones
#######################################
# Operadores
    # +
    # *
    # in
    # not in

# Funciones
    # min(lista)
    # max(lista)
    # sum(lista)
    # len(lista)

# Métodos de list
#######################################
# lista.metodo()

# append(dato)              # Agregar un nuevo elemento
# count(dato)               # Contar el número de veces que esta un elemento en la lista
# extend(lista)             # Agregar una lista dentro de otra lista
# index(dato)               # Mostrar la posición del elemento de la primera ocurrencia
# insert(posición, dato)    # Agrega un nuevo elemento en una posición
# pop() / pop(posición)     # Extrae el ultimo elemento y lo elimina / Extrae el elemento de la posición y lo elimina
# remove(dato)              # Elimina el elemento de la primera ocurrencia
# reverse()                 # Cambia el orden al revés
# sort()                    # Ordena la lista de menor a mayor
# clear()                   # Elimina todos los elementos

#######################################
# Arrays de bytes
#######################################
# Secuencia mutable de enteros

# 0 <= x < 256

# bytearray()
# bytearray(N)
# bytearray(iterable int)
# bytearray(str, codificación)
# bytearray(bytes)

#######################################
# Sets
#######################################
# Colecciones desordenadas de objetos inmutables con valor hash

# Vacío         Valores iniciales
# set()         {d1, d2, ..., dn}
#               set(iterable)

# Operaciones
    # | = or(unión)
    # & = and(intercesión)
    # ^ = or exclusivo(que solo esten en uno)
    # - = diferencia(solo al que este adelante del operador)
    # in
    # not in

# Funciones
    # max(set)
    # min(set)
    # sum(set)
    # len(set)

# Métodos de sets
#######################################
# set.metodo()

# add(dato)         # Agregar un nuevo elemento
# pop()             # Extrae un elemento aleatorio y lo elimina
# remove(dato)      # Elimina el elemento sino se encuentra lanza un error
# discard(dato)     # Elimina el elemento sino se encuentra NO lanza un error
# clear()           # Elimina todos los elementos

#######################################
# Diccionarios
#######################################
# Colecciones mutables de pares clave-valor no ordenadas

# Clave: valor hash
# Valor: tipo arbitrario

# Vacío             Valores iniciales
# {}                {k1: v1, k2: v2, ..., kn: vn}
# dict()            dict({k1: v1, k2: v2, ..., kn: vn})
#                   dict(iterable)
#                   dict(zip([k1, k2, ..., kn], [v1, v2, ..., vn]))

# Claves
#######################################
# Acceder a los datos del diccionario

# Lectura
    # diccionario[k1]

# Escritura
    # diccionario[k1] = valor

# Funciones
#######################################
# diccionario.metodo()

# keys()                                        # Devuelve un objeto iterable con todas las claves
# values()                                      # Devuelve un objeto iterable con todos los valores
# items()                                       # Devuelve todos los elementos en un objeto iterable
# clear()                                       # Elimina todos los elementos
# get(key) | get(key, default)                  # Toma el valor asociado de la clave
# update(key = valor) | update({key: valor})    # Modifica el valor de la clave si no existe la clave se crea un nuevo elemento
# pop(key) | pop(key, default)                  # Extrae el valor de la clave y elimina el elemento

# del diccionario[key]                          # elimina el elemento asociado a la clave

#######################################
# Conversion de tipos explicita (casting)
#######################################
# int()         a float(), bool(), str()
# float()       a int(), bool(), str()
# complex()     a int(), float(), bool(), str()
# bool()        a int(), float(), complex(), str()
# str()         a int(), float(), complex(), bool()

a = 5
b = 5.1
c = 5+2j
d = True
e = '1'
f = '1.3'
g = 'uno'

x = int(e)
print(x)

#######################################
# Operadores y expresiones
#######################################
# - Operadores: Realizan operaciones (cálculos) dentro de una expresión
# - Operandos: Variables, constantes y/o expresiones
# - Expresión: Conjunto de operandos y operadores que devuelven un resultado
    # Ejemplo: a * ((b+c)/d)

# Tener en cuenta la precedencia de mayor prioridad a menor prioridad

# Operador de asignación
#######################################
# variable = valor o expresión
a = 5
b = (7 + 4) * 3

# Asignación aumentada
a += b # Es igual a (a = a + b)
a *= b # Es igual a (a = a * b)
a += 1

# Operadores aritmeticos
#######################################
# Suma                            | +     | a + b
# Resta                           | -     | a - b
# Multiplicación                  | *     | a * b
# División                        | /     | a / b
# División entera                 | //    | a // b
# Módulo (resto division entera)  | %     | a % b
# Potencia                        | **    | a ** b
# -------------------------------------------------
# Cambio de signo + (implicito)   | +     | +a
# Cambio de signo -               | -     | -a

# Operadores de comparación
#######################################
# Igualdad                    | ==        | a == b
# Desigualdad                 | !=        | a != b
# Mayor exclusivo             | >         | a > b
# Menor exclusivo             | <         | a < b
# Igualdad de identidad       | is        | a is b
# Desigualdad de identidad    | is not    | a is not b
# Pertenencia                 | in        | a in b
# No pertenencia              | not in    | a not in b

# Operadores lógicos
#######################################
# Y       | a and b     # Conjunción (a = True and b = True) = True
# O       | a or b      # Disyunción (a = False or b = True) = True
# NO      | not a       # Devuelve el valor contrario (a = True) not a = False

# Precedencia
#######################################
# Mayor prioridad

# () [] {}
# await
# **
# +(unario) -(unario) ~
# * @ / // %
# + -
# <<>>
# &
# ^
# |
# in, not in, is, is not, < <= > >= != ==
# not
# and
# or
# lambda

# Menor prioridad
