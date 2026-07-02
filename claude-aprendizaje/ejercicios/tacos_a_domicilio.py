class ErrorTacos(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

def calcular_precio(cantidad, precio_unitario):
    if(cantidad <= 0):
        raise ErrorTacos("No puedes pedir 0 tacos ó -0 tacos.")

    total_pago = cantidad * precio_unitario
    print("El total a pagar es $", total_pago)
    return total_pago

try:
    cantidad = int(input("¿Cuántos tacos gusta? "))
    precio_unitario = float(input("Ingrese el precio por unidad del taco: $"))

    calcular_precio(cantidad, precio_unitario)
    print("Tus tacos van en camino")
except ValueError:
    print("Error. No haz ingresado ningún número")
except ErrorTacos as error:
    print(error)
print("Cambio xd")