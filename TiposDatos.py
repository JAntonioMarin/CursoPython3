a = 10
print(id(a))
print(a.bit_length())

az = "Hola"
print(id(az))
print(len(az))

precio = None
print(precio)

pi = 3.141592
print(pi)

numeroComplejo = 3 + 5j
print(numeroComplejo)

# Tupla
prod = ("Uvas", 1.00)
print(prod)

# Lista
precios = [2, 3, 5.0]
print(precios)
print(len(precios))

# Lista
conjunto = {"hola", "adios", "repeticion"}
print(conjunto)

# Diccionario
d = {"Precio": 34}
print(d)
print(type(d))

b = float(2)
print(type(b))


def suma(a, b):
    print(a + b)


# Tienen que ser del mismo tipo
suma(3, 4)
suma("pepe", "juan")
suma("suma", str(3))

saldoInicial = 3000
salarioMensual = 1100
gastosFijosMensuales = 435
saldoFinal = 6000
gastosExtra = saldoInicial + salarioMensual * 12 - gastosFijosMensuales * 12 - saldoFinal
gastosExtraMensuales = gastosExtra / 12

print(gastosExtraMensuales)

efectivo = 50
precioCamisa = 35
descuento = 10
precioFinal = precioCamisa - (precioCamisa * descuento / 100)
efectivoFinal = efectivo - precioFinal
print(efectivoFinal)
