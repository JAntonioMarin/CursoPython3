inicio = 1
final =1000

def isPrime(num):
    if (num < 1):
        return False
    elif (num == 2):
        return True
    else:
        for i in range(2,num):
            if (num%i == 0):
                return False
        return True

for numero in range(inicio, final):
    if(isPrime(numero)):
        print(numero)