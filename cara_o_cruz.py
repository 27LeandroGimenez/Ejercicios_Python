from random import *

lista_numeros = [1, 2, 3, 4, 5, 6]

def lanzar_moneda():
    lado = randint(1,2)
    if lado == 1:
        return 'Cara'
    else:
        return 'Cruz'

def probar_suerte(moneda, lista_numeros):
    if moneda == 'Cara':
        print('La lista se destruira!')
        lista_numeros.clear()
        return print(lista_numeros)
    else:
        print('La lista fue salvada!')
        return print(lista_numeros)

moneda = lanzar_moneda()
probar_suerte(moneda, lista_numeros)