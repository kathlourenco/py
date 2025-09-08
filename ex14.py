lista = []

for i in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)

print(f"O maior número da lista é: {max(lista)}")
print(f"O menor número da lista é: {min(lista)}")
print(f"A média dos números é: {sum(lista) / 10}")