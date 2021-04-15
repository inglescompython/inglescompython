def auxiliar_will_interrogativa(pronome):
  return "Will "+ pronome + " ..?"
  
pronomes = ["I", "You", "He", "She", 
           "It", "We", "You", "They"]

for pronome in pronomes:
  print(auxiliar_will_interrogativa(pronome))
