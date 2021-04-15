def auxiliar_will_negativa(pronome):
    return pronome + " will" + " not"

def auxiliar_will_negativa_contraido(pronome):

    auxiliar = "will"
    negativo = "not"
    negativo_contraido = auxiliar[0]+"o"+negativo.replace("o","'")

    return pronome + " " + negativo_contraido


pronomes = ["I","You","He","She",
           "It","We","You","They"]

for pronome in pronomes:
    print(auxiliar_will_negativa(pronome))
    print(auxiliar_will_negativa_contraido(pronome))
