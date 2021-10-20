
###############################################################################
#
#   Algoritmos criados para fins educativos no projeto Inglês com Python
#   Nos siga no Instagram e Facebook: @inglescompython 
#   Aula 13 - Algoritmo " Verbo To Be Passado Negativo"
#
###############################################################################

def verbo_to_be_passado_negativo(pronome):
    
    singular = ["I","He","She","It"]

    if(pronome in singular):
        return pronome+" was not"
    else:
        return pronome+" were not"

pronomes = ["I","You","He","She","It","We","You","They"]

for pronome in pronomes:
    print(verbo_to_be_passado_negativo(pronome))
