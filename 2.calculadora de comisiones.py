nombre=input("Ingrese su nombre: ")
ventas=float(input("Ingrese monto de ventas: "))

print(f"Ok {nombre} tus ventas son de {ventas}")

comision = round(ventas*13/100, 2)
print(f"Comisiones obtenidas son: {comision}")