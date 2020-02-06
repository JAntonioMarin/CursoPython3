numero = 2
print("El numero indicado es: {num}".format(num=numero))
cadena = "Hola bienvenidos a el curso"
print(cadena.ljust(50), cadena.center(50), cadena.rjust(50), sep='\n')

lista = [1, 2, 3, 4]
print(lista)
listaRange = list(range(5))
print(listaRange)
print(listaRange[0:3])

listaCadena = list('Cadena!!')
print(listaCadena)
print(listaCadena[0:5])
del listaCadena[0]
print(listaCadena)
listaCadena.extend('Pacoo')
print(listaCadena)
listaCadena.append(5)
print(listaCadena)
listaCadena.insert(len(listaCadena),'sa')
print(listaCadena)

listaCadena.remove('sa')
print(listaCadena)
valor = listaCadena.pop()
print(listaCadena)
print(valor)
listaCadena.clear()
print(listaCadena)
listaCadena = list(range(10))
# 1 es que se encuentra
print(listaCadena.count(4))
# 0 es que no se encuentra
print(listaCadena.count(20))

listaCadena = list('Paco')
listaCadena.reverse()
print(listaCadena)
listaCadenaCopia = listaCadena.copy()
listaCadenaCopia.sort()
print(listaCadena)
print(listaCadenaCopia)

# Para que una lista funcione como una pila usamos append y pop
acciones = []
# Guardamos la acciones del usuario
acciones.append("Escribir por teclado")
acciones.append("Mueve el ratón")
# Listamos contenido
print(acciones)
print("sacamos", acciones.pop())
acciones.append(("Mueve la pantalla"))
print(acciones)



