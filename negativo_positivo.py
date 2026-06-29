posiivo = 0
negativo = 0

while True:
    num = int(input("Ingresa el número: "))

    if(num < 0):
        print("El número es negativo")
        negativo = negativo + 1
    elif(num == 0):
        break
    else:
        print("El número es positivo")
        posiivo = posiivo + 1

print("Cantidad de números positivos agregados: ", posiivo)
print("Cantidad de números negativos agregados: ", negativo)
