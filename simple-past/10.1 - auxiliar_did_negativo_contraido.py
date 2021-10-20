###############################################################################
#
#   Algoritmos criados para fins educativos no projeto Inglês com Python
#   Nos siga no Instagram e Facebook: @inglescompython 
#   Aula 11 - Algoritmo "Auxiliar Did Forma Negativa Contraido"
#
###############################################################################

def auxiliar_did_negativo_contraido(pronome):
    
    negativo = "not"
    negativo_contraido = negativo.replace("o","'")
    
    return pronome + " did"+negativo_contraido

for pronome in pronomes:
    print(auxiliar_did_negativo_contraido(pronome))
