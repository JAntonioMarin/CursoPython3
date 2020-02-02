# Estos son algunos ejemplos del curso, pero esto es muy sencillo con respecto a java es basicamente igual
print("Suma de 2 + 5")
x = 2
y = 5
z = x + y
print(z)

print("Otra forma de hacer la suma")
z = 0
z += x
z += y
print(z)

print("2== (4/2)?")
print(2 == (4 / 2))
print("2!= (4/2)?")
print(2 != (4 / 2))
print("2<=4?")
print(2 <= 4)
print("2>=4?")
print(2 >= 4)

print("Conjuntos:")
a = 1
b = {1, 2, 3, 4, 5}
print("Esta a= " + str(a) + " en b= " + str(b) + "? = " + str(a in b))
a = 6
print("Esta a= " + str(a) + " en b= " + str(b) + "? = " + str(a in b))

a= [6,7,8]
b= [6,7,8]

print("A= "+str(a)+ " is B=" +str(b)+ "? = "+ str(a is b) )
print("A= "+str(a)+ " is not B=" +str(b)+ "? = "+ str(a is not b))