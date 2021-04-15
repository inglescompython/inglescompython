###############################################################################
#
#   Algoritmos criados para fins educativos no projeto Inglês com Python
#   Nos siga no Instagram e Facebook: @inglescompython 
#   Aula 15 - Algoritmo "Auxiliar Will Forma Interrogativa"
#
###############################################################################

def auxiliar_will_interrogativa(pronome):
  return "Will "+ pronome + " ..?"
  
pronomes = ["I", "You", "He", "She", 
           "It", "We", "You", "They"]

for pronome in pronomes:
  print(auxiliar_will_interrogativa(pronome))
