def uso_among_between(quantidade):
    if(quantidade == 2):
        print("Usa-se Between")
    elif(quantidade > 2):
        print("Usa-se Among")
    else:
        print("Quantidade Invalida")

qnt = int(input("Quantos Objetos/Pessoas estão entre voce: "))
uso_among_between(qnt)
