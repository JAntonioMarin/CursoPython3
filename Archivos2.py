import pickle
from os import remove

# Archivos binarios
cursos = {"sonia":[("Curso de python3", "No visto")], "ivan":[("Curso de c++", "Visto")]}

with open("Assets/info.p", "wb") as file:
    pickle.dump(cursos, file)

del cursos

with open("Assets/info.p", "rb") as file:
    cursosExtraidos = pickle.load(file)

print(cursosExtraidos)

file.close()
remove("Assets/info.p")

# Programa que guarda la suma
# with open("Assets/archivo.txt", "w") as file:
#     print("Introduce un primer valor")
#     n1= input()
#     print("Introduce un segundo valor")
#     n2 = input()
#     suma = n1 + n2
#     file.write("El resultado de la operacion es: ")
#     file.write(suma)
