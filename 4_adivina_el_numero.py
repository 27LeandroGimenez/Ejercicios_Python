from random import *

vidas = 5
numero = randint(1, 100)
intentos = 0

def inicio():
    nombre = input('Ingrese su nombre: ')
    print(f'Bienvenido {nombre} he pensado un numero entre el 1 y el 100, tienes 5 intentos para adivinarlo, podras?')
    return nombre

def adivina_el_numero(numero, vidas, intentos, nombre):
    while vidas != 0:
        numero_usuario = int(input('Ingrese numero: '))
        
        if numero_usuario > numero:
            vidas -= 1
            print(f'El numero ingresado es mayor que el numero a adivinar. Te quedan {vidas} vidas')
            intentos += 1
        elif numero_usuario < numero:
            vidas -= 1
            print(f'el numero ingresado es menor que el numero a adivinar. Te quedan {vidas} vidas')
            intentos += 1
        elif numero_usuario == numero:
            intentos += 1
            print(f'Felicidades {nombre} adivinaste el numero en {intentos} intentos. Te quedaron {vidas} vidas.')
            break
        else:
            print('Perdiste ya no te quedan mas intentos, no pudiste adivinar el numero.')

programa = inicio()
adivina_el_numero(numero, vidas, intentos, programa)