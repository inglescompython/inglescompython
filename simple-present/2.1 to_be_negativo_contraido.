###############################################################################
#
# Algoritmos criados para fins educativos no projeto Inglês com Python
# Nos sigam no Instagram e Facebook @inglescompython 
# Aula 02.1 = Algoritmo "Verbo To Be" Forma Negativa Contraida
#
###############################################################################

def to_be_negativo_contraido(pronome):
    
    negativo = "not"    
    
    excecao = ['I']
    plural = ['You','They','We']
    singular = ['He','She','It']

    negativo_contraido = negativo.replace("o","'")
    #Subistitui o "o" por "'" (aspas simples), not => n't

    if(pronome in excecao):
        print(pronome+" am "+negativo)
        #Verbo am não tem contração, nisso se usa o "not" normal
    elif(pronome in plural):
        print(pronome+" are"+negativo_contraido)
        #Junta o verbo com o negativo contraido
    elif(pronome in singular):
        print(pronome+" is"+negativo_contraido)
        #Junta o verbo e o negativo contraido
    else:
        print("Pronome Desconhecido")

todos_pronomes = ["I","You","He","She","It","We","You","They"]

for v in todos_pronomes:
    to_be_negativo_contraido(v)
