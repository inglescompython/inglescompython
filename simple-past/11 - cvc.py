def regra_cvc_passado(verbo,verifica_silaba):
    
    vogais = ['a','e','i','o','u']
    
    if(verbo[-1] not in vogais and verbo[-3] not in vogais and verbo[-2] in vogais):
        if(verifica_silaba == "s"):
            if(verbo[-1] == "y" and verbo[-2] in vogais or verbo[-1] == "x"): 
                return verbo+"ed"
            else: return verbo+verbo[-1]+"ed"
        else:
            return verbo+"ed"
    else:
        if(verbo[-1] == "e"): 
            return verbo+"d"
        elif(verbo[-1] == "y" and verbo[-2] not in vogais): 
            return verbo[:-1]+"ied"
        else: return verbo+"ed"
