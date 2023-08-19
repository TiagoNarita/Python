nome = "Tiago "
idade = 20
profissão = "programador"
linguagem = "Python"
saldo = 33.43512

print("Nome: %s Idade: %d " % (nome, idade))
print("Nome: {} Idade: {} ".format(nome, idade))

print("Nome: {1} Idade: {0} ".format(idade, nome))
print("Nome: {1} Idade: {0} e {1} é lindo".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
# essa forma as variaveis ficam mais explicitas
print("Nome: {name} Idade: {age} {name} {age}".format(name=nome, age=idade))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.1f}")


