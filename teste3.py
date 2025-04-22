numero = int(input("Digite um número: "))
multiplo = numero % 3 == 0

match multiplo:
    case True:
        print("É multiplo de 3")
    case False:
        print("Não é multiplo de 3")