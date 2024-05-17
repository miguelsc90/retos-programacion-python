# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ENUNCIADO:
# – Escribe una función que tome una lista de palabras como entrada.
# – Itera sobre cada palabra de la lista y busca cual es la más larga.
# – Retorna la palabra más larga.
# – Si hay dos o más palabras que son las más largas y tienen la misma longitud, la función debe devolver la primera palabra encontrada.
# ------------------------------------------------------------------------------------------------------------------------------------------------------

def palabraLarga(lista_palabras):
    palabraMasLarga = ""
    tamanoPalabra = 0

    for palabra in lista_palabras:
        if len(palabra) > tamanoPalabra:
            palabraMasLarga = palabra
            tamanoPalabra = len(palabra)

    return palabraMasLarga

listaPalabras = ["perro", "elefanta", "elefante", "pajaro", "gato"]
resultado = palabraLarga(listaPalabras)
print(f"La palabra mas larga es: {resultado}")