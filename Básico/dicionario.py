#Dicionários 

#Criando dicionários

dicionario = {}

dicionario = dict()

dicionario = { 'Nome': 'Tiago', 'idade': 26, 'altura': 1.71 }

print(dicionario)
print(dicionario['idade'])

#Adicionando um elemento em um dicionário 

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)

#iterando dicionario 

for chave in dicionario:
    print(chave, dicionario[chave])

print('peso' in dicionario)
print('altura' in dicionario)