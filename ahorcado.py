from random import *

juego_terminado = False
palabras = ['perro', 'gato', 'elefante', 'heladera', 'avion']
palabra = choice(palabras)
cantidad_letras = len(palabra)
letras_correctas = []
intentos = 0

for i in range(len(palabra)):
    letras_correctas.append('_')

print(f'La palabra que tienes que adivinar tiene {cantidad_letras} letras.')
print(' '.join(letras_correctas))

while juego_terminado == False:

    letra_ingresada = input('ingrese una letra: ').lower()
    intentos += 1

    for indice, letra in enumerate(palabra):
        if letra == letra_ingresada:
            letras_correctas[indice] = letra

    print(' '.join(letras_correctas))

    if ''.join(letras_correctas) == palabra:
        juego_terminado = True
        print(f'Felicidades ganaste, la palabra era {palabra} y la adivinaste en {intentos} intentos.')