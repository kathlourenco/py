lista = []
lista_pares = []
lista_impar = []

for i in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)

    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impar.append(num)

print(f"A lista principal é: {lista}")
print(f"A lista de números pares da lista principal é: {lista_pares}")
print(f"A lista de números impares da lista principal é: {lista_impar}")