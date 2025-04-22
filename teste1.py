valor = float(input("Digite o valor da compra: "))
valorf = valor - (valor * 0.1)
valorv = valor - (valor * 0.05)


print("C- Cliente comum")
print("F- Funcionário")
print("V- Vip")
atb = input("Você se encaixa em qual dessas opções?: ")

match atb:
    case "C":
        print(f"O valor da sua compra é de: {valor} reais ")
    case "F":
        print(f"O valor da sua compra é de {valorf} ")
    case "V":
        print(f"O valor da sua compra é de {valorv}")
