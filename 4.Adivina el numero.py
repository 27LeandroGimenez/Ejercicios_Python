"""
* Preguntar nombre
* generar un numero entre el 1 y el 100
* solo tiene 8 intentos
* si el numero ingresado no esta dentro del rango acordado, eligio numero incorrecto,
* Si es menor al numero secreto
* si es mayor al numero secreto
* si adivino el numero, felicidades
* contar con cuantos intentos lo adivino
"""

from random import *

secret_number = randint(1, 100)
attempts = 8
mistakes = 0

name = input('Enter your name: ')
print(f'Ok {name} you have 8 attempts for found the number between (1,100)')

while attempts > 0:
    number = int(input('Enter one number in range 1, 100: '))

    attempts = attempts - 1
    mistakes = mistakes + 1

    if (number > 100 or number < 0):
        print(f'The number joiner is incorrect! [attempts {attempts} of 8]')
    elif (number > secret_number):
        print(f'The number joined is elderly that the secret number, [attempts {attempts} of 8]')
    elif (number < secret_number):
        print(f'The number joined is minor that the secret number [attempts {attempts} of 8]')
    elif (number == secret_number):
        print(f'You find the secret number, Congratulations {name}!')
        print(f'You found the secret number {mistakes} in attempts!')
        break

else:
    print(f'Oh, you could not found the secret number!\n The number secret it was {secret_number}')