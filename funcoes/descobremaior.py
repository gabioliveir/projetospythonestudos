from time import sleep
def maior( * num):
    cont = maior = 0
    print("Analisando dados.. ")
    for valor in num:
        print(f"{valor}", end=" ", flush= True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else :
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {len(num)} valores ao todo.Sendo eles: {num}")
    print(f"O maior valor informado foi {maior}.")
        

maior(2,9,4,6,8,1)
maior(-1,0-3)
