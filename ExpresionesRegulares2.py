import re

regex_fecha_valida = re.compile('''
    ^
    (0[1-9]|[12][0-9]|3[01])
    /
    (0[1-9]|1[012])
    /
    (19\d\d|20[0-1] [0-9])
    $'''
    ,re.X
)

lista_fecha= ['22/03/1985', '0y/12/2000', '15/04/0905', '12/08/2019']

for fecha in lista_fecha:
    if re.search(regex_fecha_valida, fecha):
        print(fecha, "es una fecha valida")
    else:
        print(fecha, "no es valida")

telefono = re.compile(r'\d{3}-\d{3}-\d{3}')

texto = '''
Cliente : Juan - Contacto : 678-098-090\n
Cliente : Pepe - Contacto : 685-654-312\n
Cliente : Maria - Contacto : 645-687-622\n
Cliente : Zapatero - Contacto : 656-456-456\n
'''
# Por ejemplo para encriptar telefonos
texto_reemplazado = re.sub(telefono, "6XXXXXXXX", texto)
print(texto_reemplazado)