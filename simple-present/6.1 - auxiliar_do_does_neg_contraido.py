# -*- coding: utf-8 -*-
###############################################################################
#
# Algoritmos criados para fins educativos no projeto Inglês com Python
# Nos sigam no Instagram e Facebook @inglescompython 
# Aula 06.1 = Algoritmo Uso do Auxiliar "Do" e "Does" Negativo Contraido
#
###############################################################################

def auxiliar_do_does_negativo_contraido(verbo):

    terceira_pessoa_singular =  ['He','She','It']
    negativo = "not"
    negativo_contraido = negativo.replace("o","'")

    #Substitui no 'Not' o 'o' por 'aspa simples' => n[o]t => n[']t
    # e concatena na frente do Auxiliar: Do+n't => Don't, Does+n't => Doesn't

    if(pronome in terceira_pessoa_singular):
        return pronome+' does'+negativo_contraido
    else:
        return pronome+' do'+negativo_contraido
	
todos_pronomes = ['I','You','He','She',
                 'It','We','You','They']

for pronome in todos_pronomes:
    print(auxiliar_do_does_negativo_contraido(pronome))
