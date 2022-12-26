from random import *

def lanzar_dados():
    dado_uno = randint(1,6)
    dado_dos = randint(1,6)

    return dado_uno, dado_dos

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        resultado = (f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        resultado = (f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        resultado = (f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
    return print(resultado)
    
dado1, dado2 = lanzar_dados()
evaluar_jugada(dado1, dado2)