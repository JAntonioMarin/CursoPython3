def num_max(enteros):
    valorInicial = enteros[0]
    valorMaximo = valorInicial
    for valor in range (1, len(enteros)):
        if(valorMaximo<enteros[valor]):
            valorMaximo = enteros[valor]
        elif(valorMaximo==enteros[valor]):
            valorInicial = valorMaximo
    if(valorInicial==valorMaximo):
        print("Existen 2 o mas máximos")
    else:
        print("El valor maximo es", valorMaximo)

enteros = input("Por favor introduce enteros separados por espacio:")
cadenas = enteros.split(' ')
cadenaEnteros = []
for cadena in cadenas:
    cadenaEnteros.append(int(cadena))
if(len(cadenaEnteros)>1):
    num_max(cadenaEnteros)
else:
    print("El valor maximo es", cadenaEnteros[0])

