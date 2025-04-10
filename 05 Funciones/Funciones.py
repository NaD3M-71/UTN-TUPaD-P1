#Ejercicio 1
def hola_mundo():
    print("Hola Mundo");

hola_mundo()

#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}")
nombre=input("Ingrese su nombre: ")
saludar_usuario(nombre)

#Ejercicio 3
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre2= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
edad= int(input("Ingrese su edad: "))
residencia= input("Ingrese donde reside: ")
informacion_personal(nombre2,apellido,edad,residencia)

#Ejercicio 4
import math

def calcular_area_circulo(radio):
    area= math.pi * (radio ** 2)
    print(f"El área del círculo es: {area:.2f}")

def calcular_perimetro_circulo(radio):
    perimetro= 2 * math.pi * radio
    print(f"El perímetro del círculo es: {perimetro:.2f}")

radio = float(input("Ingresa el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

#Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresá la cantidad de segundos: "))
print("Horas:", segundos_a_horas(segundos))

#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#Ejercicio 7
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

#Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
print(f"Tu IMC es: {calcular_imc(peso, altura):.2f}")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Ingresá la temperatura en Celsius: "))
print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(celsius)}")

#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))
print("Promedio:", calcular_promedio(a, b, c))



