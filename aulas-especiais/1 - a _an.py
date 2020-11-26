def a_an(palavra):
    vogais = ['a','e','i','o','u']
    if(palavra[0] in vogais): 
        print("an "+palavra)
    else:
        print("a "+palavra)

a_an('apple')
a_an('bird')
a_an('umbrella')
a_an('house')
