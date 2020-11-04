###############################################################################
#
# Algoritmos criados para fins educativos no projeto Inglês com Python
# Nos sigam no Instagram e Facebook @inglescompython 
# Aula 03 = Algoritmo "Verbo To Be" Forma Interrogativa
#
###############################################################################

def to_be_interrogativo(pronome):
        
    excecao = ['I']
    plural = ['You','They','We']
    singular = ['He','She','It']

    # You é tanto pessoa do singular (você) como plural (vocês)
    # mas a conjugação do verbo to be é o mesmo: "You are"

    if(pronome in excecao):
        print("Am "+pronome)
    elif(pronome in singular):
        print("Is "+pronome.lower())
    elif(pronome in plural):
        print("Are "+pronome.lower())
    else:
        print("Pronome Desconhecido")

todos_pronomes = ["I","You","He","She","It","We","You","They"]

for p in todos_pronomes:
    to_be_interrogativo(p)

#Chamada de Função
#to_be_interrogativo("I")
#to_be_interrogativo("You")
#to_be_interrogativo("He")
