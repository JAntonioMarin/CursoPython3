

n = input()
print(n, 'es un tipo', type(n))

# El problema es que si introducimos una cadena dará un error en el casteo
n = int(input())
print(n, 'es un tipo', type(n))

cadenas = input("Por favor introduce una lista de numeros XJ: 1 2 3 4 5: ")
cadenas = cadenas.split(' ')
cadenaEnteros = []
print(cadenas)
for cadena in cadenas:
    cadenaEnteros.append(int(cadena))
print(cadenaEnteros)