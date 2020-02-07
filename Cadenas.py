serie = "Hola bienvenido a mi curso"

serie+=" ,gracias por venir"

print(serie)

serie = "Hola, 'Paco'"
print(serie)
serie = "Hola, \'Paco\'"
print(serie)
print(serie[3])
print(serie[-2])

# serie[1] = "A" Esto rompe el principio de inmutabilidad

serie = "Adios" + serie[1:]
print(serie)

serie = "Hola Paco tienes que venir a trabajar"
print(len(serie))
# Cuenta cuantas veces aparece
print(serie.count("Hola"))

print(serie.find("trabajar"))
print(serie.index("trabajar"))

print("Paco" in serie)

serie = "hola bienvenido"
serie = serie.capitalize()
print(serie)

serie = "EsTo Es UN"
serie = serie.lower()
print(serie)

serie = "EsTo Es UN"
serie = serie.swapcase()
print(serie)

# %s Cadena de texto
#  %d numero entero
#  %f numero real
#  %e numero real con exponencial
#  %o octal
#  %x hexadecimal

nombre = "Juan"
edad = 19
cadena = "El chico se llama %s y tiene %d años" % (nombre, edad)
print(cadena)

cadena = "El chico se llama {0} y tiene {1} años".format(nombre,edad)
print(cadena)

cadena = "El chico se llama {nom} y tiene {an} años".format(nom=nombre,an=edad)
print(cadena)

cadena = f"El chico se llama {nombre} y tiene {edad} años"
print(cadena)






