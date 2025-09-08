import random
lista = [random.randint(1, 10000) for i in range(10)]
print(lista)
num = int(input("Digite um número: "))

if num in lista:
    print(f"Este número aparece {lista.count(num)} vezes")
else:
    print("Este número não está na lista")