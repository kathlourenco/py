def menu():
    while True:
        print("Calculadora: 1 - Adição, 2 - Subtração, 3 - Multiplicação, 4 - Divisão, 5 - Sair do programa ")
        opcao = int(input("Selecione sua opção: "))

        if opcao == 5:
            print("Programa encerrado")
            break  # sai do loop
        elif opcao in [1, 2, 3, 4]:
            num1 = float(input("Digite um numero: "))
            num2 = float(input("Digite outro numero: "))

            if opcao == 1:
                print("Resultado:", num1 + num2)
            elif opcao == 2:
                print("Resultado:", num1 - num2)
            elif opcao == 3:
                print("Resultado:", num1 * num2)
            elif opcao == 4:
                if num2 != 0:
                    print("Resultado:", num1 / num2)
                else:
                    print("Não dá pra dividir por zero!")
        else:
            print("Digite um numero válido!")

menu()
