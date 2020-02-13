"""
Created by JAntonioMarin

@author: JAntonioMarin
"""

def calcular(a,b):
    teclado = input("Introduce un tipo de operación")
    if teclado == '+':
        return a + b

def restado(a,b):
    return a - b

def sumar(a,b):
    a = int(input("Operador\n"))
    b = int(input("Operador\n"))
    return a + b

def restar(a,b):
    a = int(input("Operador\n"))
    b = int(input("Operador\n"))
    return a - b

if __name__ == "__main__":
    operacion = print("Vamos a sumar y restar")
    print("\nSumar\n")
    suma = sumar(0,0)
    print("\nRestar\n")
    resta = restar(0,0)
    print("\nEl resultado de la suma es ->", suma)
    print("\nEl resultado de la resta es ->", resta)