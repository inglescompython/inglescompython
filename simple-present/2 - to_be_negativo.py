###############################################################################
#
# Algoritmos criados para fins educativos no projeto Inglês com Python
# Nos sigam no Instagram e Facebook @inglescompython 
# Aula 02 = Algoritmo "Verbo To Be" Forma Negativa
#
###############################################################################

def to_be_negativo(pronome):
    
    excecao = ['I']
    plural = ['You','They','We']
    singular = ['He','She','It']

    # You é tanto pessoa do singular (você) como plural (vocês)
    # mas a conjugação do verbo to be é o mesmo: "You are"

    if(pronome in excecao):
        print(pronome + " am"+" not")
    elif(pronome in singular):
        print(pronome + " is"+" not")
    elif(pronome in plural):
        print(pronome + " are"+ " not")
    else:
        print("Pronome Desconhecido")

todos_pronomes = ["I","You","He","She","It","We","You","They"]

for p in todos_pronomes:
    to_be_negativo(p)

#Chamadas de função
#to_be_negativo("I")
#to_be_negativo("He")
#to_be_negativo("They")
