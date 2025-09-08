import random
import time
numeros = list()


def sorteio(lista):
    print("Sorteando números...")
    for cont in range(0,5):
        lista.append(random.randint(1,10))
    for i in numeros:
        print(f"{i}", end=" ", flush=True)
        time.sleep(0.5)
    
def somarPar(lista):
    print("Somando os números pares...")
    soma = 0
    pares = []
    for n in lista:
        if (n % 2 == 0):
            print(f"O número {n} é par")
            pares.append(n)
            soma += n
    print(f"Valores pares : {pares}")
    print(f"Valor total da soma: {soma}")
        


sorteio(numeros)
print(f"Números sorteados: {numeros}")
somarPar(numeros)





