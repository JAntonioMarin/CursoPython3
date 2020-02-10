d = ['Juan', 'Mario']

print(d.pop(1))

#  texto -> entero -> realiza una busqueda -> entero -> texto

precioCurso = {'python': 1.74, 'CyC++': 3.00}
# o
precioCurso2 = dict(python=1.00, python2=5.00)
print(precioCurso2)

d1 = dict(zip(['python', 'Java', 'C'], [1.74, 2.30, 5.00]))
print(d1)

d2 = dict([('python', 1.74), ('Java', 2.00)])
print(d2)

d1['Antonio'] = 0
print(d1)

precioCurso['Base de datos'] = 10.00
print(precioCurso)
del precioCurso['CyC++']
print(precioCurso)

personas = {'Nombre': 'Jose', 'Profesion': 'Ingeniero'}
for i in personas:
    print(personas[i])

for e in personas.values():
    print(e)

for p in personas:
    print(p, '->', personas[p])

print(personas.get('Nombre'))
print(personas.get('No existe'))
precios = precioCurso.copy()
print(precios)
precios.update(python=2.00)
print(precios)

texto = 'hola, como esta?, espero que estes disfrutando el curso'
apariciones = {}
for l in texto:
    apariciones[l] = apariciones.get(l, 0) + 1
print(apariciones)
