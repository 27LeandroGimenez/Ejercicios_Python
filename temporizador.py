import time, os

def Menu():
    print('1. Cuenta atras.')
    print('2. Cronometro')
    print('3. Salir')

def Opcion():

    while True:
        try:
            opcion = int(input('\nIngrese una opcion: '))
            if opcion < 0 or opcion > 3:
                os.system('cls')
                print('** Ingrese un numero valido. **\n')
                Menu()
            else:
                break
        except ValueError:
            os.system('cls')
            print('** Ingrese solo numeros porfavor. **\n')
            Menu()

    return opcion

def Cuenta_atras():
        while True:
            try:
                horas = int(input("Horas para la \"CUENTA ATRAS\" (0-23): "))
                minutos = int(input("Minutos para la \"CUENTA ATRAS\" (0-59): "))
                segundos = int(input("Segundos para la \"CUENTA ATRAS\" (0-59): "))

                if 0 <= horas <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59:
                    
                    total_segundos = horas * 3600 + minutos * 60 + segundos

                    for i in range(total_segundos, 0, -1):
                        segundos_restantes = i % 60
                        minutos_restantes = (i // 60) % 60
                        horas_restantes = i // 3600
                        os.system('cls')
                        print(f'Tiempo total a completar: {horas:02d}:{minutos:02d}:{segundos:02d}')
                        print(f'Tiempo: {horas_restantes:02d}:{minutos_restantes:02d}:{segundos_restantes:02d}')
                        time.sleep(1)
            
                    print("\n¡Tiempo terminado!\n")
                    break
            except ValueError:
                os.system('cls')
                print('Ingrese solo numeros positivos mayores a 0.')

def Cronometro():
        while True:
            try:
                horas = int(input("Horas para el \"CRONÓMETRO\" (0-23): "))
                minutos = int(input("Minutos para el \"CRONÓMETRO\" (0-59): "))
                segundos = int(input("Segundos para el \"CRONÓMETRO\" (0-59): "))

                if 0 <= horas <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59:

                    total_segundos = horas * 3600 + minutos * 60 + segundos

                    for i in range(total_segundos + 1):
                        segundos_restantes = i % 60
                        minutos_restantes = (i // 60) % 60
                        horas_restantes = i // 3600
                        os.system('cls')
                        print(f'Tiempo total a completar: {horas:02d}:{minutos:02d}:{segundos:02d}')
                        print(f'Tiempo: {horas_restantes:02d}:{minutos_restantes:02d}:{segundos_restantes:02d}')
                        time.sleep(1)
            
                    print("\n¡Tiempo terminado!\n")
                    break
            except ValueError:
                os.system('cls')
                print('Ingrese solo numeros positivos mayores a 0.')

while True:

    Menu()

    opcion = Opcion()

    if opcion == 1:
        Cuenta_atras()

    if opcion == 2:
        Cronometro()

    if opcion == 3:
        print('Programa finalizado, hasta la proxima.')
        break