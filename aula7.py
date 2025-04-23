num = int(input("Digite um numero: "))

fatorial = 1
cont = 1

while cont <= num:
    fatorial *= cont
    cont += 1
print(f"o fatorial de {num} = {fatorial}")
