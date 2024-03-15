# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ENUNCIADO:
# – Necesitamos crear 2 variables, de forma que en una de ella guardemos nuestro nombre y en la otra nuestro apellido.
# – Debemos mostrar por terminal el siguiente texto: “Hola, mundo!!”
# – Seguido de este “Hola, mundo!!”, en una nueva linea, mostraremos en terminal nuestro nombre completo usando las 2 variables que hemos creado al inicio.
# ------------------------------------------------------------------------------------------------------------------------------------------------------

nombre = "Miguel"
apellido = "Sanchez"

print("Hola, mundo!!")
print(nombre, apellido)
print(f"Hola {nombre} {apellido}, que tal?")
print("Hola " + nombre + " " + apellido + ", que tal?")