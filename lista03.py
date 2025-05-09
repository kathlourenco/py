import random

lista = []

for n in range(20):
    num = random.randint(1, 50)
    print(num)
    lista.append(num)
    print(lista)

soma = (sum(lista))
print(f"A soma dos números contidos na lista é igual a : {soma}")

