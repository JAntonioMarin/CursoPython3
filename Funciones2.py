# Lambdas

suma = lambda x,y: x+y
print(suma(7,8))
cuadrado = lambda x: x**2
print(cuadrado(4))
mayor = lambda x,y: x if x > y else y
print(mayor(8,5))

def factorial(x):
    if x==0:
        return 1
    return x * factorial(x-1)

print(factorial(4))

# Algoritmo de la burbuja

def ordenar(l):
    def intercambiar(l,a,b):
        x= l[a]
        l[a] = l[b]
        l[b] = x
    for i in range(len(l)-1,1,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                intercambiar(l, j, j+1)

l = [12,3,45,76,4,65,98,34,6,23]
print(l)
ordenar(l)
print(l)