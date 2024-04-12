# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ENUNCIADO:
# - Aprovechamos el código del reto anterior.
# - Como mejora, debemos pedir contínuamente al usurio que nos indíque números hasta adivinarlo.
# - En caso de no adivinar el número, le indicaremos al usuario “DIME OTRO NÚMERO: “.
# - Cuando el usuario adivine el número, le indicaremos “CORRECTO!!” y finalizamos nuestro programa. 

# NOTAS:
# Puedes usar este ejercicio el bucle “while” para resolverlo. PERO CUIDADO CON LOS BUCLES INFINITOS!!
# ------------------------------------------------------------------------------------------------------------------------------------------------------

objetivo = 10

while True:
    numero = input("Dime un numero: ")
    numero = int(numero)

    if numero == objetivo:
        print("CORRECTO!!")
        break
    elif numero != objetivo:
        print("NUMERO INCORRECTO!!")