#######################################
# Funciones o Métodos
#######################################
# Entrada ----> Instrucciones ----> Salida

#######################################
# Declaración
#######################################
# def nombreFuncion ([args]):
#     instrucciones
#     [return v1, v2, ..., vn]

def imprimirLista(l):
    print('Lista: ')
    for n in l:
        print(n)

#######################################

def sumarPares(l):
    suma = 0
    for n in l:
        if n % 2 == 0:
            suma += n
    return suma

def incrementarN(l, n):
    print('Sumando', n, 'a cada elemento de la lista...')
    for i in range(len(l)):
        l[i] += n

lista = [3, 5, 9, 2, 6, 8, 3, 1]
imprimirLista(lista)
print('Suma de los pares: ', sumarPares(lista))

incrementarN(lista, 3)
imprimirLista(lista)
print('Suma de los pares: ', sumarPares(lista))

incrementarN(lista, 2)
imprimirLista(lista)
print('Suma de los pares: ', sumarPares(lista))

# Ventajas
#######################################
# - Reducir código duplicado
# - Dividir tareas complejas
# - Ocultar detalles de implementación
# - Mejorar la legibilidad
# - Mejorar la trazabilidad

#######################################
# Parámetros
#######################################
# - El parámetro es una referencia al objeto pasado como argumento (No una copia)
# - Reasignar el parámetro dentro de la función no modifica la variable original
# - Si el objeto es mutable, su contenido puede modificarse dentro de la función y el cambio se refleja fuera

def fun1(a):
    print('a:', id(a))  # Es el mismo ID de la variable 'x'
    a = 20
    print('a:', id(a))  # Cambia el ID

x = 10
print('x:', id(x))      # Es el mismo ID de la variable 'a' al inicio de la función

fun1(x)
print('x:', id(x))      # Es el mismo ID de la variable 'x'

def fun2(l):            # Se modifica la posición 0 = 20 y sigue sientdo el mismo ID
    print('l:', id(l))
    l[0] = 20
    print('l:', id(l))

lista = [4, 2, 7, 8, 3]
print('lista:', id(lista))
print(lista[0])

fun2(lista)
print('lista:', id(lista))
print(lista[0])         # Se modifico la posición 0 = 20 desde la función

# Argumentos posicionales
#######################################
# def fun1(a, b, c):
#     Operaciones

# fun1(val1, val2, val3) # val1 = a, val2 = b, val3 = c

#######################################

def sumar(n1, n2, n3 = 0): # El valor 'n3' tiene como default (predefinido) 0 sino recibe ese argumento
    print('n1:', n1, 'n2:', n2, 'n3:', n3)
    return n1 + n2 + n3

resultado = sumar(5, 6, 9)
print(resultado)

# Argumentos keywords
#######################################
# def fun1(a, b, c):
#     Operaciones

# fun1(c = val1, a = val2, b = val3)

#######################################

def fun2(a, b, c = 0): # El valor 'c' tiene como default (predefinido) 0 sino recibe ese argumento
    print('a:', a, 'b:', b, 'c:', c)

fun2(c = 9, a = 4, b = 2)

# Argumentos posicionales variables
#######################################
# def fun1(*args):
#     Operaciones

# fun1(val1, val2, val3)
# fun1(*(val1, val2, val3)) # Se pasan los valores de la tupla, NO la tupla

#######################################

def sumar(*args):
    print(type(args))
    suma = 0
    for n in args:
        suma += n
    return suma

resultado = sumar(5, 7, 8, 1, 6, 4)
print(resultado)

# Argumentos keywords variables
#######################################
# def fun1(**kwargs):
#     Operaciones

# fun1(a = val1, b = val2, c = val3)
# fun1(**{'a': val1, 'b': val2, 'c':val3})      # Se pasan los valores en un diccionario con {}
# fun1(**dict(a = val1, b = val2, c = val3))    # Se pasan los valores en un diccionario con la función dict()

#######################################

def fun2(**kwargs):
    print(type(kwargs))

    print(kwargs['a'])
    print(kwargs['b'])

    k = kwargs.keys()
    params = list(k)
    print(params)
    for p in params:
        print(p, ': ', kwargs[p])

    # for key, value in kwargs.items(): # Otra forma
    #     print(f'{key}: {value}')

fun2(a = 2, b = 5, c = 6, d = 9)
fun2(**{'a': 2, 'b': 5, 'c': 6, 'd': 9})

# Argumentos combinados
#######################################
# - Declaración: posicionales, predeterminados, posicionales variables, keywords, keywords variables
# - Llamada: posicionales, keywords y predeterminados, posicionales variables, keywords variables

def fun1(a, b, c = 0, *args, d, **kwargs):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('args:', args)
    print('d:', d)
    print('kwargs:', kwargs)

fun1(5, 7, 0, d = 3, *(4, 8, 5), **{'f': 4, 'g': 1})

#######################################
# Retorno
#######################################
# def fun1(args):
#     Instrucciones
#     return val1[val2, ..., valn]
#     Instrucciones2 # Después de un return no se ejecutan mas instrucciones lo caul quedan inaccesibles

#######################################

def calcularMax(l):
    m = max(l)

    # if l.count(l) > 1:        # Opción 1, varios returns
    #     return 1
    # else:
    #     return 0

    return m, l.count(m)        # Opción 2, un solo return

lista = [5, 4, 7, 8, 2, 3]
resultado = calcularMax(lista)  # Opción 1 o Opción 2, guarda el return en la variable
print(type(resultado))
print(resultado)

maximo, n = calcularMax(lista)  # Opción 2, guarda cada return en una variable
print(type(maximo))
print(type(n))
print(maximo)
print(n)

#######################################
# Ámbito
#######################################
# Región textual de un programa donde se puede acceder a un espacio de nombres de forma directa

# LEGB
# (local, enclosing, global, built-in)

x = 6
print('Global:', id(x), '', x)

def fun1():                             # Enclosing de 'inner()'
    x = 2                               # Si se comenta esta linea la funcion buscara la variable 'x' en el siguiente ámbito, LEGB
    print('Local f:', id(x), '', x)     # 'x' es local para fun1 pero enclosing para inner

    def inner():
        print('Local i:', id(x), '', x)

    inner()

fun1()                                  # Se accede a la variable 'x' en LECTURA
print('Global:', id(x), '', x)

# Nonlocal
#######################################
# Hace referencia a variables del ámbito superior más próximo no global

# def fun1():
#     test = 1              # Variable local de fun1
#     def inner():
#         test = 2          # Variable local de inner


# def fun1():
#     test = 1
#     def inner():
#         nonlocal test     # Indica que la variable no es local sino enclosing, permite ESCRITURA
#         test = 2

x = 6

def fun1(): # Enclosing de inner()
    x = 2
    print('Local f:', id(x), '', x)

    def inner():
        nonlocal x
        x = 8
        print('Local i:', id(x), '', x)

    inner()
    print('Local f:', id(x), '', x)

fun1()

# Global
#######################################
# Hace referencia a variables del ámbito global

# def fun1():
#     test = 2      # Variable local de fun1

# test = 1

# def fun1():
#     global test   # Indica que la variable no es local sino global, permite ESCRITURA
#     test = 2

x = 6
print('Global:', id(x), '', x)

def fun1():
    global x
    x = 2
    print('Local:', id(x), '', x)

fun1()
print('Global:', id(x), '', x)

#######################################
# Recursividad
#######################################
# def fun1(parámetros):
#     Instrucciones
#     return fun1(parámetros)
#     Instrucciones
#     return expresión

#######################################

def calcularFactorialRecursividad(n):
    if n == 0:
        return 1
    else:
        return n * calcularFactorialRecursividad(n - 1)

resultado = calcularFactorialRecursividad(5)
print(resultado)


def calcularFactorialCiclo(n):
    f = 1
    if n > 0:
        for x in range(1, n + 1):
            f *= x
    return f

resultado = calcularFactorialCiclo(4)
print(resultado)

#######################################
# Expresiones lambda
#######################################
# def fun1([parámetros]):
#     return expresión

# fun1 = lambda [parámetros] : expresión

#######################################

def calcularDobleFuncion(n):
    return n * 2

resultado = calcularDobleFuncion(6)
print(resultado)


dobleLambda = lambda n : n * 2  # Declaración

resultado =  dobleLambda(6)     # Llamada
print(resultado)

#######################################
# Built-in
#######################################
# Consultar las funciones del intérprete de Python

print(dir(__builtins__)) # Lista todas las funciones

# Documentación: https://docs.python.org/3.3/library/functions.html#built-in-functions
