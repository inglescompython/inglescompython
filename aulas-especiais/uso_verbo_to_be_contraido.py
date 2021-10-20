def uso_verbo_to_be_contraido(pronome,verbo):
    verbo_contraido = "'"+verbo[1::]
    return pronome + verbo_contraido

pronomes_verbos = [("I","am"),("You","are"),("He","is")]

for pronome,verbo in pronomes_verbos:
    print(uso_verbo_tobe_contraido(pronome,verbo))
