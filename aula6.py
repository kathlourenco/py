cont = 1
valor = int(input("Digite o primeiro numero: "))

while cont <= 10:
    num = int(input("Digite um numero: "))

    if num < valor:
        valor = num
    cont += 1

print(valor)



