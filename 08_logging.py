#######################################
# Logging/Log (registro)
#######################################
# https://docs.python.org/es/3/howto/logging.html

import logging as log

log.basicConfig(
    level = log.DEBUG,
    format = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt = '%I:%M:%S %p',
    # filename = 'static/capa_datos.log',           # Otra forma de enviar a un archivo
    handlers = [
        log.FileHandler('static/capa_datos.log'),   # Enviar a un archivo
        log.StreamHandler()                         # Seguir imprimiendo en consola
    ]                                               # 'handlers' = manejador
)                                                   # Configuración básica a nivel de 'DEBUG'

log.debug('Mensaje a nivel debug')
log.info('Mensaje a nivel info')
log.warning('Mensaje a nivel warning')
log.error('Mensaje a nivel error')
log.critical('Mensaje a nivel critical')
