# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ENUNCIADO
# – Vamos a crear un programa en el que podamos ver los principales tipos de variables que existen en Python (enteros, string, listas, ….).
# – Asigna valores a estas variables y muestra sus resultados por terminal e intenta mostrar también el tipo de dato que es.
# Para realizar este ejercicio os recomendamos que busqueis información en la documentación oficial de Python a través de este enlace.
# También podeis buscar este información el la plataforma que os resulta más comoda.
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# ---> NUMERICOS <---
# Enteros
num_entero = 25
print(f"Numero entero: {num_entero}")
print(f"Tipo: {type(num_entero)}")

print()

# Numero flotante
num_float = 30.5
#num_float = float(num_float)
print(f"Numero flotante: {num_float}")
print(f"Tipo: {type(num_float)}")

print()

# Numero complejo
num_complejo = 3j
print(f"Numero complejo: {num_complejo}")
print(f"Tipo: {type(num_complejo)}")

print()

# ---> SECUENCIAS <---
# String
secuencia_string = "Hola Mundo!"
print(f"Secuencia: {secuencia_string}")
print(f"Tipo: {type(secuencia_string)}")

print()

# Lista
secuencia_lista = ["Miguel", 25, "Juan", 34]
print(f"Lista: {secuencia_lista}")
print(f"Tipo: {type(secuencia_lista)}")
secuencia_lista[1] = 26
print(f"Lista: {secuencia_lista}")
secuencia_lista[2] = "Luis"
print(f"Lista: {secuencia_lista}")
print(f"Nombre: {secuencia_lista[2]}")

print()

# Tupla
secuencia_tupla = ("Laura", 24, "Paco", 55)
print(f"Tupla: {secuencia_tupla}")
print(f"Tipo: {type(secuencia_tupla)}")
#secuencia_tupla(1) == 25
#print(f"Tupla: {secuencia_tupla}")

print()

# Diccionario
secuencia_diccionario = {
    "Nombre": "Mazda",
    "Modelo": "MX-5",
    "Fabricacion": 1998
}
print(f"Diccionario: {secuencia_diccionario}")
print(f"Tipo: {type(secuencia_diccionario)}")
secuencia_diccionario["Fabricacion"] = 2005
print(f"Diccionario: {secuencia_diccionario}")

print()

# ---> BOOLEANO <---
# True
booleano_true = True
print(f"Bool: {booleano_true}")
print(f"Tipo: {type(booleano_true)}")

# False
booleano_false = False
print(f"Bool: {booleano_false}")
print(f"Tipo: {type(booleano_false)}")