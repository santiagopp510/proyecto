# ============================================
# GUÍA Y EJERCICIOS - For y List Comprehension
# ============================================

# --------------------------------------------
# RECORDATORIO: ¿QUÉ ES UN FOR?
# Recorre una lista, elemento por elemento, y 
# repite un bloque de código para cada uno
# --------------------------------------------






# ============================================
# NIVEL BÁSICO
# ============================================

# Ejercicio 1: Recorre la lista "colores" e imprime cada uno 
# con el formato "Color: nombre"
colores = ["rojo", "azul", "verde", "amarillo"]
for color in colores:
    print (f"color:  {color}")
print ("=========================")

# Ejercicio 2: Recorre la lista "precios" y calcula el total 
# (suma de todos)
precios = [15000, 22000, 8000, 35000]
total = 0
for precio in precios:
    total = total + precio
print(total)


# Ejercicio 3: Recorre la lista "edades" y cuenta cuántas 
# personas son mayores de edad (18 o más)
edades = [15, 22, 17, 30, 12, 19]
mayores = 0
menores = 0
for edad in edades:
    if edad >= 18:

        mayores += 1

    else: menores +=1 

print(f"{mayores} son mayores")
print(f"{menores} son menores")

print ("=========================")




# Ejercicio 4: Recorre la lista "notas" y encuentra la nota 
# más alta SIN usar la función max()
notas = [3.5, 4.2, 2.8, 4.8, 3.9]
nota_mayor = notas[0]

for nota in notas:
    if nota > nota_mayor:
        nota_mayor = nota

print("La nota más alta es:", nota_mayor)

# Ejercicio 5: Crea una nueva lista "dobles" que contenga cada 
# número de "numeros_base" multiplicado por 2
numeros_base = [1, 2, 3, 4, 5]


# ============================================
# NIVEL INTERMEDIO
# ============================================

# Ejercicio 6: Cuenta cuántas veces aparece el valor "manzana" 
# en la lista "frutas_repetidas"
frutas_repetidas = ["manzana", "pera", "manzana", "uva", "manzana"]


# Ejercicio 7: Separa la lista "numeros_mixtos" en dos listas 
# nuevas: "pares" e "impares"
numeros_mixtos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Ejercicio 8: Invierte el orden de la lista "orden_original"
# Pista: pueden usar .reverse(), slicing [::-1], o investigar 
# la función .insert() para hacerlo manualmente
orden_original = ["a", "b", "c", "d", "e"]


# Ejercicio 9: Combina "lista_a" y "lista_b" en una sola lista 
# nueva llamada "combinada"
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]


# ============================================
# NIVEL AVANZADO / RETO
# ============================================

# Ejercicio 10: Encuentra los valores que están repetidos en 
# la lista "con_duplicados" (que aparezcan más de una vez)
con_duplicados = [1, 2, 3, 2, 4, 5, 1, 6]


# --------------------------------------------
# LIST COMPREHENSION (forma corta de escribir un for)
# --------------------------------------------

numeros = [1, 2, 3, 4, 5]

cuadrados_largo = []
for n in numeros:
    cuadrados_largo.append(n**2)

cuadrados_corto = [n**2 for n in numeros]

print(cuadrados_largo)
print(cuadrados_corto)


# Ejercicio 11: Usando list comprehension, crea una lista 
# "positivos" que contenga solo los números mayores a 0 
# de la lista "mixtos"
mixtos = [-5, 3, -2, 8, -1, 10, 0]


# Ejercicio 12 (reto): Usando list comprehension, crea una 
# lista con el triple de cada número, pero SOLO de los 
# números pares de "numeros_variados"