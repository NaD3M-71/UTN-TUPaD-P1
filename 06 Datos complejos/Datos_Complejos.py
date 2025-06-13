# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Ejercicio 3
solo_frutas = list(precios_frutas.keys())

# Ejercicio 4
# Permite cargar 5 contactos y consultar uno
agenda = {}
for _ in range(5):
    nombre = input("Nombre: ")
    numero = input("Número: ")
    agenda[nombre] = numero

consulta = input("Consultar número de: ")
if consulta in agenda:
    print("Número:", agenda[consulta])
else:
    print("Contacto no encontrado")

# Ejercicio 5
# Procesa una frase para obtener palabras únicas y su frecuencia
frase = input("Ingresá una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
frecuencias = {}

for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia de palabras:", frecuencias)

# Ejercicio 6
# Calcula el promedio de 3 alumnos
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Nota {i+1}: ")) for i in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")

# Ejercicio 7
# Muestra estudiantes según combinaciones de aprobaciones
parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}

ambos = parcial1 & parcial2
uno_solo = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", uno_solo)
print("Aprobaron al menos uno:", al_menos_uno)

# Ejercicio 8
# Sistema de stock con consulta, suma y alta de productos
stock = {'Yerba': 10, 'Café': 5}

producto = input("Producto a consultar: ")
if producto in stock:
    suma = int(input("¿Cuántas unidades agregar? "))
    stock[producto] += suma
else:
    nuevo_stock = int(input("Producto nuevo. ¿Cantidad inicial? "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# Ejercicio 9
# Agenda con claves (día, hora) y eventos
agenda = {
    ('Lunes', '10:00'): 'Reunión',
    ('Martes', '15:00'): 'Clase de inglés'
}

dia = input("Día: ")
hora = input("Hora: ")
evento = agenda.get((dia, hora), "Nada agendado")
print("Evento:", evento)

# Ejercicio 10
# Invierte un diccionario de país-capital
paises = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago'
}
capitales = {capital: pais for pais, capital in paises.items()}
