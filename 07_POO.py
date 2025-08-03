#######################################
# POO
#######################################
# Paradigma de programación:
# - Objetos
# - Clases

# Objeto
#######################################
# - Estado (atributos)
# - Comportamiento (métodos)
# - Identidad

# Clases
#######################################
# Tipo de dato:
# - Atributos (estado)
# - Métodos (comportamiento)

#######################################
# Clases y objetos
#######################################
class MiClase:
    pass

x = MiClase() # objeto 'x' de MiClase
y = MiClase() # objeto 'y' de MiClase

print(type(x), id(x))
print(type(y), id(y))

# Atributos
#######################################
class Coordenada:
    x = 0 # Atributo
    y = 0 # Atributo

c = Coordenada()
c.x = 5
c.y = 2
print(Coordenada.x, ' ', Coordenada.y)  # Nos permite acceder a la clase en lectura y escritura
print(c.x, ' ', c.y)                    # Nos permite acceder al objeto 'c' en lectura y escritura

# Métodos
#######################################
# Comportamientos

# Métodos de instancia
#######################################
# class Coordenada:
#     def init(self[, params]): # 'self' hace referencia al objeto y es obligatorio, 'self' es el propio objeto que hace la llamada 'c'
#         self.x = 0
#         self.y = 0

# c = Coordenada()              # Se instancia un objeto 'c'
# c.init([params])              # Se llama al método init
# Coordenada.init(c, [params])  # Otra opción es utilizar la propia clase y se indica el objeto instanciado 'c'

#######################################

class Coordenada:
    def init(self, x, y):
        self.x = x
        self.y = y

c = Coordenada()
c.init(5, 2)

print(c.x, ' ', c.y)

i = Coordenada()
Coordenada.init(i, 8, 5)

print(i.x, ' ', i.y)

# Métodos de clases
#######################################
# class Coordenada:
#     x = 0 # Atributo
#     y = 0 # Atributo

#     @classmethod              # Decorador de método de clase
#     def init(cls[, params]):  # 'cls' hace referencia a la clase y es obligatorio
#         cls.x = 5             # 'cls' para acceder a los atributos de la clase
#         cls.y = 2             # 'cls' para acceder a los atributos de la clase

# Coordenada.init([params])

#######################################

class Coordenada:
    x = 0
    y = 0

    @classmethod
    def init(cls, a, b):
        cls.x = a
        cls.y = b

Coordenada.init(3, 9)
print(Coordenada.x, ' ', Coordenada.y)

c = Coordenada()
c.init(2, 8)
print(c.x, ' ', c.y)
print(Coordenada.x, ' ', Coordenada.y)

# Métodos estáticos
#######################################
# class Coordenada:
#     @staticmethod # Decorador de método estático
#     def fun1([params]):
#         Instrucciones

# Coordenada.fun1([params])

#######################################

class InputUtils:
    @staticmethod # No accede al objeto ni a la clase
    def leerEnteroPositivo(msg):
        n = 0
        entrada = input(msg)

        if entrada.isdigit() and int(entrada) > 0:
            n = int(entrada)

        return n

edad = InputUtils.leerEnteroPositivo('Ingrese la edad: ')
print(edad)

#######################################
# Métodos especiales
#######################################
# __nombreMetodo__

# Constructor
#######################################
class Coordenada:
    x = 0
    y = 0

    def __new__(cls, a=0, b=0): # Constructor '__new__'
        cls.x = a
        cls.y = b

Coordenada(5, 2)
print(Coordenada.x, Coordenada.y)

# Inicializador
#######################################
class Coordenada:
    x = 0
    y = 0

    def __init__(self, a=0, b=0): # Inicializador '__init__'
        self.x = a
        self.y = b

c = Coordenada(5, 2)
print(Coordenada.x, Coordenada.y)
print(c.x, c.y)

# Destructor
#######################################
class Coordenada:
    x = 0
    y = 0

    def __init__(self, a=0, b=0):
        print('__init__')
        self.x = a
        self.y = b

    def __del__(self): # Después de no usar el objeto 'c' se libera la memoria
        print('__del__', self.x, self.y)

c = Coordenada(5, 2)
print('print', c.x, c.y)

# Nombre
#######################################
print(__name__) # Nombre del script donde se ejecuta el código

if __name__ == '__main__':
    print('Script Main')

# Formato de salida
#######################################
class Coordenada:
    x = 0
    y = 0

    def __init__(self, a=0, b=0):
        print('__init__')
        self.x = a
        self.y = b

    def __str__(self): # Modifica el método de formato de salida 'c'
        # return 'x: %d y: %d' % (self.x, self.y)
        return 'x: {} y: {}'.format(self.x, self.y)

c = Coordenada(5, 2)
print(c)
print(c.x, c.y)

# Sobrecarga de operadores
#######################################
# Mas métodos de sobrecarga de operadores en la carpeta img

class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # Suma
        return f'obj 1: {self.x} + obj 2: {other.x} = {self.x + other.x}'

    def __sub__(self, other): # Resta
        return f'obj 1: {self.y} - obj 2: {other.y} = {self.y - other.y}'

c1 = Coordenada(6, 7)
c2 = Coordenada(4, 5)

print(c1 + c2)
print(c1 - c2)

#######################################
# Encapsulación
#######################################
# - Ocultación del estado
# - Acceso mediante interfaz pública (métodos)
# - Evitar errores y comportamientos no deseados
# - Definir nivel de abstracción

# Name mangling
#######################################
# class Coordenada:
#     def __init__(self):
#         self.__x = 5      # Atributo privado
#         self._y = 9       # Atributo privado

# c = Coordenada()
# print(c.__x)              # ERROR por los '__'
# print(c._y)               # Permite acceder a '_y', pero es una MALA PRACTICA
# print(c._Coordenada__x)   # Permite acceder a '__x', pero es una MALA PRACTICA

# Decorador @property y @setter
#######################################
class Coordenada:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    @property # Decorador de propiedad 'x' (get/lectura)
    def x(self):
        return self.__x

    @x.setter # Decorador de propiedad setter 'x' (setter/escritura)
    def x(self, a):
        if a < 0:
            self.__x = 0
        else:
            self.__x = a

    @property # Decorador de propiedad 'y' (get/lectura)
    def y(self):
        return self.__y

    @y.setter # Decorador de propiedad setter 'y' (setter/escritura)
    def y(self, a):
        if a < 0:
            self.__y = 0
        else:
            self.__y = a

c = Coordenada()
c.x = -8
c.y = 5
print(c.x)
print(c.y)

#######################################
# Herencia
#######################################
# Persona
#     - DNI
#     - Nombre
#     - Apellidos
#     - Teléfono

# Alumno
#     - Matrícula
#     - Nota

# Profesor
#     - Despacho
#     - Asignaturas

# Sintaxis
#######################################
# class Persona:
#     def __init__(self):
#         self.dni = ''
#         self.nombre = ''
#         self.telf = ''
#         ...


# class Alumno(Persona):
#     def __init__(self):
#         self.matricula = ''
#         self.nota = 0
#         ...

#######################################

class Persona: # Métodos de clase
    dni = '12345678A'
    nombre = 'Ana'
    telf = '612345678'

    @classmethod
    def imprimirPersona(cls):
        print('DNI:', cls.dni, '\nNombre:', cls.nombre, '\nTelf:', cls.telf)


class Alumno(Persona):
    matricula = 'XY7345A'
    nota = 8.0

    @classmethod
    def imprimirAlumno(cls):
        print('Matrícula:', cls.matricula, '\nNota:', cls.nota)

print(Alumno.matricula)
print(Alumno.dni)

alumno = Alumno() # Objeto 'alumno' de la clase 'Alumno'
print(alumno.matricula)
print(alumno.dni)
alumno.imprimirPersona()
alumno.imprimirAlumno()


class Persona: # Métodos de instancia
    def __init__(self):
        self.dni = '12345678A'
        self.nombre = 'Ana'
        self.telf = '612345678'

    def imprimirPersona(self):
        print('Hola soy una persona')
        print('DNI:', self.dni, '\nNombre:', self.nombre, '\nTelf:', self.telf) # ERROR, no se ejecuta el método '__init__' desde la clase 'Alumno' sin el método 'super()'


class Alumno(Persona):
    def __init__(self):
        self.matricula = 'XY7345A'
        self.nota = 8.0

    def imprimirAlumno(self):
        print('Matrícula:', self.matricula, '\nNota:', self.nota)

alumno = Alumno()
print(alumno.nota)
# print(alumno.dni) # ERROR, no se ejecuta el método '__init__' de la clase 'Persona' sin el método 'super()'
alumno.imprimirPersona()
alumno.imprimirAlumno()

# Método super()
#######################################
# class Persona:
#     def __init__(self, dni, nombre, telf):
#         self.dni = dni
#         self.nombre = nombre
#         self.telf = telf
#         ...


# class Alumno(Persona):
#     def __init__(self, dni, nombre, telf, matricula, nota):
#         super().__init__(dni, nombre, telf)
#         self.matricula = matricula
#         self.nota = nota
#         ...

#######################################

class Persona:
    def __init__(self):
        self.dni = '12345678A'
        self.nombre = 'Ana'
        self.telf = '612345678'

    def __str__(self):
        return 'DNI: %s\nNombre: %s\nTelf: %s\n' % (self.dni, self.nombre, self.telf)

    def imprimirPersona(self):
        print('DNI:', self.dni, '\nNombre:', self.nombre, '\nTelf:', self.telf)


class Alumno(Persona):
    def __init__(self):
        super().__init__()
        self.matricula = 'XY7345A'
        self.nota = 8.0

    def __str__(self):
        return '%sMatrícula: %s\nNota: %.1f' % (super().__str__(), self.matricula, self.nota)

    def imprimirAlumno(self):
        super().imprimirPersona()
        print('Matrícula:', self.matricula, '\nNota:', self.nota)

alumno = Alumno()
print(alumno.dni)
alumno.imprimirAlumno()
print(alumno)

#######################################
# Herencia múltiple
#######################################
# A, B } C # 'C' hereda de 'A' y de 'B'

# Sintaxis
#######################################
# class A:
#     def __init__(self):
#         ...


# class B:
#     def __init__(self):
#         ...


# class C(A, B):
#     def __init__(self):
#         ...

#######################################

class A:
    a = 2
    def saludarA(self):
        print('Soy A')


class B:
    b = 5
    def saludarB(self):
        print('Soy B')


class C(A, B):
    c = 8
    def saludarC(self):
        print('Soy C')

x = C()
print(x.a, x.b, x.c)
x.saludarA()
x.saludarB()
x.saludarC()

# MRO - Method Resolution Order
#######################################
# El orden en el que se buscan los métodos en las clases base

# class X:
#     x = 0


# class A(X):
#     pass


# class B(X):
#     pass


# class C(B, A):
#     pass

# c = C() # ¿ c.x ?
# print(c.__class__.__mro__)
# print(C.mro())
# print(c.x)

# Argumentos
#######################################
# class A:
#     def __init__(self, x):
#         self.x = x


# class B:
#     def __init__(self, y):
#         self.y = y


# class C(A, B):
#     def __init__(self, x, y):
#         super().__init__(?)

#######################################

class Base:
    def __init__(self, x):
        self.x = x


class A(Base):
    def __init__(self, a, **kwargs):
        super().__init__(**kwargs)
        self.a = a


class B(Base):
    def __init__(self, b, **kwargs):
        super().__init__(**kwargs)
        self.b = b


class C(A, B):
    def __init__(self, c, **kwargs):
        super().__init__(**kwargs)
        self.c = c

base = Base(5)
c = C(c=4, a=3, b=2, x=6)
print(c.c, c.a, c.b, c.x)

#######################################
# Polimorfismo
#######################################
# class Base:
#     ...
#     def fun1(self):
#         Instrucciones


# class Derivada(Base):
#     ...
#     def fun1(self):
#         Instrucciones

#######################################

class Base:
    def __init__(self, saludo):
        self.saludo = saludo

    def saludar(self):
        return self.__str__()

    def saludar_2(self):
        return 'Hola Base'

    def __str__(self):
        return f'Saludo: {self.saludo}'


class Derivada(Base):
    def __init__(self, saludo, nombre):
        super().__init__(saludo)
        self.nombre = nombre

    def saludar_2(self, a):
        return f'Hola Derivada {a}'

    def __str__(self):
        return f'{super().__str__()}, {self.nombre}'

b = Base('Hola 1')
print(b)
print(b.saludar_2())

d = Derivada('Hola 2', 'Alex')
if isinstance(d, Derivada):     # Si el objeto 'd' es una instancia de la clase 'Derivada'
    print(d)
    print(d.saludar())          # El método 'saludar()' se hereda de la clase 'Base'
    # print(d.saludar_2())      # ERROR, en Python no existe la sobrecarga de métodos, se debe pasar un argumento

#######################################
# Clases abstractas
#######################################
# - Interfaz sin implementación
# - Módulo ABC (Abstract Base Class)

# import abc

# class MiABC(metaclass = abc.ABCMeta):
#     ...

# Métodos
#######################################
import abc

class Forma(metaclass=abc.ABCMeta):

    @abc.abstractmethod # Decorador de método abstracto
    def calcularArea(self):
        pass


class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado

# f = Forma() # ERROR, no se puede instanciar un objeto 'f' de clases abstractas

c = Cuadrado(4) # IMPORTANTE, no se puede instanciar un objeto 'c' de una clase que hereda de una clase abstracta HASTA que se implementen sus métodos abstractos
print('Área:', c.calcularArea())

# Propiedades
#######################################
# import abc

# class Forma(metaclass=abc.ABCMeta):

#     @property # Decorador de propiedad abstracta
#     @abc.abstractmethod
#     def nombre(self):
#         pass

#######################################

import abc

class Forma(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def calcularArea(self):
        pass

    @property
    @abc.abstractmethod
    def nombre(self):
        pass


class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

c = Cuadrado(4)
c.nombre = 'Cuadrado'
print('Área:', c.calcularArea())
print('Nombre:', c.nombre)
