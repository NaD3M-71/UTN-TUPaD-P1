# #Ejercicio 1
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(6))

#Ejercicio 2
# def fibonacci_serie(pos, serie=[0, 1]):
#     if len(serie) <= pos:  
#         serie.append(serie[-1] + serie[-2])  # Añadimos el siguiente número en la serie
#         fibonacci_serie(pos, serie)  
#         return serie[:pos+1]  # Retornamos la serie completa

# print(fibonacci_serie(10)) 

#Ejercicio 3
# def potencia(n,m):
#     if m==0:
#         return 1
#     elif m==1:
#         return n
#     else:
#         return n* potencia(n,m-1)
    
# print('Ingrese la base de la potencia')
# n=int(input())
# m=int(input('Ingrese el exponente de la potencia: '))
# print(f'el resultado de la potencia es: {potencia(n,m)}')

#Ejercicio 4
# def decimal_a_binario_recursivo(n):
#     if n == 0:
#         return "0"
#     elif n == 1:
#         return "1"
#     else:
#         return decimal_a_binario_recursivo(n // 2) + str(n % 2)

# print("Ingrese un número entero positivo:")
# numero_decimal = int(input())

# if numero_decimal < 0:
#     print("Por favor, ingrese un número entero positivo.")
# elif numero_decimal == 0:
#     print("La representación binaria es: 0")
# else:
#     binario = decimal_a_binario_recursivo(numero_decimal)
#     print(f"La representación binaria de {numero_decimal} es: {binario}")

# #Ejercicio 5
# def es_palindromo(palabra):
#     palabra = palabra.lower() 
#     if len(palabra) <= 1:
#         return True
#     elif palabra[0] == palabra[-1]:
#         return es_palindromo(palabra[1:-1])
#     else:
#         return False

# print("Ingrese una palabra sin espacios ni tildes:")
# texto = input()

# if es_palindromo(texto):
#     print(f"'{texto}' es un palíndromo.")
# else:
#     print(f"'{texto}' no es un palíndromo.")

#Ejercicio 6
# def suma_digitos(num):
#     if num==0:
#         return 0
#     else:
#         return (num%10)+ suma_digitos(num//10)
# print(suma_digitos(1235))

#Ejercicios 7
# def contar_bloques(n):
#     if n == 0:
#         return 0
#     else:
#         return n + contar_bloques(n - 1)
    
# def generar_piramide(n, bloque="[ ]"):
#     if n == 0:
#         return
#     else:
#         generar_piramide(n - 1, bloque)
#         print(bloque * n)


# n=int(input("cuantos pisos tendra su piramide?"))
# print(f"Usted necesitara {contar_bloques(n)} bloques para una piramide de {n} pisos.")
# generar_piramide(n)

#Adicional 7
# def construir_y_contar_piramide(n, bloque="[ ]"):
#     if n == 0:
#         return 0
#     else:
#         total_bloques_superior = construir_y_contar_piramide(n - 1, bloque)
#         bloques_nivel_actual = bloque * n
#         print(bloques_nivel_actual)
#         return n + total_bloques_superior

# pisos = int(input("¿Cuántos pisos tendrá su pirámide? "))
# total_bloques = construir_y_contar_piramide(pisos)
# print(f"Total de bloques: {total_bloques}")

#Ejercicio 8
# def contar_digito(numero, digito):
#     if numero == 0:
#         return 0
#     else:
#         ultimo_digito = numero % 10
#         resto_numero = numero // 10
#         if ultimo_digito == digito:
#             return 1 + contar_digito(resto_numero, digito)
#         else:
#             return contar_digito(resto_numero, digito)


# numero= int(input("Ingrese un numero: "))
# digito= int(input("Ingrese el digito que desea contar: "))

# print(f"El digito {digito} aparece {contar_digito(numero,digito)} veces en el numero {numero}.")