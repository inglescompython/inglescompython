def auxiliar_do_does_neg_contraido(verbo):

    terceira_pessoa_singular =  ['He','She','It']
    negativo = "not"
    negativo_contraido = negativo.replace("o","'")
    
    if(pronome in terceira_pessoa_singular):
        return pronome+' does'+negativo_contraido
    else:
        return pronome+' do'+negativo_contraido
	
todos_pronomes = ['I','You','He','She',
                 'It','We','You','They']

for pronome in todos_pronomes:
    print(auxiliar_do_does_neg_contraido(pronome))
