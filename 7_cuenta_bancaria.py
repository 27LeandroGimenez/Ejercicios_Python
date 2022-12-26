class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, cuenta_bancaria, balance = 0):
        super().__init__(nombre, apellido)
        self.cuenta_bancaria = cuenta_bancaria
        self.balance = balance

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\n Balance de la cuenta {self.cuenta_bancaria} es de ${self.balance}"

    def depositar(self, monto_dep):
        self.balance += monto_dep
        print('Monto ingresado correctamente.')

    def retirar(self, monto_ret):
        if self.balance >= monto_ret:
            self.balance -= monto_ret
            print('Monto retirado exitosamente.')
        else: 
            print('Monto insuficiente.')

def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cuenta_bancaria = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre, apellido, cuenta_bancaria)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elije: Depositar (D), Retirar (R), o Salir (S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print("Gracias por operar en Banco Python")


inicio()