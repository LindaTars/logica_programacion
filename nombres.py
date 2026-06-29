nombres = []
cantidad_nombres = int(input("¿Cuántos nombres desea agregar? "))
hubo_a = False

for i in range (cantidad_nombres):
    nombre = input(f"Ingrese el nombre #{i + 1} " )
    nombres.append(nombre)

for nombre in nombres:
    if nombre.lower().startswith('a'):
        print(nombre)
        hubo_a = True

if not hubo_a:
    print("No se agregaron nombres con A al comienzo")
    
