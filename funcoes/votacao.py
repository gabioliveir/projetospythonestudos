

def voto(ano_nascimento):
    from datetime import date #economia de memória
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print("VERIFICAÇÃO DE VOTO")
    if idade < 16:
        return f"Com {idade} anos: NÃO É POSSÍVEL VOTAR"
    elif (16 <= idade <18) or (idade > 65):
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"

nasc = int(input("Informe o ano que vc nasceu: "))
print(voto(nasc))


    