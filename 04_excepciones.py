#######################################
# Errores o excepciones
#######################################
# try:
#     ...
# except Exception as e:
#     print(e)

#######################################

class NumerosIguales(Exception): # La clase 'NumerosIguales' hereda de 'Exception' para generar una excepción personalizada
    def __init__(self, mensaje):
        self.message = mensaje

resultado = None

try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))

    if a == b:
        raise Exception('Números iguales') # 'raise' nos permite lanzar o arrojar una excepción
        # raise NumerosIguales('Números iguales') # Otra forma mas personalizada con la clase 'NumerosIguales'

    resultado = a / b

except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e}, {type(e)}')

except TypeError as e:
    print(f'TypeError - Ocurrió un error: {e}, {type(e)}')

except Exception as e:
    print(f'Exception - Ocurrió un error: {e}, {type(e)}')

else:
    print('No hay ninguna excepción')

finally:
    print('Bloque finally')

print(f'Resultado: {resultado}')
print('Continua')
