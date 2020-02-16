# Excepciones básicas

# try:
#     lista = [1,2,3,4,5,6,7,8,9,10]
#     print(lista)
#     while True:
#         print('Elemento a borrar', lista[-1])
#         assert len(lista) > 2
#         lista.pop()
#         print(lista)
# except AssertionError:
#     print('Error al intentar borrar el ultimo elemento')
#     print('La lista no contiene 3 elementos')

# class MiExcepcion(Exception):
#     def __init__(self, valor):
#         self.valor = valor
#     def __str__(self):
#         return "Error: " + str(self.valor)
#
# try:
#     fin =False
#     while not fin:
#         entrada = input("Introduzca c para continuar o f para finalizar:")
#         if entrada != "f" and entrada != "c":
#             raise MiExcepcion(entrada + " no es una valor valido")
#         elif entrada == "f":
#             fin = True
# except MiExcepcion as e:
#     print(e)

# def fib(num):
#     if num < 2:
#         return num
#     else:
#         return fib(num - 1) + fib(num - 2)
#
#
# resultado = fib(0)
# assert resultado == 0
#
# resultado = fib(1)
# assert resultado == 1
#
# resultado = fib(2)
# assert resultado == 1


class InvalidNameException(Exception):
    def __init__(ins, valor):
        ins.valor = valor

    def __str__(ins):
        return " Erro " + str(ins.valor)

nombres = ['Juan Jose', 'J', 'Jo', 'Alfredo']

for n in nombres:
    try:
        if len(n) < 3:
            raise InvalidNameException(n)
        print(n)
    except InvalidNameException:
        pass