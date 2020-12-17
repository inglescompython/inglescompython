def plural_man_woman(pessoa):
    return pessoa.replace("a","e")

pessoas = ['Man','Woman']

for pessoa in pessoas:
    print(plural_man_woman(pessoa))
