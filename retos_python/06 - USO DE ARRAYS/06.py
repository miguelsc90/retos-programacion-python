# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ENUNCIADO:
# - Necesitamos crear un array de datos con números, pueden ser tanto enteros como flotantes. 
# - Necesitamos 2 funciones, una que realice la suma de todos los valores del array y otra que multiplique todos los datos. 
# - A cada función debemos pasarle nuestro array de datos y retorna el resultado correspondiente. 

# NOTAS:
# Usa el bucle FOR para resolver este ejercicio.
# ------------------------------------------------------------------------------------------------------------------------------------------------------

def suma(array_datos):
    resultado_suma = 0

    for n in array_datos:
        resultado_suma = resultado_suma + n

    return resultado_suma

def multiplicacion(array_datos):
    resultado_multi = 1

    for n in array_datos:
        resultado_multi = resultado_multi * n

    return resultado_multi

datos = [1,20,32,5,44]
print(f"El resultado de la suma: {suma(datos)}")
print(f"El resultado de la multiplicacion: {multiplicacion(datos)}")