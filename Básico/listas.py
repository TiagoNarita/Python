nota1 = 9.7
nota2 = 7.3
nota3 = 5.2

notas = [9.7, 7.3 , 5.2]

lista = []
lista = list()
lista = [3 + 3, 'walingotn', 5.6 , True]
lista_de_listas = [10, [2, 3, 8]]

print(lista)
print(lista[2])
print(lista[-1])

#slices

lista = [30, 40, 60 , 80 , 90 , 100]

print(lista[0:4])
print(lista [3:6])
print(lista[0:6:2])

#interações com for:

for i in lista:
    print(i)


print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])

lista = [1, 3, 12, 8, 2]

print('Antes do append: ', lista)

#append = adiciona no final da lista

lista.append(3)

print('Depois do append: ', lista)

lista.insert(2, 10)

print('Depois do insert: ', lista)

#extend

lista2 = [1, 2 , 3]

lista.extend(lista2)

print('Depois do extend: ', lista)

#pop - se não espeficiar ele retira o ultimo elemento.

lista.pop()

print('Lista após o pop: ', lista)

lista.pop(0)

print('Lista após o pop(0): ', lista)

#remove - remove o primeiro elemento desejado que ele encontra.

lista.remove(3)

print('Depois do remove: ', lista)

#count 

print('Quantidade de 2 na lista ', lista.count(2))

#index 

print('Indice do elemento 12: ', lista.index(12))

#sort

lista.sort()

print(lista)

#functions to lists:

#len = length

print(len(lista))

#sum - soma todos os elementos da lista 

print(sum(lista))

#max e #min - Imprime o maior e o menor valor da lista 

print(max(lista))
print(min(lista))