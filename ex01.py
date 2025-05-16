lista = [1, 2, 3, 4, 5, 6]

# len retorna o tamanho da lista
print(len(lista))

#  max retorna o maior valor da lista
print(max(lista))

# min retorna o menor valor da lista
print(min(lista))

# palavras que comecam com letra maiuscula tem prioridade
nomes = ["Paulo", "Julia", "Fer"]
print(max(nomes))

# sum retorna o somatorio da lista
print(sum(lista))

media = sum(lista) / len(lista)
print(media)

# append insere um item na lista
lista =[1, 2, 3, 4]
lista.append(100)
print(lista)
lista.append(200)
print(lista)

# insert (indice, num) insere um item em um indice especifico
lista.insert(0, 300)
print(lista)

# pop remove um item de um indice da lista (se não colocar a posição ele remove o ultimo item)
lista.pop(3)
print(lista)

# remove(item): remove o numero inserido
lista.remove(2)

# remover todos numeros iguais inseridos
while 1 in lista:
    lista.remove(1)
print(lista)

# index retorna o indice de um item na lista (se o valor for inexistente na lista retorna como erro)
print(lista.index(4))

# sort ordena  uma lista em ordem crescente
lista1 = [1, 3, 5, 7, 9]
lista1.sort()
print(lista1)

# lista.sort(reverse=true) ordena uma lista em ordem decrescente
lista2 = [4, 5, 8, 2, 10]
lista2.sort(reverse=True)
print(lista2)

# count conta quantas vezes um item aparece
lista3 = [2, 2, 2, 2, 4, 5]
print(lista3.count(2))

# concatenação de listas
lista4 = [200, 300, 400]
lista5 = [500, 600]
lista6 = lista4 + lista5
print(lista6)
