calificaciones = []
reprobados = 0
cantidad_calificaciones = int(input("Ingresa la cantidad de calificaciones a prosesar:  "))

for i in range (cantidad_calificaciones):
    while True:
        calificacion = int(input(f"Ingresa la calificación {i + 1}: "))
        if(calificacion < 0 or calificacion > 100):
            print("Invalido")
        else:
            calificaciones.append(calificacion)

            if calificacion >= 60:
                print("Aprobado")
            else:
                print("Reprobado")
                reprobados = reprobados + 1
            break
    c = input("¿Desea agregar más calificaciones (s/n): ")
    if c != 's':
        break

s = sum(calificaciones)
cantidad_calificaciones = len(calificaciones)
p = s / cantidad_calificaciones
print("Promedio: ", p)
print("Reprobados: ", reprobados)

