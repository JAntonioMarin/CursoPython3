
## Función de suma
def sumar(a,b):
    '''Esta funcion realiza sumas'''
    return a+b

def menoria(a,b):
    '''Funcion que calcular cual es el numero menor de los dos'''
    if a < b:
        return a
    return b

def ampliar(lista):
    '''Amplia una lista con 4 , 5 y 6 como elementos'''
    lista +=[4,5,6]

def hola(curso='python'):
    '''Esta funcion da la bienvenida al curso que se le pasa por parámetro'''
    print('Hola bienvenido al curso de', curso)

def numeros(numero, enteros=[]):
    enteros.append(numero)
    return enteros

def sumatoria(a=5, b=10, c=1):
    return a+b+c

def extraer(valores, comp):
    a = valores[0]
    for x in valores[1:]:
        if comp(x,a):
            a = x
    return a

def mayor(a,b):
    return a>b
def menor(a,b):
    return a<b

def mayorYield(a,b):
    if a<b:
        yield b

def ruta(origen, final, *ciclistas, **detalles):
    print(f'Saldremos desde {origen}, y llegaremos hasta {final}, iremos:')
    for ciclista in ciclistas:
        print(ciclista)
        print('comeremos en: ')
        for k in detalles:
            print(k, ':', detalles[k])

print(sumar(5,3))
print(sumar.__doc__)

print(menoria(4,9))

l = [1,2,3]
print(l)
ampliar(l)
print(l)

hola()
hola("cocina")

print(numeros('20'))

print(sumatoria())

print(extraer([2,40,12,45,76,23,12], menor))
print(extraer([2,40,12,45,76,23,12], mayor))

ruta('via verde', 'tibi', 'Juan', 'Javier', comer='En el dogma', bebida = 'Cerveza', comida='Chawarma')

for m in mayorYield(1,2):
    print(m)





