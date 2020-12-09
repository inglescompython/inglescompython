###############################################################################
#
# Algoritmos criados para fins educativos no projeto Inglês com Python
# Nos sigam no Instagram e Facebook @inglescompython 
# Aula 08 = Algoritmo Conjugação Verbal (Negativa)
#
###############################################################################

def conjugacao_verbal_negativo(pronome,verbo):

    terceira_pessoa_singular = ['He','She','It']
    negativo = "not"
    negativo_contraido = negativo.replace("o","'")

    if(pronome in terceira_pessoa_singular):
        return pronome+" does"+negativo_contraido+" "+verbo
    else:
        return pronome+" do"+negativo_contraido+" "+verbo

verbos = ['have','fly','watch']
pronomes = ["I","You","He","She","It","We","You","They"]

for verbo in verbos:
    for pronome in pronomes:
        print(conjugacao_verbal_negativo(pronome,verbo))
