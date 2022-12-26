# ingresar un texto por el usuario
# que ingrese 3 letras a eleccion
# cuantas veces aparece cada letra elegida
# cuantas palabras hay en total en el texto ingresado
# primera y ultima letra del texto
# el texto en order inverso
# aparece la palabra python

texto = input("Ingrese texto para analizar: ")
texto = texto.lower()

print("Ingrese letras para analizar dentro del texto.")

#Tambien se puede almacenar dentro de una lista llamada letras[] con letras.append(input("Ingrese letra: ")).lower(), y transformar las letras a minusculas con lower.
letra1 = input("Ingrese primer letra: ")
letra2 = input("Ingrese segunda letra: ")
letra3 = input("Ingrese tercer letra: ")

cant_letra1 = texto.count(letra1)
cant_letra2 = texto.count(letra2)
cant_letra3 = texto.count(letra3)

print(f"La cantidad de '{letra1}' que se repiten en el texto son {cant_letra1}, de '{letra2}' son {cant_letra2} y de '{letra3}' son {cant_letra3}")

cant_palabras = texto.split()
print(f"La cantidad de palabras que contiene el texto es de: {len(cant_palabras)}")

primera_letra = texto[0]
ultima_letra = texto[-1]

print(f"La primer letra del texto es: {primera_letra}")
print(f"La ultima letra del texto es: {ultima_letra}")

cant_palabras.reverse()
texto_invertido = ' '.join(cant_palabras)
print(texto_invertido)

print("La palabra python aparece dentro del texto?", "python" in texto)