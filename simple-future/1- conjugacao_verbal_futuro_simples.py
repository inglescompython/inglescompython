def conjugacao_verbal_futuro_simples(pronome):
  return pronome + " will" + " be" 

  
pronomes = ["I", "You", "He", "She", 
           "It", "We", "You", "They"]


for pronome in pronomes:
  print(conjugacao_verbal_futuro_simples(pronome))
