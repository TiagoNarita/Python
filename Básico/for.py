for i in range(10):
    print(i)


for i in range(1, 11):
    print(i)


for i in range(1, 12, 3):
    print(i)
soma = 0

for i in range(1,4):
    nota = float(input(f'Digite a nota {i}: '))

    soma += nota

print(soma/3)