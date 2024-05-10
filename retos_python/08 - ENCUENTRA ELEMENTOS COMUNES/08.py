# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ENUNCIADO:
# – Genera dos arrays de datos, uno con números enteros y otro con números flotantes.
# – Crea una función que reciba ambos arrays como parámetros.
# - Dentro de la función, encuentra los elementos comunes entre los dos arrays y almacénalos en un nuevo array.
# - Retorna el nuevo array con los elementos comunes y muestra el resultado.
# ------------------------------------------------------------------------------------------------------------------------------------------------------

def elementosComunes(nEntero, nFlotantes):
    nComunes = []

    for numero in nFlotantes:
        if numero in nEntero:
            nComunes.append(numero)

    return nComunes

nEnteros = [1,2,3,4,5,6,7]
nFlotantes = [1.4,4.7,2.1,10.3,6.0,34.3,7.0,4.0]

resultado = elementosComunes(nEnteros, nFlotantes)
print(f"Los comunes son: {resultado}")