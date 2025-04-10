##Ejercicio 1
# for cien in range(101):
#     print(cien)

# #Ejercicio 2
# numero = int(input("Introduce un número entero: "))
# numero = abs(numero)  # Asegurarse de que el número sea positivo
# cantidad_digitos = 0

# while numero > 0:
#     numero //= 10  # Dividir el número entre 10 para eliminar el último dígito
#     cantidad_digitos += 1

# print(f"La cantidad de dígitos es: {cantidad_digitos}")

# #Ejercicio 3
# valor1 = int(input("Introduce el primer número: "))
# valor2 = int(input("Introduce el segundo número: "))

# inicio = min(valor1, valor2) + 1
# fin = max(valor1, valor2)

# suma = 0
# for i in range(inicio, fin):
#     suma += i

# print(f"La suma de los números entre {valor1} y {valor2}, excluyendo los extremos, es: {suma}")

# #Ejercicio 4
# total = 0
# numero = int(input("Ingresa un número entero (0 para detener): "))

# while numero != 0:
#     total += numero
#     numero = int(input("Ingresa un número entero (0 para detener): "))

# print(f"El total acumulado es: {total}")

# #Ejercicio 5
# import random

# numero_secreto = random.randint(0, 9)  # Genera un número aleatorio entre 0 y 9
# intentos = 0
# acertado = False

# print("¡Adivina el número secreto entre 0 y 9!")

# while not acertado:
#     intento = int(input("Ingresa tu número: "))
#     intentos += 1
#     if intento == numero_secreto:
#         acertado = True

# print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")

# #Ejercicio 6

# for ii in range(100,-1,-2):
#     print(ii)

# #Ejercicio 7
# numero_usuario = int(input("Ingrese un numero entero"))
# sumatoria=0
# for iii in range(0,numero_usuario,1):
#     sumatoria+= iii
# print(f"La sumatoria de los numeros comprendidos entre 0 y su numero es: {sumatoria}")

# #Ejercicio 8
# cantidad = 100 # para probar con menos numeros cambiar este valor
# pares = 0
# impares = 0
# positivos = 0
# negativos = 0

# print(f"Ingresa {cantidad} números enteros:")
# for iv in range(cantidad):
#     numero = int(input())
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1

# print("Resultados:")
# print(f"Números pares: {pares}")
# print(f"Números impares: {impares}")
# print(f"Números positivos: {positivos}")
# print(f"Números negativos: {negativos}")

# #Ejercicio 9
# cantidad = 100  # Cambiar este valor para probar con menos numeros
# suma = 0

# print(f"Ingresa {cantidad} números enteros:")
# for _ in range(cantidad):
#     numero = int(input())
#     suma += numero

# media = suma / cantidad
# print(f"La media de los números ingresados es: {media}")


#Ejercicio 10
numerito = int(input("Ingrese un número: "))
numero_invertido = 0

while numerito > 0:
    parcial = numerito % 10 
    numero_invertido = numero_invertido * 10 + parcial  
    numerito = numerito // 10  
    
print(f"El número invertido es: {numero_invertido}")
