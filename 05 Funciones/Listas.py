#Ejercicio 1
def multiplos_de_4():
    lista = list(range(4, 101, 4))
    print(lista)

multiplos_de_4()

#Ejercicio 2
def mostrar_penultimo(lista):
    print("Penúltimo elemento:", lista[-2])

lista = ["Python", "Pizza", "Viajar", "Música", "Café"]
mostrar_penultimo(lista)

#Ejercicio 3
def agregar_palabras():
    lista_vacia = []
    lista_vacia.append("Hola")
    lista_vacia.append("Mundo")
    lista_vacia.append("Python")
    print(lista_vacia)

agregar_palabras()

#Ejercicio 4
def reemplazar_animales():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"
    print(animales)

reemplazar_animales()

#Ejercicio 5
def analizar_programa():
    lista = [10, 20, 30]
    lista[0] = lista[0] + 5
    lista.append(40)
    print(lista)

#El programa suma 5 al primer elemento y agrega 40 al final.
analizar_programa()

#Ejercicio 6
def lista_con_saltos():
    numeros = list(range(10, 31, 5))
    print("Primeros dos elementos:", numeros[:2])

lista_con_saltos()

#Ejercicio 7
def reemplazar_autos():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1] = "ford"
    autos[2] = "chevrolet"
    print(autos)

reemplazar_autos()

#Ejercicio 8
def agregar_dobles():
    dobles = []
    dobles.append(5 * 2)
    dobles.append(10 * 2)
    dobles.append(15 * 2)
    print(dobles)

agregar_dobles()

#Ejercicio 9
def modificar_compras():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    print(compras)

modificar_compras()

#Ejercicio 10
def crear_lista_anidada():
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print(lista_anidada)

crear_lista_anidada()
