
###############################################################################
#
#   Algoritmos criados para fins educativos no projeto Inglês com Python
#   Nos siga no Instagram e Facebook: @inglescompython 
#   Aula 11.1 - Algoritmo "Conjugação Verbal Passado Simples"
#
###############################################################################

from cvc import regra_cvc_passado

def conjugacao_verbal_passado_simples(pronome,verbo,verifica_silaba):
    return pronome + " "+regra_cvc_passado(verbo,verifica_silaba)

verbos = ["stop","visit","play","study","relax"]
pronomes = ["I","You","He","She","It","You","We","They"]

for verbo in verbos:

    verifica = input("Ultima silaba do verbo '%s' é tonica? S/N?: "%(verbo))
    
    for pronome in pronomes:
        print(conjugacao_verbal_passado_simples(pronome,verbo,verifica))
