import random

lista = [random.randint(1, 50) for i in range(20)]
print(f"A lista sorteada foi: {lista}")

print(f"O somatório dos itens da lista é: {sum(lista)}")

print(f"O maior número da lista é: {max(lista)}")

print(f"O menor número da lista é: {min(lista)}")