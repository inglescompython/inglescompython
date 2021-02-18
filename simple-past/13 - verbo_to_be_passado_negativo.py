def verbo_to_be_passado_negativo(pronome):
    
    singular = ["I","He","She","It"]

    if(pronome in singular):
        return pronome+" was not"
    else:
        return pronome+" were not"

pronomes = ["I","You","He","She","It","We","You","They"]

for pronome in pronomes:
    print(verbo_to_be_passado_negativo(pronome))
