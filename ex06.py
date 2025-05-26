num = int(input("Digite um número: "))
soma = 0

while num != 0:
    soma += num
    num = int(input("Digite o número zero para sair: "))
    print("Soma total:", soma)


