#######################################
# Base de datos con PostgreSQL
#######################################
# Crear o activar el entorno virtual
# Instalar el módulo # pip install psycopg2

# import psycopg2

# conexion = psycopg2.connect(
#     user = 'postgres',
#     password = 'postgres',
#     host = 'localhost',
#     port = '5432',
#     database = 'test_db'
# )

# cursor = conexion.cursor()
# sentencia = 'SELECT * FROM persona;'
# cursor.execute(sentencia)

# registros = cursor.fetchall() # 'fetch all()' devuelve una lista de tuplas, varios registros
# print(registros)

# registro = cursor.fetchone() # 'fetch one()' devuelve una tupla, único registro
# print(registro)

# conexion.commit() # 'commit()' guarda los cambios si se realizó alguno

# cursor.close()
# conexion.close()

# Conexión con with
#######################################
# try:
#     with conexion:
#         with conexion.cursor() as cursor:

#             sentencia = 'SELECT * FROM persona WHERE id_persona IN %s;'
#             ids_personas = (1, 2)
#             cursor.execute(sentencia, (ids_personas, )) # 'execute()' puede recibir otro parámetro de tipo tupla para remplazar '%s'
#             registros = cursor.fetchall()

#             for registro in registros:
#                 print(registro)

# except Exception as e:
#     print(f'Error: {e}')

# finally:
#     conexion.close()

# Insertar registros
#######################################
# try:
#     with conexion:
#         with conexion.cursor() as cursor:

#             sentencia = 'INSERT INTO persona (nombre, apellido, correo) VALUES (%s, %s, %s);'

#             # valores = ('Carlos', 'Lara', 'clara@mail.com') # Un solo registro
#             # cursor.execute(sentencia, valores) # Un solo registro

#             valores = (('Marcos', 'Cantu', 'mcantu@mail.com'), ('Angel', 'Gonzalez', 'agonzalez@mail.com')) # Varios registros
#             cursor.executemany(sentencia, valores) # Varios registros

#             # conexion.commit() # Al usar 'with', el 'commit()' se ejecuta automáticamente

#             registros_insertados = cursor.rowcount
#             print(f'Registros insertados: {registros_insertados}')

# except Exception as e:
#     print(f'Error: {e}')

# finally:
#     conexion.close()

# Actualizar registros
#######################################
# try:
#     with conexion:
#         with conexion.cursor() as cursor:

#             sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, correo = %s WHERE id_persona = %s;'

#             # valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1) # Un solo registro
#             # cursor.execute(sentencia, valores) # Un solo registro

#             valores = (('Sara', 'Cantu', 'scantu@mail.com', 6), ('Sofia', 'Gonzalez', 'sgonzalez@mail.com', 7)) # Varios registros
#             cursor.executemany(sentencia, valores) # Varios registros

#             # conexion.commit() # Al usar 'with', el 'commit()' se ejecuta automáticamente

#             registros_actualizados = cursor.rowcount
#             print(f'Registros actualizados: {registros_actualizados}')

# except Exception as e:
#     print(f'Error: {e}')

# finally:
#     conexion.close()

# Eliminar registros
#######################################
# try:
#     with conexion:
#         with conexion.cursor() as cursor:

#             sentencia = 'DELETE FROM persona WHERE id_persona IN %s;'

#             # valores = (7, ) # Un solo registro
#             # cursor.execute(sentencia, valores) # Un solo registro

#             valores = ((5, 6, 7), ) # Varios registros
#             cursor.execute(sentencia, valores) # Varios registros

#             # conexion.commit() # Al usar 'with', el 'commit()' se ejecuta automáticamente

#             registros_eliminados = cursor.rowcount
#             print(f'Registros eliminados: {registros_eliminados}')

# except Exception as e:
#     print(f'Error: {e}')

# finally:
#     conexion.close()

# Manejo de transacciones
#######################################
# try:
#     conexion.autocommit = False # No guardar los cambios automáticamente
#     cursor = conexion.cursor()

#     sentencia = 'INSERT INTO persona (nombre, apellido, correo) VALUES (%s, %s, %s);'
#     valores = ('Carlos', 'Lara', 'clara@mail.com')
#     cursor.execute(sentencia, valores)

#     sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, correo = %s WHERE id_persona = %s;'
#     valores = ('Juan Carlos', 'juarez', 'jcjuarez@mail.com', 1)
#     cursor.execute(sentencia, valores)

#     conexion.commit()
#     print('Termina la transacción, se hizo commit')

# except Exception as e:
#     conexion.rollback() # IMPORTANTE 'rollback()' Devuelve los cambios realizados si hay un error
#     print(f'Error, se hizo rollback: {e}')

# finally:
#     conexion.close()

# Manejo de transacciones con with
#######################################
# try:
#     with conexion:
#         with conexion.cursor() as cursor:

#             sentencia = 'INSERT INTO persona (nombre, apellido, correo) VALUES (%s, %s, %s);'
#             valores = ('Alex', 'Rojas', 'arojas@mail.com')
#             cursor.execute(sentencia, valores)

#             sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, correo = %s WHERE id_persona = %s;'
#             valores = ('Juan', 'Perez', 'jperez@mail.com', 1)
#             cursor.execute(sentencia, valores)

#             print('Termina la transacción, se hizo commit')

# except Exception as e:
#     print(f'Error, se hizo rollback: {e}')

# finally:
#     conexion.close()

#######################################
# Capa de datos
#######################################

# Logging/Log (registro)
#######################################
# https://docs.python.org/es/3/howto/logging.html

# import logging as log

# log.basicConfig(
#     level = log.DEBUG,
#     format = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
#     datefmt = '%I:%M:%S %p',
#     # filename = 'static/capa_datos.log', # Otra forma de enviar a un archivo
#     handlers = [
#         log.FileHandler('static/capa_datos.log'), # Enviar a un archivo
#         log.StreamHandler() # Seguir imprimiendo en consola
#     ] # 'handlers' = manejador
# ) # Configuración básica a nivel de 'DEBUG'

# Clase persona
#######################################
# class Persona:
#     def __init__(self, id_persona = None, nombre = None, apellido = None, correo = None):
#         self._id_persona = id_persona
#         self._nombre = nombre
#         self._apellido = apellido
#         self._correo = correo

#     def __str__(self):
#         return f'''
#             Id persona: {self._id_persona},
#             Nombre: {self._nombre},
#             Apellido: {self._apellido},
#             Correo: {self._correo}
#         '''

#     @property
#     def id_persona(self):
#         return self._id_persona

#     @id_persona.setter
#     def id_persona(self, id_persona):
#         self._id_persona = id_persona

#     @property
#     def nombre(self):
#         return self._nombre

#     @nombre.setter
#     def nombre(self, nombre):
#         self._nombre = nombre

#     @property
#     def apellido(self):
#         return self._apellido

#     @apellido.setter
#     def apellido(self, apellido):
#         self._apellido = apellido

#     @property
#     def correo(self):
#         return self._correo

#     @correo.setter
#     def correo(self, correo):
#         self._correo = correo

# Clase conexión
#######################################
# import psycopg2 as bd
# import sys

# class Conexion:
#     _DATABASE ='test_db'
#     _USERNAME = 'postgres'
#     _PASSWORD = 'postgres'
#     _DB_PORT = '5432'
#     _HOST = '127.0.0.1'
#     _conexion = None
#     _cursor = None

#     @classmethod
#     def obtenerConexion(cls):
#         if cls._conexion is None:

#             try:
#                 cls._conexion = bd.connect(
#                     host = cls._HOST,
#                     user = cls._USERNAME,
#                     password = cls._PASSWORD,
#                     port = cls._DB_PORT,
#                     database = cls._DATABASE
#                 )

#                 log.debug(f'Conexión exitosa: {cls._conexion}')

#                 return cls._conexion

#             except Exception as e:
#                 log.error(f'Ocurrió una excepción al obtener la conexión {e}')
#                 sys.exit() # Termina el programa

#         else:
#             return cls._conexion

#     @classmethod
#     def obtenerCursor(cls):
#         if cls._cursor is None:

#             try:
#                 cls._cursor = cls.obtenerConexion().cursor()

#                 log.debug(f'Se abrió correctamente el cursor {cls._cursor}')

#                 return cls._cursor

#             except Exception as e:
#                 log.error(f'Ocurrió una excepción al obtener el cursor {e}')
#                 sys.exit() # Termina el programa

#         else:
#             return cls._cursor

# Clase DAO (data access object)
#######################################
# DAO es un patrón de diseño para comunicarse con una base de datos

# class PersonaDAO:
#     _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona;'
#     _INSERTAR = 'INSERT INTO persona(nombre, apellido, correo) VALUES (%s, %s, %s);'
#     _ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, correo = %s WHERE id_persona = %s;'
#     _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s;'

#     @classmethod
#     def seleccionar(cls):
#         with Conexion.obtenerConexion() as conexion:
#             with conexion.cursor() as cursor:
#                 cursor.execute(cls._SELECCIONAR)
#                 registros = cursor.fetchall()
#                 personas = []

#                 for registro in registros:
#                     persona = Persona(registro[0], registro[1], registro[2], registro[3])
#                     personas.append(persona)

#                 return personas

#     @classmethod
#     def insertar(cls, persona):
#         with Conexion.obtenerConexion():
#             with Conexion.obtenerCursor() as cursor:
#                 valores = (persona.nombre, persona.apellido, persona.correo)
#                 cursor.execute(cls._INSERTAR, valores)

#                 log.debug(f'Persona insertada {persona}')

#                 return cursor.rowcount

#     @classmethod
#     def actualizar(cls, persona):
#         with Conexion.obtenerConexion():
#             with Conexion.obtenerCursor() as cursor:
#                 valores = (persona.nombre, persona.apellido, persona.correo, persona.id_persona)
#                 cursor.execute(cls._ACTUALIZAR, valores)

#                 log.debug(f'Persona actualizada {persona}')

#                 return cursor.rowcount

#     @classmethod
#     def eliminar(cls, persona):
#         with Conexion.obtenerConexion():
#             with Conexion.obtenerCursor() as cursor:
#                 valores = (persona.id_persona,)
#                 cursor.execute(cls._ELIMINAR, valores)

#                 log.debug(f'Persona eliminada {persona}')

#                 return cursor.rowcount

# CRUD (create, read, update, delete)
#######################################
# persona = Persona(nombre = 'Angela', apellido = 'Osorio', correo = 'aosorio@mail.com')
# personas_insertadas = PersonaDAO.insertar(persona)
# log.debug(f'Personas insertadas {personas_insertadas}')

# persona = Persona(nombre = 'Luisa', apellido = 'Perez', correo = 'lperez@mail.com', id_persona = 18)
# personas_actualizadas = PersonaDAO.actualizar(persona)
# log.debug(f'Personas actualizadas {personas_actualizadas}')

# persona = Persona(id_persona = 14)
# personas_eliminadas = PersonaDAO.eliminar(persona)
# log.debug(f'Personas eliminadas {personas_eliminadas}')

# personas = PersonaDAO.seleccionar()
# for persona in personas:
#     log.debug(persona)

#######################################
# Capa de datos con Pool de conexiones
#######################################

# Clase conexión
#######################################
# from psycopg2 import pool
# import sys

# class Conexion:
#     _DATABASE ='test_db'
#     _USERNAME = 'postgres'
#     _PASSWORD = 'postgres'
#     _DB_PORT = '5432'
#     _HOST = '127.0.0.1'
#     _MIN_CON = 1
#     _MAX_CON = 5
#     _pool = None

#     @classmethod
#     def obtenerPool(cls):
#         if cls._pool is None:
#             try:
#                 cls._pool = pool.SimpleConnectionPool(
#                     cls._MIN_CON,
#                     cls._MAX_CON,
#                     host = cls._HOST,
#                     user = cls._USERNAME,
#                     password = cls._PASSWORD,
#                     port = cls._DB_PORT,
#                     database = cls._DATABASE
#                 )

#                 log.debug(f'Creación del pool exitosa {cls._pool}')

#                 return cls._pool

#             except Exception as e:
#                 log.error(f'Ocurrió un error al obtener el pool {e}')
#                 sys.exit()

#         else:
#             return cls._pool

#     @classmethod
#     def obtenerConexion(cls):
#         try:
#             conexion = cls.obtenerPool().getconn()
#             log.debug(f'Conexión obtenida del pool {conexion}')

#             return conexion

#         except Exception as e:
#             log.error(f'Ocurrió un error al obtener la conexión {e}')

#     @classmethod
#     def liberarConexion(cls, conexion):
#         cls.obtenerPool().putconn(conexion)
#         log.debug(f'Regresamos la conexión al pool {conexion}')

#     @classmethod
#     def cerrarConexiones(cls):
#         cls.obtenerPool().closeall()

# conexion1 = Conexion.obtenerConexion()
# Conexion.liberarConexion(conexion1)

# conexion2 = Conexion.obtenerConexion()
# conexion3 = Conexion.obtenerConexion()
# Conexion.liberarConexion(conexion3)

# conexion4 = Conexion.obtenerConexion()
# conexion5 = Conexion.obtenerConexion()
# Conexion.liberarConexion(conexion5)

# conexion6 = Conexion.obtenerConexion()

# Clase cursor
#######################################
# class CursorPool:
#     def __init__(self):
#         self._conexion = None
#         self._cursor = None

#     def __enter__(self):
#         log.debug('Inicio del método with __enter__')
#         self._conexion = Conexion.obtenerConexion()
#         self._cursor = self._conexion.cursor()

#         return self._cursor

#     def __exit__(self, tipo_excepcion, valor_excepcion, traceback):
#         log.debug('Se ejecuta método __exit__')

#         if valor_excepcion:
#             self._conexion.rollback()
#             log.error(f'Ocurrió una excepción, se hace rollback {valor_excepcion} {tipo_excepcion} {traceback}')

#         else:
#             self._conexion.commit()
#             log.debug('Commit de la transacción')

#         self._cursor.close()
#         Conexion.liberarConexion(self._conexion)

# with CursorPool() as cursor:
#     log.debug('Dentro del bloque with')
#     cursor.execute('SELECT * FROM persona;')
#     log.debug(cursor.fetchall())

# Clase DAO (data access object)
#######################################
# DAO es un patrón de diseño para comunicarse con una base de datos

# class PersonaDAO:
#     _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona;'
#     _INSERTAR = 'INSERT INTO persona(nombre, apellido, correo) VALUES (%s, %s, %s);'
#     _ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, correo = %s WHERE id_persona = %s;'
#     _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s;'

#     @classmethod
#     def seleccionar(cls):
#         with CursorPool() as cursor:
#             cursor.execute(cls._SELECCIONAR)
#             registros = cursor.fetchall()
#             personas = []

#             for registro in registros:
#                 persona = Persona(registro[0], registro[1], registro[2], registro[3])
#                 personas.append(persona)

#             return personas

#     @classmethod
#     def insertar(cls, persona):
#         with CursorPool() as cursor:
#             valores = (persona.nombre, persona.apellido, persona.correo)
#             cursor.execute(cls._INSERTAR, valores)

#             log.debug(f'Persona insertada {persona}')

#             return cursor.rowcount

#     @classmethod
#     def actualizar(cls, persona):
#         with CursorPool() as cursor:
#             valores = (persona.nombre, persona.apellido, persona.correo, persona.id_persona)
#             cursor.execute(cls._ACTUALIZAR, valores)

#             log.debug(f'Persona actualizada {persona}')

#             return cursor.rowcount

#     @classmethod
#     def eliminar(cls, persona):
#         with CursorPool() as cursor:
#             valores = (persona.id_persona,)
#             cursor.execute(cls._ELIMINAR, valores)

#             log.debug(f'Persona eliminada {persona}')

#             return cursor.rowcount

# CRUD (create, read, update, delete) con Pool de conexiones
#######################################
# persona = Persona(nombre = 'Alejandra', apellido = 'Tellez', correo = 'atellez@mail.com')
# personas_insertadas = PersonaDAO.insertar(persona)
# log.debug(f'Personas insertadas {personas_insertadas}')

# persona = Persona(nombre = 'Luisa', apellido = 'Perez', correo = 'lperez@mail.com', id_persona = 18)
# personas_actualizadas = PersonaDAO.actualizar(persona)
# log.debug(f'Personas actualizadas {personas_actualizadas}')

# persona = Persona(id_persona = 14)
# personas_eliminadas = PersonaDAO.eliminar(persona)
# log.debug(f'Personas eliminadas {personas_eliminadas}')

# personas = PersonaDAO.seleccionar()
# for persona in personas:
#     log.debug(persona)
