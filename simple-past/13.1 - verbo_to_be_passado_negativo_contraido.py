
###############################################################################
#
#   Algoritmos criados para fins educativos no projeto Inglês com Python
#   Nos siga no Instagram e Facebook: @inglescompython 
#   Aula 12 - Algoritmo " Verbo To Be Passado Negativo Contraido"
#
###############################################################################

def verbo_to_be_passado_negativo_contraido(pronome):
    
    singular = ["I","He","She","It"]

    negativo_contraido = "not".replace("o","'")

    if(pronome in singular):
        return pronome+" was"+negativo_contraido
    else:
        return pronome+" were"+negativo_contraido

pronomes = ["I","You","He","She","It","We","You","They"]

for pronome in pronomes:
    print(verbo_to_be_passado_negativo_contraido(pronome))

