anioNacimiento = input("Por favor indica tu año de nacimiento: ")
anioNacimiento = int(anioNacimiento)
anioNacimientoHijo = input("En que año nació tu hijo: ")
anioNacimientoHijo = int(anioNacimientoHijo)
anioActual = 2020
edadActual = anioActual - anioNacimiento
print("Tu edad actual es de", edadActual, "años")
edadHijo = anioActual - anioNacimientoHijo
edadHijoDobleDeMiEdad = edadHijo + edadActual
print("Tu hijo que ahora tiene", edadHijo, "años, cuando tu tengas el doble de edad el tendrá", edadHijoDobleDeMiEdad)
