import re

regex_format = r'(maria.*|paula.*)@gmail\.com'

regex_format_compile = re.compile(r'(maria.*|paula.*)@gmail\.com')

# Literales -> nave(r'nave espacial')
# Secuencias de escape \n \t \w \\ \' \"
# Metacaracteres
# . ^ $ * + ? { } [ ] \ | ( )
# [ ]
# [as] a o s
# alum[noa] alumno y alumna
# [A-Z]
# [3-6]
# [a-z]
# [0-9-]
# \d = [0-9]
# \D = [^0-9]
# \w [A-Za-z0-9]
# \W [^A-Za-z0-9]
# \s [\t\n\r]
# \S [^\t\n\r\f]
# . Cualquier caracter excepto salto de linea
# ? Caracter de la izquierda puede aparecer una o mas veces
# * Puede pararecer cero o mas veces a la izq
#  + El caracter tiene que aparecer una o mas veces
# {n} El caracter tiene que aparecer n veces
# {n,}tiene que aparecer al menos n veces
# {n,m} tiene que aparecer n veces y al menos como maximo m veces
# ^Permite buscar al inicio de una cadena
#  $ Permitir buscar al final de una cadena
#  \A Buscar al inicio de una cadena
#  \Z Busca al final de una cadena
#  \b Permitir buscar al principio , enmedio de una cadena
#  \B Buscar una cadena que

texto = 'Hola, espero que os esten gustando mis explicaciones. \nIntento dar lo mejor de mi. \nAsi todos podrais aprender de forma autodidacta.'

print(re.sub(r'^Ad', 'D', texto, 0, re.M))
print('\n')
print(re.sub(r'\bIntento', 'D', texto))
print('\n')
print(re.sub(r'an\B', 'D', texto))

regex_numbers = re.compile((r'\d+'))
match = re.match(regex_numbers, "Le dijo que repitiera 20 flexiones")
if match:
    print("Hay coincidencias", match.group())
else:
    print("No hay coincidencias")

match = re.search(regex_numbers, "Ledijo que hiciera 20 flexiones e hizo 30")
print(match)

regex_espacios = re.compile(r'\s+')
cade = "Expresiones\t regulares\naburren"
print(re.split(regex_espacios,cade))


regex_m_a = re.compile(r'[jJ] [aA] {2,} \w+')
lista_coun = re.findall(regex_m_a, cade)

if len(lista_coun) > 0:
    print("Palabras que empiezan por Jj o aA")
    for coicidencia  in lista_coun:
        print("\t"+ coincidencia)
else :
    print("No hay palabras")


regex_email = re.compile(r'[\w\d.+-]+gmail\.com')
texto = "Si quieres mas informacion envia un correo a inventado@gmail.com"
texto_cam = re.sub(regex_email, "email_x", texto)
print(texto_cam)

re.purge()

print(re.A)

patron = r'\w+'

texto = re.compile(patron, re.A)

print(texto)
unicode = re.compile(patron)

print(re.findall(unicode, texto_cam))





