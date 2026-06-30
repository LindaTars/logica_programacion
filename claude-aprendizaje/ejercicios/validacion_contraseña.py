class ErrorContraseña(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class ErrorSinContenido(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class ErrorSinNumero(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

def validar_password(password):
    if(len(password) == 0):
        raise ErrorSinContenido("ERROR. No ingresaste ningún caracter.")

    if(len(password) < 8):
        raise ErrorContraseña("ERROR. La contraseña debe tener mínimo 8 caracteres.")

    tiene_numero = any(caracter.isdigit() for caracter in contraseña)
    if not tiene_numero:
        raise ErrorSinNumero("ERROR. La contraseña debe incluir por lo menos un número.")

    tiene_letra = any(caracter.isalpha() for caracter in contraseña)
    if not tiene_letra:
        raise ErrorContraseña("ERROR. La contraseña no contiene ninguna letra.")    

    return True

try:
    contraseña = input("Ingrese su contraseña: ")
    if validar_password(contraseña):
        print("Bienvenido")
except ErrorContraseña as error:
    print(error)
except ErrorSinContenido as error:
    print(error)
except ErrorSinNumero as error:
    print(error)