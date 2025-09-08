lista = []
lista_par = []

for i in range(10):
    num = int(input("Digite um numero: "))

    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)

print(f"A lista principal  é: {lista}")

print(f"A média aritmetica dos itens da lista principal é: {sum(lista) / 10}")

print(f"O somatório dos itens da lista de números pares é: {sum(lista_par)}")
