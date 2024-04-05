# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ENUNCIADO:
# - Vamos a crear el juego de adivinar un número
# - Guardaremos en una variable el número objetivo.
# - Con la función "input()" pedimos al usuario un número.
# - Si el número indicado es correcto, indicamos por terminal "CORRECTO!!", si no es el número correcto indicamos "NÚMERO INCORRECTO!!".

# NOTAS:
# Usa en este ejercicio las sentencias "if - else" para comprobar si el número es correcto.
# ------------------------------------------------------------------------------------------------------------------------------------------------------

objetivo = 10

numero = input("Dime un numero: ")
numero = int(numero)

if numero == objetivo:
    print("CORRECTO!!")
elif numero != objetivo:
    print("NUMERO INCORRECTO!!")