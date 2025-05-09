# listas

numeros = [5, 6, 7, 8]
print(numeros)

nomes = ["Ana", "João", "Leonardo"]
print(nomes)

lista = []
print(lista)

# indices começam do 0 e incrementam em uma unidade, utilizados para identificar uma posição na lista
frutas = ["Morango", "Banana", "Goiaba"]
print(frutas[0])

# indices negativos começam pelo ultimo elemento
cores = ["Amarelo", "Azul", "Laranja"]
print(cores[-3])

# alterar um item da lista
lista = [3, 6, 19, 89]
lista[0] = 100
print(lista)

# inserir um item na lista
lista = [3, 6, 19, 89]
lista.append(500)
lista.append(600)
print(lista)

# verificar tamanho de uma lista
tamanho = len(lista)
print(tamanho)

# remover item da lista
lista = [3, 6, 19, 89]
lista.pop(0)
print(lista)

# preencher lista com entradas do usuario (tamanho fixo)
listaNomes = []
for i in range(5):
    nome = input("Digite um nome: ")
    listaNomes.append(nome)
print(listaNomes)

# percorrer uma lista com entradas do usuario (tamanho indeterminado)
listaNomes = []
while True:
    nome = input("Digite um nome: ")
    if nome == "":
        break
    listaNomes.append(nome)
print(listaNomes)

# percorrer os itens da lista
lista = [3, 4, 5, 6]
for item in lista:
    print(item)

# contar a qtd de numeros impares na lista
cont = 0
for item in lista:
    if item % 2 == 0:
        cont += 1
print(f"A qtd de impares é {cont}")

# percorrer os indices da lista
for i in range(len(lista)):
    if lista[i] % 2 != 0:
        lista[i] = 0
print(lista)


