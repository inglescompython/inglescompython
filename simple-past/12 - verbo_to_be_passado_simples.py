
###############################################################################
#
#   Algoritmos criados para fins educativos no projeto Inglês com Python
#   Nos siga no Instagram e Facebook: @inglescompython 
#   Aula 12 - Algoritmo " Verbo To Be Passado Simples"
#
###############################################################################

def verbo_to_be_passado_simples(pronome):

    singular = ["I","He","She","It"]
    plural = ["You","We","They"]

    #You é tanto singular como plural, porem se
    #usa o verbo do plural em ambos. You were

    if(pronome in singular):
        return pronome+" was"
    elif(pronome in plural):
        return pronome+" were"

pronomes = ["I","You","He","She","It","We","You","They"]

for pronome in pronomes:
    print(verbo_to_be_passado_simples(pronome))
