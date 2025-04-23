soma = 0

while True:
    num1 = int(input("Digite um numero: "))
    if num1 != 0:
        soma += num1
    else:
        break

print(f"{soma}")
