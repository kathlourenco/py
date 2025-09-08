lista = []

for i in range(10):
    num = int(input("digite um numero: "))
    lista.append(num)

    media = sum(lista) / 10

    if num % 2 == 0:
        somatorio_par = sum(lista)

print(lista)
print(media)
print(somatorio_par)