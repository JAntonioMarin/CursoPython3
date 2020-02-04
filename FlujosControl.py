# If else
nacionalidad = " "
respuesta =  " "

if nacionalidad == "española":
    respuesta = "Bonito pais"
else:
    respuesta = "Y de donde eres"

print(respuesta)

# If else if
correcto = True
incorrecto = False
edad = -18

if edad == 18:
    print(correcto)
    print("Puede comprar")
elif edad > 0 and edad <18:
    print(incorrecto)
else:
    print("No tienes edad?")

# Bucles while
peso = -20

while peso <60:
    if peso <60 and peso >= 50:
        print("Pesa menos de 60 kilos")
    elif peso <50 and peso >0:
        print("Pesas menos de 50 kilos")
    else:
        print("Cuanto pesas?")
    peso+=10

# Bucles for
a = 4
f= 1
for f in range(2, a):
    a= a*f
print(a)

sabores = ['fresa', 'vainilla', 'chocolate']
s1 = ['chocolate']
s2 = ['vainilla']
for s1 in sabores:
    for s2 in sabores:
        print('Helado de', s1, 'con', s2)


sabores = ['fresa', 'vainilla', 'chocolate']
s1 = ['chocolate']
s2 = ['vainilla']
for s1 in range (len(sabores)):
    for s2 in range (s1+1, len(sabores)):
        print('Helado de', s1, 'con', s2)

num = 811
test = 'es primo'

for div in range(2, num):
    if num % div == 0:
        test= 'no es primo'
        break
print(num, test)


for div in range(2, 23):
    pass
    print("Aqui no llega")


listaNombres = ['Pedro', 'Ramon', 'Maria', 'Jose']
for n in listaNombres:
    if n == 'Maria':
        print(n, 'encontrada')
    else:
        print(n, 'no es Maria')

