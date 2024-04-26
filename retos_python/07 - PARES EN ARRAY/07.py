# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ENUNCIADO:
# – Genera un array de datos con números enteros o flotantes.
# – Crea un función que reciba el array como parámetro.
# - Dentro de la función crea un nuevo array que almacene los números pares del array original.
# – Retorna el nuevo array con los números pares y muestra el resultado.
# ------------------------------------------------------------------------------------------------------------------------------------------------------

def pares(array):
    pares = []

    for n in array:
        if n % 2 == 0:
            pares.append(n)
    
    return pares

datos = [1,2,3,4,5,6,7,8,9,10]

resultado = pares(datos)
print(f"Los pares son: {resultado}")