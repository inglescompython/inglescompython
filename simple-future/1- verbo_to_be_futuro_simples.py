###############################################################################
#
#   Algoritmos criados para fins educativos no projeto Inglês com Python
#   Nos siga no Instagram e Facebook: @inglescompython 
#   Aula 14 - Algoritmo "Verbo To Be"
#
###############################################################################

def verbo_to_be_futuro_simples(pronome):
  return pronome + " will" + " be"
  
pronomes = ["I", "You", "He", "She", 
           "It", "We", "You", "They"]

for pronome in pronomes:
  print(verbo_to_be_futuro_simples(pronome))
