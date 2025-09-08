lista = []
lista_par = []
lista_impar = []

for i in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)

    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(f"A lista é: {lista}")
print(f"A quantidade de números pares na lista é: {len(lista_par)}")
print(f"A soma dos itens impares da lista é: {sum(lista_impar)}")
