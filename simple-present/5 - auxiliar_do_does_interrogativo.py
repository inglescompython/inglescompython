# -*- coding: utf-8 -*-
###############################################################################
#
# Algoritmos criados para fins educativos no projeto Inglês com Python
# Nos sigam no Instagram e Facebook @inglescompython 
# Aula 05 = Algoritmo Uso do Auxiliar "Do" e "Does" Interrogativo
#
###############################################################################

def auxiliar_do_does_interrogativo(pronome):

    terceira_pessoa_singular = ['He','She','It']

    if(pronome in terceira_pessoa_singular):
        return "Does "+pronome+" ..?"
    else:
        return "Do "+pronome+" ...?"

todos_pronomes = ["I","You","He","She","It","We","You","They"]

for pronome in todos_pronomes:
    print(auxiliar_do_does_interrogativo(pronome))
