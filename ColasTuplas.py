from collections import deque

# Colas
cola = deque()

for i in range(5):
    cliente = 'cliente' + str(i+1)
    cola.append(cliente)
    print('Cola', cola)

while len(cola) > 0:
    print('Sale: ', cola.popleft())
    print('Quedan:', cola)



jubilados = [2,20,30,12,50,60,80,66]
mayores = [x for x in jubilados if x >=60]
print('Hay', len(mayores), 'Jubilados')
print('Edades de los jubilados:', mayores)

# Tuplas
t =  3,2,1, 'elemento'
print(t[3])
t = t[0], 23, t[2], 32
print(t)

t2 = tuple('hola paco')
print(t2)

coordenadas = 3, 2.4, 5.4
x, y, z = coordenadas
print(x,y,z)