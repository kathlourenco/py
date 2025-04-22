print("Cardápio:")
print("1- Picanha")
print("2- Lasanha")
print("3- Strogonoff")
print("4- Bife acebolado")
print("5- Pão com ovo")
prato = int(input("Digite o código do prato que você deseja: "))
taxa = input("Aceita pagar uma taxa de 10%?: ")

match (prato, taxa):
    case (1, "sim") :
        v1 = 25.00 + (25 * 0.1)
        print(f"O valor a ser pago será {v1} reais")
    case (1, "não") :
        print("O valor a ser pago será de 25 reais")
    case (2, "sim") :
        r2 = 20 + (20 * 0.1)
        print(f"O valor a ser pago será {r2} reais")
    case (2, "não") :
        print("O valor a ser pago será de 20 reais")
    case (3, "sim") :
        r3 = 20 + (20 * 0.1)
        print(f"O valor a ser pago será de {r3} reais")
    case (3, "não") :
        print("O valor a ser pago será de 20 reais")
    case (4, "sim") :
        r4 = 15 + (15 * 0.1)
        print(f"O valor a ser pago será de {r4} reais")
    case (4, "não") :
        print("O valor a ser pago será de 15 reais")
    case (5, "sim") :
        r5 = 5 + (5 * 0.1)
        print(f"O valor a ser pago será de {r5} reais")
    case (5, "não") :
        print("O valor a ser pago será de 5 reais")
