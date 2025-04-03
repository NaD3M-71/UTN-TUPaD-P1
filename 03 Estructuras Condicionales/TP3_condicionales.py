#Trabajo practico n° 3 - Programacion I

#Ejercicio 1
edad = int(input("¿Que edad tenés? "))
if edad>=18:
    print("Es mayor de edad")
    
#Ejercicio 2
nota= int(input("¿Cual es su nota? "))
if nota >=6:
    print("Aprobado")
else:
    print("Desaprobado")


#Ejercicio 3
numeroPar= int(input("Ingrese un numero PAR: "))
if numeroPar%2 == 0:
    print("Ha ingresado un número PAR")
else:
    print("Por favor, 25ingrese un número par")

#Ejercicio 4
edad = int(input("Ingrese su edad: "))

# Determinar la categoría según la edad
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
    
#Ejercicio 5
password = input("Ingrese una contraseña: ")
if password.len() <8 and password.len() > 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

password = input("Ingrese una contraseña: ")
if 8<= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import mode, median, mean

# Generar lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular parámetros estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Determinar el tipo de sesgo
if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo"

# Imprimir resultados
print(f"Lista de números: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Resultado: {sesgo}")

#Ejercicio 7
frase = input("Introduce una frase o palabra: ")
if len(frase) > 0 and frase[len(frase) - 1].lower() in "aeiou":
    frase += "!"
print(frase)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")
opcion = input("Seleccione una opción (1 - Mayúsculas, 2 - Minúsculas, 3 - Solo primer letra mayuscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida. Por favor, ingrese 1, 2 o 3.")

#Ejercicio 9
# Pedir al usuario la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasificación según la escala de Richter con descripción integrada
if magnitud < 3:
    print("La magnitud ingresada es:", magnitud)
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("La magnitud ingresada es:", magnitud)
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("La magnitud ingresada es:", magnitud)
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("La magnitud ingresada es:", magnitud)
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("La magnitud ingresada es:", magnitud)
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("La magnitud ingresada es:", magnitud)
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10
# Solicitar datos al usuario
hemisferio = input("Ingrese su hemisferio (N/S): ")
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Determinar la estación
if hemisferio.upper() == 'N':  # Hemisferio Norte
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio.upper() == 'S':  # Hemisferio Sur
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

# Mostrar el resultado
print(f"La estación del año es: {estacion}")
