#Operaciones con Listas:

#Crear una lista de números y calcula la suma, promedio y máximo de los valores.
#Filtra una lista para obtener solo los números pares.
#Combina dos listas eliminando duplicados.
#Ordena una lista de strings alfabéticamente.
#Encuentra el elemento más común en una lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista_pares = []

print(f'Lista: {lista}')


#Suma y promedio de los valores de una lista
suma_lista = 0

for i in lista:
    suma_lista += i

print(f'Suma de todos los numeros de la lista: {suma_lista}')

promedio_lista = suma_lista / len(lista)

print(f'Promedio de la lista: {promedio_lista}')


#Valor maximo y minimo dentro de una lista
valor_maximo = max(lista)
valor_minimo = min(lista)

print(f'Valor maximo de la lista: {valor_maximo}')
print(f'Valor minimo de la lista: {valor_minimo}')


# Encontrar valores pares en la lista
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)

print(f'Lista con solo los valores que son numeros pares: {lista_pares}')


#combinar 2 listas y eliminar los valores repetidos
lista_uno = [1, 2, 3, 4, 5]
lista_dos = [5, 6, 7, 3, 2]

lista_combinada = lista_uno + lista_dos
lista_combinada_sin_repetidos = []

for i in lista_combinada:
    if i not in lista_combinada_sin_repetidos:
        lista_combinada_sin_repetidos.append(i)

print(f'Lista sin valores repetidos: {lista_combinada_sin_repetidos}')


#ordernar lista de string alfabeticamente.
lista_strings = ['Zanahoria', 'Hola', 'Perro', 'Adios', 'Avion', 'Camion', 'Plato']
lista_strings.sort()
print(lista_strings)


#encontrar el elemento mas comun dentro de una lista
lista_dos = [1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 4, 4]
valor_mas_repetido = max(lista_dos, key=lista_dos.count)
print(lista_dos)
print(f'El valor que mas se repite dentro de la lista es: {valor_mas_repetido}')