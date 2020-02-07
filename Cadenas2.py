cadena = input("Introduce una cadena a comparar: ")

cadena = cadena.lower()

if cadena[0] == cadena[-1]:
    caracter_distintos = len(cadena) - cadena.count(cadena[0])
    mensaje = f"La cadena introducida tiene {caracter_distintos} caracteres distintos a los de inicio y fin"
else:
    caracteres_iguales_inicio = cadena.count(cadena[0]) - 1
    caracteres_iguales_final = cadena.count(cadena[-1]) -1
    caracteres_iguales_total = caracteres_iguales_inicio - caracteres_iguales_final
    mensaje = f"La cadena introducida tiene {caracteres_iguales_total} caracteres iguales"
print(mensaje)