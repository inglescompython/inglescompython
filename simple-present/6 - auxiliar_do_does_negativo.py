def auxiliar_do_does_negativo(pronome):

    terceira_pessoa_singular =  ['He','She','It']

    if(pronome in terceira_pessoa_singular):
        return pronome+' does'+' not'
    else:
        return pronome+' do'+' not'

todos_pronomes = ['I','You','He','She',
                 'It','We','You','They']

for pronome in todos_pronomes:
    print(auxiliar_do_does_negativo(pronome))
