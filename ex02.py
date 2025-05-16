def exibeMensagem():
    print("Exemplo de programa usando funções")

def numeroPrimo(numero):
    cont = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1

    if cont == 2:
        print("Primo")

    else:
        print("Não primo")

def soma(a, b):
    c = a + b
    print(f"A soma de {a} + {b} = {c}")

def criarLista(tamanho):
    lista = []

    for i in range(tamanho):
        n = int(input("Numero: "))
        lista.append(n)
    print(lista)

def calcularMedia(lista):
    media = sum(lista) / len(lista)
    return media

# chama a função
exibeMensagem()
n = int(input("Digite um numero: "))
numeroPrimo(n)
soma(10, 20)
criarLista(4)
print(lista)
print(f"Media da lista: {calcularMedia(lista)}")

# função que não tem return voltam  como null
# from importa funções
