try:
    numero = int(input("Dame un número: "))
    print(100 / numero)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print("Eso no es un número")