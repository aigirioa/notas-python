#######################################
# E/S - Entrada y Salida
#######################################

# Entrada de datos
#######################################

dato = input("Ingrese un dato: ") # La función 'input()' devuelve un 'str'
print(dato)

#######################################
# Archivos
#######################################

# Crear
#######################################
try:
    archivo = open('static/prueba.txt', 'w', encoding = 'utf8')     # Crear o abrir un archivo
    archivo.write('Agregamos información al archivo\n')             # Escribir información al archivo BORRANDO la existente
    archivo.write('Final\n')

except Exception as e:
    print(e)

finally:
    archivo.close()
    print('Archivo cerrado')

# Leer y agregar
#######################################
try:
    archivo = open('static/prueba.txt', 'r', encoding = 'utf8')     # Leer el archivo
    # print(archivo.read(5))                                        # Leer los primeros 5 caracteres
    # print(archivo.readline())                                     # Leer línea completa
    # print(archivo.readlines())                                    # Leer líneas completas
    # print(archivo.readlines()[0])                                 # Leer primera línea
    # print(archivo.read())                                         # Leer la información

    # for linea in archivo: # Iterar en el archivo
    #     print(linea)

    archivo_2 = open('static/copia.txt', 'a', encoding = 'utf8')    # Agregar información al archivo SIN BORRAR la existente
    archivo_2.write(archivo.read())

except Exception as e:
    print(e)

finally:
    archivo.close()
    archivo_2.close()
    print('Archivos cerrados')

# With (Resource manager / Administrador de recursos)
#######################################
# 'with' = con, 'with' tiene dos métodos '__enter__()' y '__exit__()'

# with open('static/prueba.txt', 'r', encoding = 'utf8') as archivo:
#     print(archivo.read())

#######################################

class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding = 'utf8')

        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, traceback): # 'traceback' = rastrear(detalle_excepcion)
        print('Cerrando el recurso'.center(50, '-'))
        if self.nombre:
            self.nombre.close()

with ManejoArchivos('static/prueba.txt') as archivo:
    print(archivo.read())
