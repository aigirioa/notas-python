
class InputUtils:

    @staticmethod
    def leerEnteroPositivo(msg):
        n = 0
        entrada = input(msg)

        if entrada.isdigit() and int(entrada) > 0:
            n = int(entrada)

        return n
