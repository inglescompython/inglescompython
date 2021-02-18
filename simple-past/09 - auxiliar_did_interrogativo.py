###############################################################################
#
#   Algoritmos criados para fins educativos no projeto Inglês com Python
#   Nos siga no Instagram e Facebook: @inglescompython 
#   Aula 09 - Algoritmo "Auxiliar Did Forma Interrogativa"
#
###############################################################################

def auxiliar_did_interrogativo(pronome):
    return "Did " + pronome

pronomes = ['I','You','He','She',
           'It','We','You','They']

for pronome in pronomes:
    print(auxiliar_did_interrogativo(pronome))
