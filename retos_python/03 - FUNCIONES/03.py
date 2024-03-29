# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ENUNCIADO:
# – Vamos a crear un programa con 4 funciones, una que se llame suma, otra resta, otra multiplicación y por último división.
# – Cada una de estas funciones debe recibir 2 valores, que serán los números con los que realizaremos los cálculos.
# – Debemos realizar el cálculo matemático correspondiente a cada función.
# – En cada función debemos retornar el resultado.

# DIFICULTAD EXTRA:
# – Usa la función “input()” para pedir al usuario los 2 números con los que vamos a realizar los cálculos.
# ------------------------------------------------------------------------------------------------------------------------------------------------------

def suma(n1, n2):

    resultado = n1 + n2
    return resultado

def resta(n1, n2):
    
    resultado = n1 - n2
    return resultado

def multiplicacion(n1, n2):

    resultado = n1 * n2
    return resultado

def division(n1, n2):

    resultado = n1 / n2
    return resultado

n1 = input("Dime el primer numero: ")
n2 = input("Dime el segundo numero: ")
n1 = int(n1)
n2 = int(n2)

resultado_suma = suma(n1,n2)
print(f"El resultado de la suma: {resultado_suma}")

resultado_resta = resta(n1,n2)
print(f"El resultado de la resta: {resultado_resta}")

resultado_multiplicacion = multiplicacion(n1, n2)
print(f"El resultado de la multiplicacion: {resultado_multiplicacion}")

resultado_division = division(n1, n2)
print(f"El resultado de la division: {resultado_division}")