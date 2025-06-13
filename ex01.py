while True:
    try:
        a = int(input("Digite um número: "))
        b = int(input("Digite um número: "))
        if a < 0 or b < 0:
            raise TypeError("O valor deve ser positivo")
        c = a / b
        print(f"Resultado: {c}")
    except ZeroDivisionError:
        print("Erro: ocorreu uma divisão por zero")
    except ValueError:
        print("O valor deve ser um número inteiro")
    except TypeError as mensagem:
        print(mensagem)
    except Exception:
        print("Erro inesperado")
    else:
        print("Operação realizada com sucesso")
    finally:
        print("Fim do programa")
        break
print("Continua...")
