file = open('Assets/prueba.txt', 'r')

print(file.read())

# Asi creamos un fichero
# file = open('Assets/FicheroCreadoDesdeCodigo.txt', 'w')

#  "r+" para abrir y escribir "rb" archivo binario "a" modo añadir

# file = open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=None, opener=None)

file = open("Assets/prueba.txt", "r", encoding="utf-8")

print("El archivo se llama:", file.name)
print("La codificación está en:", file.encoding)
print("El archivo está cerrado?:", file.closed)
file.close()
print("El archivo está cerrado?:", file.closed)

with open('Assets/prueba.txt', "w") as file:
    file.write("Bienvenidos a nuestro curso")
    file.write("\nEspero que os esté gustando")

tema = ["\n Este es el fichero inicial"]
with open('Assets/prueba.txt', "r+") as file:
    file.writelines(tema)

file = open('Assets/prueba.txt', 'r')
print(file.read())
file.close()

file = open('Assets/prueba.txt', 'r')
# print(file.tell())
lineas = file.readlines()
print(file.tell())
print(file.seek(0))
print(file.readlines())
print(file.seek(30, 0))
print(file.readlines())
print(file.seek(0,2))
file = open('Assets/prueba.txt', 'w')
file.write("hola")
file = open('Assets/prueba.txt', 'r')
print(file.seek(0))
print(file.readlines())
file.close()
# print(file.seek(desplazamiento, inicio))
# Esto es el final

with open('Assets/prueba.txt', "w") as file:
    file.write("Este es el fichero inicial\n")

file = open('Assets/prueba.txt', 'r')
print(file.read())
