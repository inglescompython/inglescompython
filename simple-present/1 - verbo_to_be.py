###############################################################################
#
#   Algoritmos criados para fins educativos no projeto Inglês com Python
#   Nos sigam no Instagram e Facebook: @inglescompython 
#   Aula 01 - Algoritmo "Verbo To Be"
#
###############################################################################

def verbo_to_be(pronome):
    
    excecao = ['I']
    plural = ['You','They','We']
    singular = ['He','She','It']

    # You é tanto pessoa do singular (você) como plural (vocês)
    # mas a conjugação do verbo to be é o mesmo: "You are"

    if(pronome in excecao):
        print(pronome + " am")
    elif(pronome in singular):
        print(pronome + " are")
    elif(pronome in plural):
        print(pronome + " is")
    else:
        print("Pronome Desconhecido")

todos_pronomes = ["I","You","He","She","It","We","You","They"]

for p in todos_pronomes:
    verbo_to_be(p)

#Chamadas de função
#verbo_to_be("I")
#verbo_to_be("He")
#verbo_to_be("They")
