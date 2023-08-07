from os import system

class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, nro_cuenta, balance):
        super().__init__(nombre, apellido)
        self.nro_cuenta = nro_cuenta
        self.balance = balance

    def __str__(self):
        return (f'Bienvenido {self.nombre} {self.apellido}.\nSu numero de cuenta es: {self.nro_cuenta} y tiene {self.balance} pesos.')

    def depositar(self, deposito):
        self.balance += deposito 
        system('cls')
        print('***** Deposito realizado correctamente *****')
    
    def retirar(self, retirar):
        if self.balance >= retirar:
            self.balance -= retirar
            system('cls')
            print('***** Retiro realizado correctamente *****')
        else:
            system('cls')
            print(f'***** Saldo insuficiente. Usted tiene ${self.balance} en su cuenta. *****')
        
    
def crear_cliente():
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apelldo: ')
    nro_cuenta = int(input('Ingrese su numero de cuenta: '))
    balance = 0
    cliente = Cliente(nombre, apellido, nro_cuenta, balance)
    return cliente

def inicio():
    opcion = '0'
    cliente = crear_cliente()
    system('cls')
    print(cliente)

    while opcion != '4':
        print('\nSeleccione una de las siguientes operaciones:\n1.Depositar dinero.\n2.Retirar dinero\n3.Ver balance\n4.Salir\n')
        opcion = input('Opcion: ')
        if opcion <= '0' or opcion > '4':
            system('cls')
            print('***** Porfavor ingrese una opcion valida. *****')
        elif opcion == '1':
            deposito = int(input('Ingrese monto a depositar: '))
            cliente.depositar(deposito)
        elif opcion == '2':
            retirar = int(input('Ingrese monto a retirar: '))
            cliente.retirar(retirar)
        elif opcion == '3':
            system('cls')
            print(f'***** Usted tiene ${cliente.balance} en su cuenta. *****')
        elif opcion == '4':
            system('cls')
            print(f'***** Gracias por usar nuestros servicios {cliente.nombre} {cliente.apellido}, hasta la proxima. *****')

inicio()




        


