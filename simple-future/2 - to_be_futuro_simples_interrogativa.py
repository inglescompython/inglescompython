def to_be_futuro_simples_interrogativa(pronome):
  return "Will "+ pronome + " ..?"
  
pronomes = ["I", "You", "He", "She", 
           "It", "We", "You", "They"]

for pronome in pronomes:
  print(to_be_futuro_simples_interrogativa(pronome))
