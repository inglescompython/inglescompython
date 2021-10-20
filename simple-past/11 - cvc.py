###############################################################################
#
#   Algoritmos criados para fins educativos no projeto Inglês com Python
#   Nos siga no Instagram e Facebook: @inglescompython 
#   Aula 11 - Algoritmo "Regra CVC - Consoante Vogal Consoante"
#
###############################################################################

def regra_cvc_passado(verbo,verifica_silaba):
    
    vogais = ['a','e','i','o','u']
    
    if(verbo[-1] not in vogais and verbo[-3] not in vogais and verbo[-2] in vogais):
        ## Se a ultima letra for consoante, a penultima for vogal e a antepenultima for consoante entra na regra:
        
        if(verifica_silaba == "s"):
            ## Verifica se a ultima silaba é tonica
            if(verbo[-1] == "y" and verbo[-2] in vogais or verbo[-1] == "x"): 
                
                ## Se a ultima letra for "Y" e a antepenultima for vogal ou a ultima for "X" então usa-se "ed" no final
                return verbo+"ed"
            else:
                
                return verbo+verbo[-1]+"ed"
        else:
            ## Se a palavra entra na regra CVC e a ultima silaba não for tonica, só se concatena "ed" no final da palavra
            return verbo+"ed"
    else:
        if(verbo[-1] == "e"):
            ## Se a ultima letra terminar com "e" usa-se "d" no fim da palavra
            return verbo+"d"
        
        elif(verbo[-1] == "y" and verbo[-2] not in vogais): 
            ## Se a ultima letra terminar com "y" e a antepenultima letra for consoante, 
            ## remove a ultima letra e concatena "ied" no final da palavra
            return verbo[:-1]+"ied"
        
        else: 
            ## Em outros casos que a palavra não seguir a regra CVC só se concatena "ed" 
            ## no final da palavra
            return verbo+"ed"
