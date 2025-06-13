def lerIdade():
    try:
        idade = int(input("Digite a idade: "))
        if idade < 0:
            raise ValueError
        return idade
    except ValueError:
        print("O valor deve ser inteiro")

idade = lerIdade()
print(f"A idade informada é: {idade}")

