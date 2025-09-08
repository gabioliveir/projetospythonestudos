from time import sleep



def contador(inicio,fim,passo):
    cont = inicio
    print(f"Contagem de {inicio} até o {fim} de {passo} em {passo}")
    if (passo < 0):
        passo *= -1 # *= == variável = variável * número
    if passo == 0:
        passo =1
 
    if inicio < fim:
        while cont <= fim:
            print(f"{cont}",end=" ",flush=True) #flush pra forçar que o resultado apareça imediatamente
            sleep(0.5)
            cont += passo
        print("FIM <3")
    else :
        while cont >= fim:
            print(f"{cont}",end=" ",flush=True)
            sleep(0.5)
            cont -= passo
        print("FIM <3")

print("-Contador-")
contador(1,10,1)
contador(10,0,2)
print(f"Sua vez de personalizar sua contagem!")
nome = input("Digite sua nome: ")
i = int(input("Início: "))
f = int(input("Fim:    "))
p = int(input("Passo:  "))
contador(i,f,p)
print(f"Contagem feita por {nome}.")




