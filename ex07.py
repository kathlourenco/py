num = 5
tentativa = int(input("Digite um numero: "))
cont = 0

while tentativa != num:
    print("Tentativa incorreto")
    tentativa = int(input("Digite um numero: "))
    cont += 1
    if tentativa == num:
        print("Você acertou o número")