n = int(input("Digite um número:"))
cont = 1
print(f"Números ímpares de 1 até {n}:")

while cont <= n:
    if cont % 2 != 0:
        print(cont)
    cont += 1
