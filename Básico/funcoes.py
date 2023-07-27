def saudacao():
    print('Sejá bem-vinda(o)!') 

saudacao()


def saudacaos(nome, curso='Python'):
    print(f'Seja bem vindo(a) {nome}')
    print(f'Ola é um prazer ter você fazendo parte do curso de {curso}')

saudacaos('tiago')

saudacaos('Maria','C#')

#funcoes com retorno 

def soma (N1, N2):
    return N1 + N2

resultado = soma(5,7)

print(f'O resultado da soma é {resultado}')

def calculadora(num1, num2 , operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    else:
        print('Essa operação é invalida')

resultado = calculadora(10, 20, '-')

print(resultado)