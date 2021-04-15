def verbo_to_be_futuro_simples(pronome):
  return pronome + " will" + " be"
  
pronomes = ["I", "You", "He", "She", 
           "It", "We", "You", "They"]

for pronome in pronomes:
  print(verbo_to_be_futuro_simples(pronome))
