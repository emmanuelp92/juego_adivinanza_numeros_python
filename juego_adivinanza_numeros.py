import random


def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinanza de numero.")
    print("Debes adivinar el número entre 1 y 100.")
    print("¡Intenta adivinarlo!")

    while not adivinado:

        adivinanza = input("Introduzca un numero del 1 al 100: ")

        if adivinanza.isdigit():
           adivinanza = int(adivinanza)
           intentos += 1

           if adivinanza < numero_secreto:
            print(f"El número secreto es mayor a {adivinanza}")
           elif adivinanza > numero_secreto:
            print(f"El número secreto es menor a {adivinanza}")
           else:
            print(f"¡Felicitaciones, has ganado! El numero secreto es {adivinanza} y lo has logrado en {intentos} intentos.")

        else:
           print("Por favor, ingresa un número válido entre el 1 y el 100")



juego_adivinanza()
